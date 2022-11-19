# 풀이1. 중위 순회로 노드 값 누적
class Solution:
    val: int = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 중위 순회 노드 값 누적
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)

            return root    # 재귀에서 리턴값을 사용하지는 않지만 채점을 위해 트리를 넘겨줘야 하므로
