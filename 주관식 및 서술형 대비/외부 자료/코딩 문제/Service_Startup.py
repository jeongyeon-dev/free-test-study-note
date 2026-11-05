import heapq

# Adv는 추후에..
deps = ["order account", "order market", "balance account", "order balance", "gateway order"]

def solution(deps):
    graph = {}
    degree = {}
    

    # 인접 리스트와 차수 만들기
    for dep in deps:
        wrds = dep.split(' ')
        a = wrds[0]
        b = wrds[1]

        graph.setdefault(b, []).append(a) 
        degree[a] = degree.get(a, 0) + 1
        degree[b] = degree.get(b, 0)


    order = []
    hq = []
    count = 0
    
    # 맨 처음 가능한 거  
    for k, v in degree.items():
        if v == 0:
            heapq.heappush(hq, k)
            count += 1


    # 빼기
    while hq:
        val = heapq.heappop(hq)
        order.append(val)

        for neighbor in graph.get(val, []):
            if degree[neighbor] > 0:
                degree[neighbor] -= 1

            if degree[neighbor] == 0:
                heapq.heappush(hq, neighbor)
                count += 1

    return order if count == len(degree) else []

result = solution(deps)
print(result)