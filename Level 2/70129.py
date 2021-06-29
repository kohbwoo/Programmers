def solution(x):
    del0len = 0
    bincount = 0
    while x != "1":
        bincount += 1
        tmp = len(x)
        x = ''.join(x for x in x if x not in "0")
        del0len += (tmp - len(x))
        c = len(x)
        x = format(c, "b")
    return [bincount,del0len]


print(solution("110010101001"))