# ================================
# Python List Tutorial
# لیست ها در پایتون
# لیست ها مجموعه ای از آیتم ها هستند که
# قابل تغییر (mutable)
# مرتب دار (ordered)
# و قابلیت نگهداری داده‌های تکراری دارند
# ================================

# ایجاد لیست
my_list = [10, 20, 30, "Python", True]

print(my_list)  # چاپ لیست

# دسترسی به عناصر لیست
print(my_list[0])  # عنصر اول
print(my_list[-1]) # آخرین عنصر

# تغییر مقدار یک عنصر
my_list[1] = 200

# اضافه کردن عنصر جدید
my_list.append("New item")  # اضافه به آخر
my_list.insert(2, "Inserted item")  # افزودن در مکان مشخص

# حذف عناصر
my_list.remove("Python")  # حذف اولین مقدار مطابق
deleted_item = my_list.pop(0)  # حذف با ایندکس
my_list.pop()  # حذف آخرین عنصر

# پاک کردن کل لیست
# my_list.clear()

# طول لیست
print(len(my_list))

# بررسی عضویت
print(30 in my_list)

# شمارش یک مقدار
numbers = [1, 2, 2, 3, 2, 4]
print(numbers.count(2))

# پیدا کردن ایندکس
print(numbers.index(3))  # مکان 3

# مرتب سازی لیست
nums = [10, 3, 8, 1]
nums.sort()  # صعودی
print(nums)

nums.sort(reverse=True) # نزولی
print(nums)

# کپی لیست
copy_list = nums.copy()

# ترکیب دو لیست
a = [1, 2, 3]
b = [4, 5]
a.extend(b)  # اضافه کردن b به a

# حلقه روی لیست
for item in a:
    print(item)

# تبدیل رشته به لیست
text = "a,b,c"
parts = text.split(",")
print(parts)

# تبدیل لیست به رشته
print(",".join(["apple", "banana", "orange"]))

print("Done ✅")
