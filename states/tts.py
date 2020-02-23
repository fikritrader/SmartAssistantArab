import pygame
import states.commandHelper as commandHelper
def say(fileName):
    commandHelper.toggleState("talk")
    pygame.mixer.init()
    pygame.mixer.music.load("audioBase/"+fileName)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    commandHelper.toggleState("idle")
