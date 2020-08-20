setofpeople = [
    {"name": 'Jack', "house": "Howard"},
    {"name": 'Rebecca', "house": "Harvard"},
    {"name": 'Kevin', 'house': 'Hollywood'},
    {"name": 'Dracon', 'house': 'Ravenclaw'}
]

def f(setofpeople):
    return setofpeople['house']

setofpeople.sort(key=f)

print(setofpeople)