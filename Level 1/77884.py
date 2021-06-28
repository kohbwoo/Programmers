def solution(left, right):
    tmp = []
    count = []
    answer = 0
    for i in range(left,right+1):
        tmp.append(i)
    for j in range(0, len(tmp)):
        for a in range(1, tmp[j] + 1):
            if tmp[j] % a == 0:
                count.append(a)
        if len(count) % 2 == 0:
            answer = answer + a
        else:
            answer = answer - a
        count = []
    return answer


print(solution(13,17))