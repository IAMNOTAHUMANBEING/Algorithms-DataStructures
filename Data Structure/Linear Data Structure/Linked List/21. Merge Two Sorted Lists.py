# 풀이1. 재귀구조로 연결
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            if (not list1) or (list2 and list1.val > list2.val):    # 마지막 노드일 때, 더 큰 값을 찾았을 때
                list1, list2 = list2, list1
            if list1:   # 재귀가 종료될 조건(마지막 노드가 None임을 이용)
                list1.next = self.mergeTwoLists(list1.next, list2)

            return list1

