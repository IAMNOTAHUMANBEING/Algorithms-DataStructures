# 풀이1. 재귀구조 DFS로 브루트 포스 탐색
import collections


class Solution:
    result: int = 0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root:
            if low <= root.val <= high:
                self.result += root.val
            self.rangeSumBST(root.left, low, high)
            self.rangeSumBST(root.right, low, high)

        return self.result

# 풀이2. DFS 가지치기로 필요한 노드 탐색
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0

            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)

            return node.val + dfs(node.right) + dfs(node.left)

        return dfs(root)

# 풀이3. 반복구조 DFS로 필요한 노드 탐색
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack, sum = [root], 0

        while stack:
            node = stack.pop()
            if node:
                if node.val < low:
                    stack.append(node.right)
                elif node.val > high:
                    stack.append(node.left)
                else:
                    sum += node.val
                    stack.append(node.right)
                    stack.append(node.left)

        return sum

# 풀이4. 반복구조 BFS로 필요한 노드 탐색
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue, sum = collections.deque(root), 0

        while queue:
            node = queue.popleft()
            if node:
                if node.val < low:
                    queue.append(node.right)
                elif node.val > high:
                    queue.append(node.left)
                else:
                    sum += node.val
                    queue.append(node.right)
                    queue.append(node.left)

        return sum






