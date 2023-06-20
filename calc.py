import math

#Menu
initInput = eval(input("This is a calculator app!\nChoose what you want to formulate from below: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Square Root\n6. Exponent"))


#Functions

def add(num1 , num2):
    return num1+num2
    
def subtract(num1, num2):
    return num1-num2

def multi(num1, num2):
    return num1*num2

def divide(num1, num2):
    return num1/num2

def sqrt(num1):
    return math.sqrt(num1)
    
def expo(num1, num2):
    return num1**num2

#Logic
while initInput>0 and initInput<7:
    if initInput == 1:
        num1, num2 = eval(input("Insert the 2 digits you would like to add!"))
        print(add(num1, num2))
        again = input("Do you want another calculation? (y/n)")
        if again == y:
            
        break
    elif initInput == 2:
        print(subtract())
        break
    elif initInput == 3:
        print(multi())
        break
    elif initInput == 4:
        print(divide())
        break
    elif initInput == 5:
        print(sqrt())
        break
    elif initInput == 6:
        print(expo())
        break
else:
    print("That is not a valid input")