import pywapi
from gtts import gTTS
import speech_recognition as sr
from playsound import playsound

language=["ara","ar"]
r=sr.Recognizer()


def main():
    #print("Enter a city name for weather forecast : ")
    #cityName = input()
    cityName = "Morocco"
    lookups = pywapi.get_location_ids(cityName)
    for lookup in lookups:
        location_id = lookup
    
    weather_com_result = pywapi.get_weather_from_weather_com(location_id)
    print(weather_com_result['forecasts'][0]['day_of_week'])
    print(weather_com_result['forecasts'][0]['high'])
    print(weather_com_result['forecasts'][0]['low'])
    print(weather_com_result['forecasts'][0]['day']['icon'])
    print(weather_com_result['forecasts'][0]['day']['text'])

    temperature = weather_com_result['forecasts'][0]['day']['icon']
    HightTemp = weather_com_result['forecasts'][0]['high']
    LowTemp = weather_com_result['forecasts'][0]['low']
    textWeather = weather_com_result['forecasts'][0]['day']['text']

    if textWeather == "Partly Cloudy":
        textWeather = "غائم جزئيا"
    elif textWeather == "Cloudy":
        textWeather = "غائم"
    elif textWeather == "Sunny":
        textWeather = "مشمس"
    elif textWeather == "Mostly Sunny":
        textWeather = "في الغالب مشمس"
    else:
        textWeather = "معتدل"

    mystring= "الجو حاليا يصل إلى"+temperature+"درجة  أما فيما يخص أقصى درجة حرارة فاليوم ستصل إلى"+HightTemp+"درجة  و أدنى درجة حرارة هي"+LowTemp+" درجة  و إنطلاقا من المعطيات يمكن القول أن الجو"+textWeather

    tts=gTTS(mystring,lang="ar")
    tts.save('audioBase/AudioWeather.mp3')
    
if __name__ == "__main__":
    main()