
events = ["t1 X DEPOSIT 100", "t2 X WITHDRAW 300", "t2 X WITHDRAW 300"]

def solution(events):
    # 처리된 id
    done = set()

    # 계좌별 잔고
    deposits = {}
    rejected = []

    for event in events:
        event_words = event.split(" ")
        event_id = event_words[0]

        # 중복 요청이라면?
        if event_id in done:
            continue

        # 입금
        if event_words[2] == 'DEPOSIT':
            account_a = event_words[1]
            amount = int(event_words[3])

            deposits[account_a] = deposits.get(account_a, 0) + amount

        # 출금
        elif event_words[2] == 'WITHDRAW':
            account_a = event_words[1]
            account_a_deposit = deposits[account_a]
            amount = int(event_words[3])

            # 예금이 충분하면 => 출금
            if account_a_deposit >= amount:
                deposits[account_a] -= amount
            # 실패 시
            else:
                rejected.append(f"REJECTED:{event_id}")

        # 송금
        elif event_words[2] == 'TRANSFER':
            account_a = event_words[1]
            account_b = event_words[3]
            amount = int(event_words[4])

            # 예금이 충분하면 => 출금
            if deposits[account_a] >= amount:
                deposits[account_a] -= amount
                deposits[account_b] = deposits.get(account_b, 0) + amount
            # 실패 시
            else:
                rejected.append(f"REJECTED:{event_id}")
        
        done.add(event_id)

    answer = []

    for key, value in deposits.items():
        answer.append(f"{key}:{value}")
    
    answer.extend(rejected)
    
    return answer

result = solution(events)
print(result)