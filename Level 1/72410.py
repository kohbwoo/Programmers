def solution(new_id):
    ban = "~!@#$%^&*()=+[{]}:?,<>/"
    count = 0
    answer3 = ""
    answer1 = new_id.lower()
    answer2 = ''.join(x for x in answer1 if x not in ban)

    i = 0
    if len(answer2) <= 2:
        answer3 = answer2
    while i < len(answer2):
        if answer2[i - 1] == "." and answer2[i] == ".":
            answer2 = answer2[0:i] + answer2[i + 1:]
        i = i + 1
        answer3 = answer2

    if len(answer3) > 2:
        if answer3[0] == "." and answer3[1] == ".":
            answer3 = answer3[1:]

    if answer3[0] == ".":
        answer4 = answer3[1:len(answer3)]
    else:
        answer4 = answer3

    if answer4 == "":
        answer5 = "a"
    else:
        answer5 = answer4

    if len(answer5) > 16:
        answer6 = answer5[0:15]
        tmp = len(answer6)
        if answer6[tmp - 1] == ".":
            answer6 = answer6[:len(answer6) - 1]
    else:
        answer6 = answer5

    if len(answer6) < 3:
        answer7 = answer6
        for i in range(len(answer6), 3):
            answer7 = answer7 + "a"
    else:
        answer7 = answer6

    return answer7


print(solution("=.="))
