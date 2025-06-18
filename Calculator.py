# Function definations 
def add (x, y) :
    return x + y 

def substract (x, y) :
    return x - y

def multiply (x, y) :
    return x * y

def divide (x, y) :
    if y==0:
        return "Error! Division by zero."
    return x/y

# Main programm
print ("Welcom to the simple calculator.")

#Display option 
print ("Select operator:")
print ("1. +")
print ("2. -")
print ("3. *")
print ("4. /")

#Get user input 
choice = input("Enter choice(1/2/3/4): ")

#Check if choice is valid 
if choice in ('1', '2', '3','4'):

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))

    elif choice == '2':
        print("Result:", substract(num1, num2))
    
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    
    elif choice == '4':
        print("Result:", divide(num1, num2))
    
else:
    print("Invalid input!")