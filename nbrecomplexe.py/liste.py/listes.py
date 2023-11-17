plats_preferes = [ ]
nb_plats = int(input("Combien de plats préférés voulez-vous ajouter ? "))
for i in range(nb_plats):
   plat = input("Entrez le plat préféré numéro {}: ".format(i+1)) 
   plats_preferes.append(plat)
print("Voici vos plats préférés :")
for plat in plats_preferes:

 print(plat)

