# 풀이1. 상태값 누적 트리 DFS
# 클래스 변수를 사용한 이유: 중첩함수는 부모 함수의 변수를 자유롭게 읽을 수 있지만 중첩함수에서 부모함수 변수를 재할당할 경우 ID가 변경되며 별도의 로컬변수로 저장된다
# 만약 값이 숫자나 문자 같은 불변객체가 아니라 리스트나 딕셔너리라면 append 등의 메서드를 이용해 재할당 없이 조작이 가능하다

# 그럼 클래스 변수를 선언한 후 클래스.변수이름이 아니라 self.변수이름으로 재할당하는 이유는 뭘까?
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

