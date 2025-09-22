def func_a():
    pass

def func_b():
    pass



class ParentClass:
    def step_a(self):
        pass

    def step_b(self):
        pass

    def run(self):
        self.step_a()
        self.step_b()

class ChildClass(ParentClass):
    def step_a(self):
        print('is child step a')

    def step_b(self):
        print('is child step b')

obj = ChildClass()
obj.run()


        
