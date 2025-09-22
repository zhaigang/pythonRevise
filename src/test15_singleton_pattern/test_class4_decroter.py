def singleton(cls):  
    instances = {}  # 缓存所有单例类的实例  
    def wrapper(*args, **kwargs):  
        if cls not in instances:  
            instances[cls] = cls(*args, **kwargs)  
        return instances[cls]  
    return wrapper

@singleton
class MyClass:
    # __init__ will run after __new__ return the class instance
    def __init__(self, name):
        print(f"2. __init__ called, and this class id is :%s" % id(self))

# instantiation
obj = MyClass("test")
obj2 = MyClass("test2")