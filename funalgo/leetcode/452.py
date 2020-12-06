def removeCoveredIntervals(intvs: list):
    if not intvs: return 0
    intvs = sorted(intvs, key=lambda intv: intv[0])
    cur_intv = intvs[0]
    rest = len(intvs)
    for intv in intvs[1:]:
        if cur_intv[1] >= intv[1]:
            rest -= 1
            cur_intv = intv
    return rest


if __name__ == '__main__':
    print(removeCoveredIntervals([(1, 4), (3, 6), (2, 8)]))
