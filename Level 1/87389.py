def solution(n):
    i = 1
    while(not n % i == 1):
        i += 1
    return i



print(solution(10))
print(solution(12))