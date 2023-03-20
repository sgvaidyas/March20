l = [3,3,4,6,4,8,5,3];
l = list(dict.fromkeys(l))
l.sort()
for i in range(max(l)+1):
    if i not in l and i>0:
        print (i)
