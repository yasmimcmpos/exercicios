# =========================Unpacking use=====================
# Get all the values contained in the tuple and sing each on to a different
# variable.

# ========Exercise 1======
# In Tuples:
products = [
    ("iphone", 5_000, 2020),
    ("notebook", 10_000, 2025),
    ("airpods", 1_000, 2024),
]

for name, price, manufactured in products:
    print(name, price, manufactured)

# or use a '_' for variables witch you don't want use

for _, price, manufactured in products:
    print(price, manufactured)


# In Def:


def calc_impost(sales: int):
    ir = 0.10 * sales
    csll = 0.035 * sales
    return ir, csll


ir, csll = calc_impost(1000)
print(ir, csll)


# ======Exercise 2======
# Receive a list of num int from the user
# Use unpacking to separate the first number from the list and the remaining
# numbers
# Calculate:
# The sum of all numbers
# The product of the first number and the sum of the remaining numbers
# Display the results

number = [
    1,
    50,
    100,
    500,
]

num1, *remaining = number
# '*' I don't know how much numbers have

sum_all = sum(number)
print(sum_all)

remaining = sum(remaining)
print(remaining)

product = num1 * (remaining)
print(product)
