# is annotation
print('hellow world')


a = 5
print(type(a))
print(dir(a))
print(a.__class__)

b = "string"
print(type(b))
print(dir(b))
print(b.__class__)


c = 'string2'
d = '''string3'''
e = """string4"""
print(c)
print(d)
print(e)

f = "select a from table_a where a='f' "
print(f)
g = 'select a from table_a where a=\'g\' '
print(g)
h = '''Select table_a.field_a, xxxx,
    from table_a
    inner join table_b
'''
print(h)

def func_1(args1):
    """
    this function is used for test
    :args1 int : you need give me a argrs
    """
    pass

print(f + g)
print('%s%s' % (f, g))
print('{}{}'.format(f,g))
print('{var1}{var2}'.format(var1=f, var2=g))
print(func_1.__doc__)