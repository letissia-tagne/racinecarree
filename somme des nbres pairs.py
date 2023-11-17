
numbers=[1,2,3,4,5,6,7,8,9,10]
sum_of_squares=0

for num in numbers:
    if num%2==0: 
        #verifier si le nombre est pair 
        square=num**2
        #calcule le carré du nombre 
        sum_of_squares+=square
        # ajoute le carre à la somme
        print ("la somme des carées des nombre pairs est :" ,sum_of_squares)
        