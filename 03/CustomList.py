"""Custom List Class with defined add, sub and relation operations"""


class CustomList(list):
    """Custom List"""
    def __init__(self, params=None):
        if params is None:
            params = []
        super().__init__(params)

    def __add__(self, other):
        result_list = []
        for i in range(min(len(self), len(other))):
            result_list.append(self[i] + other[i])

        if len(self) > len(other):
            for i in self[len(other):len(self)]:
                result_list.append(i)

        if len(self) < len(other):
            for i in other[len(self):len(other)]:
                result_list.append(i)

        return CustomList(result_list)

    def __radd__(self, other):
        result_list = []
        for i in range(min(len(self), len(other))):
            result_list.append(self[i] + other[i])

        if len(self) > len(other):
            for i in self[len(other):len(self)]:
                result_list.append(i)

        if len(self) < len(other):
            for i in other[len(self):len(other)]:
                result_list.append(i)

        return CustomList(result_list)

    def __sub__(self, other):
        result_list = []
        for i in range(min(len(self), len(other))):
            result_list.append(self[i] - other[i])

        if len(self) > len(other):
            for i in self[len(other):len(self)]:
                result_list.append(i)

        if len(self) < len(other):
            for i in other[len(self):len(other)]:
                result_list.append(-i)

        return CustomList(result_list)

    def __rsub__(self, other):
        result_list = []
        for i in range(min(len(self), len(other))):
            result_list.append(self[i] - other[i])

        if len(self) > len(other):
            for i in self[len(other):len(self)]:
                result_list.append(-i)

        if len(self) < len(other):
            for i in other[len(self):len(other)]:
                result_list.append(i)

        return CustomList(result_list)

    # Relation operations

    def __lt__(self, other):
        """less """
        return sum(self) < sum(other)

    def __le__(self, other):
        """less equal"""
        return sum(self) <= sum(other)

    def __eq__(self, other):
        """equal"""
        return sum(self) == sum(other)

    def __ne__(self, other):
        """not equal"""
        return sum(self) != sum(other)

    def __gt__(self, other):
        """greater"""
        return sum(self) > sum(other)

    def __ge__(self, other):
        """greater equal"""
        return sum(self) >= sum(other)

    def __rlt__(self, other):
        """less """
        return sum(self) < sum(other)

    def __rle__(self, other):
        """less equal"""
        return sum(self) <= sum(other)

    def __req__(self, other):
        """equal"""
        return sum(self) == sum(other)

    def __rne__(self, other):
        """not equal"""
        return sum(self) != sum(other)

    def __rgt__(self, other):
        """greater"""
        return sum(self) > sum(other)

    def __rge__(self, other):
        """greater equal"""
        return sum(self) >= sum(other)

    def __str__(self):
        return f"{super().__str__()}, sum={sum(self)}"


# if __name__ == '__main__':
#     print("ho")
