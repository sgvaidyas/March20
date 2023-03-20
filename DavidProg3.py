n = int(input())
for i in range(1, n + 1):
    print((n - i) * " " + "/" + 2 * (i-1) * " " + "\\")
print(2 * n * "-")
for i in range (1, n):
    print("|" + (2*n - 2) * " " + "|")
print("|" + (2*n - 2) * "_" + "|")
