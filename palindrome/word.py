w = input("enter word : ")

word = w
wo = ""
i = len(w) - 1

while i >= 0 :
    wo = wo + w[i]
    i -= 1

if w == wo :
    print("True,", word, "is a palindrome word.")
elif w != wo :
    print("False,", word, " is not a palindrome word.")
else :
    print("error")

