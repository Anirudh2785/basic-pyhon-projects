class solution:

    def printNumber(self,current, i):

        if current < 1 :
            return

        print(current , end=" ")

        self.printNumber(current + 1 , i - 1)
        
        
if __name__ =="__main__":
    sol = solution()
    n = int(input("enter the num = "))

    sol.printNumber(1 , n)
    print()








    