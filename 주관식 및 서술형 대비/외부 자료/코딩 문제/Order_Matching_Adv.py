import heapq

commands = ["S 1 70100 5", "S 2 70000 3", "S 3 70000 4", "B 4 70100 10", "C 1", "B 5 70100 1"]

def solution(commands):
    buys = []
    sells = []
    seq = 0
    canceled = set()

    out = []

    for command in commands:
        p = command.split(' ')
        
        order = p[0]
        id = p[1]

        if order == 'C':
            canceled.add(id)
            continue

        price = int(p[2])
        amount = int(p[3])

        if order == 'S':
            while buys and amount > 0:
                biggest = buys[0]

                if biggest[3] in canceled:
                    heapq.heappop(buys)
                    continue

                if -biggest[0] < price:
                    break

                q = min(amount, biggest[2])
                amount -= q
                biggest[2] -= q
                
                out.append(f"{biggest[3]} {id} {price} {q}")
                
                if biggest[2] == 0:
                    heapq.heappop(buys)

            if amount > 0:
                heapq.heappush(sells, [price, seq, amount, id])

        elif order == 'B':
            while sells and amount > 0:
                smallest = sells[0]

                if smallest[3] in canceled:
                    heapq.heappop(sells)
                    continue

                if smallest[0] > price:
                    break

                q = min(amount, smallest[2])
                amount -= q
                smallest[2] -= q

                if smallest[2] == 0:
                    heapq.heappop(sells)

                out.append(f"{id} {smallest[3]} {price} {q}")
                

            if amount > 0:
                heapq.heappush(buys, [-price, seq, amount, id])
        
        seq += 1

    return out


result = solution(commands)
print(result)

