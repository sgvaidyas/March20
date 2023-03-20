n = int(input("Enter the n = "))

for i in range(1,n+1):
    print(" "*(n-i) + "/" + " "*((i-1)*2) + "\\")
print("-"*2*n + "\n" +("|" + " "*2*(n-1) + "|\n" )*(n-1),end="")
print("|" + "_"*2*(n-1) + "|\n" )
