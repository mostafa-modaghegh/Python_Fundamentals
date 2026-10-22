students = []

for i in range(5):
    name = input("Enter name: ")
    math = float(input("Math score: "))
    english = float(input("English score: "))
    programming = float(input("Programming score: "))

    student_info = {
        "Name": name,
        "Math": math,
        "English":english,
        "Programming":programming 
    }

    students.append(student_info)

for i in students:
    print("Name:",i["Name"])
    print("Math score:",i["Math"])
    print("English score:",i["English"])
    print("Programming score:",i["Programming"])