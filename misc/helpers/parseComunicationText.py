import random
from gtts import gTTS
import speech_recognition as sr
import states.tts as ttsUtil

questionArray = []
answersArray = []
NewArrayAnswers = []
index = 0
TextQuestionWithIndex = " "
TextAnswerWithIndex = " "
language=["ara","ar"]

file=open("misc/dialogueText.txt",'r',encoding='utf_8')
text=file.read()
TextWithoutAt = text.split("@")
print(len(TextWithoutAt))
#print("the text is :"+str(TextWithoutAt))
for st in TextWithoutAt:
    print("iteration")
    TextWithoutTir = st.split("-")
    TextQuestionSplit = TextWithoutTir[0].split(":")
    for question in TextQuestionSplit:
        print("this is the lenght"+str(len(questionArray)))
        TextQuestionWithIndex = question+"#"+str(index)
        questionArray.append(TextQuestionWithIndex)
    
    TextAnswerSplit = TextWithoutTir[1].split(":")
    for question in TextAnswerSplit:
        TextAnswerWithIndex = question+"#"+str(index)
        answersArray.append(TextAnswerWithIndex)
    index = index+1

r=sr.Recognizer()
with sr.Microphone() as source:
    print("say somethng")
    audio=r.listen(source)
    print("time over, thanks")
try:
    commande=r.recognize_google(audio,language='ar')
    print("this is the thing you said" + commande)
except:
    pass

#commande = "مرحبا"
print("this is the lenght of question array"+str(questionArray))
for question in questionArray:
    textSplitByHashQ = question.split("#")
    print(commande+" - "+textSplitByHashQ[0])
    if commande == textSplitByHashQ[0]:
        index = textSplitByHashQ[1]

print("this is the index"+str(index))
for answers in answersArray:
    textSplitByHashA = answers.split("#")
    if index == textSplitByHashA[1]:
        NewArrayAnswers.append(textSplitByHashA[0])   

varRand = random.randint(0, len(NewArrayAnswers))
ans = NewArrayAnswers[varRand]
print("the answer is : "+ans)
tts=gTTS(ans,lang="ar")
tts.save('audioBase/finalAudioAnswer.mp3')
