import os, sys
from bs4 import BeautifulSoup
import pickle

#soup = BeautifulSoup(open('./data/gap-html/gap_CnnUAAAAMAAJ/00000027.html'), "html5lib")
wordDict = {}
#print(soup.span.contents[0].string)
#retval = os.getcwd()
def handleString(string) :
    if string[-1].isdigit() or string[-1].isalpha() :
        return string
    else :
        if len(string) != 1 :
            string = string[0:-1]
            handleString(string)
        else :
            return string
        
def addToDict(string, Dict) :
    if string in Dict :
            Dict[string] += 1
    else :
            Dict[string] = 1



path = "./data/gap-html"
lastString = ''
isPart = False
filedirs = os.listdir(path)
for filedir in filedirs :
    newPath = path +'/' +filedir
    if os.path.isdir(newPath) :
        print(newPath)
        files = os.listdir(newPath)
        for simfile in files :
            if simfile != '.DS_Store' :
                print(simfile)
                soup = BeautifulSoup(open(newPath + '/' +simfile), "html5lib")
                for string in soup.body.stripped_strings:
                    if string == '\xad' :
                        #print("\xad")
                        isPart = True
                    else:
                        if lastString == '':
                            lastString = string
                        else :     
                            if isPart :
                                lastString = lastString + string
                                isPart = False
                            else :
                                lastString = handleString(lastString)
                                addToDict(lastString, wordDict) 
                                lastString = string

addToDict(lastString, wordDict) 
print(wordDict)

'''
#print ("当前工作目录为 %s" % retval)
for string in soup.body.stripped_strings:
    if string != '\xad' :
        print(string)
        if string[-1].isdigit() or string[-1].isalpha() :
            print('true')
        else :
            print(string[0:-1])
            print('false')
#pickle.dump(wordDict, open("./models/wordsDict", "wb"))
'''
