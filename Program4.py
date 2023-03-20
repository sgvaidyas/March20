m1 = int(input("Enter the marks 1  = "))
m2 = int(input("Enter the marks 2  = "))
m3 = int(input("Enter the marks 3  = "))

total = m1+m2+m3
avg = total/3

if avg>=0 and avg<=34:
    print("fail")
elif avg>34 and avg <=60:
    print("Pass class")
elif avg>60 and avg <=80:
    print("Second class")
elif avg>80 and avg <=100:
    print("First class")
else:
    print("\n invalid marks \n")
