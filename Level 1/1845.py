def solution(nums):
    return int(min(len(set(nums)),len(nums)/2))
print(solution([3,1,2,3]))