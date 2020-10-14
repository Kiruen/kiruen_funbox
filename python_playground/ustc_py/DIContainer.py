from enum import Enum
import re

class Scope(Enum):
    SINGLETON = 1
    PROTOTYPE = 2

class Arg:
    def __init__(self):
        self.isRef = False
        self.type = None
        self.arg = None

class BeanDef:
    # __slots__ = ['id', 'className', 'constArgs']
    def __init__(self):
        self.id = ''
        self.className = ''
        self.constArgs = []
        self.scope = Scope.SINGLETON
        self.lazyInit = False


class IniBeanConfigParser:
    PATTERN_DEF = r'^\b*(\w+)?\b*=\b*(\w+)\b*$'
    def parse(self, content):
        defs = []
        for one_def_text in content.split('[Bean]'):
            defi = BeanDef()
            defs.append(defi)
            for defi_tuple in re.search(self.PATTERN_DEF, one_def_text):
                name, val = defi_tuple[1], defi_tuple[2]
                if name in {'className', 'id'}:
                    setattr(defi, name, val.replace('"', ''))
                elif name == 'scope':
                    setattr(defi, name, getattr(Scope, val))
                elif name == 'constrArgs':
                    args = []
                    for arg_str in val.split([',', '[', ']']):
                        arg = Arg()
                        # TODO: 解析三种元素
                        args.append(arg)
                    setattr(defi, name, args)
                elif name == 'lazyInit':
                    setattr(defi, name, bool(val))

        return defs



class BeansFactory:
    def __init__(self):
        self.__bean_container = {}

    def __getitem__(self, id):
        return self.__bean_container[id]

    def addBeanDefs(self, defs):
        # TODO:把def对象导入进来
        pass


class AppContext:
    def __init__(self, config_path):
        self.beanFactory = BeansFactory()
        self.beanConfigParser = IniBeanConfigParser()
        self.loadBeanDefs(config_path)

    def loadBeanDefs(self, config_path):
        with open(config_path, 'r') as fp:
            content = fp.read()
            defs = self.beanConfigParser.parse(content)
            self.beanFactory.addBeanDefs(defs)

    def __getBean(self, id):
        return self.beanFactory[id]

    def __getitem__(self, id):
        return self.__getBean(id)


if __name__ == '__main__':
    # print(getattr(Scope, 'SINGLETON'))
    pass