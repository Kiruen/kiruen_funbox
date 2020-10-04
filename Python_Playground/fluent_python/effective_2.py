import collections

print({}.__class__)

class MissingState:
    def __init__(self):
        self.missing_count = 0

    def __call__(self, *args, **kwargs):
        self.missing_count += 1
        return 0

def inc_with_missingreport(current_colors, increments):
    state = MissingState()
    # def missing_handler():
    #     nonlocal missing_count
    #     missing_count += 1
    #     return 0  # 不存在就创建新条目（一开始值为0），并且统计上一个missing
    result = collections.defaultdict(state, current_colors)
    for color_name in increments:
        result[color_name] += increments[color_name]
    return result, state.missing_count


current = {'red':3, 'black':5}
increments = {'black':12, 'green':2, 'orange':12}
# 额，这样字典遍历是错误的
# for color_name, amount in increments:
#     print(color_name)
res, count = inc_with_missingreport(current, increments)
print(res, count)
assert count == 2

#其实父类不应该raise的吧。。但python又不给定义抽象方法
class Animal:
    @classmethod
    def generate_instance(cls):
        raise Exception

    def bark(self):
        raise Exception

class Dog(Animal):
    @classmethod
    def generate_instance(cls):
        return cls()

    def bark(self):
        print("Wolf!")


class Cat(Animal):
    @classmethod
    def generate_instance(cls):
        return cls()

    def bark(self):
        print("Meow!")

anis = [Cat(), Dog()]
for ani in anis:
    ani.bark()

