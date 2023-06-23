import math



some_bool = True
while (some_bool):
    #Menu
    initInput = input("This is a calculator app!\nChoose what you want to formulate from below: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Square Root\n6. Exponent")
    
    try:
        initInput = eval(initInput)
    except:
        print("That is a string please input an integer.")
        some_bool = True
    if str != type(initInput):   
        some_bool = False
    

    

    

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
while ((initInput>0) and (initInput<7)):
    if initInput == 1:
        num1, num2 = eval(input("Insert the 2 digits you would like to add!"))
        print(add(num1, num2))
        oof = 0
        if oof == 0:
            again = input("Do you want another calculation? (y/n)")
            if again == "y":
                initInput = eval(input("\nChoose what you want to formulate from below: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Square Root\n6. Exponent"))
                oof = 1
            elif again == "n":
                oof = 1
                break
            else:
                print("That is not a valid response, please try again.")
                break
     
     
        
    elif initInput == 2:
        num1, num2 = eval(input("Insert the 2 digits you would like to subtract!"))
        print(subtract(num1, num2))
        oof = 0
        if oof == 0:
            again = input("Do you want another calculation? (y/n)")
            if again == "y":
                initInput = eval(input("\nChoose what you want to formulate from below: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Square Root\n6. Exponent"))
                oof = 1
            elif again == "n":
                oof = 1
                break
            else:
                print("That is not a valid response, please try again.")
                break
        
        
        
    elif initInput == 3:
        num1, num2 = eval(input("Insert the 2 digits you would like to multiply!"))
        print(multi(num1, num2))
        oof = 0
        if oof == 0:
            again = input("Do you want another calculation? (y/n)")
            if again == "y":
                initInput = eval(input("\nChoose what you want to formulate from below: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Square Root\n6. Exponent"))
                oof = 1
            elif again == "n":
                oof = 1
                break
            else:
                print("That is not a valid response, please try again.")
                break        
        
        
        
        
    elif initInput == 4:
        num1, num2 = eval(input("Insert the 2 digits you would like to divide!"))
        print(divide(num1, num2))
        oof = 0
        if oof == 0:
            again = input("Do you want another calculation? (y/n)")
            if again == "y":
                initInput = eval(input("\nChoose what you want to formulate from below: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Square Root\n6. Exponent"))
                oof = 1
            elif again == "n":
                oof = 1
                break
            else:
                print("That is not a valid response, please try again.")
                break
        
        
        
        
       
    elif initInput == 5:
        num1 = eval(input("Insert the digit you would like to find the square root of!"))
        print(sqrt(num1))
        oof = 0
        if oof == 0:
            again = input("Do you want another calculation? (y/n)")
            if again == "y":
                initInput = eval(input("\nChoose what you want to formulate from below: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Square Root\n6. Exponent"))
                oof = 1
            elif again == "n":
                oof = 1
                break
            else:
                print("That is not a valid response, please try again.")
                break
      
      
      
      
      
    elif initInput == 6:
        num1, num2 = eval(input("Insert the 2 digits first one being the primary number 2nd one being the exponent."))
        print(expo(num1, num2))
        oof = 0
        if oof == 0:
            again = input("Do you want another calculation? (y/n)")
            if again == "y":
                initInput = eval(input("\nChoose what you want to formulate from below: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Square Root\n6. Exponent"))
                oof = 1
            elif again == "n":
                oof = 1
                break
            else:
                print("That is not a valid response, please try again.")
                break
      
else:
    print("That is not a valid input")