#پنج نام از کاربر بگیرید و به آنها سلام کنید به جز شفیق

for i in range(5):
    name = input("enter your name: ")
    if name == "Shafiq":
        continue
    print(f"Hello, Mr {name}")


#اعداد یک تا سی ، به جز مضارب پنج را نمابش دهید.
for i in range(1,30):
    if i % 5 == 0:
        continue
    print(i)