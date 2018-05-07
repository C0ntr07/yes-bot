#!/usr/bin/env python3
from tkinter import *
from tkinter.font import Font
import pygame.mixer

def sayYes():
    yes_s.play()

def key(event):
    yes_s.play()

def shutdown():
    sounds.stop()
    app.destroy()

app = Tk()
app.title("Yes Bot")
app.geometry('450x120+200+100')
app.resizable(False, False)
myFont = Font(family = "Arial", size = 12)
sounds = pygame.mixer
sounds.init()
yes_s = sounds.Sound("wav/c-falcon_YES.wav")
#                    You can replace this sound with any other voice saying
#                    "yes." Be sure to replace the "c-falcon_YES.wav" in this
#                    line with the new recorded sound file that you saved in
#                    the wav folder.
#                    For French speaking telemarketers, say "oui."
#                    For Spanish speaking telemarketers, say "si."
lab = Label(
    app,
    text = 'Annoy those telemarketers with one word.',
#          French: Agiter les télévendeurs avec un mot.
#          Spanish: Molestar a los agentes de telemercadeo con una sola palabra.
    height = 3,
    font = myFont
)
lab.pack(side = TOP)
btn = Button(
    app,
    text = "\"Yes\"",
#          French: Oui
#          Spanish: Si
    width = 10,
    command = sayYes,
    font = myFont
)
btn.pack(side = TOP)
app.bind("<Key>", key)
app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()
