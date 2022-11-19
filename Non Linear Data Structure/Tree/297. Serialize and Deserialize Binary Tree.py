# 풀이1. BFS를 통한 직렬화& 역직렬화
import collections


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = collections.deque([root])
        result = ['#']  # 일반적으로 트리의 배열 표현은 계산의 편리성을 위해 index 1부터 사용, 깊이가 1, 2, 4, 8 .. 증가하므로 노드 인덱스를 알면 위치를 알 수 있음
        while queue:    # 부모 [i/2], 왼쪽 자식 2i, 오른쪽 자식 2i + 1
            node = queue.popleft()
            if node is None:
                result.append('#')
            else:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ' '.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # 예외 처리
        if data == '# #':
            return None

        nodes = data.split()

        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        index = 2
        # 빠른 런너처럼 자식 노드 결과를 먼저 확인 후 큐 삽입
        while queue:
            node = queue.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index += 1

            if nodes[index] is not '#':
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))