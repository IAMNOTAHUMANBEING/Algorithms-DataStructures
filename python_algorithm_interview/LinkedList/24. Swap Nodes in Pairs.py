# 풀이1. 값만 교환
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur and cur.next:
            cur.val, cur.next.val = cur.next.val, cur.val
            cur = cur.next.next

        return head

# 현업에서는 간단한 값이 들어있지 않기 때문에 비 실용적인 방법

# 풀이2. 반복구조로 스왑
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next :
            # b가 a를 가리키도록 할당
            head.next = head.next.next
            head.next.next = head

            # prev가 b를 가리키도록 할당
            prev.next = head.next

            # 다음번 비교를 위해 이동
            head = head.next
            prev = prev.next.next

        return root.next

# 풀이3. 재귀구조로 스왑
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            head.next = self.swapPairs(head.next.next)
            head.next.next = head
            return head.next
        return head
# 반복 풀이와 달리 더미 노드나 추가 변수가 필요 없음



