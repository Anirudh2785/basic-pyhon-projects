# word = input("enter word : ")
# print(word[::-1])

w = input("enter word : ")

wo = ""
i = len(w) - 1

while i >= 0 :
    wo = wo + w[i]
    i -= 1

print("your revers word is ",wo)