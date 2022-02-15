# 힙: 힙의 특성(최소 힙에서는 부모가 항상 자식보다 작거나 같다)을 만족하는 거의 완전하 트리인 특수한 트리 기반의 자료구조
# 최소 힙은 부모가 항상 자식보다 작고 우선순위 큐에서 가장 작은 값을 추출하는 것은 매번 힙의 루트를 가져오는 형태로 구현 된다.
# 우선순위 큐 ADT는 힙으로 구현하고 힙은 배열로 구현한다.
# 오해하기 쉬운 특징은 힙은 정렬된 구조가 아니라는 점, 부모 자식 간의 관계만 정의할 뿐 좌우에 대한 관계는 정의하지 않기 때문
# 힙은 완전 이진 트리이기 때문에 배열에 순서대로 표현하기 적합
# 힙은 균형을 유지하는 특징 때문에 다양한 분야에 활용 ex. 다익스트라, 힙 정렬, 최소 신장 트리를 구현하는 프림, 중앙값의 근사값

# 힙 연산:
class BinaryHeap(object):
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):
        i = len(self)
        parent = i // 2
        while parent >= 0:
            if self.items[i] < self.items[parent]:
                self.items[parent], self.items[i] = self.items[i], self.items[parent]
            i = parent
            parent = i // 2

    # 삽입(logn)
    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def _percolate_down(self, idx):
        left = idx * 2
        right = idx * 2 + 1
        smallest = idx

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != idx:
            self.items[idx], self.items[smallest] = self.items[smallest], self.items[idx]
    # 추출(logn)
    def

