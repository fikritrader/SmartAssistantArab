import speech_recognition as sr


r=sr.Recognizer()
with sr.Microphone() as source:
    print('please speak')
    audio=r.listen(source)
    print('got the audio')
try:
    print('will recognize the audio')
    text=r.recognize_google(audio,language='en')
    print('recognized the audio')
except:
    pass