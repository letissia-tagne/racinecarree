import shutil
fichier=open("formation/mavie.txt","r")
print(fichier.read())
fichier =open("formation/les realites.txt","r")
print(fichier.read())
#la module copystat permet de copier le contenu du fichier les realites vers le fichier mavie sans affecter le contenu a la fois des permissions et les dates de drnier acces et dernieres modifications presentes sur le fichier m
shutil.copystat("formation/mavie.txt","formation/les realites.txt")
# le module shutil.copyfile fair la copie du fichier ma vie en fichier les realites en affectant le contenu

