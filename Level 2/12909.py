def solution(s):
    k = 0
    if s.count(")") != s.count("(") :
        return False

    for i in range(0,len(s)):
        if s[i] == "(":
            k += 1
        if s[i] == ")":
            k -= 1
        if k < 0:
            return False
    return True

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
print(solution('()())(()'))