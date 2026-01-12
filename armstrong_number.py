no = int(input("enter num :"))

a = no 
b = 0 


while a > 0:
    c = a % 10
    b = b + c*c*c
    a //= 10

if no == b :
    print("True,",no,"is a armstrong number" )
elif no != b :
    print("False,",no,"is a armstrong number")
else :
    print("error")

