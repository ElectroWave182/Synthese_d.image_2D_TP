from numpy import *


def blanche ():

    image = [[[255, 255, 255]]]
    return array (image)


def noire ():
    
    image = [[[0, 0, 0]]]
    return array (image)



def rose ():
    
    image = [[[255, 140, 150]]]
    return array (image)



def bleue ():
    
    image = [[[50, 50, 200]]]
    return array (image)



def drapeau ():
    
    image = [[[200, 200, 50], [200, 200, 50]], [[50, 50, 200], [50, 50, 200]]]
    return array (image)



def cercle ():
    
    image = [[[0, 0, 0]]]
    return array (image)



def carres ():
    
    image = [[[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]], [[255, 255, 255], [255, 140, 150], [255, 140, 150], [255, 255, 255], [255, 255, 255]], [[255, 255, 255], [255, 140, 150], [0, 0, 0], [50, 50, 200], [255, 255, 255]], [[255, 255, 255], [255, 255, 255], [50, 50, 200], [50, 50, 200], [255, 255, 255]], [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]]]
    return array (image)



def degrades ():
    
    image = [[[ligne, ligne, ligne] for ligne in range (256)] for colonne in range (256)]
    return array (image)


def sapinsNoel ():
    
    image = [[[100, 200, 100] if dansSapin (ligne, colonne) else [255, 255, 255] for ligne in range (256)] for colonne in range (256)]
    return array (image)

def dansSapin (x, y):

    dans = False
    dans = dans or abs (x - 128) < y // 2 - 8  and y < 50
    dans = dans or abs (x - 128) < y // 2 - 16 and 50 < y < 100
    dans = dans or abs (x - 128) < y // 2 - 24 and 100 < y < 150
    dans = dans or abs (x - 128) < y // 2 - 32 and 150 < y < 200
    dans = dans or 100 < x < 156 and 200 < y 

    return dans



def fractale ():
    
    image = [[[255, 255, 255] for ligne in range (265)] for colonne in range (265)]
    recFractale (image, x = 0, y = 0, ampleur = 8)
    return array (image)

def recFractale (image, x, y, ampleur):

    # Cas récursif
    if ampleur != 0:
        rayon = 2 ** ampleur
        xIncrement, yIncrement = direction (ampleur % 4)
        for _ in range (rayon):
            for largeur in range (ampleur):
                image [x + largeur * yIncrement] [y + largeur * xIncrement] = [50, 50, 200]
            x += xIncrement
            y += yIncrement
        ampleur -= 1
        recFractale (image, x, y, ampleur)

    # Cas de base : factale trop petite

def direction (id):

    match id:
        case 0: return (0, 1)
        case 1: return (-1, 0)
        case 2: return (0, -1)
        case 3: return (1, 0)
        case other:
            print ("Erreur : identifiant de direction différent de 0, 1, 2 et 3")
            exit (1)
