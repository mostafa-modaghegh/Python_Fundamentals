# گرفتن یک عدد و ضرب آن در اعداد 0 تا 9
num = int(input("Enter a number: "))

for i in range(10):
    print(num, "x", i, "=", num * i)
