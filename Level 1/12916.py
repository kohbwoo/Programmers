def solution(s):
    p = 0
    y = 0
    for i in range(0,len(s)):
        if s[i] == "p" or s[i] == "P":
            p = p + 1
        if s[i] == "y" or s[i] == "Y":
            y = y + 1
    if p == y:
        return True
    else:
        return False


print(solution("Pyy"))