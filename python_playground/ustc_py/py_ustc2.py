import sys
import re

i = 100000
print(sys.getrefcount(i))

print(re.findall(r"(\w+) \1", "aca bb bb aa aa _ _"))

import random
l = [1,2,3] * 10
random.shuffle(l)
print(l)
print(l[random.randint(0, 30)])

code = """
print(1)
"""
print(type(compile(code, "<string>", "exec")))
print(slice)