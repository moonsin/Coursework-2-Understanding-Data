import pickle
import numpy  as np
import math

filename = './data/FinalVectors_TF'
wordDictpath = './data/gapArticles_Dic/WordDic_Cleaned'

FinalVectors = pickle.load(open(filename,'rb'))
wordDict = pickle.load(open(wordDictpath,'rb'))

print(math.log10(10))
print(FinalVectors)
list1 = []

for key in wordDict :
    list1.append(wordDict[key])

for i in range(len(FinalVectors)) :
    for index in range(len(FinalVectors[i])) :
        print(FinalVectors[i][index])
        FinalVectors[i][index] = FinalVectors[i][index] * math.log10(24/ list1[i])
        print(FinalVectors[i][index])


pickle.dump(FinalVectors,open('./data/FinalVectors_TFIDF' ,'wb'))
