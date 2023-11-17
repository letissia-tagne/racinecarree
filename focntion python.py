def saluer():
    print("bonjour!")
    
    saluer()# affiche "bonjour!"


    def saluer(nom):
        print("bonjour",nom,"!")

        saluer ("alice")# affiche "bonjour alice!"

        def saluer (nom="alice,ghjkl"):
            if nom!="leticia":
                print("bonjour",nom,"!")
            else:
                print("bonjour à tous!")
                

def count_words(phrase):
    mots=phrase.split()
    return len(mots)
phrase="bonjour tout le monde"
nombre_de_mots=count_words(phrase)
print(nombre_de_mots)
#output:4
def read_file(file_path):
    with open(file_path,'r')as file:
        for line in file:
            print(line.strip())
            file_path='liste_noms.txt'
            read_file(file_path)
