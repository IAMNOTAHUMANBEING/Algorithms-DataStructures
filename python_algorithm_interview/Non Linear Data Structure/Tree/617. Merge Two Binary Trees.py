# 풀이1. 재귀 탐색
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)

            return node
        else:
            return root1 or root2   # 둘 중에 존재하는 것만 리턴, 둘다 없으면 None 리턴

# 깊이가 다른 트리라면 안될 거 같은데?

