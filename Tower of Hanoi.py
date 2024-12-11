#Partie A:
#1)
def init(n):
    p0 = []
    p1 = []
    p2 = []
    plateau =[p0, p1, p2]
    for i in range(n,0,-1):
        p0.append(i)
    return plateau


#2)
def nbDisques(plateau, numtour):
    p0 = plateau[0]
    p1 = plateau[1]
    p2 = plateau[2]
    if numtour == 0:
        return len(p0)
    elif numtour == 1:
        return len(p1)
    elif numtour == 2:
        return len(p2)

#3)
def disqueSup(plateau, numtour):
    x = nbDisques(plateau, numtour)
    if x == 0:
        return -1
    else:
      p0 = plateau[0]
      p1 = plateau[1]
      p2 = plateau[2]
      if numtour == 0:
          return min(p0)
      elif numtour == 1:
          return min(p1)
      elif numtour == 2:
          return min(p2)


#4)
def posDisque(plateau, numdisque):
    p0 = plateau[0]
    p1 = plateau[1]
    p2 = plateau[2]
    if numdisque in p0:
        return (f"Le disque {numdisque} est dans  le premier tour")
    elif numdisque in p1:
        return (f"Le disque {numdisque} est dans  le deuxième tour")
    elif numdisque in p2:
        return (f"Le disque {numdisque} est dans  le troisième tour")

# 5)
def verifDepl(plateau, nt1, nt2):
    if plateau[nt1] and (not plateau[nt2] or disqueSup(plateau, nt1) < disqueSup(plateau, nt2)): #il faut que hayala shi ykoon bi nt1 w eno ya ykoon nt2 fadi aw iza fiyo shi ykoon l jeyi hajmo azghar
        return True
    else:
        return False


#6)
def verifVictoire(plateau, n):
    p0 = plateau[0]
    p1 = plateau[1]
    p2 = plateau[2]
    for i in range(n,0,-1):
        if len(p0) == 0 and len(p1) == 0 and len(p2) == n:
            return True
        else:
            return False


#Partie B
#1

from turtle import *
xplateau = -300
yplateau = -200
def dimension_du_plus_grand_disque(n):
    dimension = 40
    for i in range(1,n+1):
        dimension +=30
    return dimension



def base(n):
    x = dimension_du_plus_grand_disque(n)
    for i in range(0,2): # ma khasa bil tour, kermel ma n3id l kitebi martayn
        forward(30 + x + 20 + x + 20 + x +30)
        right(90)
        forward(n*2)
        right(90)

def tour(n):
    x = dimension_du_plus_grand_disque(n)
    hauteur = (n+1)*30
    epaisseur = n+(n*0.3)
    xtour1 = 30 + x/2
    xtour2 =  x + 20 + xtour1
    xtour3 = xtour2 + x + 20
    liste_x = [xplateau + xtour1,xplateau + xtour2,xplateau + xtour3]
    for i in range (0,3):
        penup()
        goto(liste_x[i] + epaisseur,yplateau)
        pendown()
        left(90)
        forward(hauteur)
        left(90)
        forward(epaisseur)
        left(90)
        forward(hauteur)
        left(90)

def dessinePlateau(n):
    speed(6)
    penup()
    goto(xplateau,yplateau)
    pendown()
    base(n)
    tour(n)





#2)
def dimension_disque(n,nd):
    x = dimension_du_plus_grand_disque(n)
    for i in range (n,nd,-1) :
        x -=30
    return(x)




