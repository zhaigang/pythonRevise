import random
import time

def my_decorator(*args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)
    # return args[0] # there must return a executable function,otherwise this error occur error.

@my_decorator
def function1_basic():
    print('execute function')
    time.sleep(random.randint(3, 4))
    return True, 'Bussinse run success'

function1_basic()