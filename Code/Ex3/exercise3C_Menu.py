# برنامه شماره ۳
# شبیه‌سازی منوی ساده با استفاده از match-case

print("Menu:")
print("1. Say hello")
print("2. Show numbers 0 to 10")
print("3. Mean of 4 numbers")
print("4. Say Goodbye")

# گرفتن عدد از کاربر برای انتخاب گزینه
choice = int(input("Enter your choice (1-4): "))

# استفاده از match برای انجام عمل مربوط به هر گزینه
match choice:
    case 1:
        print("Hello, user!")

    case 2:
        for i in range(11):   # چاپ اعداد از 0 تا 10
            print(i)

    case 3:
        total = 0
        for i in range(4):    # گرفتن ۴ عدد و جمع آن‌ها
            num = float(input(f"Enter number {i+1}: "))
            total = total + num
        mean = total / 4
        print("The mean of these numbers is:", mean)

    case 4:
        print("Goodbye!")

    case _:
        print("Invalid choice, please select from 1 to 4.")
