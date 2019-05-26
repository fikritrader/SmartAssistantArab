import datetime,re,commandHelper
from gtts import gTTS
from playsound import playsound

def getToday():
    todaytime =  datetime.datetime.now()
    possible_characters = (':', ' ', '-', '.')
    date = re.split("[%s]" % ("".join(possible_characters)), str(todaytime))

    months= ["يناير","فبراير","مارس","ابريل","ماي","يونيو","يوليوز","غشت","شتنبر","اكتوبر","نونبر","دجنبر"]
    day = months[int(date[1])-1]

    text = "اليوم هو"+date[2]+ " من "+day+ " لعام  "+date[0]+ "والسَاعةُ تشير إلى"+date[3]+ "وَ"+date[4]+"دقيقة"
    tts = gTTS(text=text, lang='ar')
    tts.save("audioBase/dateTime.mp3")
    commandHelper.toggleState("talk")
    playsound("audioBase/dateTime.mp3")
    commandHelper.toggleState("idle")
