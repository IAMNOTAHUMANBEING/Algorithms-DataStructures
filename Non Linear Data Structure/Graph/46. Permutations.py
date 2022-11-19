# 풀이1. DFS를 활용한 순열 생성
import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        sets = []

        def dfs(elements):
            # 리프 노드일 때 결과 추가
            if len(elements) == 0:
                results.append(sets[:]) # 참조가 추가되므로 copy하여 추가해야함

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)     # 선택된 숫자 빼고

                sets.append(e)     # 탐색한 숫자 삽입
                dfs(next_elements) # 다음 조합 문자들
                sets.pop()  # 한 줄기가 끝나면 위 단계 반복문 돌기 위해 초기조건 맞춰줘야함

        dfs(nums)
        return results

# 풀이2. itertools 모듈 사용
def permute(self, nums: List[int]) -> List[List[int]]:
    return list(map(list, itertools.permutations(nums)))

