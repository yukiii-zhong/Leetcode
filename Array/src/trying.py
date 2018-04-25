'''
dic = {'c':1, 'b':2,'a':3}
print(dic)

a = sorted(dic)
print(a)
print(sorted(dic,key = lambda k: dic[k]))


L = [
    {'x': 3, 'y': 2, 'z': 1},
    {'x': 2, 'y': 1, 'z': 3},
    {'x': 1, 'y': 3, 'z': 2},
]


L.sort(key=lambda dic: dic['z'])

print(L)
'''

dic = {
    'a': {'x': 3, 'y': 2, 'z': 1},
    'b': {'x': 2, 'y': 1, 'z': 3},
    'c': {'x': 1, 'y': 3, 'z': 2},
}
print(dic)
L = sorted(dic,key=lambda k:dic[k]['y'])

print(L)
