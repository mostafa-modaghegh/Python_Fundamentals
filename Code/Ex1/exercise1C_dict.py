# تمرین ۳: دیکشنری از ولایت‌ها و جمعیت‌ها
# دیکشنری شامل ۵ ولایت و جمعیت آن‌ها ایجاد کنید.
# سپس یک مورد را با del حذف کرده، یک مورد جدید اضافه کنید و یک مورد دیگر را با pop حذف نمایید.

provinces = {
    "Kabul": 5000000,
    "Herat": 2000000,
    "Balkh": 1500000,
    "Nangarhar": 1800000,
    "Kandahar": 1300000
}

print(provinces)

# حذف با del
del provinces["Herat"]

# افزودن مورد جدید
provinces["Badakhshan"] = 900000

# حذف با pop
provinces.pop("Balkh")

print("keys:", provinces.keys())
print("values:", provinces.values())
print("items:", provinces.items())
