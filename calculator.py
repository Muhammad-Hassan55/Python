def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

num_1 = float(input("please enter any number: "))

operator = input("Enter any operator ( + - * / ) : ")

num_2 = float(input("please enter any number: "))

if operator == "+":
    print("Result : ",add(num_1,num_2))

elif operator == '-':
    print("Result : ", subtract(num_1, num_2))

elif operator == '*':
    print("Result : ", multiply(num_1, num_2))

elif operator == '/':
    print("Result : " , divide(num_1,num_2))

else:
    print("invalid number ,PLEASE TRY AGAIN")