import pandas as pd
from sklearn.cross_validation import train_test_split

def readin():
	nlinks = ['movieId','imdbId','tmdbId']
	links = pd.read_csv('ml-latest-small/links.csv', sep=',', header=None, names=nlinks)
	# print links[:5]
	rnames = ['userId','movieId','rating','timestamp']
	ratings = pd.read_csv('ml-latest-small/ratings.csv', sep=',', header=None, names=rnames)
	# print ratings[:5]
	mnames = ['movieId', 'title', 'genres']
	movies = pd.read_csv('ml-latest-small/movies.csv', sep=',', header=None, names=mnames)
	# print movies[:5]
	mtags = ['userId','movieId','tag','timestamp']
	tags = pd.read_csv('ml-latest-small/tags.csv', sep=',', header=None, names=mtags)
	# print tags[:5]
	return links,ratings,movies,tags

def SplitData(data,k):
	train,test = train_test_split(data, test_size=k,random_state=0)
	return train,test


# unittest for readin data
if __name__ == '__main__':
	lk,rt,mv,tg = readin()
	print lk[:20]
	print rt[:20]
	print mv[:20]
	print tg[:20] 
	tr,te = SplitData(rt.loc[:,['userId','movieId']],0.2)
	print te[:10]
	print tr[:10]