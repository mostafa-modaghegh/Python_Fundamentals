sum = 0
for i in range(10):
    number = float(input("enter a number: "))
    sum += number
    if sum > 50:
        print("Too large!")
        break
    if i == 9:
        print(sum)    