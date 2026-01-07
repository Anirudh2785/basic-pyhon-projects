
print("1. Numbers from 1 to 100")
print("2. Odd Numbers (1 to 100)")
print("3. Even Numbers (1 to 100)")
print("4. Factorial of a Number")

choice = int(input("Enter your choice (1-6): "))

                    # 1 to 100
if choice == 1:
    for i in range(1, 101):
        print(i)

                     # Odd numbers
elif choice == 2:
    for i in range(1, 101):
        if i % 2 != 0:
            print(i)

                     # Even numbers
elif choice == 3:
    for i in range(1, 101):
        if i % 2 == 0:
            print(i)

                     # Factorial
elif choice == 4:
    num = int(input("Enter a number: "))
    fact = 1

    i = 1
    while i <= num:
        fact = fact * i
        i = i + 1

    print("Factorial of is", fact)

else:
    print("error")

