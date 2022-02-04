# 풀이1. 개별 체이닝 방식을 이용한 해시 테이블 구현
import collections

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    # 초기화
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    # 삽입
    def put(self, key: int, value: int) -> None:
        index = key % self.size
        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None: # 노드 존재성을 체크하는게 아닌 노드의 값 존재성을 체크 하는 이유는 디폴트 딕트라서 노드가 존재하지 않을 경우 자동 생성하므로
            self.table[index] = ListNode(key, value)
            return

        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.table[index]
        while p:
            # 종료조건: 키가 이미 존재하는 경우 -> 업데이트, 마지막까지 조회한 경우 -> 추가
            if p.key == key:
                p.value = value
                return
            if p.next is None:  # 없어도 될 거 같은데? 없으면 인덱스가 마지막 칸까지 넘어가 버려서 p.next 에 노드 삽입이 불가능
                break
            p = p.next
        p.next = ListNode(key, value)

    # 조회
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        # 노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # 삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next    # 디폴트 딕트를 썼으므로 빈 노드로 업데이트가 삭제 기능을 함
            return

        # 연결리스트 노드 삭제
        prev = p    # 이전 노드를 이렇게 초기화하면 첫 번째 노드에서 일치하는 경우 문제가 생길 수 있지만 첫번째 노드인 경우는 앞에서 미리 처리하도록 했으므로 문제 없음
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
        return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)