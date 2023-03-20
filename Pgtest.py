n = '78hjuib841'
s = ""
n = ""
for i in n:
    if i.isdigit():
        n = n + i
    elif isinstance(i, str):
        s = s + i
    else:
        print("non alpha numeric")
print(s)
print(n)
