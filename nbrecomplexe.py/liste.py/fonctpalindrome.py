def est_palindrome(chaine):
 chaine = chaine.lower() # Convertit la chaîne en minuscules
 chaine = chaine.replace(" " , "") # Supprime les espaces de la chaîne

 return chaine == chaine[::-1] # Vérifie si la chaîne est égale à sa version inversée

print(est_palindrome("radar")) # pour afficher le résultat
print(est_palindrome("hello")) # pour afficher le résultat
print(est_palindrome("Bonjour le monde"))