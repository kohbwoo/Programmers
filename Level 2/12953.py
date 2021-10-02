def solution(arr):
    answer = max(arr)
    check = 0
    while check != len(arr):
        check = 0
        for i in range(0, len(arr)):
            if answer % arr[i] == 0:
                check = check + 1
        answer = answer + 1


    return answer-1



print(solution([1,2,3]))