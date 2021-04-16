"""
Escape game
Auteur: Lise AMEN
Date : 10 octobre 2018
"""


from src.CONFIGS import *
from datasets import *

from math import *

from turtle import *

# importing package
import turtle

def tracer_carre(coord, couleur, dimension):
    """tracer_case [summary]
    recoit en arguments un couple de coordonnées en indice dans la matrice contenant le plan, une couleur, 
    et un pas (taille d'un côté) et qui va tracer un carré d’une certaine 
    couleur et taille à un certain endroit
    """
    turtle.penup()
    turtle.setposition(coord)
    turtle.pendown()
    s = dimension

    # set the fillcolor
    turtle.fillcolor(couleur)

    # start the filling color
    turtle.begin_fill()

    # drawing the square of side s
    for _ in range(4):
        turtle.forward(s)  # Forward turtle by s units
        turtle.left(90)  # Turn turtle by 90 degree

    # ending the filling of the color
    turtle.end_fill()
    turtle.penup()


def calculer_pas():
    """
    calcule la dimension à donner aux cases pour que le plan tienne dans la zone de la fenêtre 
    turtle définie, la largeur et la hauteur de la zone est divisée par le nombre de cases qu’elle doit
    accueillir, la fonction retourne la valeur la plus faible des deux.
    """
    f = open("datasets/plan_chateau.txt", "r")
    text = f.readlines()
    NumberOfLine = len(text)
    #print('Nombre de lignes :', NumberOfLine)
    NumberOfColumn = len(text[0])//2
    #print('Nombre de colonnes :', NumberOfColumn)
    LargueurCarre = LARGEUR_PLAN//NumberOfLine
    LongueurCarre = LONGUEUR_PLAN//NumberOfLine
    if LargueurCarre > LongueurCarre:
        return LongueurCarre
    else:
        return LargueurCarre


def lire_matrice():
    """
    La fonction lit le plan du château et l'enregistre dans
    une matrice 
    """
    with open("datasets/plan_chateau.txt", "r") as plan:
        lines = plan.readlines()
    plan = []
    for l in lines:
        as_list = l.split(",")
        plan.append([as_list[0].replace('\n', '')])
    return plan


def transformer_coordonnees(case):
    """
    Calcule les coordonnées en pixels turtle du coin inférieur gauche d’une case définie par ses coordonnées 
    (numéros de ligne et de colonne).
    La fonction retourne les coordonnées en pixels turtle calculées
    """
    pas = calculer_pas()
    coord = (-case[0]*pas + 10*pas, case[1]*pas - 13*pas)
    return coord 

def transformer_coordonnees_caractere(case):
    """
    Calcule les coordonnées des caractères du fichier texte
    """
    pas = calculer_pas()
    coord = (floor((-case[0]+ 10*pas)/pas), floor((case[1] + 13*pas)/pas))
    return coord 


