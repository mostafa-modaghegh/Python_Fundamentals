# Calculator Functions 


def add(a, b):
    return a + b  # addition

def sub(a, b):
    return a - b  # subtraction

def mul(a, b):
    return a * b  # multiplication

def div(a, b):
    if b == 0:
        return "Error"  # division by zero
    return a / b

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def remainder(a, b):
    return a % b


# Main Program 

while True:
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Factorial")
    print("6. Sum 1 to N")
    print("7. Remainder")
    print("8. Exit")

    choice = input("Choose option: ")

    match choice:

        # Exit
        case "8":
            print("Exiting...")
            break

        # Factorial
        case "5":
            n = int(input("Enter number: "))
            print("Result:", factorial(n))

        # Sum 1..N
        case "6":
            n = int(input("Enter N: "))
            print("Sum:", sum_to_n(n))

        # Remainder
        case "7":
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            print("Remainder:", remainder(a, b))

        # Add, Sub, Mul, Div
        case "1" | "2" | "3" | "4":
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))

            match choice:
                case "1":
                    print("Result:", add(a, b))
                case "2":
                    print("Result:", sub(a, b))
                case "3":
                    print("Result:", mul(a, b))
                case "4":
                    print("Result:", div(a, b))

        # Invalid choice
        case _:
            print("Invalid option.")
