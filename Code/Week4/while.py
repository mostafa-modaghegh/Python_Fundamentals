# while   condition:
#     do something
#when? until condition is true 

i = 0
total = 0

while i < 20:
    user_input = float(input("Enter your number: "))

    if user_input == 0:
        break

    total += user_input

    if i == 19:
        print(total)

    i += 1
    