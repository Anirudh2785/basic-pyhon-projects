class solution :

    def printnumber(self , current ):

        if current < 1:
            return 

        print(current , end=" ")

        self.printnumber(current - 1)

if __name__ =="__main__":
    sol = solution()
    n = int(input("enter the num = "))

    sol.printnumber(n)
    print()