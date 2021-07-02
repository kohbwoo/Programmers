def solution(answers):
    user = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,3,3,5,5]]
    score = [0,0,0]
    for i in range(0,3):
        if len(answers) > len(user[i]):
            count = 0
            while len(user[i]) != len(answers):
                user[i].append(user[i][count])
                count = count + 1
    for i in range(0,3):
        for j in range(0,len(answers)):
            if user[i][j] == answers[j]:
                score[i] = score[i] + 1
    answers = []
    if (score.count(max(score))) == 1:
        answers.append(score.index(max(score)) + 1)
        return answers
    else:
        for i in range(0,3):
            if score[i] == (score.count(max(score))-1):
                answers.append(i+1)
        return answers


print(solution(([1, 3, 2, 4, 2])))