def dessineDisque(nd, plateau, n):
    dimension = dimension_disque(n,nd)
    x = dimension_du_plus_grand_disque(n)

    if nd in plateau[0]:
            a = plateau[0].index(nd)
            x1 = -300 +30+ x/2 - dimension/2 + (n+(n*0.3))/2
            y1 = -200 + 30*(a)
            penup()
            goto(x1,y1)
            pendown()
            for i in range(0,2):
                forward(dimension_disque(n,nd))
                left(90)
                forward(30)
                left(90)

    elif nd in plateau[1]:
            a = plateau[1].index(nd)
            x2 = -300 + 30 + x + 20 +x/2 - dimension/2 + (n+(n*0.3))/2
            y2 = -200 + 30*(a)
            penup()
            goto(x2,y2)
            pendown()
            for i in range(0,2):
                forward(dimension_disque(n,nd))
                left(90)
                forward(30)
                left(90)

    elif nd in plateau[2]:
            a = plateau[2].index(nd)
            x3 = -300 + 30 + x + 20 + x +20+x/2 - dimension/2 + (n+(n*0.3))/2
            y3 = -200 + 30*(a)
            penup()
            goto(x3,y3)
            pendown()
            for i in range(0,2):
                forward(dimension_disque(n,nd))
                left(90)
                forward(30)
                left(90)




#3)
def effaceDisque(nd, plateau, n) :
    pencolor("white")
    dessineDisque(nd, plateau, n)
    pencolor("black")
    dessinePlateau(n)


#4)
def dessineConfig(plateau, n) :
    for tour in plateau:
        for disque in tour:
            dessineDisque(disque,plateau,n)


#5)
def efface_tout(plateau, n) :
    pencolor("white")
    dessinePlateau(n)
    dessineConfig(plateau, n)
    pencolor("black")



#Partie C
#1)
def lireCoords(plateau,n):
    condition = True
    while condition:
        tour_depart = int(input("Choisissez le tour de départ (0, 1, 2): "))
        while tour_depart > 2 or tour_depart < 0 or len(plateau[tour_depart])==0 :
            print("Invalide, tour vide.")
            tour_depart = int( input("Numéro de la tour de départ (0, 1, 2) : "))
        if len(plateau[tour_depart]) != 0:
            x = min(plateau[tour_depart])

        tour_arrive = int(input("Numéro de la tour d'arrivée (0, 1, 2) : "))
        while tour_arrive > 2 or tour_arrive < 0 :
             tour_arrive = int(input("Numéro de la tour d'arrivée (0, 1, 2) : "))
        if len(plateau[tour_arrive]) != 0:
            x1 = min(plateau[tour_arrive])
        if len(plateau[tour_arrive]) ==0 or x<x1: # comme verifier deplacement
            condition = False
            return tour_depart, tour_arrive
        else :
            print("Déplacement non autorisé. Veuillez réessayer.")
            condition = True




#2)
def jouerUnCoup(plateau, n):

    tour_depart, tour_arrivee = lireCoords(plateau,n)
    dessinePlateau(n)
    dessineConfig(plateau, n)
    disque = min(plateau[tour_depart])
    print(f"Je déplace le disque {disque} de la tour {tour_depart} à la tour {tour_arrivee}")
    effaceDisque(disque, plateau, n)
    plateau[tour_depart].remove(disque)
    plateau[tour_arrivee].append(disque)
    dessineDisque(disque, plateau, n)
    dessineConfig(plateau, n)
    return plateau



#3)
def boucleJeu(plateau, n):
    coups_joues = 1
    victoire = verifVictoire(plateau, n)
    max_coups = 2**(n) +4
    while victoire == False :
        plateau = jouerUnCoup(plateau, n)
        victoire = verifVictoire(plateau, n)
        if victoire == True:
            print(f"Victoire après {coups_joues} coups ")
            return True
        if coups_joues == max_coups:
            victoire = True
            print(f"perdu après {coups_joues} coups")
            return  False
        coups_joues += 1






# Fonction principale
def main():
    print("Bienvenue dans les Tours de Hanoi")
    n = int(input("Combien de disques? "))
    plateau = init(n)

    setup(width=800, height=600)

    text_x = -window_width() / 2 + 50
    text_y = window_height() / 2 - 20
    penup()
    goto(text_x, text_y)
    write("Les Tours de Hanoi (par Alaa SAAB)", align="right", font=("Courier", 12, "normal"))
    dessinePlateau(n)
    dessineConfig(plateau, n)

    boucleJeu(plateau, n)

