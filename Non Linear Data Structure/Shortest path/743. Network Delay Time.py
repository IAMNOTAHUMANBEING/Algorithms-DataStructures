# 풀이1. 다익스트라 알고리즘 구현
import collections
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in times:
            graph[u].append((v, w))

        # 큐 변수[(소요 시간, 정점)]: 노드 별 누적 도달 시간 저장
        Q = [(0, k)]
        dist = collections.defaultdict(int) # 시간 짧은 순으로 key & value 뒤집어서 저장하는 변수, node가 key가 되어야 중복 확인 가능하므로

        # 큐에서 최소 시간 순으로 꺼내서 노드 도착하면 선택지들 누적 시간 더해서 Q에 추가, 이미 값이 존재한다면 저장되어 있는 값이 최단 경로이므로 제거
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

        # 모든 노드의 최단 경로 존재 여부 분별
        if len(dist) == n:
            return max(dist.values())
        return -1



