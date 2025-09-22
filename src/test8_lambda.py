f1 = lambda : print('test arg1, arg2\n you should give arg3')

f1()

f2 = lambda x: x*x

print(f2(2))

f3 = lambda x,y: x*y

print(f3(5, 3))

pairs = [(1, 'one'), (2, 'two'), (4, 'four'), (3, 'three')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)


pairs.sort(key=lambda pair: pair[0], reverse=True)
print(pairs)