
def my_decorator(*decorator_args, **decorator_kwargs):
    def wrapper(*wrapper_args, **wrapper_kwargs):
        def function(*function_args, **function_kwargs):
            print('function_args', function_args)
            print('function_kwargs', function_kwargs)
            return wrapper_args[0](*function_args, **function_kwargs)
        print("wrapper_args", wrapper_args)
        print("wrapper_kwargs", wrapper_kwargs)
        return function
    print('decorator_args', decorator_args)
    print('decorator_kwargs', decorator_kwargs)
    return wrapper

@my_decorator(5)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('my name is %s, my age is :%s' % (self.name, self.age))

obj = Person('Tom', 18)
obj.run()


