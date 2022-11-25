import weakref
import numpy as np
from profiler import profile_deco

N = 1_000_000


# attribute class
class SomeType:
    def __init__(self, params):
        self.params = params

# weakref
class WeakrefClass:
    def __init__(self, params):
        self.params = weakref.ref(params)

# simple attributes
class SimpleAttributesClass:
    def __init__(self, params):
        self.params = params

# slots
class SlotsClass:
    __slots__ = ("params")
    def __init__(self, params):
        self.params = params


@profile_deco
def create(cls):
    array = []
    for i in range(N):
        attributes = SomeType(np.random.randint(0, 1000, size=100))
        array.append(cls(attributes))
    return array


@profile_deco
def geting(array):
    help_array = []
    for i in range(N):
        help_array.append(array[i].params)

@profile_deco
def seting(array):
    for i in range(N):
        attributes = SomeType(np.random.randint(0, 1000, size=100))
        array[i].params = attributes

@profile_deco
def deleting(array):
    for i in range(N):
        del array[i].params


def run():
    array = create(SlotsClass)
    geting(array)
    seting(array)
    deleting(array)
    
    print("===========Create==========")
    create.print_stat()
    print("===========Get==========")
    geting.print_stat()
    print("===========Set==========")
    seting.print_stat()
    print("===========Delete==========")
    deleting.print_stat()


if __name__ == "__main__":
    run()
