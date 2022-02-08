# 풀이1. 상태값 누적 트리 DFS
class Solution:
    longest: int = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:    # 종료조건
                return -1   # + 2 와 맞춰주기 위해
            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)
            # 상태값(리프 노드부터 해당 노드까지 길이)
            return max(left, right) + 1

        dfs(root)
        return self.longest

