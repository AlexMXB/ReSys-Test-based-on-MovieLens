#-*- coding: utf-8 -*-
import sys, random, math
from operator import itemgetter

random.seed(0)

class UserBasedCF():
    ''' TopN recommendation - UserBasedCF '''
    def __init__(self):
        self.trainset = {}
        self.testset = {}

        self.n_sim_user = 20
        self.n_rec_movie = 10

        self.user_sim_mat = {}
        self.movie_popular = {}
        self.movie_count = 0

        print >> sys.stderr, 'Welcome to UserBasedCF Test System'
        print >> sys.stderr, 'Similar user number = %d' % self.n_sim_user
        print >> sys.stderr, 'recommended movie number = %d' % self.n_rec_movie


    @staticmethod
    def loadfile(filename):
        ''' load a file, return a generator. '''
        fp = open(filename, 'r')
        for i,line in enumerate(fp):
            yield line.strip('\r\n')
            if i%10000 == 0:
                print >> sys.stderr, 'loading lines%s(%s)' % (filename, i)
        fp.close()
        print >> sys.stderr, 'load %s succ' % filename


    def generate_dataset(self, filename, pivot=0.5):
        ''' load rating data and split it to training set 80% and test set 20% '''
        trainset_len = 0
        testset_len = 0

        for line in self.loadfile(filename):
            user, movie, rating, timestamp = line.split(',')
            # split the data by pivot
            if (random.random() < pivot):#train
                self.trainset.setdefault(user,{})
                self.trainset[user][movie] = float(rating)
                trainset_len += 1
            else:#test
                self.testset.setdefault(user,{})
                self.testset[user][movie] = float(rating)
                testset_len += 1
        #   trainset format : {'user':{'movie':'(float)rating'}} 
        print >> sys.stderr, 'split training set and test set succ'
        print >> sys.stderr, 'train set = %s' % trainset_len
        print >> sys.stderr, 'test set = %s' % testset_len


    def calc_user_sim(self):
        ''' calculate user similarity matrix using train set'''
        # build inverse table for item-users
        # key=movieID, value=list of userIDs who have seen this movie
        print >> sys.stderr, 'building movie-users inverse table...'
        movie2users = dict()

        for user,movies in self.trainset.iteritems():
        #   trainset format : {'user':{'movie':'(float)rating'}} 
            for movie in movies:
                # inverse table for item-users
                if movie not in movie2users:
                    movie2users[movie] = set()
                movie2users[movie].add(user)
                # count item popularity at the same time
                if movie not in self.movie_popular:
                    self.movie_popular[movie] = 0
                self.movie_popular[movie] += 1
        print >> sys.stderr, 'build movie-users inverse table success'
        # movie2users format : {'movie':(user1,user2,...)} 
        # movie_popular format : {'movie':'number that indicates frequency'} 
        # save the total movie number, which will be used in evaluation
        self.movie_count = len(movie2users)
        print >> sys.stderr, 'total movie number = %d' % self.movie_count

        # '''that is similarity matrix'''
        # count co-rated items between users
        usersim_mat = self.user_sim_mat
        print >> sys.stderr, 'building user co-rated movies matrix...'

        for movie,users in movie2users.iteritems():
            for u in users:
                for v in users:
                    if u == v: 
                        continue
                    usersim_mat.setdefault(u,{})
                    usersim_mat[u].setdefault(v,0)
                    usersim_mat[u][v] += 1
        print >> sys.stderr, 'build user co-rated movies matrix success'
        # usersim_mat format : {'user1':{'user2':'times of concurrency'}}
        # calculate similarity matrix (ratio of frequency)
        print >> sys.stderr, 'calculating user similarity matrix...'
        simfactor_count = 0
        PRINT_STEP = 100000
        for u,related_users in usersim_mat.iteritems():
            for v,count in related_users.iteritems():
                usersim_mat[u][v] = count / math.sqrt(
                        len(self.trainset[u]) * len(self.trainset[v]))
                #   concurrency of u,v
                simfactor_count += 1
                if simfactor_count % PRINT_STEP == 0:
                    print >> sys.stderr, 'calculating user similarity factor(%d)' % simfactor_count
        # usersim_mat format : {'user1':{'user2':'frequency or ratio'}}
        print >> sys.stderr, 'calculate user similarity matrix(similarity factor) succ'
        print >> sys.stderr, 'Total similarity factor number = %d' %simfactor_count


    def recommend(self, user):
        ''' Find K similar users and recommend N movies. '''
        K = self.n_sim_user
        N = self.n_rec_movie
        rank = dict()
        watched_movies = self.trainset[user]
        punish_movies = sorted(self.movie_popular.items(),key=itemgetter(1))[0:5]
        # v=similar user, wuv=similarity factor
        for v, wuv in sorted(self.user_sim_mat[user].items(),
                key=itemgetter(1), reverse=True)[0:K]:
        #   sort by frequency
            for movie in self.trainset[v]:
                if movie in watched_movies or movie in punish_movies:
                    continue
                    # if watched, skip
                    # if too popular, skip
                # predict the user's "interest" for each movie
                rank.setdefault(movie,0)
                rank[movie] += wuv
        # return the N best movies
        return sorted(rank.items(), key=itemgetter(1), reverse=True)[0:N]


    def evaluate(self):
        ''' return precision, recall, coverage and popularity '''
        print >> sys.stderr, 'Evaluation start...'

        N = self.n_rec_movie
        #  varables for precision and recall 
        hit = 0
        rec_count = 0
        test_count = 0
        # varables for coverage
        all_rec_movies = set()
        # varables for popularity
        popular_sum = 0

        for i, user in enumerate(self.trainset):
            if i % 50 == 0:
                print >> sys.stderr, 'recommending for %d' %i
            test_movies = self.testset.get(user, {})
            rec_movies = self.recommend(user)
            for movie, w in rec_movies:
                if movie in test_movies:
                    hit += 1
                all_rec_movies.add(movie)
                popular_sum += math.log(1 + self.movie_popular[movie])
            rec_count += N
            test_count += len(test_movies)

        precision = hit / (1.0*rec_count)
        recall = hit / (1.0*test_count)
        coverage = len(all_rec_movies) / (1.0*self.movie_count)
        popularity = popular_sum / (1.0*rec_count)

        print >> sys.stderr, 'precision=%.4f\trecall=%.4f\tcoverage=%.4f\tpopularity=%.4f' % \
                (precision, recall, coverage, popularity)


if __name__ == '__main__':
    ratingfile = 'ml-latest-small/ratings.csv'
    usercf = UserBasedCF()
    usercf.generate_dataset(ratingfile)
    usercf.calc_user_sim()
    usercf.evaluate()
