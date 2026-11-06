import heapq

deps = ["order account", "order market", "balance account", "order balance", "gateway order"]

def solution(deps):
    graph = {}
    degree = {}
    hq = []
    count = 0

    for dep in deps:
        dp = dep.split(' ')
        a = dp[0]
        b = dp[1]

        graph.setdefault(b, []).append(a)
        degree[a] = degree.get(a, 0) + 1
        degree[b] = degree.get(b, 0)

    for k, v in degree.items():
        if v == 0:
            heapq.heappush(hq, k)
            count += 1

    order = []

    while hq:
        q = heapq.heappop(hq)
        order.append(q)
    
        for n in graph.get(q, []):
            if degree[n] > 0:
                degree[n] -= 1

            if degree[n] == 0:
                heapq.heappush(hq, n)
                count += 1

    return order if count == len(degree) else []

result = solution(deps)
print(result)