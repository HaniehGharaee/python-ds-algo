#############ENUM##############
from enum import Enum
#Creation of an enum
class color(Enum):
    red = 1
    green = 2
    blue = 3
print(color.red)
print(color(1))
print(color['red'])
######################
#iterable
iterable = [c for c in color]
print(iterable)
