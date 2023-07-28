import plotgraph as pg

def fonction(x):
    return 3 * x

abscisse, ordonne = pg.plotgraph(0.3, fonction)
print("abscisse", abscisse)
print("ordonne", ordonne)
