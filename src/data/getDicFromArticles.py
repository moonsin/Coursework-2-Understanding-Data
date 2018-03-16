import pickle
import os, sys
import pandas as pd


path = "./data/gapArticles"
newPath = "./data/gapArticles_Dic" 
filedirs = os.listdir(path)
WordDict = {}

#fileDic表示该单词在本文章中出现次数
#WordDict表示该单词在多少篇文章中出现过

for handleFile in filedirs:
    print(handleFile)
    if handleFile != '.DS_Store' :
        newDict = {}
        ArticleList = pickle.load(open(path + '/' + handleFile, "rb"))
        series = pd.Series(ArticleList)
        for index in  range(len(series)):
            print("index为",index)
            print("该单词为", series[index])

            if series[index] in newDict :
                newDict[series[index]] += 1
            else :
                newDict[series[index]] = 1
                if series[index] in WordDict :
                    WordDict[series[index]] += 1
                else :
                    WordDict[series[index]] = 1
        
        pickle.dump(newDict,open(newPath + '/' +handleFile + 'Dic' ,'wb'))


pickle.dump(WordDict,open(newPath + '/' + 'WordDic' ,'wb'))
