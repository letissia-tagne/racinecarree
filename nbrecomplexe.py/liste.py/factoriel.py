def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n-1)
nombre = 12
resultat = factorielle(nombre)
print("Le factoriel de", nombre, "est", resultat)