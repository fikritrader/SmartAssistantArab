import states.tts as ttsUtil
from gtts import gTTS
import states.readImageText as readImageText
import states.commandHelper as commandHelper


def readImgText():
    # commandHelper.toggleState("talk")
    # playsound("audioBase/willReadSp.mp3")
    # commandHelper.toggleState("idle")
    ttsUtil.say("willReadSp.mp3")
    result = readImageText.readText()
    if(result != 0):
        # commandHelper.toggleState("talk")
        # playsound("audioBase/hasReadSp.mp3")
        # commandHelper.toggleState("idle")
        ttsUtil.say("hasReadSp.mp3")

        tts=gTTS(result,"ar")
        tts.save("audioBase/tempTextSp.mp3")
        # commandHelper.toggleState("talk")
        # playsound("audioBase/tempTextSp.mp3")
        # commandHelper.toggleState("idle")
        ttsUtil.say("tempTextSp.mp3")

    else:
        # commandHelper.toggleState("talk")
        # playsound("audioBase/cantReadSp.mp3")
        # commandHelper.toggleState("idle")
        ttsUtil.say("cantReadSp.mp3")
