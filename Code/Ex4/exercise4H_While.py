# گرفتن یک متن و تکرار آن تا زمانی که درست وارد شود
text = input("Enter a text: ")

while True:
    repeat = input("Repeat the text: ")
    if repeat == text:
        print("متن‌ها مطابقت دارند")
        break
    else:
        print("Incorrect! Try again.")
