# تمرین ۲: بررسی شرایط شرکت در مسابقه
# شرط: فقط افراد از شهر کابل با سن کمتر از ۳۰ سال می‌توانند شرکت کنند.

age = int(input("Enter your age: "))
city = input("Enter your city: ")

if age < 30 and city == "Kabul":
    print("You can participate in the competition ✅")
else:
    print("Sorry, you cannot participate ❌")
