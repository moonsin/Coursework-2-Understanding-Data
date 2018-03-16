import pickle
import numpy  as np

filename = './data/FinalVectors'
FinalVectors = pickle.load(open(filename,'rb'))
newVectorsSet = np.zeros((24, FinalVectors.columns.size))

#print(len(FinalVectors.loc['gap_2X5KAAAAYAAJDicVector']))
# 防止科学计数法
#np.set_printoptions(precision=5, suppress=True)

i = 0
for index in FinalVectors.index:
    wordNum = 0
    for index2 in range(len(FinalVectors.loc[index])):
        wordNum += FinalVectors.loc[index][index2]
    for index3 in range(len(FinalVectors.loc[index])):
        newVectorsSet[i][index3] = FinalVectors.loc[index][index3] / wordNum
        print(newVectorsSet[i][index3])
    i = i+1
    print(index)
    print(wordNum)


pickle.dump(newVectorsSet,open('./data/FinalVectors_TF' ,'wb'))

