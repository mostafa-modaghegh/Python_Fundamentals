# این برنامه از match-case استفاده می‌کند و تا وقتی گزینه 3 وارد نشود ادامه دارد

while True:
    print("\nMenu:")
    print("1. Sum from 1 to N")
    print("2. Print all even numbers to N")
    print("3. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            # گرفتن عدد N و محاسبه مجموع 1 تا N
            n = int(input("Enter N: "))
            total = 0
            for i in range(1, n + 1):
                total += i
            print("Sum =", total)

        case "2":
            # چاپ اعداد زوج تا N
            n = int(input("Enter N: "))
            for i in range(1, n + 1):
                if i % 2 == 0:
                    print(i)

        case "3":
            # خروج از برنامه
            print("Exiting program...")
            break
        
        case _:
            # در صورت وارد شدن گزینه اشتباه
            print("Invalid choice, try again!")
