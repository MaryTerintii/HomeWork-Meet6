#Remake 1d robo game -> for loop

from os import system
roboX = 5
roboHP = 100
roboBT = 100
bombX = 7
bombY = 3
heart = 9
money = 1
Rmoney = 0
LENGTH = 10 
option = ""


while True:
    ############### DRAW MAP #################
     system ("cls")
     print ("\n")

     for x in range (1, LENGTH +1): # 1..10
        if x == roboX:
            print ("☃", end=" ")
        elif x == bombX:
            print ("💣", end=" ")
        elif x == bombY:
            print ("💣", end=" ")
        elif x == heart:
            print ("💙", end=" ")
        elif x == money:
            print ("💰", end=" ")
        else:
            print (".", end=" ")

     print ("\nHP: ", roboHP)   #\n rind nou
     print ("\nBT: ", roboBT, "%")
     print ("\nRM: ", Rmoney)
     print ("\n")

    ############### 1. DRAW MAP #################

    ############### 2. READ INPUT #################
     option = input ( ">>> ") # move direction
    ############### 2. READ INPUT #################

    ############### 3. DECIDE #################
     if option == "a" and roboX > 1:  # move left
        roboX -= 1
        roboBT -=1

     if option == "d" and roboX <= 9 : # move right
        roboX += 1 
        roboBT -=1
         
    # check if bomb
     if roboX == bombX:
        roboHP -= 10
    
     if roboX == bombY:
        roboHP -= 10
    
     if roboX == heart:
        roboHP += 10

     if roboX == Rmoney:
        Rmoney += 10
    
     

     
    ############### 3. DECIDE #################

    ############### 3. DECIDE #################