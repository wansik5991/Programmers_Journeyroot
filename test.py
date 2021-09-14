a = ['inc']

from collections import defaultdict
b = defaultdict(list)
b['1'] = [1,2,3,4,5]
b['2'] = [6,7,8,9,10]

print(b.items())
print(sum(list( map( lambda x : x[1], b.items() ) )[0] ) )

print(2 in map( lambda x : x[1], b.items()))
print(7 in list(map( lambda x : x[1], b.items())))