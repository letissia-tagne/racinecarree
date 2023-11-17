l=[]
for i in range(1,6):
     print('l[',i,']=',end='')
     l.append(int(input()))
     p=[]
     for i in l:
      if i%2==0:
       p.append(i)
print('affichez les nombres paire de l:', p)
     
