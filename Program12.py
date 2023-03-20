t = (22,)
t1 = tuple([11])
print(t,type(t))
print(t1,type(t1))


t1=(11,22,33)
t2=(1,2,3)

t3 = t1+t2
print(t3)
print(max(t3))
print(min(t3))
print(sum(t3))
print(t3.count(33))


print(33 in t3)
print(33 not in t3)
