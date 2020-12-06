def naive_compute(exp: str) -> int:
    opmap = {
        "+": getattr(int, "__add__"),
        "-": getattr(int, "__sub__"),
        "*": getattr(int, "__mul__"),
    }

    def divide(i):
        val = 0
        while i < len(exp) and exp[i].isnumeric():
            val = val * 10 + int(exp[i])
            i += 1
        if i < len(exp):
            return opmap[exp[i]](val, divide(i + 1))
        else:
            return val

    return divide(0)


# 可以回忆一下那个纯粹的合法括号组合问题
def diffWaysToCompute(exp: str) -> list:
    opmap = {
        "+": getattr(int, "__add__"),
        "-": getattr(int, "__sub__"),
        "*": getattr(int, "__mul__"), }
    memo = {}

    def divide(l, r):
        if (l, r) in memo: return memo[(l, r)]
        res = []
        for k in range(l, r):
            # 碰到运算符才切分
            if not exp[k].isnumeric():
                left_res = divide(l, k)
                right_res = divide(k + 1, r)
                for i in left_res:
                    for j in right_res:
                        res.append(opmap[exp[k]](i, j))
        if not res:
            res.append(int(exp[l: r]))
        memo[(l, r)] = res
        return res

    return divide(0, len(exp))


if __name__ == '__main__':
    print(naive_compute("11-2*33"))
    print(diffWaysToCompute("1+2*3"))
    print(diffWaysToCompute("1+2*3-5"))
