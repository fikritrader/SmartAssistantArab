from playsound import playsound
from gtts import gTTS
import states.readImageText as readImageText
import states.commandHelper as commandHelper


def readImgText():
    commandHelper.toggleState("talk")
    playsound("audioBase/willReadSp.mp3")
    commandHelper.toggleState("idle")

    result = readImageText.readText()
    if(result != 0):
        commandHelper.toggleState("talk")
        playsound("audioBase/hasReadSp.mp3")
        commandHelper.toggleState("idle")
        tts=gTTS(result,"ar")
        tts.save("audioBase/tempTextSp.mp3")
        commandHelper.toggleState("talk")
        playsound("audioBase/tempTextSp.mp3")
        commandHelper.toggleState("idle")
    else:
        commandHelper.toggleState("talk")
        playsound("audioBase/cantReadSp.mp3")
        commandHelper.toggleState("idle")