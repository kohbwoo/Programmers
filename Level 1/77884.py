def solution(left, right):
    tmp = []
    count = []
    answer = 0
    for i in range(left, right + 1):
        tmp.append(i)
    for j in range(0, len(tmp)):
        for a in range(1, tmp[j] + 1):
            if not tmp[j] % a:
                count.append(a)
        if not len(count) % 2:
            answer += a
        else:
            answer -= a
        count = []
    return answer


print(solution(13, 17))
