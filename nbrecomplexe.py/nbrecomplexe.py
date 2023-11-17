import cmath

reel = float(
           input ("Entrez la partie réelle du nombre complexe : ")
                    )
imaginaire = float(input("Entrez la partie imaginaire du nombre complexe : "))
nombre_complexe = complex(reel, imaginaire)
racine_carree = cmath.sqrt(nombre_complexe)
print("La racine carrée de", nombre_complexe, "est", racine_carree)




