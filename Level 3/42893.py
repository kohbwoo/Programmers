import re
def solution(word, pages):
    score = []
    domainscore = []
    domains = []
    domain = []
    domain_ = []
    for i in range(0,len(pages)): #점수 리스트 생성
        score.append(0)

    for i in range(0,len(pages)):#해당 페이지의 도메인 추출
        key = re.compile('{}(.*){}'.format(re.escape('"og:url\" content=\"'), re.escape('\"/>\n')))
        tmp = (key.findall(pages[i]))
        domain.append(tmp)

    for i in range(0,len(domain)):#도메인 배열 변경
        for j in range(0,len(domain[i])):
            domain_.append(domain[i][j])
            domainscore.append(0)



    for i in range(0,len(pages)): #문자열 소문자 변환
        pages[i] = pages[i].lower()

    for i in range(0,len(pages)): #검색어 점수 추가
        score[i] = score[i] + pages[i].count(word)


    print("------------------")

    for i in range(0,len(pages)):

        key = re.compile('{}(.*){}'.format(re.escape('<a href=\"'), re.escape('\"> link to')))
        tmp = (key.findall(pages[i]))
        domains = domains + 1




    for i in range(0,len(pages)):

        key = re.compile('{}(.*){}'.format(re.escape('<a href=\"'), re.escape('\"> link to')))
        tmp = (key.findall(pages[i]))
        domains = domains + 1

        for j in range(0,len(domain_)):
            if tmp == domain_[j]:
                domainscore[j] = domainscore[j] + 1





    # for i in range(0,len(pages)):
    #     for j in range(0,len(domain)):
    #         print(domain)
    print(domain_)




    answer = score
    return answer


a = "blind"
b = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
     "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
     "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
print(solution(a,b))