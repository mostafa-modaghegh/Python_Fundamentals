# تمرین ۳: محاسبه میانگین نمرات و تعیین وضعیت تحصیلی

# get three scores
math = float(input("Enter Math score: "))
english = float(input("Enter English score: "))
programming = float(input("Enter Programming score: "))

# calculate average
average = (math + english + programming) / 3

print(f"Your average is: {average}")

# check grade level
if average >= 75 and average <= 100:
    print("Excellent")
elif average >= 50 and average < 75:
    print("Good")
elif average >= 25 and average < 50:
    print("Average")
else:
    print("Needs more effort")
