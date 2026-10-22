# برنامه شماره ۱
# ایجاد یک لیست از نام‌ها و بررسی حضور نام ورودی

# ایجاد لیست اولیه از نام‌ها
names = ["Ali", "Farhad", "Omid", "Edris", "Mirwais"]

# گرفتن نام از کاربر
user_name = input("Enter your name: ")

# بررسی اینکه آیا نام در لیست وجود دارد یا نه
if user_name in names:
    print("Hello", user_name, ", welcome to the program!")
else:
    print("You were not in the list, but now you are added.")
    names.append(user_name)   # افزودن نام جدید به لیست

# چاپ لیست نهایی
print("Updated list:", names)
