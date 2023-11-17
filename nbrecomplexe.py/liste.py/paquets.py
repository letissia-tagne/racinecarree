#creer un paquet en python, ils suffit de creer un repertoire avec un nom significatif, conatenat un fichier special appelé __init__.py
ce fichier peut etre vide ou contenir du code d'initialisation specifique au paquet.

# voici uen exempple  de structure de paquet en python
mon_paquet/
__init__.py
module1.py
module2.py
# dans cet exemple, mon_paquet est le nom du paquet,__init__.py est le fichier d'initialisation du paquet ,et le module2.py sont des modules faisant partie du paquet.

#il faut importer le paquet et les modules souhaite pour utiliser dans un script python 
# exemple d'importation d'un paquet et ses modules
import mon_paquet.module1
import mon_pauqet.module2

mon_paquet.module1.fonction1()
mon_paquet.module2.fonction2()

# ilest eaglement possible de d'importer directementles modules d'un paquet en utilisant l'instruction from:
module1.fonction1()
module2.fonction2()


 