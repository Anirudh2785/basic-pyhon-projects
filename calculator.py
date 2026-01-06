num1 = float(input("enter number :"))
ao = input("enter + - / * :")   # ao = arthmatic operator 
num2 = float(input("enter number :"))

if ao == '+' :
    print("your result is : " , num1 + num2)
elif ao == '-' :
    print("your result is : " , num1 - num2)    
elif ao == '*' :
    print("your result is : " , num1 * num2)
elif ao == '/' :
    if num2 != '0':
        print("your result is : " , num1 / num2 )    
    else:    
        print("error : Division by zero not allowed")
else:
    print("invalid operator")