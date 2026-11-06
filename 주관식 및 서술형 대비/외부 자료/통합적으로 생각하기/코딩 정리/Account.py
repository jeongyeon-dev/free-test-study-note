
events = ["e1 A DEPOSIT 10000", "e2 A WITHDRAW 3000", "e2 A WITHDRAW 3000", "e3 A TRANSFER B 8000", "e4 B DEPOSIT 500", "e5 A TRANSFER B 7000"]

def solution(events):
    done = set()
    balance = {}
    out = []
    rejected = []

    for event in events:
        evnt = event.split(' ')

        id = evnt[0]
        acc_a = evnt[1]
        cmd = evnt[2]

        if id in done:
            continue
        done.add(id)

        if cmd == 'DEPOSIT':
            amt = int(evnt[3])
            balance[acc_a] = balance.get(acc_a, 0) + amt
        elif cmd == 'WITHDRAW':
            amt = int(evnt[3])
            cur_amt = balance.get(acc_a, 0)

            if amt > cur_amt:
                rejected.append(f"REJECTED:{id}")
                continue
            else:
                balance[acc_a] -= amt
        elif cmd == 'TRANSFER':
            acc_b = evnt[3]
            amt = int(evnt[4])
            a_amt = balance.get(acc_a, 0)

            if amt > a_amt:
                rejected.append(f"REJECTED:{id}")
                continue
            else:
                balance[acc_a] -= amt
                balance[acc_b] = balance.get(acc_b, 0) + amt

    
    for k, v in balance.items():
        out.append(f"{k}:{v}")

    for v in rejected:
        out.append(v)
    
    return out

result = solution(events)
print(result)