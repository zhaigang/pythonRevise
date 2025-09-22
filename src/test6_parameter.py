def func_a():
    print('func_a not have parameter')

func_a()

def func_add(a, y):
    print('func_add need two argument:%s + %s = %s' % (a, y, a+y))

func_add(4, 7)
func_add(a=6, y=7)
func_add(y=7, a=1)

parameter_1 = [1, 3]
func_add(*parameter_1)

parameter_2 = (2, 4)
func_add(*parameter_2)

parameter_3 = {'a': 8, 'y': 9}
func_add(**parameter_3)


def func_add_five_default(a, y=5):
    print('func_add_default_five need two argument:%s + %s = %s' % (a, y, a+y))
func_add_five_default(1)

#def func_add_five_default_v2(y=5, a):
#    pass

def func_add_many_number(*args):
    result = 0
    for i in args:
        result += i
    print('too many value add result is %s' % result)

func_add_many_number(1, 2, 3, 4)

def func_set_db_connect(host, db_user, db_password, port=3306, **argv):
    print('db_host is %s ' % host)
    print('db_user is %s ' % db_user)
    print('db_password is %s ' % db_password)
    print('db_port is %s ' % port)
    print('other argument:%s ' % str(argv))

func_set_db_connect('127.0.0.0', 'test_user', '123', connect_timeout=6)

parameter_4 = {'host': '127.0.0.1', 'db_user': 'test_user_2', 'db_password': '123', 'connect_timeout': 7}
func_set_db_connect(**parameter_4)

