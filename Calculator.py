def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def modulo(a,b):
    return a%b
print("Welcome to the Calculator !!")
number1=int(input("Enter the first number : "))
number2=int(input("Enter the second number: "))
flag=True
r=0
print("Operations available are :")
print("1 - addiition")
print("2 - subtraction")
print("3 - multiplication")
print("4 - division")
print("5 - modulo")
choice=int(input("Enter the operation to be performed: "))
print("Processing.....")
if choice==1:
    r=add(number1,number2)
elif choice==2:
    r=sub(number1,number2)
elif choice==3:
    r=multiply(number1,number2)
elif choice==4:
    r=divide(number1,number2)
elif choice==5:
    r=modulo(number1,number2)
else:
    flag=False
    print("Sorry this operation is not there in this calculator!")
# r=add(number1,number2)
if flag:
    print("The result is ",r)