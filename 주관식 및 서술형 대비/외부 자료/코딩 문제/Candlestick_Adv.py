import math

ticks = ["09:00:05 70000 10", "09:00:01 70100 5", "09:00:59 69900 2", "09:02:10 70200 1"]

def solution(ticks):
    _ticks = []

    for tick in ticks:
        p = tick.split(' ')
        t = p[0].split(':')

        sec = int(t[0]) * 3600 + int(t[1]) * 60 + int(t[2]) 
        price = p[1]
        vol = p[2]

        amt = [sec, price, vol]
        _ticks.append(amt)

    _ticks.sort(key=lambda x: x[0])

    start_sec = _ticks[0][0]
    end_sec = _ticks[-1][0]
    
    
    out = []
    k = 0
    prevClose = 0

    for m in range(int(start_sec / 60), int(end_sec / 60) + 1):
        o = -1
        h = float('-inf')
        l = float('inf')
        c = 0
        v = 0
        
        while k < len(ticks) and int(_ticks[k][0] / 60) == m:
            pr = int(_ticks[k][1])

            if o < 0:
                o = pr

            h = max(h, pr)
            l = min(l, pr)
            c = pr
            v += int(_ticks[k][2])

            k += 1

        if o < 0:
            o = h = l = c = prevClose
        prevClose = c

        out.append(f"{int(m/60):02d}:{int(m%60):02d} {o} {h} {l} {c}")

    return out

result = solution(ticks)
print(result)