import heapq

# 주식에서 지정가 주문 로직을 구현하는 테스트이다.
# 한 종목을 대상으로 가정한다.  

commands = ["S 1 70100 5", "S 2 70000 3", "S 3 70000 4", "B 4 70100 10", "C 1", "B 5 70100 1"]
# 명령어는 각 행에 B: 매수, S: 매도, C: 취소이며,
# 두 번째 열은 id, 세 번째는 가격, 네 번째는 수량이다.
# 시간 순으로 주문이 들어있다.


# 체결 내역을 순서대로 반환해야 함
# [매수id 매도id 가격 수량]이 한 개
# lazy deletion을 수행하기로 => set에 저장

# 난해하다... 다음에 풀기로
def solution(commands):

    # 하나에 (가격, 시퀀스, 아이디, 수량)
    # 매도 호가 주문들 => 낮은 순으로 정렬
    selling_ask = []
    # 매수 호가 주문들 => 높은 순으로 정렬
    buying_ask = []

    canceled = set()
    seq = 1


    for command in commands:
        # 살 때
        if command[0] == 'S':
            order_amount = command[3]
            # 만약 팔겠다는 주문이 있다면?
            while buying_ask:
                top = buying_ask[0]

                # 파는 호가가 살 가격보다 낮다면? => 체결
                if top[0] <= command[2]:
                    bought = heapq.heappop(buying_ask)

                    # 수량 비교
                    left_amount = 0 if order_amount > bought[3] else bought[3] - order_amount

                    # 잔여분이 있을 때 => 수량 차감한 후 다시 넣는다
                    if left_amount != 0:
                        heapq.heappush(buying_ask, (bought[0], bought[1], bought[2], left_amount))

                    # 주문 량도 체결 수량 만큼 차감
                    order_amount -= (bought[1] - left_amount)
                    print(f"판매됨, 가격: {top[0]} , 수량: {order_amount}, 시퀀스: {bought[1]}")
                
            # 만족하는 호가가 없다면? => hq에 넣기
            if len(buying_ask) == 0:
                heapq.heappush(buying_ask, (command[2], seq, command[1], command[3]))
                
        # 팔 때
        elif command[0] == 'B':
            order_amount = command[3]
            
            # 만약 사겠다는 주문이 있으면?
            while selling_ask:
                top = selling_ask[0]

                # 사는 호가가 팔 가격보다 높다면? => 체결
                # 음수로 넣을 것: 높은 순이니
                if -top[0] >= command[2]:
                    selled = heapq.heappop(selling_ask)

                    left_amount = 0 if order_amount > selled[3] else selled[3] - order_amount

                    if left_amount != 0:
                        heapq.heappush(selling_ask, (-selled[0], selled[1], selled[2], left_amount))

                    order_amount -= (selled[1] - left_amount)
                    print(f"구매함, 가격: {top[0]} , 수량: {order_amount}, 시퀀스: {selled[1]}")

            if len(selling_ask) == 0:  
                heapq.heappush(selling_ask, (-command[2], seq, command[1], command[3]))
        
        # 취소할 때
        elif command[0] == 'C':
            canceled.add(command[1])


        seq += 1




solution(commands)

