from tkinter import *
from random import *
from math import*

#Partie Tkinter.
Fenetre1=Tk()
Fenetre1.title('Menu Principal')

#Pour pouvoir m'être une image en Background (Arièrre Plan).
bg_image = PhotoImage(file ="fond1.png")
x = Label (image = bg_image)
x.grid(row = 0, column = 0)

Fenetre1.geometry("904x604+500+250")
Fenetre1.resizable(width='false',height='false')

#Fonction qui défini la fermeture de la fenètre.

def stopProg():
    Fenetre1.destroy()

#Fonction qui défini le changement de page entre le "Menu Principal" et le "Labyrinthe" mode 1.
def show_next():
    Fenetre1.destroy()
    import Lelabi.py

#Fonction qui défini le changement de page entre le "Menu Principal" et le "Labyrinthe" mode 2.
def show_next1():
    Fenetre1.destroy()
    import Lelabi2.py

#On ajoute le 2 images pour les boutons "Quitter" et "Mode 1".
stop_image = PhotoImage(file ="buttonquit.png")
mi_but=PhotoImage(file="button.png")

#Partie des boutons.
Bouton_Lab1=Button(Fenetre1,image=mi_but,borderwidth=0,command=show_next,font = ("Helvetica", 15))
Bouton_Lab1.place(x=345,y=260)

Bouton_Lab2=Button(Fenetre1,image=mi_but,borderwidth=0,command=show_next1,font = ("Helvetica", 20))
Bouton_Lab2.place(x=345,y=332)

Bouton_Quitter=Button(Fenetre1,image=stop_image,borderwidth=0,command=stopProg,font=("Helvetica", 25))
Bouton_Quitter.place(x=342,y=460)

Fenetre1.mainloop()