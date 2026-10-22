# تمرین ۱: برنامه‌ای که یک عدد از کاربر بگیرد و مشخص کند منفی، مثبت یا صفر است.

# get number from user
num = float(input("Enter a number: "))

# check if number is positive, negative or zero
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
