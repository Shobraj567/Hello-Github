print("**** Simple Calculator ****")
print(" 1. Addition\n 2. Subtraction\n 3. Division\n 4. Multiplication\n 5. Exit ")
Operation = int(input("Select the Your option : "))
print()
match Operation:
    case 1: 
        a = float(input("enter the first number: "))
        b = float(input("enter the second number:  "))
        Result = a+b
        print(f"Addition of given number is {Result}")
        print()
        Operation = int(input("Select the Your Next option : "))

match Operation:
    case 2:
        a = float(input("enter the first number: "))
        b = float(input("enter the second number: "))
        Result = a-b
        print(f"Subtraction of given number is : {Result}")
        print()
        Operation = int(input("Select the Your Next option : "))

match Operation:
    case 3:
        a = float(input("enter the first number: "))
        b = float(input("enter the second number: "))
        Result = a/b
        print(f"Division of given number is : {Result}")
        print()
        Operation = int(input("Select the Your Next option : "))

match Operation:
    case 4:
        a = float(input("enter the first number: "))
        b = float(input("enter the second number: "))
        Result = a*b
        print(f"Multplication of given number is : {Result}")
        print()
        Operation = int(input("Select the Your Next option : "))

