n = int(input())
for i in range(1, n + 1):
    print ((n - 1) * " " + (n - i) * " " + (2 * i - 1) * "*")
for i in range (1, n):
    print((n - i - 1) * " " + (i + 1) * "*" + (2 * n - 3)* " " + (i + 1) * "*")
for i in range (1, n - 1):
    print (i * " " + (n - i) * "*" + (2 * n - 3)* " " + (n - i) * "*")
if n > 1:
    for i in range (1, n + 1):
        print ((n - 2 + i) * " " + (2 * (n - i + 1) - 1) * "*")
