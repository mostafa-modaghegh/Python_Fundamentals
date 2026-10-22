# تمرین ۴: f-string و دیکشنری
# نام، تخلص و سن کاربر را گرفته و در دیکشنری ذخیره کنید.
# سپس با f-string بنویسید چند سال دیگر کاربر چند ساله خواهد بود.

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))

user = {
    "first_name": first_name,
    "last_name": last_name,
    "age": age
}

# محاسبه‌ی سن کاربر در ۵ سال آینده
future_age = user["age"] + 5

# نمایش نتیجه با استفاده از f-string
print(f"{user['first_name']} {user['last_name']} will be {future_age} years old in 5 years.")
