def solution(n):
    answer = []
    for i in map(int, str(n)):
        answer.append(i)
    answer.reverse()
    return answer

print(solution(12345))