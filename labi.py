from tkinter import *
from random import *
from math import*
import pygame
from pygame.locals import *
from algorandom import algorandom
import time

Fenetre2=Tk()
Fenetre2.title('Mode 1 | Labyrinthe')
Fenetre2.geometry("904x604+500+250")
Fenetre2.resizable(width='false',height='false')

def stopProg():
    Fenetre2.destroy()

def labi():
    import Maze.py

Bouton_start=Button(Fenetre2,text="test",borderwidth=0,command=labi,font=("Helvetica", 25))
Bouton_start.place(x=450,y=300)

stop_image = PhotoImage(file ="buttonquit.png")
Bouton_Quitter=Button(Fenetre2,image=stop_image,borderwidth=0,command=stopProg,font=("Helvetica", 25))
Bouton_Quitter.place(x=705,y=550)

Fenetre2.mainloop()