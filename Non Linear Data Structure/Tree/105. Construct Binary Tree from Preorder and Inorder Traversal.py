# 풀이1. 전위 순회 결과로 중위 순회 분할 정복
# 전위 순회 결과 요소들을 순서대로 중위 순회 결과 요소와 매핑해보면 이진 트리가 어떤 식으로 구성되는지 생각해볼 수 있음
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder: # 빈 리스트가 될 때까지 분할
            index = inorder.index(preorder.pop(0))

            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[:index])
            node.right = self.buildTree(preorder, inorder[index + 1:])

            return node
        return