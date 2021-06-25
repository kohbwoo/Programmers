def solution(A, B):
    answer = 0
    while len(A) > 0:
        if min(B) < min(A):
            Am = max(A)
            Bm = min(B)
            A.remove(Am)
            B.remove(Bm)
        else:
            Am = min(A)
            Bm = min(B)
            A.remove(Am)
            B.remove(Bm)
            answer = answer + 1


    return answer


print(solution([5,1,3,7], [2,2,6,8]))