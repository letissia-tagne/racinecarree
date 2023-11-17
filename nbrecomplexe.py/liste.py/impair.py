l=[]
for i in range(1,6):
   print('l[',i,']=',end='')
   l.append(int(input()))
   impair=[]
   for i in l:
      if i%2!=0:
         impair.append(i)
print('afficher les nombres impaires',impair)

