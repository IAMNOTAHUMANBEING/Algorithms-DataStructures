# 풀이1. 재귀구조로 뒤집기
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev # 역순의 헤드가 될 노드를 리턴해야함
            node.next, next = prev, node.next
            return reverse(next, node)

# 풀이2. 반복구조로 뒤집기
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            node, prev = node, next

        return prev
