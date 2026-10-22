#وارد کردن ۱۰ عدد مثبت و محاسبه مجموع آن

sum = 0
for i in range(10):
    num = float(input("Enter a positive number: "))
    if num > 0 :
        sum += num  # sum = sum + num
    else:
        break
    if i == 9:
        print("sum is:",sum)
 
  