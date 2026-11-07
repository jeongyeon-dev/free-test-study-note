import heapq

commands = ["S 1 70100 5", "S 2 70000 3", "S 3 70000 4", "B 4 70100 10", "C 1", "B 5 70100 1"]

def solution(commands):
    buy = []
    sell = []
    canceled = set()
    seq = 0

    out = []

    for command in commands:
        cmd = command.split(' ')
        type = cmd[0]
        id = cmd[1]

        if type == 'C':
            canceled.add(id)
            continue

        target_q = buy if type == 'S' else sell
        putin_q = sell if type == 'S' else buy
        
        price = int(cmd[2])
        quantity = int(cmd[3])

        while quantity > 0 and target_q:
            peek = target_q[0]
            
            if peek[3] in canceled:
                heapq.heappop(target_q)
                continue

            peek_price = -peek[0] if type == 'S' else peek[0]
            peek_quantity = peek[2]
            peek_id = peek[3]

            crosses = price <= peek_price if type == 'S' else price >= peek_price

            if not crosses:
                break

            q = min(quantity, peek_quantity)
            quantity -= q
            peek[2] -= q

            if peek[2] == 0:
                heapq.heappop(target_q)

            buyId = peek_id if type == 'S' else id
            sellId = id if type == 'S' else peek_id

            out.append(f"{buyId} {sellId} {peek_price} {q}")

        if quantity > 0:
            heapq.heappush(putin_q, [-price if type == 'B' else price, seq, quantity, id])

        seq += 1
        
    return out


result = solution(commands)
print(result)


# 설계 방식: 우선순위 큐
# 
# 체결되지 않은 주문들:
# selling(팔 주문) => 내림 차순: 낮은 녀석부터 체결 .. 동일 시 seq 낮은 녀석 우선
# buying(살 주문) => 오름 차순: 높은 녀석부터 삼 .. 동일 시 seq 낮은 녀석 우선
# cancel(취소 주문) => set에 id 넣음
# 
# 
# for 주문 in commands.. 순으로 순회
# 
# 팔 주문일 경우: 
#   buying 있다면? => while
#   1. buying을 peek 함 => peekID = cancelID라면? pop 하고 다음
#   2. peek 가격 >= 팔 주문 가격: 수량 만큼 체결
#   3. peek의 수량 = 0 이라면? pop | peek 수량이 남아있다면? peek 수량만 차감
#   4. 팔 주문의 남은 수량이 > 0 이라면? selling에 넣음
# 
# 살 주문일 경우:
#   selling 있다면? => while
#   1. selling을 peek 함 => peekID = cancelID라면? pop 하고 다음
#   2. selling 가격 <= 살 주문 가격: 수량 만큼 체결
#   3. peek의 수량 = 0 이라면? pop | peek 수량이 남아있다면? peek 수량만 차감
#   4. 살 주문의 남은 수량이 > 0 이라면? buying에 넣음
#
#