import sys

class RegularNode:
    def __init__(self, val):
        self.val = val

class SlottedNode:
    __slots__ = ('val',)
    def __init__(self, val):
        self.val = val

r = RegularNode(10)
s = SlottedNode(10)

# Memory of the object + its internal dictionary:
print(sys.getsizeof(r) + sys.getsizeof(r.__dict__))  # ~152 bytes
print(sys.getsizeof(s))                              # ~48 bytes
