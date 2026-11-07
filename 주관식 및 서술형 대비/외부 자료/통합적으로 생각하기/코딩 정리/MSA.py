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


# 위상정렬 문제: graph, dic 두 개 필요
# heapq 필요
#
# 먼저 graph를 만든다.. { 시작 프로그램: [의존되서 실행 가능한 프로그램들..] }
# degree는 { 특정 프로그램: 차수 } 식으로 한다
#   
# 실행이 가능한 복수의 프로그램: 사전 순으로 실행
#
# degree 순회: 차수 = 0 인 프로그램 => heapq
#  
#  
# heapq가 없어질 때 까지:
#   실행 가능 & 사전 순 첫째 = heapq.heappop()
#   
#   for 이웃 in graph[숫 첫째]:
#       degree[이웃] 1 차감하기
#
#       degree[이웃] = 0 이라면? heapq에 넣기
#       count 횟수 더하기  
#  
# 총 count = degree 노드 수와 같다면 위상정렬 성립