import math

ticks = ["09:00:05 70000 10", "09:00:01 70100 5", "09:00:59 69900 2", "09:02:10 70200 1"]

def solution(ticks):

    # ticks 길이가 최대 50만이니 정렬해도 괜찮을 듯
    ticks.sort(key=lambda x: x.split(' ')[0])

    minutes = 0
    hours = 0

    min_val = float('inf')
    max_val = float('-inf')

    start_last = 0
    total_cmt = 0

    per_min_info = []

    for tick in ticks:
        infos = tick.split(' ')
        times = infos[0].split(':')
        h = times[0]
        m = times[1]
        s = times[2]

        val = int(infos[1])
        cmt = int(infos[2])

        # minutes와 m이 다를 때 마다 갱신을 한다
        if minutes != m or hours != h:


            # 바로 이전 값 갱신하기( , , 최댓값, 최솟값, , 카운트)
            if len(per_min_info) != 0:
                per_min_info[-1][2] = max_val
                per_min_info[-1][3] = min_val
                per_min_info[-1][5] = total_cmt

            # 중간에 갭이 있는지 검사하고 있으면 추가 삽입
            if len(per_min_info) != 0:
                last_val = per_min_info[-1][4]
                prev_time = per_min_info[-1][0].split(':')
                prev_min = int(prev_time[0]) * 60 + int(prev_time[1]) + 1
                curr_min = int(h) * 60 + int(m)

                # 값 삽입
                while prev_min < curr_min:
                    Min = prev_min%60
                    per_min_info.append([f"{int(prev_min/60)}:{Min:02d}", last_val, last_val, last_val, last_val, 0])
                    prev_min += 1


            # 현재 새롭게 시작한 값 넣기(시간, 첫 값, , , , )
            per_min_info.append([f"{h}:{m}", val, -1, -1, -1, -1])

            # 초기화
            min_val = float('inf')
            max_val = float('-inf')
            
            minutes = m
            hours = h
            total_cmt = 0

        # 기본 갱신
        min_val = min(min_val, val)
        max_val = max(max_val, val)

        # 마지막 값은 언제나 갱신
        if len(per_min_info) != 0:
            per_min_info[-1][4] = val
        
        total_cmt += cmt


    # 마지막 보강
    per_min_info[-1][2] = max_val
    per_min_info[-1][3] = min_val
    per_min_info[-1][5] = total_cmt

    out = []

    # 문자열 처리
    for per in per_min_info:
        out.append(f"{per[0]} {per[1]} {per[2]} {per[3]} {per[4]} {per[5]}")

    return out



result = solution(ticks)
print(result)