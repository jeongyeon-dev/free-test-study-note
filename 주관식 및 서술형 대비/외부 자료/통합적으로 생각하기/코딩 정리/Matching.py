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