#5 Partie D: annulation de coups
#1
def dernierCoup(coups):
    dernier_coup = coups[len(coups)]
    avant_coup = coups[len(coups) - 1]

    tour_depart = [i for i in range(3) if len(avant_coup[i]) > len(dernier_coup[i])][0]
    tour_arrivee = [j for j in range(3) if len(avant_coup[j]) < len(dernier_coup[j])][0]
    return tour_depart, tour_arrivee

#2
def annulerDernierCoup(coups):
    dernier_coup = list(dernierCoup(coups))
    inverse = dernier_coup[::-1]

    del coups[len(coups)]
    return coups, inverse


#3
#annulation
def annulation (plateau,tour_depart,tour_arrivee,n):
            speed(11)
            dessinePlateau(n)
            speed(11)
            dessineConfig(plateau,n)
            speed(3)
            liste_depart = plateau[tour_depart]
            liste_arrivee = plateau[tour_arrivee]
            disque = min(liste_depart)
            effaceDisque(disque,plateau,n)
            liste_depart.remove(disque)
            liste_arrivee.append(disque)
            plateau[tour_depart] = liste_depart
            plateau[tour_arrivee] = liste_arrivee

            dessineDisque(disque,plateau,n)
            speed(11)
            dessineConfig(plateau,n)
            speed(3)
            return plateau
#boucle jeu modifier
import copy
def boucleJeu1(plateau, n):
    coups = {1: copy.deepcopy(plateau)}
    compteurs = 2
    nombre_total_de_coup = 2 ** n - 1 + 4
    bol = True
    while compteurs != nombre_total_de_coup and not verifVictoire(plateau, n):
        plateau = jouerUnCoup(plateau, n)
        coups[compteurs] = copy.deepcopy(plateau)

        if not verifVictoire(plateau, n):
            annuler = input("annuler? (oui/non): ")
            if annuler == "oui":
                coups, liste = annulerDernierCoup(coups)
                tour_depart, tour_arrivee = liste
                plateau = annulation(plateau, tour_depart, tour_arrivee, n)
                compteurs -= 1
                bol = False
        else:
            print("Victoire!")
            print("Bravo,Le jeu est gagné!")
            bol = True

        compteurs += 1

    return [compteurs - 2,bol, plateau]



# Partie E: comparaison des scores et temps de jeu
#1
def sauvScore(nom,n,nb_coups,d):
    d[nom] = {}
    d[nom]["nombre de disques"] = n
    d[nom]["nombre de coups"] = nb_coups
    return d

#3
def main1():
    print("Bienvenue dans les Tours de Hanoi :)")
    x = True
    d = {}
    while x == True:
        n = int(input("Combien de disques? "))
        text_x = -window_width() / 2 + 50
        text_y = window_height() / 2 - 20
        penup()
        goto(text_x, text_y)
        write("Les Tours de Hanoi (par Alaa SAAB )", align="right", font=("Courier", 12, "normal"))
        dessinePlateau(n)
        dessineConfig(init(n),n)
        liste_boucle = boucleJeu1(init(n),n)
        score = liste_boucle[0]
        bol = liste_boucle[1]
        plateau = liste_boucle[2]
        if bol:
            nom = input("Nom?")
            print(sauvScore(nom,n,score,d))
        continuer = input("rejouer? (oui/non) :")
        if continuer == "non":
            x = False
        elif continuer == "oui":
            efface_tout(plateau,n)
    print("Fin du jeu")
    mainloop()

#4
def auxiliere1(d):#nafs 3adad l disk (tsof hasa nb de disque) created  dictionary lal nb de disque 1 masalan
    d_n = {}
    liste_n = []
    for joueur in d.keys():
        liste_n.append(d[joueur]["nombre de disques"])
    sorted_n = sorted(liste_n)
    for n in range (0,len(sorted_n)):
        d_n[sorted_n[n]] = {}
    for n in range (0,len(sorted_n)):
        for joueur in d.keys():
            if d[joueur]["nombre de disques"] == sorted_n[n]:

                d_n[sorted_n[n]][joueur]= d[joueur]
    return d_n


