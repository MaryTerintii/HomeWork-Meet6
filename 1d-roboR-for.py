#Remake 1d robo game -> for loop
from os import system

system ("cls")


roboX = 5
LENGTH = 10

while True:

    ########### 1. DRAW MAP ##########
    print ("\n")

    for x in range (1, LENGTH + 1):   # 1....10
        if x ==roboX:
             print ("R", end=" ")
        else:
            print (".", end=" ")


    print ("\n")

    ########### 2.READ IMPUT ##########
    option = input (">>> ")
    ########### 3. DECIDE #############
    if option == "a" and roboX > 1: #move left
        roboX -= 1
    if option == "d" : # move right
        roboX += 1
    if option == "X":
        print ("Thank you for playing! ")
        break
