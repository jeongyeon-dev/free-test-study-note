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