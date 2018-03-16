from sklearn.cluster import KMeans
import pickle
import os, sys
import pandas as pd
import matplotlib.pyplot as plt
import csv
from matplotlib.ticker import NullFormatter
import numpy  as np
from mpl_toolkits.mplot3d import Axes3D
from time import time
from sklearn import (manifold, datasets, decomposition, ensemble,
                             discriminant_analysis, random_projection)

filename = './data/FinalVectors'

FinalVectors = pickle.load(open(filename,'rb'))

#print(FinalVectors)
dmatrix = np.zeros((24,24))
ArticleNameList = [] 

# Next line to silence pyflakes. This import is needed.
Axes3D

n_points = 1000
X, color = datasets.samples_generator.make_s_curve(n_points, random_state=0)
n_neighbors = 10
n_components = 2

fig = plt.figure(figsize=(15, 8))
plt.suptitle("Manifold Learning with %i points, %i neighbors"
             % (1000, n_neighbors), fontsize=14)

for index in FinalVectors.index :
    ArticleNameList.append(index)

ArticleNameList = np.array(ArticleNameList)

print(ArticleNameList)

#print(FinalVectors[0])
#print(FinalVectors.loc[FinalVectors.index[1]])

for index1 in range(24):
    for index2 in range(24):
        name1 = ArticleNameList[index1]
        name2 = ArticleNameList[index2]
        vec1 = np.array(FinalVectors.loc[name1])
        vec2 = np.array(FinalVectors.loc[name2])
        dmatrix[index1,index2] = np.linalg.norm(vec1 - vec2)  
print(dmatrix)

X_mds = manifold.MDS().fit(dmatrix)
print(X_mds)

t0 = time()
mds = manifold.MDS(n_components, max_iter=100, n_init=1)
Y = mds.fit_transform(X)
t1 = time()
print("MDS: %.2g sec" % (t1 - t0))
ax = fig.add_subplot(258)
plt.scatter(Y[:, 0], Y[:, 1], c=color, cmap=plt.cm.Spectral)
plt.title("MDS (%.2g sec)" % (t1 - t0))
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis('tight')

plt.show()

