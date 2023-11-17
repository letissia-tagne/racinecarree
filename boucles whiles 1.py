import random
#generation d'un nombre aleatoire entre 1 et 100
nombre_secret=random.randint(1,100)
print("devinez le nombre secret compris entre 1 et 100!")

#initialisation des variables 
essais=0
devine=False
 #boucle principale du jeu 
while not devine:
 essais +=1
devinette=int(input("entrez votre devinette:"))
#verification de la devinette 
if devinette==nombre_secret:
 print("felicitations! vous avez devine le nombre en ",essais,"essais")
 devine=True 
elif devinette<nombre_secret: 
 print("le nombre secret est plus grand.")
else :
 print("le nombre secret est plus petit.") 
