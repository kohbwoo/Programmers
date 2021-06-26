def solution(s):
    s = s.replace("},{", " ")
    s = s.replace("{", "")
    s = s.replace("}", "")
    s = s.split(" ")
    answer = []

    for i in range(0,len(s)):
        k = s[i].split(",")
        for j in range(0,len(k)):
            answer.append(int(k[i]))

    return answer




print(solution(("{{1,2,3},{2,1},{1,2,4,3},{2}}")))