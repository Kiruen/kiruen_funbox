from functools import singledispatch
import collections as coll
import re
import operator
import unittest

class Todo(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

    def __repr__(self):
        return self.__str__()


class Exp:

    def __repr__(self):
        return self.__str__()


class ExpVar(Exp):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def eval(self):
        return self.value

class ExpMonad(Exp):
    def __init__(self, op, exp):
        self.op = op
        self.exp = exp

    def __str__(self):
        return f"{self.op}{self.exp}"

    def eval(self):
        if self.op is '-':
            return -self.exp.eval()
        else:
            return self.exp.eval()

class ExpAdd(Exp):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left} + {self.right}"

    def eval(self):
        return self.left.eval() + self.right.eval()


class ExpMinus(Exp):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left} - {self.right}"

    def eval(self):
        return self.left.eval() - self.right.eval()


class ExpMulti(Exp):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "%s * %s" % (self.left, self.right)

    def eval(self):
        return self.left.eval() * self.right.eval()


class ExpDiv(Exp):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return "%s / %s" % (self.left, self.right)

    def eval(self):
        return self.left.eval() / self.right.eval()


class ExpPar(Exp):
    def __init__(self, exp):
        self.exp = exp

    def __str__(self):
        return f"({self.exp})"

    def eval(self):
        return self.exp.eval()


@singledispatch
def eval_value(exp: Exp):
    if isinstance(exp, ExpVar):
        return exp.value
    else:
        return exp.eval()


@eval_value.register(str)
def _(exp: str):
    p_num = r"\d+(\.\d+)?"
    p_op = r"[\+\-\*\/\(\)\#]"
    token_tuples = re.findall(f"(({p_num})|({p_op}))", f"{exp}#")
    # print(token_tuples)
    ast = gen_ast(token_tuples)
    return eval_value(ast) # ,ast


def gen_ast(token_tuples: list):
    num_que, op_que, monad_exp_que = coll.deque(), coll.deque(['$']), coll.deque()
    i = 0
    sign, last_token, monad_op = 1, None, None
    # print("input tokens: ", token_tuples)
    while i < len(token_tuples): # len(num_que) > 1 or
        # print("start:", op_que, num_que)
        token = token_tuples[i]
        i += 1
        val = token[0]
        if token[1] is not '':
            if monad_op:
                num_que.append(ExpMonad(monad_op, ExpVar(float(val))))
            else:
                num_que.append(ExpVar(float(val)))
        elif token[3] is not '':
            if last_token and last_token[3] is not '' and val in {'-'} :
                monad_op = val
            else:
                while len(num_que) >= 2 and \
                        comp_ops(val, op_que[-1]) <= 0:  # 不断将当前栈顶op与扫描到的op对比，如果栈顶优先级高，先让栈顶计算完再说
                    if op_que[-1] is '(':
                        if monad_op:
                            monad_exp_que.append(ExpMonad(monad_op, None))  # 创建一个空的Monad结点，放入专用栈
                            monad_op = None
                        break  # 无视(，直到()相遇
                    else:
                        op = op_que.pop()
                        num2 = num_que.pop()
                        num1 = num_que.pop()
                        if op is '+':
                            num_que.append(ExpAdd(num1, num2))
                        elif op is '-':
                            num_que.append(ExpMinus(num1, num2))
                        elif op is '*':
                            num_que.append(ExpMulti(num1, num2))
                        elif op is '/':
                            num_que.append(ExpDiv(num1, num2))
                # 这时才把刚才的符号入栈
                if val is ')':
                    op_que.pop()  # 消耗掉(
                    par_exp = ExpPar(num_que.pop())
                    if len(monad_exp_que) > 0:
                        monad_exp = monad_exp_que.pop()
                        monad_exp.exp = par_exp
                        num_que.append(monad_exp)
                    else:
                        num_que.append(par_exp)
                else:
                    op_que.append(val)
        last_token = token
        # print("end:", op_que, num_que)
    return num_que.pop()


op_prio_map = {
    '+': 1, '-': 1,
    '*': 2, '/': 2,
    '$': -1000, '(': 10000, ')': -10000, '#': -1000
}


def comp_ops(op1, op2):
    return op_prio_map[op1] - op_prio_map[op2]


# print(eval_value('(+1 - (-2 * -( 3/ (2 +1.00))))'))  # 20.5+5.35
# que = coll.deque()
# que.append(1)
# print(que.pop())
# print(que)

test_case_1 = ExpAdd(
    ExpMulti(ExpVar(3), ExpVar(4)),
    ExpDiv(ExpVar(10), ExpVar(2))
)

test_case_2 = ExpMinus(
    ExpMulti(
        ExpPar(ExpAdd(ExpVar(12), ExpVar(217))),
        ExpVar(3)
    ),
    ExpVar(621)
)


class TestTableau(unittest.TestCase):

    def test_print_1(self):
        self.assertEqual(str(test_case_1), "3 * 4 + 10 / 2")

    def test_print_2(self):
        self.assertEqual(str(test_case_2), "(12 + 217) * 3 - 621")

    def test_eval_1(self):
        self.assertEqual(eval_value(test_case_1), 17)

    def test_eval_2(self):
        self.assertEqual(eval_value(test_case_2), 66)

    def test_eval_3(self):
        self.assertEqual(eval_value('1 + 65'), 66)

    def test_eval_4(self):
        self.assertEqual(eval_value('1 + 65 / (66 - 3 * (1 + 2) + (4 + 4))'), 2)

if __name__ == '__main__':
    unittest.main()