from collections import deque

# Adv는 추후에..
request = ["0 a", "100 a", "200 a", "300 b", "400 c", "1000 a", "1100 a"]
userLimit = 2
globalLimit = 3
windowMs = 1000

def solution(request, userLimit, globalLimit, windowMs):

    dq = deque()
    dict = {}
    glob = 0
    outs = []
    
    for req in request:
        rq = req.split(' ')
        time = int(rq[0])
        user = rq[1]

        while dq:
            peek = dq[0]

            # 시간 경과함 => 윈도우 범위 아님
            if time - 1000 >= peek[0]:
                out = dq.popleft()
                out_user = out[1]

                dict[out_user] -= 1
                glob -= 1
            else:
                break

        user_amt = dict.get(user, 0)

        # 두 조건을 만족해야 넣을 수 있음
        if glob < globalLimit and user_amt < userLimit:
            dq.append([time, user])
            dict[user] = dict.get(user, 0) + 1
            glob += 1

            outs.append("ALLOW")
        else:
            outs.append("DENY")
    
    return outs

result = solution(request, userLimit, globalLimit, windowMs)
print(result)