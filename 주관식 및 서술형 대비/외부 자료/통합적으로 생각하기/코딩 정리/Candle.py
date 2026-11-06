import math

ticks = ["09:00:05 70000 10", "09:00:01 70100 5", "09:00:59 69900 2", "09:02:10 70200 1"]

def solution(ticks):
    _ticks = []    
    out = []

    for tick in ticks:
        tk = tick.split(' ')
        time = tk[0]
        price = int(tk[1])
        amount = int(tk[2])

        hr, m, s = time.split(':')
        total_sec = int(hr) * 3600 + int(m) * 60 + int(s)

        amt = [total_sec, price, amount]
        _ticks.append(amt)

    _ticks.sort(key=lambda x:x[0]) 

    start_s = _ticks[0][0]
    end_s = _ticks[-1][0]
    idx = 0
    prev = 0

    for m in range(int(start_s/60), int(end_s/60) + 1):
        o = -1
        h = float('-inf')
        l = float('inf')
        c = 0
        v = 0


        while idx < len(_ticks) and int(_ticks[idx][0] / 60) == m:
            cur = _ticks[idx]

            h = max(h, cur[1])
            l = min(l, cur[1])
            v += cur[2]

            if o == -1:
                o = cur[1]
            
            c = cur[1]
            prev = cur[1]

            idx += 1

        if o == -1:
            o = h = l = c = prev
            
        out.append(f"{int(m/60):02d}:{(m%60):02d} {o} {h} {l} {c} {v}")


    return out

result = solution(ticks)
print(result)