'''l = [11,22,33,33,44,55,66,22,66,78,55,66,77,88]

l.insert(3,6666)
print(l)
l.remove(66)
print(l)

print(l.pop())
l.pop(6)
print(l)

print(l.count(33))

print(6666 in l)
print(6666 not in l)

a=999999
b = a
print(id(a))
print(id(b))
b=5554
print(a,b)
print(id(a))
print(id(b))

l=[11,22,33]
b = l

print(l)
print(b)
b.append(345)
b.append("aaa")
print(l)
print(b)


l=[11,22,33]
b = l.copy()

print(l)
print(b)
b.append(345)
b.append("aaa")
print(l)
print(b)
'''
import copy
l=[11,22,33,[1,2,3,4]]
b = copy.deepcopy(l)

print(l)
print(b)
b.append(345)
b.append("aaa")
b[3][0] = 8888
print(l)
print(b)






