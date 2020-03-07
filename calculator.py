def add(x,y):
    return x+y

def substract(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def divide(x,y):
    return x/y

number1=float(input("Enter a number: "))
operator=input("Enter the operator: ")
number2=float(input("Enter another number: "))

if operator=='+':
   print(number1,"+",number2,"=",add(number1,number2))
elif operator=='-':
    print(number1,"-",number2,"=",substract(number1,number2))
elif operator=='*':
    print(number1,"*",number2,"=",multiplication(number1,number2))
elif operator=='/':
    print(number1,"/",number2,"=",divide(number1,number2))
else:
    print("Incorrect operator")

