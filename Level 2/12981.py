def solution(n, words):
    for i in range(0,len(words)):
        if i > 0 and i < len(words)-1 and words[i][len(words[i])-1:] != words[i+1][0]:
            return (i % n + 1)-1, (int((i + 1) / n)+1)
        if i != words.index(words[i]):
            print("-----")
            return i%n+1 ,int((i+1)/n)
    return [0,0]


print(solution(3 ,["tank", "kick", "know", "wheel", "land",
                   "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either",
                   "recognize", "encourage", "ensure", "establish",
                   "hang", "gather", "refer", "reference", "estimate",
                   "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))