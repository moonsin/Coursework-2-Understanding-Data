import numpy as np
from sklearn.cluster import KMeans
import pickle

'''
filename = './data/FinalVectors_TFIDF'
FinalVectors = pickle.load(open(filename,'rb'))
data = np.array(FinalVectors)
'''

def getClustersByNumberOfClusters(num, FinalVectors) :
    data = np.array(FinalVectors)
    estimator = KMeans(n_clusters=num)#构造聚类器
    estimator.fit(data)#聚类

    label_pred = estimator.labels_ #获取聚类标签
    centroids = estimator.cluster_centers_ #获取聚类中心
    inertia = estimator.inertia_ # 获取聚类准则的总和

    return label_pred
