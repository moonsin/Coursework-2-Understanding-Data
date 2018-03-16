import pickle
import os, sys
import pandas as pd
import csv


vectorPath = "./data/VectorsForArticles"
VectorDict = {}
filedirs = os.listdir(vectorPath)

for fileName in filedirs :
    if fileName != '.DS_Store' :
        Vector = pickle.load(open(vectorPath + '/' + fileName, "rb"))
        VectorDict[fileName] = Vector

data = pd.DataFrame(VectorDict)
data_T = data.T

print(data_T)
pickle.dump(data_T,open('./data/FinalVectors','wb'))
data_T.to_csv('./data/DataVectors.csv', index=True)
