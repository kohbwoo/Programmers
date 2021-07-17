def solution(n):
    f = [0,1]
    for i in range(2,n+1):
        tmp = f[i-1] + f[i-2]
        f.append(tmp)
    answer = f[n] % 1234567
    return answer

print(solution(3))