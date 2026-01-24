def f(i , n):
    if i > n :
        return
    print(i)
    f(i + 1 , n)
def main():
    n = int(input("enter number : "))
    f(1 , n)
main()
    