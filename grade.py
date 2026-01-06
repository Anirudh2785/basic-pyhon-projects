sub1 = int(input("enter your 1'st subujet mark :"))
sub2 = int(input("enter your 2'nd subujet mark :"))
sub3 = int(input("enter your 3'rd subujet mark :"))
sub4 = int(input("enter your 4'th subujet mark :"))
sub5 = int(input("enter your 5'th subujet mark :"))

add =   sub1 + sub2 + sub3 + sub4 + sub5
pct = add / 500 * 100 

if pct > 90:
    print(" grade : A")
elif pct > 80 and pct <= 90:
    print(" grade : B")
elif pct > 70 and pct <= 80:
    print(" grade : c")
elif pct > 60 and pct <= 70:
    print(" grade : D")
else :
    print(" grade : F ")