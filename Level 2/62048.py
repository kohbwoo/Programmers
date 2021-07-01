def solution(w,h):
    answer = 0
    if w % 2 == 0 and h % 2 == 0:
        answer = (w/2) * (h/2) * 2
    elif w % 2 == 0 or h % 2 == 0:
        if w % 2 == 0:
            n = w
            m = h
        else:
            m = w
            n = h
        ((m-1)/2) * (n/2) * 2
    else:
        answer = (w - 2) * (h - 2)


    return answer


print(solution(8,16))