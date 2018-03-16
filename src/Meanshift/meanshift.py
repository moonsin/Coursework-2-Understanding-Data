import numpy as np
from sklearn.cluster import MeanShift
import pickle
'''
filename = './data/FinalVectors_TFIDF'
FinalVectors = pickle.load(open(filename,'rb'))
data = np.array(FinalVectors)
'''


def getClustersByNumberOfClusters(FinalVectors) :
    data = np.array(FinalVectors)
    estimator = MeanShift()#构造聚类器
    estimator.fit(data)#聚类

    label_pred = estimator.labels_ #获取聚类标签
    return label_pred



