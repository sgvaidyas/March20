def message():
    print("Just a message")
def add(a,b):
    print("SUM = ",a+b)

def swap(a,b):
    return b,a

def maximum(a=0,b=0):
    if(a>b):
        return a
    else:
        return b
def fun(a,b,c=0):
    print(a,b,c)

def fun1(*args):
    print(type(args))
    for x in args:
        print(x)

def fun2(a):
    for x in a:
        print(x)

def fun3(**kwargs):
    print("------------------------")
    for x,y in kwargs.items():
        print(x, ": ",y)

message()
add(3,44)
a=88
b=11
a,b = swap(a,b)
print(a,b)
print(swap(a,b))
print(maximum(22,77))
fun(22,33,43)
fun(c=77,a=11,b=29)

fun1(11,22,33,44,55,77,[8888,99,76],(66,44,33))
#fun2([22,33,44])

fun3(name="Shilpa",age=34)
