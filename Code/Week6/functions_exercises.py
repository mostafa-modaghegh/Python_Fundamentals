# =========================================
# Exercises using functions
# تابع ها – تمرین ها
# =========================================


# -----------------------------------------
# 1) تابع برای محاسبه میانگین سه عدد
# دریافت سه عدد از کاربر و محاسبه میانگین
# -----------------------------------------

def average_of_three(a, b, c):
    # جمع سه عدد تقسیم بر سه = میانگین
    avg = (a + b + c) / 3
    return avg

# گرفتن ورودی از کاربر
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))

print("Average =", average_of_three(n1, n2, n3))


# -----------------------------------------
# 2) تابع برای چاپ 1 تا 30
# با استفاده از حلقه داخل تابع
# -----------------------------------------

def print_numbers():
    # چاپ اعداد 1 تا 30
    for i in range(1, 31):
        print(i)

print("\nNumbers from 1 to 30:")
print_numbers()


# -----------------------------------------
# 3) تابع برای محاسبه محیط و مساحت مستطیل
# ورودی: طول و عرض
# خروجی: محیط و مساحت
# -----------------------------------------

def rectangle(width, height):
    # محیط = 2 * (طول + عرض)
    perimeter = 2 * (width + height)
    # مساحت = طول * عرض
    area = width * height
    return perimeter, area

# گرفتن اطلاعات از کاربر
w = float(input("\nEnter width of rectangle: "))
h = float(input("Enter height of rectangle: "))

p, a = rectangle(w, h)
print("Perimeter =", p)
print("Area =", a)


#تابع زوج یا فرد بودن عدد

def even_odd():
    a = int(input("Enter your number: "))    
    if a == 0:
        print("It is Zerooo!")
    elif a % 2 == 0:
        print("It is Even!")
    else:
        print("It is Odd")

even_odd()