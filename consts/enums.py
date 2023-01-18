from enum import Enum

class EnumProperty:
    def __init__(self, enum_type):
        self.enum_type = enum_type

    def __get__(self, obj, objtype=None):
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        if not isinstance(value, self.enum_type):
            raise ValueError("color must be a member of the Color enumeration")
        obj.__dict__[self.name] = value

# 组件类型枚举
class ComponentType(Enum):
    PET = 1
    FUN = 2


# 组件类型枚举
class PetType(Enum):
    STATIC = 1
    GIF = 2
    FRAME = 3


