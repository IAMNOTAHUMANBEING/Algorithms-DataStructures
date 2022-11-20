# 풀이1. DFS로 k개 조합 생성
import itertools


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):  # elem은 탐사 숫자 저장, start는 조합할 숫자 위치, k는 조합 횟수
            if k == 0:
                results.append(elements[:])

            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return results

# 풀이2. itertools 모듈 사용
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n+1), k))

# 풀이3. 점화식 이용
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == k or k == 0:
            return 1
        return self.combine(n - 1, k) + self.combine(n - 1, k - 1)
