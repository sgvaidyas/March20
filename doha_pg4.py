n=5
for i in range(1,n+1):
    print((" "*((n+2)-i)+("*"*(i)))+("*"*(i-1)),end="\n")

print(" "+"*"*(n-1)+(" "*n)+"*"*(n-1))
print("*"*(n)+(" "*n)+"*"*(n))
print(" "+"*"*(n-1)+(" "*n)+"*"*(n-1))
for i in range(1,n+1):
    print((" "*(i+1)+("*"*(((n+1))-i))+("*"*(n-i))),end="\n")
