import re
import numpy as np
import json
import time
from keras.preprocessing.text import Tokenizer
print() # no emoji

file = open('dataSets/arabchatDataset.txt','r',encoding="utf_8")
test = file.readlines()
file = open('new.txt','w',encoding="utf_8")

vocabularyQues=[]
vocabularyAns=[]

i=0
emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

outerTable='0123456789\'".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS)TUVWXYZ/@ᖇᗩᗰᗩᗪᗩᑎнυєɪиαв_=#>&%:،'
maxQues=0
maxAns=0
Questions=[]
Answers=[]
for line in test:
    remove_digits = str.maketrans('','',outerTable)
    res=emoji_pattern.sub(r'', line)
    res = res.translate(remove_digits)
    hasQuesAns=res.split(',')


    if len(hasQuesAns) > 1:
        Questions.append(hasQuesAns[1])
        Answers.append(hasQuesAns[0])
        vocabularyQues.extend(hasQuesAns[1].split(' '))
        vocabularyAns.extend(hasQuesAns[0].split(' '))
        lenAns=len(hasQuesAns[0].split(' '))
        lenQues=len(hasQuesAns[1].split(' '))
        if lenAns>maxAns:
            maxAns=lenAns
        if lenQues>maxQues:
            maxQues=lenAns
    i=i+1
    print('line ',i )
    file.write(res)
file.close()
dictionnaryQues=set(vocabularyQues)
dictionnaryAns=set(vocabularyAns)

quesWordToInt=dict()
quesIntToWord=dict()
ansWordToInt=dict()
ansIntToWord=dict()

for i,word in enumerate(dictionnaryQues):
    quesWordToInt[word] = i
    quesIntToWord[i]    = word
for i,word in enumerate(dictionnaryAns):
    ansWordToInt[word] = i
    ansIntToWord[i]    = word

timeBeforData=time.time()
dataSetMatrix=[Questions,Answers]
t = Tokenizer()
t.fit_on_texts(dataSetMatrix)
print('the lenght of the question dictionary is :',len(dictionnaryQues))
print('the lenght of the answer dictionary is :',len(dictionnaryAns))

# summarize what was learned
open('file.txt','w',encoding="utf_8").write(str(t.word_counts))

#finalArray for questions
#dataMatrix=np.zeros((10,len(dictionnaryQues)),dtype="int8")
#for i in range(0,10):
#    print("generating the line {} of the questions data matrix".format(i))
#    vector=np.zeros((len(dictionnaryQues)),dtype="int8")
#    for word in Questions[i].split(' '):
#        vector[quesWordToInt[word]]=1
#    dataMatrix[i,:]=vector

#sparseDataMatrix=sparse.csr_matrix(dataMatrix)
#file=open("chatModel/data/dataMarix.json","w",encoding="utf_8")
#json.dump(sparseDataMatrix.tolist(),file)
#file.close()
#print(sparseDataMatrix)
#print(dataMatrix.shape)

maxWords=10000

timeNeeded=time.time()-timeBeforData
print("it took :",str(round(timeNeeded,2)),"sec to finish the data making")
tokenize=Tokenizer()