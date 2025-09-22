import threading

class LazyLoader:
    def __init__(self, method_path, method_class, class_init_argument):
        self.method_path = method_path
        self.method_class = method_class
        self.class_init_argument = class_init_argument
        self.class_instance = None
        print('lazy class: %s %s' % (self.method_path, self.method_class))

    def __load_class(self):
        if self.class_instance is None:
            with threading.Lock():
                if self.class_instance is None:
                    print('load class once')
                    module = __import__(self.method_path, fromlist=[self.method_class, ])
                    class_cls = getattr(module, self.method_class)
                    self.class_instance = class_cls(**self.class_init_argument)
    
    def __getattr__(self, name):
        print('call_function:%s' % name)
        self.__load_class()
        setattr(self, name, getattr(self.class_instance, name))
        return getattr(self, name)
        