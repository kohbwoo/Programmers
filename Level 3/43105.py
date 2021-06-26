def solution(triangle):
    answer = 0
    tmp = []
    for i in range(len(triangle)):  # 세로 크기
        for j in range(len(triangle[i])):  # 가로 크기 a[i] [값, 값]의 len은 2
            print(triangle[i][j], end='\n')









print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))