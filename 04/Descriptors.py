"""Module define Integer, String and Positive Integer descriptors"""


class Integer:
    """Integer descriptor"""

    def __init__(self):
        self.__variable = 0

    def __get__(self, obj, objtype):
        return self.__variable

    def __set__(self, obj, val):
        if isinstance(val, int):
            self.__variable = val
        else:
            raise TypeError("Value is not instance of int")

    def __delete__(self, obj):
        del self.__variable


class String:
    """String descriptor"""

    def __init__(self):
        self.__variable = ""

    def __get__(self, obj, objtype):
        return self.__variable

    def __set__(self, obj, val):
        if isinstance(val, str):
            self.__variable = val
        else:
            raise TypeError("Value is not instance of str")

    def __delete__(self, obj):
        del self.__variable


class PositiveInteger:
    """Positive Integer descriptor"""

    def __init__(self):
        self.__variable = 0

    def __get__(self, obj, objtype):
        return self.__variable

    def __set__(self, obj, val):
        if isinstance(val, int):
            if val >= 0:
                self.__variable = val
            else:
                raise ValueError("Value that less than zero "
                                 "cannot be positive integer")
        else:
            raise TypeError("Value is not instance of int")

    def __delete__(self, obj):
        del self.__variable


class Data:
    """class for testing descriptors"""
    num = Integer()
    name = String()
    price = PositiveInteger()
