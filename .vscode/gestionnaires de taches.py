from operator import index
from re import T
from typing import Self

# creation de la classe Task avec ses attributs
class Task:
   def __init__(self, titre, description, date_echeance, statut):
    self.titre=titre
    self.description=description
    self.date_echeance=date_echeance
    self.statut=statut 
#creation de la sous classe Taskmanager contenant une liste vide 
class Taskmanager:
    def __init__(self):
      self.task=[]

#
    def creer(self, titre, description, date_echeance, statut):
      task = Task(titre, description, date_echeance, statut)
      self.task.append(task)



    def modifier(self,index, titre, description, date_echeance, statut ):
        if index>=0 and index<len(self.task):
            self.task[index].titre=titre
            self.task[index].description=description
            self.task[index].date_echeance=date_echeance
            self.task[index].statut=statut
    
    def supprimer(self,index):
        if index>=0 and index<len(self.task):
            del self.task[index]

    def afficher(self,):
            for index,task in enumerate(self.task):
                   print(f" task {index+1}:")
                   print(f" titre {task.titre}:")
                   print(f" description {task.description}:")
                   print(f" statut {task.statut}:")
    tache1=Taskmanager()
    tache1.creer("voyage","bienvenu_route_ouest", "10-04-2023", "en attente,en cour,termine")
    tache1.modifier(0, "voyage","bienvenu_route_ouest","10-04-2023", "en attente,en cour,termine")
    tache1.supprimer(1)
    tache1.afficher()
   