def tracer_map(matrice) :
    """
    Affichage du fichier contenant le plan 
    """
    pas = calculer_pas()
    for i, ligne in enumerate(matrice, start = 0) : 
        for _, element in enumerate(ligne, start = 0) :
            for k, number in enumerate(element, start = 0) :
                    if number == '1' :
                        coordonnees = [k//2, i]
                        coord = transformer_coordonnees(coordonnees)
                        tracer_carre(coord, COULEUR_MUR, pas)
                    if number == '0' :
                        coordonnees = [k//2, i]
                        coord = transformer_coordonnees(coordonnees)
                        tracer_carre(coord, COULEUR_COULOIR, pas)
                    if number == '2' :
                        coordonnees = [k//2, i]
                        coord = transformer_coordonnees(coordonnees)
                        tracer_carre(coord, COULEUR_OBJET, pas)
                    if number == '3' :
                        coordonnees = [k//2, i]
                        coord = transformer_coordonnees(coordonnees)
                        tracer_carre(coord, COULEUR_PORTE, pas)
                    if number == '4' :
                        coordonnees = [k//2, i]
                        coord = transformer_coordonnees(coordonnees)
                        tracer_carre(coord, COULEUR_OBJECTIF, pas)

def verification_objet(coord, mouvement) :
    dic = creer_dictionnaire_des_objets('datasets/dico_objets.txt')

    print(coord)
    if(coord) in dic :
        print(dic[coord])  


def verification_obstacle(mouvement) :

    if mouvement == 'GAUCHE':
        coord_text = transformer_coordonnees_caractere((POSITION_DEPART_TRANSFORME[0]-20, POSITION_DEPART_TRANSFORME[1]))
    elif mouvement == 'DROITE': 
        coord_text = transformer_coordonnees_caractere((POSITION_DEPART_TRANSFORME[0], POSITION_DEPART_TRANSFORME[1]))
    elif mouvement == 'BAS': 
        coord_text = transformer_coordonnees_caractere((POSITION_DEPART_TRANSFORME[0], POSITION_DEPART_TRANSFORME[1]-10))
    elif mouvement == 'HAUT' :
        coord_text = transformer_coordonnees_caractere((POSITION_DEPART_TRANSFORME[0], POSITION_DEPART_TRANSFORME[1]+10))
        
    ligne = MATRICE[coord_text[1]]
    number = ligne[0]
    number = [elt for idx, elt in enumerate(number) if idx % 2 == 0]

    if mouvement == 'GAUCHE' or mouvement == 'DROITE' :
        number = number[coord_text[0]:coord_text[0]+1]
    else :
        number = [number[coord_text[0]+1]]
    
    if number == ['1'] :
        return False
    else : 
        return True 

def deplacer_gauche(): 
    mouvement = 'GAUCHE'
    turtle.onkeypress(None, "Left")   # Désactive la touche Left
    if verification_obstacle(mouvement)==True:
        turtle.setposition(POSITION_DEPART_TRANSFORME[0], POSITION_DEPART_TRANSFORME[1])
        turtle.dot(RATIO_PERSONNAGE*10, "white") 
        turtle.setposition(POSITION_DEPART_TRANSFORME[0]-10, POSITION_DEPART_TRANSFORME[1])
        POSITION_DEPART_TRANSFORME[0] = POSITION_DEPART_TRANSFORME[0]-10
        turtle.dot(RATIO_PERSONNAGE*10, "yellow") 
    print(transformer_coordonnees_caractere((POSITION_DEPART_TRANSFORME[0], POSITION_DEPART_TRANSFORME[1])))
    verification_objet((transformer_coordonnees_caractere((POSITION_DEPART_TRANSFORME[0], POSITION_DEPART_TRANSFORME[1]))), mouvement) 
    turtle.onkeypress(deplacer_gauche, "Left")   # Réassocie la touche Left à la fonction deplacer_gauche

def deplacer_droite():
    mouvement = 'DROITE'
    turtle.onkeypress(None, "Right")   # Désactive la touche Right
    if verification_obstacle(mouvement)==True:
        turtle.setposition(POSITION_DEPART_TRANSFORME[0], POSITION_DEPART_TRANSFORME[1])
        turtle.dot(RATIO_PERSONNAGE*10, "white") 
        turtle.setposition(POSITION_DEPART_TRANSFORME[0]+10, POSITION_DEPART_TRANSFORME[1])
        POSITION_DEPART_TRANSFORME[0] = POSITION_DEPART_TRANSFORME[0]+10
        turtle.dot(RATIO_PERSONNAGE*10, "yellow") 
    print(transformer_coordonnees_caractere((POSITION_DEPART_TRANSFORME[0], POSITION_DEPART_TRANSFORME[1])))
    verification_objet((transformer_coordonnees_caractere((POSITION_DEPART_TRANSFORME[0], POSITION_DEPART_TRANSFORME[1]))), mouvement) 
    turtle.onkeypress(deplacer_droite, "Right")   # Réassocie la touche Right à la fonction deplacer_gauche

def deplacer_haut(): 
    mouvement = 'HAUT'
    turtle.onkeypress(None, "Up")   # Désactive la touche Up
    if verification_obstacle(mouvement)==True:
        turtle.setposition(POSITION_DEPART_TRANSFORME[0], POSITION_DEPART_TRANSFORME[1])
        turtle.dot(RATIO_PERSONNAGE*10, "white") 
        turtle.setposition(POSITION_DEPART_TRANSFORME[0], POSITION_DEPART_TRANSFORME[1]+10)
        POSITION_DEPART_TRANSFORME[1] = POSITION_DEPART_TRANSFORME[1]+10
        turtle.dot(RATIO_PERSONNAGE*10, "yellow") 
    print(transformer_coordonnees_caractere((POSITION_DEPART_TRANSFORME[0], POSITION_DEPART_TRANSFORME[1])))
    verification_objet((transformer_coordonnees_caractere((POSITION_DEPART_TRANSFORME[0], POSITION_DEPART_TRANSFORME[1]))), mouvement) 
    turtle.onkeypress(deplacer_haut, "Up")   # Réassocie la touche Up à la fonction deplacer_gauche

def deplacer_bas(): 
    mouvement = 'BAS'
    turtle.onkeypress(None, "Down")   # Désactive la touche Down
    if verification_obstacle(mouvement)==True:
        turtle.setposition(POSITION_DEPART_TRANSFORME[0], POSITION_DEPART_TRANSFORME[1])
        turtle.dot(RATIO_PERSONNAGE*10, "white") 
        turtle.setposition(POSITION_DEPART_TRANSFORME[0], POSITION_DEPART_TRANSFORME[1]-10)
        POSITION_DEPART_TRANSFORME[1] = POSITION_DEPART_TRANSFORME[1]-10
        turtle.dot(RATIO_PERSONNAGE*10, "yellow") 
    print(transformer_coordonnees_caractere((POSITION_DEPART_TRANSFORME[0], POSITION_DEPART_TRANSFORME[1])))
    verification_objet((transformer_coordonnees_caractere((POSITION_DEPART_TRANSFORME[0], POSITION_DEPART_TRANSFORME[1]))), mouvement) 
    turtle.onkeypress(deplacer_bas, "Down")   # Réassocie la touche Down à la fonction deplacer_gauche

def deplacer() :
    turtle.onkeypress(deplacer_gauche, "Left")
    turtle.onkeypress(deplacer_droite, "Right")
    turtle.onkeypress(deplacer_haut, "Up")
    turtle.onkeypress(deplacer_bas, "Down")

def creer_dictionnaire_des_objets(fichier_des_objets) :
    dic = {}
    with open(fichier_des_objets) as f:
        for line in f:
            key, value = eval(line)
            dic[key] = value
    return dic

            


matrice = lire_matrice()

turtle.tracer(False)

tracer_map(matrice)

coordonnees_depart = transformer_coordonnees((POSITION_DEPART))
turtle.setposition(coordonnees_depart)
turtle.dot(RATIO_PERSONNAGE*10, "yellow") 
turtle.listen()
deplacer()
turtle.mainloop()  

