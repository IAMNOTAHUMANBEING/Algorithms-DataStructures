# 풀이1. 재귀구조로 높이 차이 계산
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1 or (left or right) == -1:  # 처음에 만든 클래스 변수 선언하여 상태값 바꾸는 방법보다 한번 음수 되면 계속 음수 리턴 되는 방식으로 구성하면 더 깔끔
                return -1
            return max(left, right) + 1

        return dfs(root) != -1

