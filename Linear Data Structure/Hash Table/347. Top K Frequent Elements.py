import collections
import heapq
# 풀이1. 파이썬다운 방식
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]  # 언패킹

#풀이2. Counter를 이용한 음수 순 추출
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []
        # 힙에 음수로 삽입
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))  # 파이썬 heap은 최소 힙만 지원하므로 부호를 바꿔서 상위값 찾기
                                                        # 힙은 키 순으로 정렬되므로 빈도 수가 키가 되도록 키/값을 뒤집어서 저장
        topk = list()
        # k번 만큼 추출, 최소 힙이므로 가장 작은 음수 순으로 추출
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk




