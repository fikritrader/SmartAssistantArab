# Arab talking Smart Assistant
## Made by 
[Nouamane BITOR](https://github.com/nimotli/) - 
[Zarmoum Siham](https://github.com/SihamZR) - 
[Souad Abakarim](https://github.com/souadabakarim) - 
[Sanae Abakarim](https://github.com/sanaeaba)
## Supervised by
Professor Hajar Moussanif

## Description
This is a smart assistant like Microsoft's Cortana or Apple's Siri but its completely in arabic
it can chat (in arabic and english), fix you a plan on your schedule, alert you if you have anything on that day, get the time & date, get the weather and read an arabic text from using a camera. it works by listening to your voice commands and responding by voice also, all the commands are in arabic (requires an internet connection)

## Installation
just clone this repo
```
git clone https://github.com/nimotli/SmartAssistantArab
```
then cd to it
```
cd SmartAssistantArab
```
Preferably create a virtual envirenment (optional but recommended)
```
python -m venv venv
venv\Scripts\activate
```
and run 
```
pip install -r requirments
pip install misc\reqs\PyAudio-0.2.11-cp37-cp37m-win_amd64.whl  64bit systems
pip install misc\reqs\PyAudio-0.2.11-cp37-cp37m-win32.whl  32bit systems
cd misc\reqs\pywapi
python setup.py build
python setup.py install
cd ..
cd ..
cd ..
```
if none of the Pyaudio whl files work for you download and install the one that works in your platform from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
you need to have at least python 3.6 installed then you can just run 
or 
```
python mainApp.py
```
and you're good to go