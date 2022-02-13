# 풀이1. 자료형 변환
class Solution:
    # 연결리스트 뒤집기
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev
    # 연결리스트 -> 리스트
    def toList(self, node: ListNode) -> List:
        list: List = []
        while node:
            list.append(node.val)
            node = node.next

        return list
    # 문자열 -> 역순 연결리스트
    def toReversedLinkedList(self, result: String) -> ListNode:
        prev: ListNode = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

        return node
    # 두 수의 합
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = self.toList(self.reverseList(l1))
        b = self.toList(self.reverseList(l2))

        result = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))
        # 다른 방법
        # result = int(''.join(map(str, a))) + int(''.join(map(str, b)))
        # functools.reduce(lambda x, y: 10 * x + y, a, 0)

        return self.toReversedLinkedList(str(result))

# 풀이2. 전가산기 구현
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next

        return root.next




