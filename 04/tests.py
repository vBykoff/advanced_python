import unittest
from custom_meta_class import CustomMeta
from Descriptors import Data


class CustomClass(metaclass=CustomMeta):
    """class for testing metaclass"""
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


class CustomMetaTest(unittest.TestCase):

    def test_attribute_names(self):
        inst = CustomClass()
        self.assertEqual(inst.custom_x, 50)
        self.assertEqual(inst.custom_val, 99)
        self.assertEqual(inst.custom_line(), 100)
        self.assertEqual(CustomClass.custom_x, 50)

        inst.dynamic = "f"
        self.assertEqual(inst.custom_dynamic, "f")
        self.assertEqual(inst.__str__(), "Custom_by_metaclass")


class DescriptorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.data = Data()

    def test_integer(self):
        self.assertEqual(self.data.num, 0)
        self.data.num = 1
        self.assertEqual(self.data.num, 1)

        with self.assertRaises(TypeError):
            self.data.num = 0.9

    def test_string(self):
        self.assertEqual(self.data.name, "")
        self.data.name = "f"
        self.assertEqual(self.data.name, "f")

        with self.assertRaises(TypeError):
            self.data.name = 9

    def test_positive_integer(self):
        self.assertEqual(self.data.price, 0)
        self.data.price = 2
        self.assertEqual(self.data.price, 2)

        with self.assertRaises(TypeError):
            self.data.price = "yu"
        with self.assertRaises(ValueError):
            self.data.price = -1


if __name__ == '__main__':
    unittest.main()
