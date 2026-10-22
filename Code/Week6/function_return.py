# ======================================
# Return in Python Functions
# ======================================


# ----------------------------
# Example 1: basic return
# ----------------------------
def add(a, b):
    # تابع جمع دو عدد و برگرداندن نتیجه
    return a + b

result = add(5, 7)
print("Result (Example 1):", result)  # خروجی: 12


# ----------------------------
# Example 2: return vs print
# ----------------------------
def add_print(a, b):
    # این فقط چاپ می‌کند و مقدار را برنمی‌گرداند
    print(a + b)

value = add_print(3, 4)
print("Value returned:", value)  # خروجی None چون return نداشتیم


# ----------------------------
# Example 3: multiple returns
# ----------------------------
def math_ops(a, b):
    # جمع و تفریق را برمی‌گرداند
    return a + b, a - b

s, d = math_ops(10, 3)
print("Sum:", s)
print("Difference:", d)


# ----------------------------
# Example 4: return inside loop
# ----------------------------
def find_first_even(nums):
    # اولین عدد زوج را پیدا کرده و برگرداند
    for n in nums:
        if n % 2 == 0:
            return n  # بقیه اجرا نمی‌شود

print("First even number:", find_first_even([1, 3, 5, 8, 12]))


# --------------------
