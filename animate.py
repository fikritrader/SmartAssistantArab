import os
import time

def Animate():
    blink = ['misc/animation/woman-blink-0.txt','misc/animation/woman-blink-1.txt']
    durationBlink=[1,0.3]
    talk = ['misc/animation/woman-talk-1.txt','misc/animation/woman-talk-0.txt']
    durationTalk=[.2,.1]
    framesBlink = []
    framesTalk = []

    for name in blink:
        with open(name,'r',encoding="utf_8") as f:
            framesBlink.append(f.readlines())

    for name in talk:
        with open(name,'r',encoding="utf_8") as f:
            framesTalk.append(f.readlines())
    while(True):
        index=0
        file=open('misc/animation/state.txt','r')
        if file.read() == "talk":
            frames=framesTalk
            duration = durationTalk
        else:
            frames=framesBlink
            duration = durationBlink

        for frame in frames:
            os.system('cls')
            print("".join(frame))
            index=index+1
            if index==1:
                time.sleep(duration[0])
            else:
                time.sleep(duration[1])