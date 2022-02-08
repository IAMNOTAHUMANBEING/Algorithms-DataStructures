# 풀이1. 다익스트라 알고리즘 구현
import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in flights:
            graph[u].append((v, w))

        # 큐 변수[(가격, 정점, 경유 수)]: 노드 별 누적 도달 가격 저장
        Q = [(0, src, k)]
        dist = collections.defaultdict(list)

        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst: # 제한 경유 내에 도착
                return price

            if k >= 0:  # 도착지 못가고 제한 경유 수 도달하면 더이상 Q에 선택지가 쌓이지 않아서 반복문이 다 끝나고 -1 리턴하게 됨
                for v, w in graph[node]:
                    if v not in dist or price + w < dist[v][0] or k-1 > dist[v][1]:
                        # 743번 문제처럼 비용만 기준으로 중복 경로 제거하면 경유 제한 조건 아래에서는 최단 경로를 제외하게 될수도 있기 때문에 두가지 조건 중에서 효율적인 경우가 있다면 경로 유지
                        dist[v] = [w + price, k-1]
                        heapq.heappush(Q, (price + w, v, k-1))

        return -1