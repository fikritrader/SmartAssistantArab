from playsound import playsound
import speech_recognition as sr
import os,threading,asyncio
from gtts import gTTS
import animate
import states.readText as readText
import states.commandHelper as commandHelper
import states.dateRecognition as dateRecognition
import states.setAppointment as setAppointment
import states.getAppointment as getAppointment
import states.communicate as communicate
#import states.weatherCommande as weatherCommande
import states.predictIntent as predictIntent
import states.utilityState as utilityState
#import states.chat as chat
#Animation thread
animThread=threading.Thread(target=animate.Animate)
#animThread.start()

#main Ai loop
justStarted=True
if justStarted:
    commandHelper.toggleState("talk")
    playsound("audioBase/startingSp.mp3")
    commandHelper.toggleState("idle")


#waitForCommand
r=sr.Recognizer()

#ExecuteCommand
intents = ['speak','weather','remind me','schedule today','silence','read this','date','api']
while(True):
    text=""
    if not justStarted:
        commandHelper.toggleState("talk")
        playsound("audioBase/idleSp.mp3")
        commandHelper.toggleState("idle")

    with sr.Microphone() as source:
        print('speak')
        audio=r.listen(source)
    try:
        #text = input('your command : \n')
        print('got it will now recognize')
        text=r.recognize_google(audio,language='ar')
        print('recognized')
        file=open("misc/debug/yourCommand.txt","w",encoding="utf_8")
        file.write(text)
        file.close()
    except:
        pass
    intent = predictIntent.predict(text)
    # print('the intent is',intents[intent])
    # continue
    #rcvCommand=text.split(" ")

    intents = ['speak','weather','remind me','schedule today','silence','read this','date','api']
    options = [communicate.communicate,None,lambda x :setAppointment.setAppointment(x) ,
    getAppointment.getAppointment, None, readText.readImgText, dateRecognition.getToday,utilityState.utilityState]
    if intent != 2:
        options[intent]()
    else:
        options[intent](text)

    # readCnd=commandHelper.checkReadTextCondition(rcvCommand)
    # dateCnd=commandHelper.checkDateTextCondition(rcvCommand)
    # setDateCnd=commandHelper.checkSetAppointmentCondition(rcvCommand)
    # getDateCnd=commandHelper.checkGetAppointmentCondition(rcvCommand)
    # comCnd=commandHelper.checkCommunicationCondition(rcvCommand)
    # wheatherCnd=commandHelper.checkWeather(rcvCommand)
    # exitCnd=commandHelper.checkSilence(rcvCommand)
    # chatCnd=commandHelper.checkChat(rcvCommand)
    # if intents == 0:
    #     readText.readImgText()
    # elif dateCnd:
    #     dateRecognition.getToday()
    # elif setDateCnd:
    #     setAppointment.setAppointment(text)
    # elif getDateCnd:
    #     getAppointment.getAppointment()
    # elif comCnd:
    #     communicate.communicate()
    # elif wheatherCnd:
    #     continue
    #     #weatherCommande.getWeather()
    # elif chatCnd:
    #     chat.chatEng()
    # elif exitCnd:
    #     commandHelper.toggleState("talk")
    #     playsound("audioBase/bySp.mp3")
    #     commandHelper.toggleState("idle")
    #     break;
    # elif text!="":
    #     commandHelper.toggleState("talk")
    #     playsound("audioBase/unknownCmdSp.mp3")
    #     commandHelper.toggleState("idle")
    if justStarted:
        justStarted=False


