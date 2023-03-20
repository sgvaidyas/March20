n = int(input("Enter n: "))

#roof
for i in range(1, n+1):
    print((n-i) * " ", end="")
    print("/", end = "")
    print((2*(i-1)) * " ", end="")
    print("\\")

#roof bottom
print((2*n) * "-")

#walls
for i in range(1, n):
    print("|", end = "")
    print((2*(n-1)) * " ", end="")
    print("|")

#floor
print("|", end="")
print((2*(n-1)) * "_", end="")
print("|")
