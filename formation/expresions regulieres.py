import re

texte = "Bonjour, je m’appelle Alice. Je suis ravie de vous rencontrer, Alice."
motif = r"Alice"
remplacement = "Bob"

nouveau_texte = re.sub(motif, remplacement, texte)
print(nouveau_texte)