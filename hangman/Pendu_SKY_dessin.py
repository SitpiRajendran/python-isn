from random import *

vie = 0
motverif = True

def recup_lettre():
    global lettre
    lettre = input("Tapez une lettre: ")
    lettre = lettre.lower()
    if len(lettre)>1 or not lettre.isalpha():
        print("Vous n'avez pas saisi une lettre valide.")
        return recup_lettre()
    else:
        return lettre

print ("Bonjour, et Bienvenue dans le jeu du Pendu \n-------------------------------------------------------------- \n Attention n'oubliez pas l'existence des lettres suivantes : \n é / è / ç / ù / â / ê / ï / .... \n-------------------------------------------------------------- \n")

multi = input("Voulez-vous jouer tous seul ? (Oui ou Non) : ")
multi = multi.lower()

Jvie = input("Voulez-vous jouer avec des vies? (Oui ou Non) : ")
Jvie = Jvie.lower()

if multi=="oui":
    motverif = False
    dico = open ("MOTS.txt", "r")
    dicoc = dico.readlines()
    mot = choice(dicoc)
    mot = mot.replace("\n","")
    dico.close
    
while motverif:
        mot = input("Quel mot, Joueur 2, doit-il trouver ? ")
        mot2 = mot+"\n"
        dico = open ("MOTS.txt", "r")
        dicoc = dico.readlines()
        if mot2 in dicoc:
            motverif = False
            print("Mot Valide")
        else:
            print("\n -------------------------------------------------------------- \nMot non repertorié\n")
        dico.close
print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n  \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")


mot_trouve = "*" * len(mot)


while 1:
    recup_lettre()
    nbltr = 0
    for i in range(len(mot)):
            if lettre == mot[i]:
                mot_trouve = mot_trouve[:i] + lettre + mot_trouve[i+1:]
                nbltr = 0 + 1
    if Jvie=="oui":
        if nbltr == 0:
            vie = vie + 1
        if vie==0:
            print (" ")
        if vie==1:
            print ("  O   ")
        if vie==2:
            print ("  O   \n  |")
        if vie==3:
            print ("  O   \n  |  \n /")
        if vie==4:
            print ("  O   \n  |  \n / \ ")
        if vie==5:
            print ("  O   \n  |  \n / \   \n  |")
        if vie==6:
            print ("  O   \n  |  \n / \   \n  |   \n / ")
        if vie==7:
            print ("  O   \n  |  \n / \   \n  |   \n / \ ")
            print ("Vous avez Perdu ;-( \n Le mot à trouver était '", mot, "'")
            break
    print (mot_trouve)
    if mot_trouve == mot:
            print ("Bravo ! Le mot a été trouvé") 
            break
