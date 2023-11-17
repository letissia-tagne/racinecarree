#:anagramme se sont des mots qui s'ecrivent avec les meme lettres 
def anagramme ( a,b):
    print(anagramme(a,b))
    if len(a)!=len(b):
        return False
    # la fontion sorted() permet de trier les element dd'une liste ou d'un objet iterable 
    if sorted(a.upper())==sorted(b.upper()):
        return True 
    else:
        return False
    