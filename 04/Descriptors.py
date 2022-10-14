"""Module define Integer, String and Positive Integer descriptors"""


class Integer:
    """Integer descriptor"""

    def __set_name__(self, owner, name):
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

    def __set_name__(self, owner, name):
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

    def __set_name__(self, owner, name):
        self.__variable = 0

    def __get__(self, obj, objtype):
        return self.__variable

    def __set__(self, obj, val):
        if isinstance(val, int):
            if val >= 0:
                self.variable = val
            else:
                raise ValueError("Value that less than zero "
                                 "cannot be positive integer")
        else:
            raise TypeError("Value is not instance of int")

    def __delete__(self, obj):
        del self.__variable


class Data:
    num = Integer()
    name = String()
    price = PositiveInteger()

    def __init__(self):
        pass


if __name__ == "__main__":
    d = Data()

