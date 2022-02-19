
def LV1(ID):
    ID = ID.lower()
    return ID


def LV2(ID):
    result = ""

    for i in ID:
        if i == "[" or i == "]" or i == "(" or i == ")":
            continue
        if i.isdigit() or i.islower() or i == "." or i == "-" or i == "_":
            result = result + i

    return result


def LV3(ID):
    result = ""
    for i in range(len(ID)):
        if i < len(ID) - 1 and ID[i] == "." and ID[i + 1] == ".":
            continue
        result = result + ID[i]

    return result

def LV4(ID):
    result = ""
    if len(ID) >= 1:

        if ID[0] == "." and ID[len(ID)-1] == ".":
            result = ID[1:len(ID)-1]

        elif ID[0] == ".":
            result = ID[1:]

        elif ID[len(ID) - 1] == ".":
            result = ID[:len(ID) - 1]
        else:
            result = ID
    return result


def LV5(ID):
    if ID == "":
        ID = ID + "a"
    return ID


def LV6(ID):
    if len(ID) > 15:
        ID = ID[:15]
    if ID[len(ID)-1] == ".":
        ID = ID[:14]
    return ID


def LV7(ID):
    if len(ID) < 3:
        while len(ID) <= 2:
            ID = ID + ID[len(ID)-1]
    return ID



def solution(new_id):
    print("\n")
    print("input =", new_id)
    ID = LV1(new_id)
    print("LV1 = ", ID)
    ID = LV2(ID)
    print("LV2 = ", ID)
    ID = LV3(ID)
    print("LV3 = ", ID)
    ID = LV4(ID)
    print("LV4 = ", ID)
    ID = LV5(ID)
    print("LV5 = ", ID)
    ID = LV6(ID)
    print("LV6 = ", ID)
    ID = LV7(ID)
    print("LV7 = ", ID)


    return ID


print(solution('-_.~!@#$%^&*()=+[{]}:?,<>/._-'))
# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
# print(solution("=.="))
# print(solution("123_.def"))
# print(solution("abcdefghijklmn.p"))