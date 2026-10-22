# تمرین ۴: کار با لیست و شرط ساده
# یک لیست از ۵ عدد ایجاد کن، از کاربر بپرس آیا می‌خواهد لیست را ببیند یا نه.

numbers = [10, 20, 30, 40, 50]   # list of numbers

# ask user if they want to see the list
answer = input("Do you want to see the list? (for yes enter Y/for no enter N): ")

if answer == "Y":
    print("Here is the list:", numbers)
else :
    print("Hello world")
