from playsound import playsound
import speech_recognition as sr
import os,threading,asyncio
from gtts import gTTS
import animate,readText,commandHelper
import dateRecognition,setAppointment
import getAppointment,communicate

#Animation thread
animThread=threading.Thread(target=animate.Animate)
animThread.start()

#main Ai loop
justStarted=True
if justStarted:
    commandHelper.toggleState("talk")
    playsound("audioBase/startingSp.mp3")
    commandHelper.toggleState("idle")


#waitForCommand
r=sr.Recognizer()

#ExecuteCommand

while(True):
    text=""
    if not justStarted:
        commandHelper.toggleState("talk")
        playsound("audioBase/idleSp.mp3")
        commandHelper.toggleState("idle")

    with sr.Microphone() as source:
        audio=r.listen(source)
    try:
        text=r.recognize_google(audio,language='ar')
        #file=open("misc/debug/yourCommand.txt","w",encoding="utf_8")
        #file.write(text)
        #file.close()
    except:
        pass
    rcvCommand=text.split(" ")
    readCnd=commandHelper.checkReadTextCondition(rcvCommand)
    dateCnd=commandHelper.checkDateTextCondition(rcvCommand)
    setDateCnd=commandHelper.checkSetAppointmentCondition(rcvCommand)
    getDateCnd=commandHelper.checkGetAppointmentCondition(rcvCommand)
    comCnd=commandHelper.checkCommunicationCondition(rcvCommand)
    if readCnd:
        readText.readImgText()
    elif dateCnd:
        dateRecognition.getToday()
    elif setDateCnd:
        setAppointment.setAppointment(text)
    elif getDateCnd:
        getAppointment.getAppointment()
    elif comCnd:
        communicate.communicate()
    elif text!="":
        commandHelper.toggleState("talk")
        playsound("audioBase/unknownCmdSp.mp3")
        commandHelper.toggleState("idle")
    if justStarted:
        justStarted=False


