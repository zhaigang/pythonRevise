import random
import time

def my_decorator(*decorator_args, **decorator_kwargs):
    def wrapper(*wrapper_args, **wrapper_kwargs):
        def function(*function_args, **function_kwargs):
            print('function_args', function_args)
            print('function_kwargs', function_kwargs)
            wrapper_args[0](*function_args, **function_kwargs)
        print("wrapper_args", wrapper_args)
        print("wrapper_kwargs", wrapper_kwargs)
        return function
    print('decorator_args', decorator_args)
    print('decorator_kwargs', decorator_kwargs)
    return wrapper

@my_decorator(5)
def function1_basic(bussiness_type):
    print('execute function:%s' % bussiness_type)
    time.sleep(random.randint(3, 4))
    return True, 'Bussinse run success'

function1_basic('create cloud server')
