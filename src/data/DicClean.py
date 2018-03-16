import pickle
import os, sys
import pandas as pd


path = "./data/gapArticles_Dic/WordDic"
newPath = "./data/gapArticles_Dic"

ArticleList = pickle.load(open(path, "rb"))

#ArticleList =  ArticleList[ArticleList != '1']
#print(ArticleList[ArticleList >1])

ser = pd.Series(ArticleList)
#print(ser)
ser = ser[ser >2]
ser = ser[ser<17]
ser = dict(ser)

#df = pd.DataFrame(ser)
print(len(ser))
for index in ser:
    if(len(index) < 2) :
        ser[index] = 0

ser = pd.Series(ser)
ser = ser[ser !=0]
ser = dict(ser)

print(len(ser))

pickle.dump(ser,open(newPath + '/' + 'WordDic_Cleaned' ,'wb'))

