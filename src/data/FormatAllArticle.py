import os, sys
from bs4 import BeautifulSoup
import pickle

path = "./data/gap-html"
newFileDirPath = "./data/gapArticles"

lastString = ''
isPart = False
filedirs = os.listdir(path)
list1 = []
wordDict = {}

def ifExist(path) :
    return os.path.exists(path)

def handleString(string) :
    if not (string[-1].isdigit() or string[-1].isalpha()) :
        if len(string) != 1 :
            string = string[0:-1]
            return handleString(string)
        else :
            return string
    elif not (string[0].isdigit() or string[0].isalpha()) :
        if len(string) != 1 :
            string = string[1:len(string)]
            return handleString(string)
        else :
            return string
    else :
        return string

def addToDict(string, Dict) :
    if string in Dict :
            Dict[string] += 1
    else :
            Dict[string] = 1




if not ifExist(newFileDirPath):
   os.makedirs(newFileDirPath) 

for filedir in filedirs :
    newPath = path +'/' +filedir

    if(filedir != '.DS_Store') :
        newFilePath = newFileDirPath + '/' + filedir
        f=open(newFilePath ,'w') 

    if os.path.isdir(newPath) :
        files = os.listdir(newPath)
        for simfile in files :
            if simfile != '.DS_Store' :
                print(simfile)
                soup = BeautifulSoup(open(newPath + '/' +simfile), "html5lib")
                for string in soup.body.stripped_strings:
                    if string == '\xad' :
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
                                if lastString != None :
                                    #addToDict(lastString, wordDict) 
                                    list1.append(lastString);
                                lastString = string
                if lastString != None :
                    list1.append(lastString);
                    #addToDict(lastString, wordDict) 
                lastString = ''            
        #f.write(str(list1))
        pickle.dump(list1,open(newFilePath ,'wb'))
        list1 = []

