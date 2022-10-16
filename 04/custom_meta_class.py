"""Custom Meta class: add 'custom' to each attribute except magic methods"""


class CustomMeta(type):
    """Custom Meta class: add 'custom'
    to each attribute except magic methods"""
    def __new__(cls, name, bases, class_dict):
        new_class_dict = {}
        for key, value in class_dict.items():
            if key not in dir(name) and key not in dir(cls):
                new_class_dict["custom_" + key] = value
            else:
                new_class_dict[key] = value

        def custom__setattr__(self, name, val):
            name = "custom_" + name
            self.__dict__[name] = val

        new_class_dict["__setattr__"] = custom__setattr__
        cls = super().__new__(cls, name, bases, new_class_dict)
        return cls
