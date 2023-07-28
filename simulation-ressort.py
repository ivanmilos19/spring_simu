 # projet approfondissement informatique appliqué a la physique 
 # projet simulation ressort 
 # ivan milosavljevic T02
 # 2021-2022


from tkinter import *

from matplotlib import pyplot as plt

from PIL import ImageTk, Image

from math import sin, pi, cos, exp, sqrt

root = Tk()


canvas = Canvas(root,width = 400, height = 400)
img = None
image_container = canvas.create_image(0,0, anchor=NW, image = img)
canvas.grid(row = 5, column = 5,rowspan = 5,columnspan = 3)

Titre = Label(root, bg = "orange", text="Simulation de ressort")
Titre.grid(row = 0, column = 5)

blank = Label(root, text="                                  ")
blank.grid(row = 0, column = 20)

label_longueur = Label(root, text="Longueur du ressort")
label_longueur.grid(row = 2, column = 0)
Longueur = Entry(root)
Longueur.grid(row = 2, column = 2)

label_vitesse = Label(root, text="Valeur de la vitesse")
label_vitesse.grid(row = 3, column = 0)
Vitesse = Entry(root)
Vitesse.grid(row= 3, column = 2)

label_position = Label(root, text="Valeur de la position")
label_position.grid(row = 4, column = 0)
Position = Entry(root)
Position.grid(row = 4, column = 2)

label_raideur = Label(root, text="Valeur de la raideur")
label_raideur.grid(row = 6, column = 0)
Raideur = Entry(root)
Raideur.grid(row = 6, column = 2)

label_masse = Label(root, text="Valeur de la masse")
label_masse.grid(row = 7, column = 0)
Masse = Entry(root)
Masse.grid(row = 7, column = 2)

label_frott = Label(root, text="Valeur des frottements")
label_frott.grid(row = 8, column = 0)
Frott = Entry(root)
Frott.grid(row = 8, column = 2)

label_angle = Label(root, text="Valeur de l'angle")
label_angle.grid(row = 9, column = 0)
Angle = Entry(root)
Angle.grid(row  = 9, column = 2)

label_type = Label(root, text="")
label_type.grid(row = 10, column = 5)


import calculate_position as cp   

def runProgram():
    g = 9.81
    f = float(Frott.get()) 
    v0 = float(Vitesse.get())
    x0_réel = float(Position.get())
    k = float(Raideur.get())
    m = float(Masse.get())
    theta = float(Angle.get())
    L0 = float(Longueur.get())
    
    valeurs_impossibles = True
    label_type["text"] = ""
    if f < 0: 
        label_type["text"] = "les frottements doivent être positifs ou nul"
        valeurs_impossibles = False
    if k <= 0:
        label_type["text"] = "La raideur doit être positif"  
        valeurs_impossibles = False
    if m <= 0:
        label_type["text"] = "La masse doit être positif" 
        valeurs_impossibles = False
    if L0 <= 0:
        label_type["text"] = "La longueur doit être positif"
        valeurs_impossibles = False
    
    if valeurs_impossibles == False:
        return False
 
    x0 = x0_réel - m*g*sin(theta)/k - L0 

    import plotgraph as pg

    abscisse, ordonne = pg.plotgraph(20, lambda t: cp.calculate_position(t, f, v0, x0, k, m, theta, L0))

    import matplotlib.pyplot as plt
    plt.plot(abscisse, ordonne)
    plt.xlabel("Temps")
    plt.ylabel("Position")
    
    import os
    if os.path.exists("graph.png"):
        os.remove("graph.png")

    plt.savefig('graph.png')
    plt.close()

    label_type["text"] = cp.type_de_courbe

    return True

def Showgraph():
    global img
    img = None 
    
    if runProgram() == True:
        img = ImageTk.PhotoImage(Image.open("graph.png").resize((390, 390), Image.LANCZOS))

    canvas.itemconfig(image_container, image=img)
        

bouton = Button(root, bg = "orange", text = "Lancer la simulation", command=Showgraph)
bouton.grid(row = 12, column = 5)

root.mainloop()
