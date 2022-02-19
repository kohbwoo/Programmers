ID = "abcdefghijklmn.p"

result = ""
if len(ID) >= 1:

    if ID[0] == ".":
        result = ID[1:]
        print("A")
        print("A")
    elif ID[len(ID)-1] == ".":
        print("A")
        result = ID[:len(ID)-1]
    else:
        result = ID

print(result)