d = {}

d["name"] = "aaaa"
d["sub"] = "python"
d["marks"] = (11,22,33)
d["incomeMonth"] = [1000,2000,2200]
d[(11,22)] = "just a sample"
print(d)

print(d.pop("marks"))
print(d.popitem())
print(d)

'''
for key,val in d.items():
    print(key , " = ",val)
    
for x in d.keys():
    print(x)    
    
for x in d.values():
    print(x)
    
for x in d.values():
    print(x)
d["name"] = "bbb"
print(d.keys())
print(d.values())
print(d.items())

d.clear()
print(d)

    '''
