from enum import Enum

class Zoo(Enum):
    Dog = 'dog'
    Sheep = 'sheep'
    calf = 'calf'

class SystemErrorType(Enum):
    InputError = 'you need input the value as we need format'

print(Zoo)
print(Zoo.Dog)
print(type(Zoo.Dog))
print(SystemErrorType.InputError.name)
print(SystemErrorType.InputError.value)
