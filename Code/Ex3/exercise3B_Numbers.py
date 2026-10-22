# برنامه شماره ۲
# دریافت دو عدد از کاربر و ذخیره اعداد زوج بین آن‌ها در لیست

start = int(input("Enter first number: "))
end = int(input("Enter second number: "))

# ایجاد یک لیست خالی برای ذخیره اعداد زوج
even_numbers = []

# حلقه برای عبور از محدوده اعداد
for num in range(start, end + 1):
    if num % 2 == 0:        # بررسی زوج بودن
        even_numbers.append(num)

# چاپ لیست اعداد زوج
print("Even numbers:", even_numbers)

# شمارش تعداد اعداد در لیست
print("Total even numbers:", len(even_numbers))
