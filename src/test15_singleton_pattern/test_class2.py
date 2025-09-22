class MyClass:
    class_instance = None
    initialized = False
    def __new__(cls, *args, **kwargs):
        if MyClass.class_instance is None:
            print(f"1. __new__ called, create {cls.__name__} instance")
            MyClass.class_instance = super().__new__(cls)
        else:
            print('dont need instantiate class')
        return MyClass.class_instance

    # __init__ will run after __new__ return the class instance
    def __init__(self, name):
        if MyClass.initialized is False:
            print(f"2. __init__ called, and this class id is :%s" % id(self))
            self.name = name
            MyClass.initialized = True
        else:
            print("dont need init it.")

# instantiation
obj = MyClass("test")
obj2 = MyClass("test2")