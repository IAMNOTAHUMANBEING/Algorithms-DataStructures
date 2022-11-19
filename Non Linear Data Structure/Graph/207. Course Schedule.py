# 풀이1. DFS로 순환 구조 판별
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x,y in prerequisites:
            graph[x].append(y)

        traced = set()

        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):  # 순환 구조가 발견되는 순간 그 라인의 노드를 거슬러 올라가며 모두 False 처리
                    return False
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)

            return True

        # 순환 구조 판별
        for x in list(graph):   # 디폴트 딕트는 반복문 속에서 빈 값 조회 시 크기가 변경되므로 복사본을 분리해야한다 
            if not dfs(x):
                return False

        return True

# 풀이2. 가지치기를 이용한 최적화
# 한번 방문한 그래프를 또 방문할 필요가 없음
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x,y in prerequisites:
            graph[x].append(y)

        visited = set()
        traced = set()

        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False
            # 이미 방문 했던 노드이면 탐색 중지
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):  # 순환 구조가 발견되는 순간 그 라인의 노드를 거슬러 올라가며 모두 False 처리
                    return False
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            # 탐색 종료 후 방문 노드 추가
            visited.add(i)

            return True

        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False

        return True
