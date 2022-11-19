# 풀이1. 우선순위 큐를 이용한 리스트 병합
# PriorityQueue를 쓰지 않고 Heap을 쓰는 이유: PriorityQueue는 스레드 세이프 클래스인데 파이썬은 GIL 특성상 멀티 스레딩이 거의 의미가 없고
# 성능에만 영향을 끼치므로 굳이 멀티 스레드로 구현할 것이 아니라면 Heap을 쓰는 것이 좋다.
# GIL은 전역 인터프리터 락의 약어로서 하나의 스레드가 자원을 독점하는 형태로 실행된다. CPU가 하나이던 시대에선 당연했지만 멀티코어가 당연한
# 지금 시대에서는 하나의 스레드가 자원을 독점하는 형태로 실행되는 제약은 성능에 치명적이다.
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        root = result = ListNode(None)
        heap = []

        # 각 연결 리스트의 루트를 힙에 저장
        for i in range(len(lists)):
            if lists[i]:    # 빈 리스트는 제외
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        # 힙 추출 이후 다음 노드는 다시 저장
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]   # 위에서 3가지 요소 저장한 것 중 1번 인덱스에 있는 요소 의미
            result.next = node[2]

            result = result.next
            if result.next: # 노드가 끝나면 저장하면 안되므로
                heapq.heappush(heap, (result.next.val, idx, result.next)) # 다시 루트들 끼리 비교하기 위해
        
        return root.next