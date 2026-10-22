# محاسبه مجموع و میانگین تعدادی عدد
count = int(input("How many numbers you want to enter? "))

total = 0
for i in range(count):
    num = float(input("Enter a number: "))
    total += num

average = total / count

print("Sum =", total)
print("Average =", average)

if average < 40:
    print("Low performance")
elif average <= 80:
    print("Good")
else:
    print("Excellent")
