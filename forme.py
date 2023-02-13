import abc
from abc import ABC
from tkinter import *
import math


class FormGeo(ABC):
    def __init__(self, intitule):
        self.intitule = intitule

    def __str__(self):
        return f"Description de la figure : {self.intitule} \n"

    @abc.abstractmethod
    def Surface(self):
        pass


class Rectangle(FormGeo):
    def __init__(self, largeur, longueur, intitule):
        super().__init__(intitule)
        self.longueur = longueur
        self.largeur = largeur

    def Surface(self):
        return self.largeur * self.longueur

    def __str__(self):
        return f"forme:{FormGeo.__str__(self)} la largeur est :{self.longueur} \n la largeur est :{self.largeur} \n la surface est :{self.Surface()}"


class Cercle(FormGeo):
    def __init__(self, rayon, intitule):
        super().__init__(intitule)
        self.rayon = rayon

    def Surface(self):
        return math.pi * (self.rayon * self.rayon)

    def __str__(self):
        return f"forme:{FormGeo.__str__(self)}  le rayon est :{self.rayon} \n la surface est :{self.Surface()}"


fen = Tk()
fen.title("Forme Géométrique")
fen.geometry("1080x720")
fen.minsize(480, 240)
fen.config(background="#2F4F4F")

MDP = Label(fen, text="Mot de passe : ", background="#2F4F4F", fg="white", width=30, font=("Helvetica", 15))
MDP.pack()
MDP.place(x=200, y=100)

motdepasse = StringVar()
CASE = Entry(width=30, font=("Helvetica", 15), textvariable=motdepasse, show="*")
CASE.pack()
CASE.place(x=600, y=100)

resultat = Text(fen, width=80, height=20, font=("Helvetica", 15), background="#2F4F4F", fg="white")
resultat.pack()
resultat.place(x=200, y=300)

def Validite():
    MT = int(motdepasse.get())
    P = 12345
    if MT == P:
        TB = []
        c1 = Cercle(15, "forme circulaire")
        c2 = Cercle(10, "forme circulaire")
        R1 = Rectangle(20, 25, "forme recrtangulaire")
        R2 = Rectangle(30, 35, "forme rectangulaire")
        TB.append(c1)
        TB.append(c2)
        TB.append(R1)
        TB.append(R2)
        resultat.delete("1.0", END)
        for elt in TB:
            resultat.insert(END, elt.__str__() + "\n")
    else:
        resultat.delete("1.0", END)
        resultat.insert(END, "Mot de passe incorrect !\n")

VLD = Button(fen, text="Valider", command=Validite, activebackground="gray", width=10, font=("Helvetica", 15))
VLD.pack()
VLD.place(x=500, y=200)
fen.mainloop()
