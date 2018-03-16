import pickle
import os, sys
import pandas as pd

wordDictpath = "./data/gapArticles_Dic/WordDic_Cleaned"
vectorPath = "./data/VectorsForArticles"
path = "./data/gapArticles_Dic"
WordDict = pickle.load(open(wordDictpath, "rb"))

filedirs = os.listdir(path)

for fileName in filedirs :
    if fileName != "WordDic" and fileName != "WordDic_Cleaned" and fileName != '.DS_Store' :
        fileWordDict = pickle.load(open(path + '/' + fileName, "rb"))
        vector = []
        for key in WordDict :
            if key in fileWordDict :
                vector.append(fileWordDict[key])
            else :
                vector.append(0)

        pickle.dump(vector,open(vectorPath + '/' + fileName + 'Vector' ,'wb'))

#print(WordDict)


