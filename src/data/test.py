import pickle
import os, sys
import pandas as pd



path = "./data/VectorsForArticles/gap_2X5KAAAAYAAJDicVector"
newPath = "./data/gapArticles_Dic"

WordDict = pickle.load(open(path, "rb"))

print(WordDict)
