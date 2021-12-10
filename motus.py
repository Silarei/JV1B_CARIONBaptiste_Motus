import random
import colorama

#Déclaration des variables
fichier = open("listeMot.txt", "r")
listeMots = fichier.readlines()
#listeMots = ["loutre", "wombat", "furets", "orques", "ratons", "phoque", "otarie", "saumon", "canide", "arctos"]
mot = listeMots[random.randint(0, len(listeMots) - 1)].replace("\n", "")
#patate est utilisé pour tester les mots à lettres multiples, retirer des commentaires patates pour tester
#mot = "patate"
#le compteur sert à compter le nombre de tentative
compteur = 0
#victoire compte le nombre de lettre à la bonne position
victoire = 0
#tabLettre et lettrePlace vont chacune vérifier que la lettre de la tentative ou du mot à deviner à la position désiré n'ait pas déjà été compté
tabLettre = [False, False, False, False, False, False]
lettrePlace = [False, False, False, False, False, False]
#listeMotCouleur va stocker les lettres coloré à leurs place correcte afin de les ressortirs au bon endroit
listeMotCouleur = ["", "", "", "", "", ""]

#initialisation de colorama
colorama.init()

print("Le mot fait 6 lettres !")
#boucle principale du programme, on en sort lorsque l'on dépasse les huit tentatives ou lorsque toute les lettres sont placé au bon endroit
while (compteur < 8 and victoire != 6) :
    #on reset les couleurs afin que les messages de la consoles qui vont suivre soit de la couleur normale
    print(colorama.Fore.RESET)
    #on reset les différents compteurs et liste pour la nouvelle tentative
    tabLettre = [False, False, False, False, False, False]
    lettrePlace = [False, False, False, False, False, False]
    victoire = 0
    #on demande un mot en input à l'utilisateur
    tentative = input("Tentative :\n")
    #on vérifie que la tentative possède le bon nombre de lettre
    if (len(tentative) != len(mot)) :
        print("Ta tentative ne fait pas le bon nombre de lettres !")
    #si la tentative est valide, on l'examine
    else :
        #on cherche une première fois les lettres à la bonne position
        for i in range(len(mot)) :
            for j in range(len(mot)) :
                #on vérifie que les lettres soit les mêmes, et qu'aucune des deux ne soit déjà utilisé dans une autre paire
                if (tentative[i] == mot[j] and tabLettre[j] == False and lettrePlace[i] == False) :
                    #on vérifie que les lettres soit à la même place
                    if (i == j) :
                        #s'il y en a, on les stock et on augmente le compteur de victoire, avant de signaler aux listes que les deux lettres comparés ont été utilisées
                        listeMotCouleur[i] = colorama.Fore.RED + tentative[i]
                        victoire = victoire + 1
                        tabLettre[j] = True
                        lettrePlace[i] = True
        #on cherche une seconde fois les lettres qui ne sont pas à la bonne position ou juste pas dans le mot
        for i in range(len(mot)) :
            for j in range(len(mot)) :
                #on vérifie que les lettres soit les mêmes, et qu'aucune des deux ne soit déjà utilisé dans une autre paire
                if (tentative[i] == mot[j] and tabLettre[j] == False and lettrePlace[i] == False) :
                    #on stock les lettres présentes mais pas à la bonne place, avant de signaler aux listes que les deux lettres comparés ont été utilisées
                    listeMotCouleur[i] = colorama.Fore.YELLOW + tentative[i]
                    tabLettre[j] = True
                    lettrePlace[i] = True
            #on s'occupe des lettres qui ne sont pas présentes dans le mot
            if (lettrePlace[i] == False) :
                listeMotCouleur[i] = colorama.Fore.BLUE + tentative[i]
        #on imprime le mot coloré
        for i in range(len(mot)) :
            print(listeMotCouleur[i], end = "")        
        #on augmente le compteur
        compteur = compteur + 1
#on reset la couleur avant d'afficher le message indiquant si l'on a gagné ou perdu
print(colorama.Fore.RESET)
if (victoire == 6) :
    print("\nVictoire !\n")
else :
    print("\nDefaite !\n")