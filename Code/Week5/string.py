# ================================
# Python String Tutorial
# رشته ها در پایتون
# رشته ها دنباله ای از کاراکترها هستند
# مرتب دار و غیرقابل تغییر (immutable)
# ================================

text = "Hello Python"

# چاپ
print(text)

# طول رشته
print(len(text))

# دسترسی با ایندکس
print(text[0])
print(text[-1])

# تکه برداری (Slicing)
print(text[0:5])   # Hello
print(text[6:])    # Python
print(text[:5])    # Hello
print(text[::2])   # HloPto

# تغییر حروف
msg = "hello world"
print(msg.upper())
print(msg.lower())
print(msg.title())       # هر کلمه اول بزرگ
print(msg.capitalize())  # فقط اول جمله بزرگ
print(msg.swapcase())    # برعکس کردن بزرگی و کوچکی

# جستجو و جایگزینی
print(msg.find("world"))
print(msg.replace("world", "Python"))

# حذف فضاهای اضافی
name = "   Ali   "
print(name.strip())
print(name.lstrip())
print(name.rstrip())

# بررسی شروع/پایان رشته
print(text.startswith("Hello"))
print(text.endswith("thon"))

# شمارش تکرار کاراکتر
print(msg.count("l"))

# تقسیم و اتصال رشته
words = "apple,banana,orange".split(",")
print(words)

print("-".join(["A", "B", "C"]))

# چک کردن نوع کاراکتر
s = "abc123"
print(s.isalpha())  # فقط حرف؟
print(s.isdigit())  # فقط عدد؟
print(s.isalnum())  # حرف + عدد؟
print("hello".islower())
print("HELLO".isupper())

# جایگذاری با فرمت f-string
name = "Sara"
age = 20
print(f"My name is {name} and I am {age} years old")

print("Done ✅")
