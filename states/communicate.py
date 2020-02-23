import json ,random,os
from gtts import gTTS
import speech_recognition as sr
from states.commandHelper import toggleState
import states.tts as ttsUtil

def communicate():
    file=open("misc/parsedDialogue.json","r")
    dialogue=json.load(file)
    questionArray = dialogue[0]
    answersArray = dialogue[1]
    # toggleState("talk")
    # playsound("audioBase/willSpeakSp.mp3")
    # toggleState("idle")
    ttsUtil.say("willSpeakSp.mp3")
    print("will start the main loop")
    comunicating=True
    i=0
    while comunicating:
        NewArrayAnswers=[]
        index=-1
        i=i+1
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
        command=command.replace('أ','ا')
        command=command.replace('إ','ا')
        command=command.replace('آ','ا')
        command=command.replace('ة','ه')
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
        if len(NewArrayAnswers)>0:
            varRand = random.randint(0, len(NewArrayAnswers)-1)
            ans = NewArrayAnswers[varRand]
            tts=gTTS(ans,lang="ar")
            tts.save('audioBase/finalAudioAnswer'+str(i)+'.mp3')
            # toggleState("talk")
            # playsound("audioBase/finalAudioAnswer"+str(i)+".mp3")
            # toggleState("idle")
            ttsUtil.say("finalAudioAnswer.mp3")

            os.remove('audioBase/finalAudioAnswer'+str(i)+'.mp3')
        else:
            # toggleState("talk")
            # playsound("audioBase/noUnderstandSp.mp3")
            # toggleState("idle")
            ttsUtil.say("noUnderstandSp.mp3")
        if(command=="رجوع"):
            comunicating=False