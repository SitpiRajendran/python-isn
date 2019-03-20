n=eval(input("Entrez un nombre en base 10, à transformer en base Shadoks : "))
s=n                  # Je garde la variable n pour la phrase de fin
r=122                # Il fallait initialiser r avec un chiffre différent de 0
sha = str("")        # Il faut indiquer qu'il s'agit de chaines de caractères
shs = str("")        # Il faut indiquer qu'il s'agit de chaines de caractères

def shadok(chiffre):
	if chiffre==0 :
		return "Ga"
	if chiffre==1 :
		return "Bu"
	if chiffre==2 :
		return "Zo"
	if chiffre==3 :
		return "Meu"

if s==0:
	sha = "Ga"
	
while s!=0:
        r=s%4
        s=s//4       #Cela nous permet d'avoir un nombre entier
        shs=shadok(r)
        sha = shs+sha #Cela permet d'indiquer les nombres dans le bonne ordre
print(n,"en base shadoks donne",sha)
