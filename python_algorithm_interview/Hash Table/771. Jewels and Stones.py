# 풀이1.
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = [ stone for stone in stones if stone in jewels ]
        return len(result)

# 풀이2.
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        