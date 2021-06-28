def solution(arr):
    answer = []
    for i in range(0,len(arr)):
        if len(arr) == 2 and arr[0] == arr[1]:
            answer.append(arr[0])
            return answer
        if i < len(arr) and i != 1:
            if arr[i-1] != arr[i]:
                answer.append(arr[i])
        elif arr[i] != arr[i+1]:
            answer.append(arr[i])
    return answer

print(solution([1,1]))