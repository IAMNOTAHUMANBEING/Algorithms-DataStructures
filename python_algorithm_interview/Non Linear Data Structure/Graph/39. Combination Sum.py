# 풀이1. DFS 중복조합 그래프 탐색
# 테스트 케이스에는 없어서 통과됐지만, 0이 들어있는 경우 무한 탐색을 하게 되므로 예외처리가 필요하다
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(index, sets):
            if sets is None:    # 처음에 빈 리스트가 들어가는 경우 예외처리
                pass
            elif sum(sets) > target: # 가지치기
                return
            elif sum(sets) == target:   # 종료조건
                result.append(sets[:])
                return

            for i in range(index, len(candidates)): # 항상 모든 후보를 탐색하면 순서가 다른 중복된 경우도 나오게 됨 -> 순열
                dfs(i, sets + [candidates[i]])  # append로 추가해주면 pop으로 지워줘야 다른 반복문에서 초기조건으로 진행 가능한데 참조값을 바꾸지 않으면 pop이 필요 없어짐

        if candidates is None:
            return []
        result = []
        dfs(0, [])

        return result