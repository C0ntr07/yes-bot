#!/usr/bin/env python
from tkinter import *
import pygame.mixer

def sayYes():
    yes_en.play()

app = Tk()
app.title("Yes Bot")
app.geometry('350x100+200+100')
app.resizable(False, False)
sounds = pygame.mixer
sounds.init()

yes_en = sounds.Sound("wav/c-falcon_YES.wav") # You can replace this sound with any other voice saying "yes."
                                              # For French speaking telemarketers, say "oui."
                                              # For Spanish speaking telemarketers, say "si."

lab = Label(app, text='Annoy those telemarketers with one word.', height = 3) # French: Agiter les télévendeurs avec un mot.
                                                                              # Spanish: Molestar a los agentes de telemercadeo con una sola palabra.
lab.pack(side = TOP)

btn = Button(app, text = "\"Yes\"", width = 10, command = sayYes) # French: Oui
                                                                  # Spanish: Si
btn.pack(side = TOP)

app.mainloop()
