import cv2
from pathlib import Path
from matplotlib import pyplot

from generation import *


def main ():
    
    
    # Initialisation
    
    nbLignes = 3
    nbColonnes = 4
    compteur = 1


    # Read images

    cheminImages = str (Path (__file__). resolve (). parent) + "/images/"
    
    
    # Treat them
    
    imageBlanche    = blanche ()
    imageNoire      = noire ()
    imageRose       = rose ()
    imageBleue      = bleue ()
    imageDrapeau    = drapeau ()
    imageCercle     = cercle ()
    imageCarres     = carres ()
    imageDegrades   = degrades ()
    imageSapinsNoel = sapinsNoel ()
    imageFractale   = fractale ()
    
    
    # Show result
    
    pyplot. subplot (nbLignes, nbColonnes, compteur)
    pyplot. imshow (imageBlanche)
    pyplot. title ("")
    compteur += 1

    pyplot. subplot (nbLignes, nbColonnes, compteur)
    pyplot. imshow (imageNoire)
    pyplot. title ("")
    compteur += 1

    pyplot. subplot (nbLignes, nbColonnes, compteur)
    pyplot. imshow (imageRose)
    pyplot. title ("")
    compteur += 1

    pyplot. subplot (nbLignes, nbColonnes, compteur)
    pyplot. imshow (imageBleue)
    pyplot. title ("")
    compteur += 1

    pyplot. subplot (nbLignes, nbColonnes, compteur)
    pyplot. imshow (imageDrapeau)
    pyplot. title ("")
    compteur += 1

    pyplot. subplot (nbLignes, nbColonnes, compteur)
    pyplot. imshow (imageCercle)
    pyplot. title ("")
    compteur += 1

    pyplot. subplot (nbLignes, nbColonnes, compteur)
    pyplot. imshow (imageCarres)
    pyplot. title ("")
    compteur += 1

    pyplot. subplot (nbLignes, nbColonnes, compteur)
    pyplot. imshow (imageDegrades)
    pyplot. title ("")
    compteur += 1

    pyplot. subplot (nbLignes, nbColonnes, compteur)
    pyplot. imshow (imageSapinsNoel)
    pyplot. title ("")
    compteur += 1

    pyplot. subplot (nbLignes, nbColonnes, compteur)
    pyplot. imshow (imageFractale)
    pyplot. title ("")
    compteur += 1
    
    
    pyplot.show ()


main ()
