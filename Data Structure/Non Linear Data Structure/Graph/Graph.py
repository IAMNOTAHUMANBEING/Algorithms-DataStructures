# 그래프: 객체의 일부 쌍들이 연관되어 있는 객체 집합 구조

# 오일러 경로: 모든 간선을 한 번씩 방문하는 유한 그래프 경로
# 해밀턴 경로: 각 정점을 한 번씩 방문하는 무향 또는 유향 그래프 경로

# 그래프 순회: 그래프 탐색이라고도 부르며 그래프의 각 정점을 방문하는 과정
# 깊이 우선 탐색(DFS): 주로 스택이나 재귀로 구현, 백트래킹을 통해 효용을 보임
# 넓이 우선 탐색(BFS): 주로 큐로 구현, 최단경로 문제 등에 사용

# 그래프 표현 방법: 인접 행렬과 인접 리스트
graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

# DFS
# 재귀 구조로 구현
def recursive_dfs(v, discovered = []):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            discovered = recursive_dfs(w, discovered)

    return discovered
# 1 2 5 6 7 3 4

# 스택을 이용한 반복 구조로 구현
def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)

    return discovered
# 1 4 3 5 7 6 2

# BFS
# 큐를 이용한 반복 구조로 구현
def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)

    return discovered

# 재귀 구현 불가

# 백트래킹: 해결책에 대한 후보를 구축해 나가다 가능성이 없다고 판단되는 즉시 후보를 포기해 정답을 찾아가는 범용적인 알고리즘으로 제약 충족 문제에 유용
# 제약 충족 문제: 수많은 제약조건을 충족하는 상태를 찾아내는 수학문제





