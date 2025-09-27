from functools import wraps

def my_decorator(func):
    """this doc is for my_decorator"""
    @wraps(func) # use wraps to keep function doc and name
    def wrapper(*args, **kwargs):
        """this doc is for wrapper"""
        print("before run...")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def original_function(a, b):
    """this doc is for original_function"""
    return a + b

# 运行结果：
print(original_function.__name__) # if we not add the wraps to the wrapper, the output will be wrapper
print(original_function.__doc__)  # if we not add the wraps to the wrapper, the output will be this doc is for wrapper