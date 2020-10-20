import collections as coll
import sys
import unittest

#汉诺塔问题，从柱子a移到柱子b。抽象的过程很重要！抽象得好，问题就格外简单了。
def hanno(cylinders: list, source: int, target: int, transfer: int, level: int=2):
    if not hasattr(hanno, 'steps_memo') or not hanno.steps_memo:
        setattr(hanno, 'steps_memo', [])
    def move(from_, to_):
        old_val = cylinders[from_].pop()
        cylinders[to_].append(old_val)
        hanno.steps_memo.append((from_, to_))
        return old_val

    if level == 2:
        # src_val = cylinders[source].pop()
        # cylinders[transfer].append(src_val)
        move(source, transfer)
        move(source, target)
        move(transfer, target)
    else:
        hanno(cylinders, source, transfer, target, level - 1)
        move(source, target)
        hanno(cylinders, transfer, target, source, level - 1)

class MyTest(unittest.TestCase):
    def test_level2(self):
        cylinders = [[3,2,1],[],[]]
        hanno(cylinders, 0, 2, 1, level=2)
        self.assertEqual(cylinders, [[3],[],[2,1]])

    def test_level3(self):
        cylinders = [[3, 2, 1], [], []]
        hanno.steps_memo = None
        hanno(cylinders, 0, 2, 1, level=3)
        print(hanno.steps_memo)
        self.assertEqual(cylinders, [[], [], [3, 2, 1]])

    def test_level5(self):
        cylinders = [[5, 4, 3, 2, 1], [], []]
        hanno.steps_memo = None
        hanno(cylinders, 0, 2, 1, level=5)
        print(hanno.steps_memo)
        self.assertEqual(cylinders, [[], [], [5, 4, 3, 2, 1]])