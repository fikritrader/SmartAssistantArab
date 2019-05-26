import json ,random
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from commandHelper import toggleState

def communicate():
    file=open("misc/parsedDialogue.json","r")
    dialogue=json.load(file)
    NewArrayAnswers = []
    questionArray = dialogue[0]
    answersArray = dialogue[1]
    toggleState("talk")
    playsound("audioBase/willSpeakSp.mp3")
    toggleState("idle")
    print("will start the main loop")
    comunicating=True
    while comunicating:
        index=-1
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("say something")
            audio=r.listen(source)
            print("got it")
        try:
            command=r.recognize_google(audio,language='ar')
        except:
            pass
        file=open("misc/debug/dialogueSp.txt","w",encoding="utf_8")
        file.write(command)
        file.close()
        for question in questionArray:
            textSplitByHashQ = question.split("#")
            print (u""+command+" - "+textSplitByHashQ[0])
            if command == textSplitByHashQ[0]:
                index = textSplitByHashQ[1]
        for answers in answersArray:
            textSplitByHashA = answers.split("#")
            if index == textSplitByHashA[1]:
                NewArrayAnswers.append(textSplitByHashA[0])   

        varRand = random.randint(0, len(NewArrayAnswers))
        ans = NewArrayAnswers[varRand]
        tts=gTTS(ans,lang="ar")
        tts.save('audioBase/finalAudioAnswer.mp3')
        toggleState("talk")
        playsound("audioBase/finalAudioAnswer.mp3")
        toggleState("idle")
        if(command=="رجوع"):
            comunicating=False