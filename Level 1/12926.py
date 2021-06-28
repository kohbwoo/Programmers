def solution(s, n):
    small = "abcdefghijklmnopqrstuvwxyz"
    large = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small = list(small)
    large = list(large)
    s = list(s)
    for i in range(0,len(s)):
        if s[i].isupper():
            if large.index(s[i]) + n > 24:
                s[i] = small[(i + n)-27]
            else:
                s[i] = large[large.index()+n]
        elif s[i] == " ":
            continue
        else:
            if small.index(s[i]) + n > 24:
                s[i] = small[(i + n)-27]
            else:
                s[i] = small[small.index()+n]

    answer = "".join(s)
    return answer

print(solution("AB"	,4))