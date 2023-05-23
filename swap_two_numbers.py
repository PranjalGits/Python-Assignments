def swap_variables(a, b):
    temp = a
    a = b
    b = temp
    return a, b

x = 5
y = 10
print("Before swap: x =", x, "and y =", y)

x, y = swap_variables(x, y)
print("After swap: x =", x, "and y =", y)