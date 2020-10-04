class IntroduceMixin:
    def introduce(self):
        intro = "Name: %s" % self.name
        return intro

class SpeakMixin:
    def speak(self):
        print("Hi, my %s." % self.introduce())

class Dog(IntroduceMixin, SpeakMixin):
    def __init__(self, name):
        self.name = "Dog-%s" % name


dog = Dog("Bobby")
print(dog.introduce())
dog.speak()


class MyObject:
    def __init__(self):
        self.__private_name = "kiruen"
        self.__name = "ky"

    def __getattr__(self, item):
        value = 'Default value for %s' % item
        setattr(self, item, value)
        return value

    def foo(self):
        print(self.__private_name)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == "zky":
            print('(你这个名字起得很棒！)')
        self.__name = name

obj = MyObject()
obj.foo()
print(obj._MyObject__private_name)
print(obj.__dict__)
print(obj.name)
obj.name = 'zky'
# print(obj.__private_name)

# __xxattr__测试
print(obj.myvalue)
# print(obj.__dict__)


class MyObject2:
    def __init__(self, data={}):
        self._data = data

    # def __setattr__(self, key, value):
    #     print("You have setted %s!" % key)
    #     self.__dict__[key] = value

    def __getattribute__(self, item):
        data = super().__getattribute__('_data') #解决了无限递归
        return data[item]

obj2 = MyObject2({'name': 'ky1997'})
# print(obj2.__dict__)
print(obj2.name)