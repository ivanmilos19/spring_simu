# NOM: calculate_position
# DESCRIPTION: Donne une valeur qui correspond a la position du ressort en un temps dnne
# ENTREES : t(temps), f(frottements), v0(vitesse initiale), x0(position initiale), k(raideur), m(masse), theta(angle), L0(longueur du ressort)
# SORTIE: Valeur de la position en un temps donné

from math import sin, cos, exp, sqrt

# une variable globale de ce module qui indique la nature de l'oscillation
type_de_courbe = None

def calculate_position(t, f, v0, x0, k, m, theta, L0): 

    global type_de_courbe

    gamma = f/m
    w0 = sqrt(k/m)
    delta = gamma**2 - 4*w0**2
    g = 9.81
    
    F = m*g*sin(theta)/k + L0
    

    if f == 0:
        A = x0
        B = v0/w0
        type_de_courbe = "C'est une courbe periodique"       
        return  A*cos(w0*t) + B*sin(w0*t) + F


    if delta < 0:
        w1 = sqrt(w0**2 - (gamma**2/4))
        A = x0
        B = 2*v0 + x0*gamma / (2*w1)
        type_de_courbe = "C'est une courbe pseudo-périodique"       
        return exp(-gamma/2*t) * (A*cos(w1*t) + B*sin(w1*t)) + F
    
    elif delta > 0:
        w1 = sqrt(gamma**2/4-w0**2)
        B = (2*v0 + gamma*x0 - 2*w1*x0) / (-4*w1)
        A = x0 - B
        type_de_courbe = "C'est une courbe apériodique"        
        return exp(-gamma/2*t) * (A*exp(w1*t) + B*exp(-w1*t)) + F
 
    
    else:
        A = x0
        B = v0 + gamma*x0/2
        type_de_courbe = "C'est une courbe critique"       
        return exp(-gamma/2*t) * (A + B*t) + F