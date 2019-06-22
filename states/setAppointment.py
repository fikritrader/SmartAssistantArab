from gtts import gTTS
from playsound import playsound
from states.commandHelper import toggleState
def setAppointment(command):
    months=["يناير","فبراير","مارس","ابريل","ماي","يونيو","يوليوز","غشت","شتنبر","اكتوبر","نونبر","دجنبر"]
    foundMonth=False
    while(foundMonth == False):
        for month in months:
            if month in command:
                foundMonth=True
                monthvalue = months.index(month)+1
                if monthvalue<= 9:
                    monthvalue="0"+str(monthvalue)
                    appointmentText= command.replace(month,monthvalue)
                    toggleState("talk")
                    playsound("audioBase/wasRecordedSp.mp3")
                    toggleState("idle")
                    f=open('misc/appointments.txt', 'ab')
                    f.write(str(appointmentText+"\n").encode('utf-8')) 
                break
        if foundMonth==False:
            toggleState("talk")
            playsound("audioBase/noMonthSp.mp3")     
            toggleState("idle")
            break