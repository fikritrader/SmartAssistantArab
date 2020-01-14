from gtts import gTTS
from io import BytesIO
from playsound import playsound

text='oh! i don\'t think i know any stories of this genre'
name="noStories"

tts=gTTS(text,"en")
tts.save("audioBase/"+name+".mp3")
playsound("audioBase/"+name+".mp3")
