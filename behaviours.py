from playsound import playsound
from gtts import gTTS
import readImageText
def toggleState(st):
    file=open('misc/animation/state.txt','w')
    file.write(st)
    file.close()

def readImgText():
    toggleState("talk")
    playsound("audioBase/willReadSp.mp3")
    toggleState("idle")

    result = readImageText.readText()
    if(result != 0):
        toggleState("talk")
        playsound("audioBase/hasReadSp.mp3")
        toggleState("idle")
        tts=gTTS(result,"ar")
        tts.save("audioBase/tempTextSp.mp3")
        toggleState("talk")
        playsound("audioBase/tempTextSp.mp3")
        toggleState("idle")
    else:
        toggleState("talk")
        playsound("audioBase/cantReadSp.mp3")
        toggleState("idle")