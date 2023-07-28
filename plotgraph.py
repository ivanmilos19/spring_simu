def plotgraph(tmax, f):

# NOM: plotgraph
# DESCRIPTION: tracerune courbe d’une fonction en fonction du temps et va la convertir en image
# ENTREES: tmax, f
# SORTIE: la liste des points 
   
    abscisse = []
    ordonne = []
    t = 0
    while t < tmax:
        ordonne.append(f(t))
        abscisse.append(t)
        t += 0.1
    
    return (abscisse, ordonne)