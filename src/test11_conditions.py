print('1', 'value a' or 'value b')
print('2', '' or 'value a' or 'value b')
print('3', 0 or 'value a' or 'value b')
print('4', None or 'value a' or 'value b')

print('5', 'value a' and 'value b')
print('6', '' and 'value a' and 'value b')
print('7', 0 and 'value a' and 'value b')
print('8', None and 'value a' and 'value b')

print('9', [one for one in [1,2,3,4, None] ])
print('10', [one for one in [1,2,3,4, None] if one is not None])
print('11', [one for one in [1,2,3,4, None] if one is not None and one % 2 == 0])

httpcode = 200
print('12', 'execute success' if httpcode == 200 else  'execute failed')
print('13', True if not httpcode == 200 and False else False)