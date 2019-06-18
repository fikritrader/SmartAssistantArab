from datetime import datetime
from gtts import gTTS
from playsound import playsound
import re
from states.commandHelper import toggleState

def getAppointment():
    foundAppointment=False
    appointments=open("misc/appointments.txt","r",encoding="utf_8").readlines()
    forbid=["سجل","تسجيل","موعد","يوم","\ufeffسجل","\ufeffتسجيل","سجلي","حجز","تسجلي","لقاء"]
    for line in appointments :
        digitsInLine=[]
        digitsInLine=re.findall('\d+', line)
        DateInLine=[]
        DateInLine+=digitsInLine
        formatedDate=DateInLine[2]+"-"+DateInLine[1]+"-"+DateInLine[0]
        maintenant = datetime.now()
        dt=str(maintenant.date())
        if (formatedDate == dt):
            foundAppointment=True
            wordsInLine = line.split(" ")
            appointmentType=""
            for word in wordsInLine :
                if not word in forbid and not(word.isdecimal()):
                    appointmentType = appointmentType + " " + word
            outpuText="نَعَمْ لَدَيْكَ مَوْعِدٌ "+appointmentType
            tts=gTTS(outpuText,"ar")
            tts.save("audioBase/appointmentTempSp.mp3")     
            toggleState("talk")
            playsound("audioBase/appointmentTempSp.mp3")
            toggleState("idle")
    if foundAppointment==False:
        toggleState("talk")
        playsound("audioBase/noAppointmentSp.mp3")
        toggleState("idle")