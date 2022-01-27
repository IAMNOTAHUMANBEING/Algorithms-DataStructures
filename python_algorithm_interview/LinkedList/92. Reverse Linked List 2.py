# 풀이1. 반복구조로 노드 뒤집기
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 예외 처리
        if head is None or left == right:
            return head

        root = start = ListNode(None)
        root.next = head

        # start, end 지정
        for _ in range(left - 1):
            start = start.next
        end = start.next

        # 반복하면서 노드 차례대로 뒤집기
        for _ in range(right - left):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp

        return root.next  #

# 풀이2.
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        if left > 1:
            prev = None
            result = head

            for _ in range(left - 2):
                head = head.next
            front_end = head
            head = head.next
            start = head

            for _ in range(right - left - 1):
                next, head.next = head.next, prev
                head, prev = next, head
            next, head.next = head.next, prev
            front_end.next = head
            start.next = next

            return result

        start = head

        for _ in range(right):
            next, head.next = head.next, prev
            head, prev = next, head
        next, head.next = head.next, prev
        start.next = next

        return head