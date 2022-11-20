# 풀이1. 파이썬 다운 방식
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len([ stone for stone in stones if stone in jewels ])

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stone in jewels for stone in stones)

# 풀이2. 해시 테이블을 이용한 풀이
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = {}

        for char in stones:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        count = 0
        for char in jewels:
            if char in freqs:
                count += freqs[char]

        return count

# 풀이3. default dict를 이용한 비교 생략
import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        for char in stones:
            freqs[char] += 1

        for char in jewels:
            count += freqs[char]

        return count

# 풀이4. counter로 계산 생략
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)
        count = 0

        for char in jewels:
            count += freqs[char]

        return count


