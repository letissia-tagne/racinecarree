
# creation d'un dictionnaire vide 
mon_dictionnaire={}
#ajout d'elements au dictionnaire
mon_dictionnaire["fruit"]="pomme"
mon_dictionnaire["animal"]="chat"
mon_dictionnaire["couleur"]="bleu"
# acces au element du dcitionnaire 
print(mon_dictionnaire)["fruit"]#affiche "pomme"
print(mon_dictionnaire)["animal"]#affiche "chat"
print(mon_dictionnaire)["couleur"]#affiche "bleu"
# modification d'un élement du dictionnaire
mon_dictionnaire["fruit"]="banane"
print(mon_dictionnaire)#affiche'banane'
#suppression d'un element du dictionnaire
del mon_dictionnaire["animal"]
print(mon_dictionnaire)#affiche{"fruit":"banane,""couleur":"rouge"}
#parcourir les clés et les valeurs du dcitionnaire
for cle,valeur in mon_dictionnaire.items():
    print(cle,"=",valeur)

