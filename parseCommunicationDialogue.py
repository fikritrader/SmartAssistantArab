#This script is for turning the dialogue txt file into a json object 
#to ease the search and response for the communication module

import json
questionArray = []
answersArray = []
index = 0

file=open("misc/dialogueText.txt",'r',encoding='utf_8')
text=file.read()
TextWithoutAt = text.split("@")
print(len(TextWithoutAt))
for st in TextWithoutAt:
    print("iteration")
    
    TextWithoutTir = st.split("-")
    TextQuestionSplit = TextWithoutTir[0].split(":")
    for question in TextQuestionSplit:
        print("this is the lenght"+str(len(questionArray)))
        question=question.replace('إ','ا')
        question=question.replace('آ','ا')
        question=question.replace('أ','ا')
        question=question.replace('ة','ه')
        TextQuestionWithIndex = question+"#"+str(index)
        questionArray.append(TextQuestionWithIndex)
    
    TextAnswerSplit = TextWithoutTir[1].split(":")
    for question in TextAnswerSplit:
        TextAnswerWithIndex = question+"#"+str(index)
        answersArray.append(TextAnswerWithIndex)
    index = index+1
dialogue=[questionArray,answersArray]
jsonFile=open("misc/parsedDialogue.json","w")
json.dump(dialogue,jsonFile)
print("dialogue parsed")