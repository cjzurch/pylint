"""Check unpacking non-sequences in assignments. """

# pylint: disable=too-few-public-methods, invalid-name

from sys import exit as nonseq_func
from input.unpacking import nonseq

__revision__ = 0

# Working

class Seq(object):
    """ sequence """
    def __init__(self):
        self.items = range(2)

    def __getitem__(self, item):
        return self.items[item]

    def __len__(self):
        return len(self.items)

class Iter(object):
    """ Iterator """
    def __iter__(self):
        for number in range(2):
            yield number

def good_unpacking():
    """ returns should be unpackable """
    if True:
        return [1, 2]
    else:
        return (3, 4)

def good_unpacking2():
    """ returns should be unpackable """
    return good_unpacking()

a, b = [1, 2]
a, b = (1, 2)
a, b = set([1, 2])
a, b = {1: 2, 2: 3}
a, b = "xy"
a, b = Seq()
a, b = Iter()
a, b = (number for number in range(2))
a, b = good_unpacking()
a, b = good_unpacking2()

# Not working
class NonSeq(object):
    """ does nothing """

def bad_unpacking():
    """ one return isn't unpackable """
    if True:
        return None
    return [1, 2]

a, b = NonSeq()
a, b = ValueError
a, b = None
a, b = 1
a, b = nonseq
a, b = nonseq()
a, b = bad_unpacking()
a, b = nonseq_func