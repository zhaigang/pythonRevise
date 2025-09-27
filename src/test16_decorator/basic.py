import random
import time

def function1_basic():
    time.sleep(random.randint(3, 4))
    return True, 'Bussinse run success'

print(function1_basic())
