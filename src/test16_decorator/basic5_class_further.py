
class MyDecorator:
    def __init__(*decorator_args, **decorator_kwargs):

        print('decorator_args', decorator_args)
        print('decorator_kwargs', decorator_kwargs)

    def __call__(self, *call_args, **call_kwargs):

        def wrapper(*wrapper_args, **wrapper_kwargs):
            print('wrapper args', wrapper_args)
            print('wrapper kwargs', wrapper_kwargs)
            call_args[0](*wrapper_args, **wrapper_kwargs)
        print('call_args', call_args)
        print('call_kwargs', call_kwargs)
        return wrapper
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @MyDecorator(5)
    def run(self, kilometers):
        print('my name is %s, my age is :%s, today i will run %s kilometers' % (self.name, self.age, kilometers))

obj = Person('Tom', 18)
obj.run(8)


