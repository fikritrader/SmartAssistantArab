from playsound import playsound
import os,threading,asyncio
from gtts import gTTS
import animate,behaviours

rcvCommand="اقرئي هدا النص".split(" ")

animThread=threading.Thread(target=animate.Animate)
animThread.start()

if "اقرئي" in rcvCommand and "النص" in rcvCommand:
    behaviours.readImgText()
else:
    toggleState("talk")
    playsound("audioBase/unknownCmdSp.mp3")
    toggleState("idle")


