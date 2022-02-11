# 풀이1. 상대값 거리 계산 DFS
class Solution:
    result: int = 0
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            # 백트래킹 되면서 연속되는 노드 상태값 더하기
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            self.result = max(self.result, left + right)

            return max(left, right)

        dfs(root)

        return self.result

