# 여기서는 이전에 구현한 코드를 더 간결하고, 유용하게 작성을 한다.

events = ["e1 A DEPOSIT 10000", "e2 A WITHDRAW 3000", "e2 A WITHDRAW 3000", "e3 A TRANSFER B 8000", "e4 B DEPOSIT 500", "e5 A TRANSFER B 7000"]

def solution(events):
    balance = {}
    seen = set()
    rejected = []

    for event in events:
        p = event.split(' ')
        id = p[0]
        account = p[1]
        typ = p[2]

        if id in seen:
            continue

        seen.add(id)

        balance[account] = balance.get(account, 0)

        if typ == 'DEPOSIT':
            balance[account] += int(p[3])
        elif typ == 'TRANSFER':
            to = p[3]
            amount = int(p[4])
            balance[to] = balance.get(to, 0)

            if balance[account] < amount:
                rejected.append(id)
            else:
                balance[to] += amount
                balance[account] -= amount
        elif typ == 'WITHDRAW':
            amount = int(p[3])

            if balance[account] < amount:
                rejected.append(id)
            else:
                balance[account] -= amount
    
    out = []

    for key, val in balance.items():
        out.append(f"{key}:{val}")

    for ids in rejected:
        out.append(f"REJECTED:{ids}")

    return out


# 실행부
result = solution(events)
print(result)