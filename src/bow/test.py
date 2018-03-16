import pickle
import os, sys
import pandas as pd
import csv
import numpy  as np
import matplotlib.pyplot as plt


filename = './data/FinalVectors'


FinalVectors = pickle.load(open(filename,'rb'))

ArticleNameList = [] 

for index in FinalVectors.index :
    ArticleNameList.append(index)

ArticleNameList = np.array(ArticleNameList)

filename = './data/FinalVectors_TFIDF'
FinalVectors_standered = pickle.load(open(filename,'rb'))

FinalVectors_standered = pd.DataFrame(FinalVectors_standered, index = ArticleNameList)

pickle.dump(FinalVectors_standered,open('./data/FinalVectors_TFIDF' ,'wb'))

