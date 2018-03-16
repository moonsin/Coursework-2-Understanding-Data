import pickle
import os, sys
import pandas as pd


path = "./data/gapArticles"
newPath = "./data/gapArticles_Cleaned" 
WordDict = {}

filedirs = os.listdir(path)

def getDF(string):
    num =1  
    sumNum = 24
    allfiledirs = os.listdir(path)
    for filedir in allfiledirs :
        if filedir != '.DS_Store' :
            ArticleList = pickle.load(open(path + '/' + filedir, "rb"))
            if string in ArticleList :
                num += 1
    DF = num / sumNum
    return DF

filedir = 'gap_aLcWAAAAQAAJ'
newDict = {}
ArticleList = pickle.load(open(path + '/' + filedir, "rb"))
series = pd.Series(ArticleList)
for index in  range(len(series)):
    series[index] = str(series[index])
    print("index为",index)
    print("该单词为", series[index])
    if( len(series[index]) <=2) :
        print('step1')
        series[index] = '' 
    elif(series[index] in newDict ) :
        print('step2')
        series[index] = series[index]
    elif(getDF(series[index]) <0.1 or getDF(series[index]) > 0.75) :
        print('step3')
        series[index] = '' 
    print("处理过的该单词为", series[index])
    if series[index] != '' :
        if series[index] in newDict :
            newDict[series[index]] += 1
        else :
            newDict[series[index]] = 1

print(len(series))
series = series[series != ''] 
print(len(series))
pickle.dump(list1,open(newPath + '/' +filedir ,'wb'))
pickle.dump(newDict,open(newPath + '/' +filedir + 'Dic' ,'wb'))

#pickle.dump(WordDict,open(newPath + 'WordDic' ,'wb'))

#print(ArticleList[5])