def afficheScore(d): #sta3malna l auxiliaire bi nafs l tari2a
    d_n = auxiliere1(d)# lal auux 3melna for iza nafs l disque bas lal affiche mna3mel for en cas general kermel kaza nb disque

    for i in d_n.keys():
        liste_score = []

        for joueur in d_n[i]:
            liste_score.append(d_n[i][joueur]["nombre de coups"])
        sorted_score = sorted(liste_score)
        for n in range (0,len(sorted_score)):
            for joueur in d_n[i].keys():
                if d_n[i][joueur]["nombre de coups"] == sorted_score[n]:

                 print(f"{joueur}:{d_n[i][joueur]}")
            break


#8
def menu(d):

    scores = input("voir les scores? (oui/non) :")
    if scores == "oui":
        afficheScore(d)


# Partie F: jeu automatique, fonction recursive
#1
def resout_automatiquement(n, source, target, auxiliary):
    if n == 1:
        return [(source, target)]
    else:
        # Déplacer n-1 disques de la source à l'auxiliaire en utilisant la cible comme tampon
        moves = resout_automatiquement(n - 1, source, auxiliary, target)
        # Déplacer le plus grand disque de la source vers la cible
        moves.append((source, target))
        # Déplacer les n-1 disques restants de l'auxiliaire vers la cible en utilisant la source comme tampon
        moves.extend(resout_automatiquement(n - 1, auxiliary, target, source))
        return moves

def jouerUnCoup1(plateau,n,tour_depart,tour_arrivee) :
    print(f"tu deplace de {tour_depart} au {tour_arrivee}")
    speed(11)
    dessinePlateau(n)
    speed(11)
    dessineConfig(plateau,n)
    speed(3)
    liste_depart = plateau[tour_depart]
    liste_arrivee = plateau[tour_arrivee]
    disque = min(liste_depart)
    effaceDisque(disque,plateau,n)
    liste_depart.remove(disque)
    liste_arrivee.append(disque)
    plateau[tour_depart] = liste_depart
    plateau[tour_arrivee] = liste_arrivee
    dessineDisque(disque,plateau,n)
    speed(11)
    dessineConfig(plateau,n)
    speed(3)
    return plateau

#2
def solutionTurtle(plateau,n, source, target, auxiliary):
    liste = resout_automatiquement(n, source, target, auxiliary)
    for i in liste:
        tour_depart,tour_arrivee = i
        jouerUnCoup1(plateau,n,tour_depart,tour_arrivee)


#3

def main2():
    print("Bienvenue dans les Tours de Hanoi :)")
    print("")
    x = True
    d = {}
    while x == True:
        n = int(input("entrez le nombre de disques :"))
        text_x = -window_width() / 2 + 50
        text_y = window_height() / 2 - 20
        penup()
        goto(text_x, text_y)
        write("Les Tours de Hanoi (par Alaa SAAB)", align="right", font=("Courier", 12, "normal"))
        dessinePlateau(n)
        dessineConfig(init(n),n)
        liste_boucle = boucleJeu1(init(n),n)
        score = liste_boucle[0]
        bol = liste_boucle[1]
        plateau = liste_boucle[2]
        if bol :
            nom = input("Nom?")
            d = sauvScore(nom,n,score,d)

        continuer = input("rejouer? (oui/non) :")
        if continuer == "non":
            x = False
        elif continuer == "oui":
            efface_tout(plateau,n)
    solution = input("voir la solution? (oui/non) :")
    if solution == "oui":
        efface_tout(plateau,n)
        solutionTurtle(init(n),n,0,2,1)

    menu(d)
    print("")
    print("Fin du jeu")
    mainloop()

main2()
