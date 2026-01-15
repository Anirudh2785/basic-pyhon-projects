num = int(input("enter number : "))

n = int(num**0.5)
n +=1 

small = []
large = []

print("division of",num,"are : ",end=" ")

for i in range (1,n):
    rim = num % i 
    if rim == 0 :
        div = int(num / i) 
        if div == i : 
           small.append(i)
        else :
            small.append(i)
            large.append(div)
    else :
        print(end="")

large.reverse()

re = small + large

for no in re:
    print(no,end=" , ")