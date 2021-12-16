def solution(s):
    answer = list(s)
    tmp = []
    for i in range(1, len(s)):
        count = 0
        while(s[i] == s[i-1]):
            if s[i] == s[i-1]:
                count += 1
            i += 1
        tmp.append(count)

    return answer


print(solution("aabbaccc"))
#print(solution("ababcdcdababcdcd"))
# print(solution("abcabcdede"))
# print(solution("abcabcabcabcdededededede"))
