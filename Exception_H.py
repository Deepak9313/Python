try:
    num1 = int(input("Enter the number 1 : \n"))
    num2 = int(input("Enter the number 2 : \n"))
    if num2 == 0:
        raise ZeroDivisionError
    else:
        print("Integar value :- ",int(num1/num2))
        print("Float value :- ",num1/num2)
except ZeroDivisionError:
    print(ZeroDivisionError)
else:
    print("Try is working fine")
finally:
    print("Try Except finished!")
