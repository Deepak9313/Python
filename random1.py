import random
num = int(input("Enter your number in range 1-6:\n"))
com_num = random.randrange(1,7)
if(num == com_num):
    print("Win")
else:
    print(f"Computer number is {com_num}")
    print("Lose")