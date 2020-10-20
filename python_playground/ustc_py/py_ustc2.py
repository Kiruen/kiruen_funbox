import sys
import re

i = 100000
print(sys.getrefcount(i))

print(re.findall(r"(\w+) \1", "aca bb bb aa aa _ _"))