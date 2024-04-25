age = None
age = int(input("Enter your age : \n"))
if age >= 18 and age <= 150:
    print("you are eligible to vote")
elif age > 150:
    print("hello ghost person")
else:
    print("you are not eligible to vote")

days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
num = 3
match num:
    case 1:
        print("Fun day")
    case 2:
        print("working day")
    case 3:
        print("hanuman day")