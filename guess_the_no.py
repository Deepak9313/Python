import random as rd
rg = rd.randrange(0,10)
user = int(input("Enter your lucky no :- \n"))
if rg == user:
    print("Congratulations !! You won!")
else:
    print("Sorry, Bad Luck !")