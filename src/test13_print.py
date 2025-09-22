print('simple print')
print('simple print', 'with a value')
print('print list', ['a', 'b'])
print('print tuple', ('a', 'b'))
print('print set', (('a', 'b')))

class test_class:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
obj = test_class(4, 5)
print(obj)

class test_print_class(test_class):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return 'class test_print_class: x=%s,y=%s' % (self.x, self.y)

obj2 = test_print_class(5, 6)
print(obj2)


print('is_number:%d, %f' % (5, 1.5))
print('is_number:%d, %.2f' % (5, 1.54321))
print('is_number:%d, %.2f' % (5, 1.5))


print('is_string:%s' % '12345678910')
print('is_string:%5send' % '1')
print('is_string:%5send' % '12345678910')
print('is_string:%.5send' % '1')
print('is_string:%.5send' % '12345678910')


print('{} to {}'.format(4,5))
print('{var1} to {var2}'.format(var1=4,var2=5))
var1=5
var2=6
print(f'{var1} to {var2}')