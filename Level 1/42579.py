def solution(participant, completion):
    for i in range(0, len(participant)):
        if participant[i] not in completion:
            return participant[i]



print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))