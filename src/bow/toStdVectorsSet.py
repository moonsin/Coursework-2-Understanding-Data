import pickle
import os, sys
import pandas as pd
import csv
import numpy  as np
import matplotlib.pyplot as plt


filename = './data/FinalVectors'

FinalVectors = pickle.load(open(filename,'rb'))
ArticleNameList = [] 
dmatrix = np.zeros((24, FinalVectors.columns.size))

for index in FinalVectors.index :
    ArticleNameList.append(index)

ArticleNameList = np.array(ArticleNameList)


print(FinalVectors)
#print(FinalVectors[1][4])
print(FinalVectors[0][3] / 6)

for index1 in range(FinalVectors.columns.size) :
    print(index1)
    maxValue = FinalVectors[index1][0]
    minValue = FinalVectors[index1][0]
    for index2 in ArticleNameList :
        if maxValue < FinalVectors[index1][index2] :
            maxValue = FinalVectors[index1][index2]
        if minValue > FinalVectors[index1][index2] :
            minValue = FinalVectors[index1][index2]
    sumValue = maxValue - minValue
    i = 0
    for index2 in ArticleNameList :
        dmatrix[i][index1] = float(FinalVectors[index1][index2]) / float(sumValue)
        i +=1

print(dmatrix)
print(dmatrix[0])
pickle.dump(dmatrix,open('./data/FinalVectors_standered' ,'wb'))
    

# 转换为Df格式，并添加文件名index 
filename = './data/FinalVectors'

FinalVectors = pickle.load(open(filename,'rb'))
ArticleNameList = [] 

for index in FinalVectors.index :
    ArticleNameList.append(index)

ArticleNameList = np.array(ArticleNameList)


filename = './data/FinalVectors_standered'
FinalVectors_standered = pickle.load(open(filename,'rb'))

FinalVectors_standered = pd.DataFrame(FinalVectors_standered, index = ArticleNameList)

#print(FinalVectors_standered[20005])
pickle.dump(FinalVectors_standered,open('./data/FinalVectors_standered' ,'wb'))

