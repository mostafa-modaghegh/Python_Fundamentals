# برنامه مدیریت نمرات محصل
# ورودی: نمرات سه درس (ریاضی، زبان انگلیسی، برنامه نویسی)
# خروجی: نمایش میانگین نمرات

math = float(input("Enter your Math score: "))
english = float(input("Enter your English score: "))
programming = float(input("Enter your Programming score: "))

average = (math + english + programming) / 3
print("Your average score is:", average)
