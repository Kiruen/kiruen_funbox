import time
def foo():
    val = do_something()
    return 1000 * val + do_somethingelse()

def do_something():
    time.sleep(5)
    return 768

def do_somethingelse():
    time.sleep(50)
    return 768

class Blob:
    def __init__(self):
        self.name = "ky"
        self.age = 10000
