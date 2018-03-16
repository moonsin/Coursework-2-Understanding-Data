import pickle
from scipy.cluster.hierarchy import dendrogram, linkage,cophenet,fcluster
import numpy as np
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt

#print(FinalVectors)

#matplotlib inline
# 防止科学计数法
np.set_printoptions(precision=5, suppress=True)

def getAHCClusters(FinalVectors) :
    X = np.array(FinalVectors)

    Z = linkage(X, 'centroid')
    return Z
#print(Z)

'''
filename = './data/FinalVectors_TFIDF'

FinalVectors = pickle.load(open(filename,'rb'))

Z = getAHCClusters(FinalVectors)
# 计算 Cophenetic correlation
X = np.array(FinalVectors)
c, coph_dists = cophenet(Z, pdist(X))
print(c)

#print(Z)
#用来画聚类的树状图
plt.figure(figsize=(50, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(Z, leaf_rotation=90., leaf_font_size=8.)
plt.show()
'''

# 设置阈值
#max_d = 50
#clusters = fcluster(Z, max_d, criterion='distance')

#设置簇数
#k = 4
#clusters =fcluster(Z, k, criterion='maxclust')

def getClustersByNumberOfClusters(num, FinalVectors) :
    Z = getAHCClusters(FinalVectors)
    clusters =fcluster(Z, num, criterion='maxclust')
    return clusters

#print(clusters)
