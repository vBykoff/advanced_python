import unittest.mock
from CustomList import CustomList
import io


class CustomListTest(unittest.TestCase):

    def test_add(self):
        l1 = CustomList([1, 2, 3, 4])
        l2 = CustomList([1, 2, 3])
        l3 = [1, 2, 3]
        l4 = CustomList([1, 2])

        self.assertEqual(l1 + l2, CustomList([2, 4, 6, 4]))
        self.assertEqual(l2 + l1, CustomList([2, 4, 6, 4]))
        self.assertEqual(l3 + l1, CustomList([2, 4, 6, 4]))
        self.assertEqual(l3 + l4, CustomList([2, 4, 3]))
        self.assertEqual(type(l3 + l1), CustomList)

    def test_sub(self):
        l1 = CustomList([1, 2, 3, 4])
        l2 = CustomList([1, 2, 3])
        l3 = [1, 2, 3]
        l4 = CustomList([1, 2])

        self.assertEqual(l1 - l2, CustomList([0, 0, 0, 4]))
        self.assertEqual(l2 - l1, CustomList([0, 0, 0, -4]))
        self.assertEqual(l3 - l1, CustomList([0, 0, 0, -4]))
        self.assertEqual(l3 - l4, CustomList([0, 0, 3]))

        self.assertEqual(type(l3 - l1), CustomList)

    def test_relations(self):
        l1 = CustomList([3, 1, 2])
        l2 = CustomList([1, 2, 3])
        l3 = [1, 2, 3]

        self.assertEqual(l1 == l2, True)
        self.assertEqual(l3 == l1, True)

        l1.append(1)

        self.assertEqual(l1 != l2, True)
        self.assertEqual(l3 != l1, True)

        self.assertEqual(l1 < l2, False)
        self.assertEqual(l3 < l1, True)

        self.assertEqual(l1 > l2, True)
        self.assertEqual(l3 > l1, False)

        self.assertEqual(l1 <= l2, False)
        self.assertEqual(l3 <= l1, True)
        self.assertEqual(l3 <= l2, True)

        self.assertEqual(l1 >= l2, True)
        self.assertEqual(l3 >= l1, False)
        self.assertEqual(l3 >= l2, True)

    def test_str(self):
        l1 = CustomList([3, 1, 2])
        self.assertEqual(l1.__str__(), "[3, 1, 2], sum=6")
        l2 = CustomList()
        self.assertEqual(l2.__str__(), "[], sum=0")


if __name__ == '__main__':
    unittest.main()
