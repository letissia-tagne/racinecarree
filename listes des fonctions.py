def guests():
    invites=["Mask","Leo","Marc","Agile"]
    nom=input("entrez le nom de l'utilisateur:")
    if nom.capitalize() in invites:
        print("bonjour monsieur",nom)
        print("bienvenue")
    else:
        print("desolé monsieur{},vous ne faites pas partir de la liste.".format(nom))    
guests()