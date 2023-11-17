def guests():

    nom=input("entrez le nom de l'utilisateur:")
    print("bonjour monsieur", nom)

guests()


def guests():
    invites=["Mask","Leo","Marc","Agile"]
    nom=input("entrez le nom de l'utilisateur:")
    if nom.capitalize() in invites:
        print("bonjour monsieur",nom)
    else:
        print("desolé monsieur{}, vous ne faites pas partir de la liste")    
guests()

