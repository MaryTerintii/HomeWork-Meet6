from os import system

system ("cls")



print()



big_ship = 5

big_ship = int(input ("ship coorditantor: "))
 ############### 1. DRAW MAP #################

    
while True:
    system ("cls")

    for x in range(1,11):
     if x == big_ship:
        print( "W", end="" )
     elif x == big_ship + 1:
        print ("w", end= "")
     elif x == big_ship - 1:
        print ("w", end= "")
     else:
        print( "~", end="" )
    

    print()

    ############### 2. READ INPUT #################
    option = input ( ">>> ") # move direction

    if option == "a" and big_ship > 1:
     big_ship -= 1
            

    if option == "d" and big_ship <= 9 : # move right
     big_ship+= 1 
       
