def solution(left, right):
    list_ = []
    sum = 1
    for i in range(left,right+1):
        list_.append(i)


    for j in range(left, right):
        for i in range(1,j+1):
            if list_[left-left] % i == 0:
                print(i)
        print()



print(solution(13,17))