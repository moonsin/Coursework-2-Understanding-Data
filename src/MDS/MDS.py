import pickle
import os, sys
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
import pandas as pd
import csv
import numpy  as np
import matplotlib.pyplot as plt
sys.path.append("./src/HierarchicalClustering/AHC")
import AHC
sys.path.append("./src/Kmeans")
import Kmeans
sys.path.append("./src/Meanshift")
import meanshift

filename = './data/FinalVectors_TFIDF'

dmatrix = np.zeros((24,24))
ArticleNameList = [] 


FinalVectors = pickle.load(open(filename,'rb'))

for index in FinalVectors.index :
    ArticleNameList.append(index)

ArticleNameList = np.array(ArticleNameList)

'''
#使用函数生成欧几里得距离矩阵
print(FinalVectors)
npFinalVectors = np.array(FinalVectors)
dist = euclidean_distances(npFinalVectors)
print(dist)
dmatrix = dist
'''

#手工生成余弦相似度距离矩阵
for index1 in range(24):
    for index2 in range(24):
        name1 = ArticleNameList[index1]
        name2 = ArticleNameList[index2]
        vec1 = np.array(FinalVectors.loc[name1])
        vec2 = np.array(FinalVectors.loc[name2])
        dmatrix[index1,index2] = np.dot(vec1,vec2)/(np.linalg.norm(vec1)*(np.linalg.norm(vec2)))  
print(dmatrix)
dmatrix = 1 - dmatrix

from sklearn import manifold
mds = manifold.MDS(n_components=2,dissimilarity = 'precomputed',random_state=1 )
xtrans = mds.fit_transform(dmatrix)

#print(xtrans)
'''
#输出前后距离对比
print('original distance','\tnew distance')
for i in range(24):
    for j in range(24):
        print(np.str(dmatrix[i,j]),'\t\t',np.str("%.4f"%np.linalg.norm(xtrans[i]-xtrans[j])))
'''

'''
#AHC获取簇的序列
Z = []
Z = AHC.getClustersByNumberOfClusters(4,FinalVectors)
print(Z)
'''
'''
#使用Kmeans获取序列
Z = []
Z = Kmeans.getClustersByNumberOfClusters(12, FinalVectors)
print(Z)
'''

#使用Meanshift
Z = []
Z = meanshift.getClustersByNumberOfClusters(FinalVectors)
print(Z)

#标记名字
n = ArticleNameList
for index in range(24):
    n[index] = n[index][4:]
    n[index] = n[index][0:-9]
'''
标记数量
n = range(24)
'''
fig,ax=plt.subplots()
colorDict = {
	0:'#686868',
	1:'#000000',
	2:'#929292',
	3:'#B8B8B8',
	4:'#FF0000',
	5:'#00FF00',
	6:'#0000FF',
	7:'#00FFFF',
	8:'#FFFF00',
	9:'#FF00FF',
	10:'#FF7F00',
	11:'#7F007F',
	12:'#996633',
        }
#按颜色分类
for index in range(24) :
    #ax.scatter(xtrans[index,0],xtrans[index,1],marker='o',c='',edgecolors=colorDict[Z[index]])
    ax.scatter(xtrans[index,0],xtrans[index,1],marker='o',c=colorDict[Z[index]])

'''
#画出全部点
ax.scatter(xtrans[:,0],xtrans[:,1],marker='o',c='b')
'''


for i,txt in enumerate(n):
    ax.annotate(txt,(xtrans[:,0][i],xtrans[:,1][i]))

plt.title("Multidimensional Scaling")  
plt.show()
