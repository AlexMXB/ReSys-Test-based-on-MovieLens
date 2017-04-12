from surprise import SVD,KNNBasic,BaselineOnly,KNNWithMeans,KNNBaseline,SVDpp,NMF,SlopeOne,CoClustering
from surprise import Dataset,Reader
from surprise import evaluate, print_perf
import os

file_path = os.path.expanduser('ml-100k/u.data')

# As we're loading a custom dataset, we need to define a reader. In the
# movielens-100k dataset, each line has the following format:
# 'user item rating timestamp', separated by '\t' characters.
reader = Reader(line_format='user item rating timestamp', sep='\t')

data = Dataset.load_from_file(file_path, reader=reader)
data.split(n_folds=3)
trainset = data.build_full_trainset()
sim_options = {'name': 'pearson',
               'user_based': True  # compute  similarities between items
               }
# algo = SVD()
algo = KNNBasic(sim_options=sim_options)
# algo = BaselineOnly()
# algo = NMF()
# algo = KNNWithMeans(sim_options=sim_options)
algo.train(trainset)
# uid = str(1)
# iid = str(367)

# get a prediction for specific users and items.
for i in range(1,600):
	uid = str(i)
	for j in range(1,10):
		iid = str(j)
		pred = algo.predict(uid, iid, r_ui=4, verbose=True)
# Evaluate performances of our algorithm on the dataset.
# perf = evaluate(algo, data, measures=['RMSE', 'MAE'])

# print_perf(perf)
