def solution(s):
    s = sorted(s)
    s.sort(reverse= True)
    return "".join(s)

print(solution("Zbcdefg"))