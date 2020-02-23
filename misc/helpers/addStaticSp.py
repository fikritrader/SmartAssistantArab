from gtts import gTTS
from io import BytesIO
import states.tts as ttsUtil

text='oh! i don\'t think i know any stories of this genre'
name="noStories"

tts=gTTS(text,"en")
tts.save("audioBase/"+name+".mp3")
ttsUtil.say(name+".mp3")