# 트리: 계층형 트리 구조를 시뮬레이션 하는 추상 자료형으로 루트 값과 부모-자식 관계의 서브트리로 구성되며, 서로 연결된 노드의 집합이다
# 재귀로 정의된 자기 참조 자료구조 -> 트리의 자식도 트리, 서브트리로 구상된다고 표현 -> 순회에서 재귀가 자연스러움
# 그래프와의 차이는 트리는 순환구조를 갖지 않고 단방향이고 루트(and 부모노드)가 하나라는 점

# 이진 트리: 최대 2개의 자식을 갖는 트리, 다진트리에 비해 알고리즘 구현이 간단하여 많이 사용
# 정(full) 이진 트리: 모든 노드가 0개 또는 2개의 자식 노드를 갖는다
# 완전(complete) 이진 트리: 마지막 레벨을 제외하고 모두 채워져 있으며 마지막 레벨의 모든 노드는 왼쪽부터 채워져있다
# 포화(perfect) 이진 트리: 모든 노드가 2개의 자식 노드를 가지며 모든 리프 노드가 동일한 깊이 또는 레벨을 갖는다

# 이진 탐색 트리(BST): 노드 왼쪽 서브트리는 그 노드의 값보다 작은 값, 오른쪽 서브트리는 큰 값으로 정렬된 트리
# 탐색 시 시간 복잡도가 O(logn) 그러나 트리의 균형이 맞지 않으면 효율이 떨어진다.
# 자가 균형(높이 균형) 이진 탐색 트리: 삽입, 삭제 시 자동으로 높이를 작게 유지하는 노드 기반의 이진 탐색 트리
# ex. AVL 트리, 레드-블랙 트리 등

# 트리 순회: 트리 자료구조에서 각 노드를 정확히 한 번 방문하는 과정. 크게 전위NLR 중위LNR 후위LRN로 구분 됨
# 전위 순회:
def preorder(node):
    if node is None:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)

# 중위 순회:
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)

# 후위 순회:
def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)









