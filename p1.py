n = input("Enter alphanumeric input: ")
b = ""
a = ""
for i in n:
    if i.isdigit():
        a = a + i
    elif isinstance(i, str):
        b = b + i
print("a: ",a)
print("b: ",b)
