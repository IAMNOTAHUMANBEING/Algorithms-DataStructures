# 풀이1. 리스트 변환
import collections


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True

# 풀이2. 데크를 이용한 최적화
# 동적 배열로 구성된 리스트는 맨 앞 요소를 가져오기에 적합하지 않은 자료형이다.
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q: Deque = collections.deque()

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

# 풀이3. 런너를 이용한 풀이
# 연결 리스트를 순회할 때 2개의 포인터를 동시에 사용하는 기법
# 한 포인터가 다른 포인터를 앞서게 하여 병합지점이나 중간위치, 길이 등을 판별할 때 유용하다
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next  # 다중 할당하지 않으면 실행되지 않음, 차이점 인식
        if fast:
            slow = slow.next    # 노드 개수가 홀수인 경우

        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev  # None, [] 등도 False 기능을 함


