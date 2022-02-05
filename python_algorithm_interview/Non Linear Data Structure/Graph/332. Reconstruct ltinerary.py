# 풀이1. DFS로 일정 그래프 구성
import collections


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)

        route = []
        def dfs(a):
            # 첫 번째 값을 읽어 어휘 순 방문
            while graph[a]: # if가 아닌 이유: 사전 순으로 뒤인 지역부터 가야 일정이 연결 되는 경우 때문에, 여행 일정은 완성되는 상태에서 사전 순임을 요구하는 것
                dfs(graph[a].pop(0))
            route.append(a)

        dfs('JFK')
        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]

# 풀이2. 스택 연산으로 큐 연산 최적화 시도
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프 뒤집어서 구성
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []
        def dfs(a):
            # 마지막 값을 읽어 어휘 순 방문
            while graph[a]: # if가 아닌 이유: 사전 순으로 뒤인 지역부터 가야 일정이 연결 되는 경우 때문에, 여행 일정은 완성되는 상태에서 사전 순임을 요구하는 것
                dfs(graph[a].pop())
            route.append(a)

        dfs('JFK')
        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]

# 풀이3. 일정 그래프 반복
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        # 그래프 순서대로 구성
        for a, b in sorted(tickets):
            graph[a].append(b)

        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:     # 어휘 순으로 탐색
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())   # 마지막 지점에 올 때 마다 저장(역순으로 저장되는 이유)
        
        return route[::-1]



