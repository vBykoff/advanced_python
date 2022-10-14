"""Custom Meta class: add 'custom' to each attribute except magic methods"""


class CustomMeta(type):
    """Custom Meta class: add 'custom' to each attribute except magic methods"""
    def __new__(mcs, name, bases, class_dict, **kwargs):
        print(class_dict)
        new_class_dict = {}
        for key, value in class_dict.items():
            if key not in dir(name) and key not in dir(mcs):
                new_class_dict["custom_" + key] = value
            else:
                new_class_dict[key] = value

        def f(self, name, val):
            name = "x" + name
            self.__dict__[name] = val

        new_class_dict["__setattr__"] = f
        cls = super().__new__(mcs, name, bases, new_class_dict)
        return cls
