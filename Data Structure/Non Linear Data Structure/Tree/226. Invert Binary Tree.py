# 풀이1. 파이썬다운 방식
import collections


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None

# 풀이2. 반복구조로 BFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            # 부모노드부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)

        return root

# 풀이3. 반복구조로 DFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()
            # 부모노드부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)

        return root


# 풀이4. 재귀구조로 DFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def change(root):
            if root:
                root.left, root.right = root.right, root.left
                change(root.left)
                change(root.right)
                return

        change(root)

        return root

# 풀이5. 반복구조로 DFS 후위 순회
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()

            if node:
                stack.append(node.left)
                stack.append(node.right)

                node.left, node.right = node.right, node.left # 후위 순회

        return root
