# definition de la classe Rectangle 
class Rectangle:
  # entre les attributs de la classe Rectangle
  def __init__(self, longueur, largeur):
    self.longueur = longueur
    self.largeur = largeur
# on entre les methodes de la classe Rectangle 
  def claculer_perimetre (self):
     return  (self.longueur + self.largeur)*2

  def calculer_surface(self):
      return self.longueur * self.largeur
#on cree un objet quelconque
mon_rectangle=Rectangle(5,3)
print("le perimetre de mon rectangle est:",mon_rectangle.claculer_perimetre ())
print("la surface de mon rectangle est :",mon_rectangle.calculer_surface())







class compte_bancaire:
  def __init___(self, titulaire, solde):
    self.titulaire= titulaire
    self.solde= solde 

  def deposer(self,montant):
     return self.solde+=montant
  def retirer(self,montant):
     if self.solde>=montant :
      self.solde-=montant
     else:
       print("solde insuffisant.")
  def 