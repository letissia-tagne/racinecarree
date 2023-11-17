import tkinter as tk

def afficher_message():
 label_message= nom
 message = "Bonjour " + nom.get() + "!"
label_message.config(text=message)

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Mon Application")

# Création des widgets
label_nom = tk.Label(fenetre, text="Nom:")
label_nom.pack()

nom = tk.Entry(fenetre)
nom.pack()

bouton_valider = tk.Button(fenetre, text="Valider", command=afficher_message)
bouton_valider.pack()

label_message = tk.Label(fenetre, text="")
label_message.pack()

# Lancement de la boucle principale
fenetre.mainloop()
  