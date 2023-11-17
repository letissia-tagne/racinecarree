def somme_pair():
    l=[]
    for i in range(1,6):
      print('[',i,']=' ,end='')
      l.append(int(input()))  
      pair=[]
    for i in l:
      if i%2==0:
        pair.append(i)
    print('affichez les nombres pairs de la liste:',pair)
    somme_pair=sum(pair)
    print('afficher la somme des nombres pair:',somme_pair)
somme_pair()
    

