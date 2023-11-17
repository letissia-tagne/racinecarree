def factorielle(n):
  if n==0:
    return 1
  else:
    return n*factorielle(n-1)
nombre=10
resultat=factorielle(nombre)
print('le factorielle de',nombre,"est",resultat)

