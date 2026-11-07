from collections import deque

request = ["0 a", "100 a", "200 a", "300 b", "400 c", "1000 a", "1100 a"]
userLimit = 2
globalLimit = 3
windowMs = 1000

def solution(request, userLimit, globalLimit, windowMs):

    outs = []
    dq = deque()
    dic = {}
    glob = 0

    for req in request:
        r = req.split(' ')
        ms = int(r[0])
        user = r[1]

        while dq:
            p = dq[0]
            p_time = p[0]
            p_user = p[1]

            if ms - windowMs >= p_time:
                dq.popleft()
                dic[p_user] -= 1
                glob -= 1
            else:
                break

        dic[user] = dic.get(user, 0)

        if dic[user] < userLimit and glob < globalLimit:
            dic[user] += 1
            glob += 1
            outs.append("ALLOW")
            dq.append([ms, user])
        else: 
            outs.append("DENY")

    
    return outs

result = solution(request, userLimit, globalLimit, windowMs)
print(result)


# 설계 방식: 슬라이딩 윈도우
# 
# glob: windowMs내 총 수, dic: windowMs내 특정 유저 총 수
# deque: 들어간 요청 리스트 
#
# for 순회 request 를 req로
# req를 '시간', '유저'로 분리
# 
# 각 req 돌 때마다: 
# 1. Ms 지났을 경우 빼는 로직
# => deque를 peek 하면서 지난 거 뺌: glob/dic에 반영
# 
# 2. 진입 조건 만족 & 불만족 판별:
# => 만족 시 glob/dic에 반영 .. ALLOW
# => 불만족 시 미반영 .. DENY
#
#