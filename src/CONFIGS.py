# Définition des constantes globales

ZONE_PLAN_MINI = (-240, -240)  # Coin inférieur gauche de la zone d'affichage du plan
ZONE_PLAN_MAXI = (50, 200)  # Coin supérieur droit de la zone d'affichage du plan
POINT_AFFICHAGE_ANNONCES = (-240, 240)  # Point d'origine de l'affichage des annonces
POINT_AFFICHAGE_INVENTAIRE = (70, 200)  # Point d'origine de l'affichage de l'inventaire
LARGEUR_PLAN = 460
LONGUEUR_PLAN = 290
POSITION_DEPART_TRANSFORME = [95.0, -125.0]

# Les valeurs ci-dessous définissent les couleurs des cases du plan
COULEUR_CASES = 'white'
COULEUR_COULOIR = 'white'
COULEUR_MUR = 'grey'
COULEUR_OBJECTIF = 'yellow'
COULEUR_PORTE = 'orange'
COULEUR_OBJET = 'green'
COULEUR_VUE = 'wheat'
COULEURS = [COULEUR_COULOIR, COULEUR_MUR, COULEUR_OBJECTIF, COULEUR_PORTE, \
            COULEUR_OBJET, COULEUR_VUE]
COULEUR_EXTERIEUR = 'white'

# Couleur et dimension du personnage
COULEUR_PERSONNAGE = 'red'
RATIO_PERSONNAGE = 0.9  # Rapport entre diamètre du personnage et dimension des cases
POSITION_DEPART = (0.5, 0.5)  # Porte d'entrée du château

#MATRICE 

MATRICE = [['1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 '], ['1 0 0 0 1 0 0 0 1 0 1 0 0 0 1 0 4 0 1'], ['1 1 1 0 1 0 1 0 1 0 1 0 1 0 1 1 1 0 1'], 
            ['1 0 0 0 3 0 1 0 0 0 1 0 1 0 0 0 0 0 1'], ['1 0 1 1 1 1 1 0 1 0 1 0 1 1 1 1 1 1 1'], ['1 0 0 0 1 0 0 0 1 0 3 0 0 0 0 0 0 1 1'], 
            ['1 1 1 0 1 0 1 1 1 1 1 1 1 0 1 1 1 0 1'], ['1 4 1 0 1 0 0 0 1 0 0 0 0 0 1 0 1 0 1'], ['1 0 1 0 1 1 1 0 1 0 1 1 1 0 1 1 1 0 1'], 
            ['1 0 0 0 1 0 0 0 1 0 0 0 1 0 3 0 0 0 1'], ['1 1 1 1 1 0 1 1 1 0 1 1 1 1 1 0 1 0 1'], ['1 0 0 0 3 0 1 4 0 0 1 0 0 0 1 0 0 4 1'], 
            ['1 0 1 1 1 1 1 1 1 1 1 0 1 0 1 1 1 1 1'], ['1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 0 0 1'], ['1 0 1 0 1 0 1 0 1 0 1 1 1 1 1 1 1 0 1'], 
            ['1 0 1 0 1 0 1 0 1 0 0 0 0 0 1 0 0 0 1'], ['1 1 1 3 1 0 1 0 1 1 1 1 1 3 1 0 1 1 1'], ['1 0 0 0 1 0 1 0 1 0 0 0 0 0 1 0 0 0 1'], 
            ['1 0 1 1 1 1 1 0 1 1 1 0 1 1 1 1 1 0 1'], ['1 0 0 0 1 0 0 0 1 0 1 0 0 0 0 0 1 0 1'], ['1 1 1 0 1 0 1 1 1 0 1 1 1 0 1 0 1 0 1'], 
            ['1 0 0 0 3 0 0 0 3 0 1 0 0 0 1 0 1 0 1'], ['1 0 1 1 1 1 1 1 1 0 1 0 1 1 1 1 1 0 1'], ['1 0 0 0 1 4 0 0 1 0 3 0 0 0 1 0 0 0 1'], 
            ['1 1 1 0 1 1 1 0 1 0 1 0 1 1 1 0 1 1 1'], ['1 4 0 0 0 0 1 0 0 0 1 0 0 0 1 0 3 0 1'], ['1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 1']]

# Désignation des fichiers de données à utiliser
fichier_plan = 'plan_chateau.txt'
fichier_questions = 'dico_questions.txt'
fichier_objets = 'dico_objets.txt'
