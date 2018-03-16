import pickle

wordDict = pickle.load(open("./models/wordsDict", "rb"))

print(len(wordDict))
