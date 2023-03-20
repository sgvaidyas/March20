'''
a = [11,22,33,44,"kjhkjh",77.8,4+6j]



for i in range(len(a)):

    print(a[i]," = " , type(a[i]))


print(a)



a = []
a.append(111)
a.append(222)
a.append(333)
a.append([22,33,44])
print(a)
print(a[3][1])

a.extend([11,22,33,44,55])
print(a)

'''



a = [11,22,33,44]
print(a*3)
b = [1,2,3]

c = a+b
print(c)

print(max(a))
print(min(a))
print(sum(a))


