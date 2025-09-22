class MyClass:
    class_var = None
    # custom define __new__，observe how to create
    def __new__(cls, *args, **kwargs):
        print(f"1. __new__ called, create {cls.__name__} instance")
        # call father class __new__function and retruen a instance 
        instance = super().__new__(cls)
        return instance

    # __init__ will run after __new__ return the class instance
    def __init__(self, name):
        print(f"2. __init__ called, and class_var id is :%s" % id(MyClass.class_var))
        self.name = name

# instantiation
obj = MyClass("test")
obj2 = MyClass("test2")