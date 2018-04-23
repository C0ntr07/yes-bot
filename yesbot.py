#!/usr/bin/env python3
from tkinter import *
from tkinter.font import Font
import pygame.mixer

def sayYes():
    yes_en.play()

def shutdown():
    sounds.stop()
    app.destroy()

app = Tk()
app.title("Yes Bot")
app.geometry('450x120+200+100')
app.resizable(False, False)
sounds = pygame.mixer
sounds.init()

yes_en = sounds.Sound("wav/c-falcon_YES.wav") # You can replace this sound with any other voice saying "yes." Be sure to replace the "c-falcon_YES.wav" in this line with the new recorded sound file that you saved in the wav folder.
                                              # For French speaking telemarketers, say "oui."
                                              # For Spanish speaking telemarketers, say "si."
myFont = Font(family = "Arial", size = 12)
lab = Label(app, text = 'Annoy those telemarketers with one word.', # French: Agiter les télévendeurs avec un mot.
            height = 3, font = myFont)                              # Spanish: Molestar a los agentes de telemercadeo con una sola palabra.
lab.pack(side = TOP)
btn = Button(app, text = "\"Yes\"",                       # French: Oui
             width = 10, command = sayYes, font = myFont) # Spanish: Si
btn.pack(side = TOP)
app.protocol("WM_DELETE_WINDOW", shutdown)
app.mainloop()
