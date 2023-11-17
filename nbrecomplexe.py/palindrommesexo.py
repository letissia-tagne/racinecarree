def palindrome():
 mot=input("saisir un mot: ")
# cette syntaxe permet de trouver l'inverse du mot
 inv=mot[::-1]
 if mot==inv:
    print("le mot",mot," est un palyndrome")
 else:
    print("le mot",mot," n'est pas un palyndrome")

palindrome()