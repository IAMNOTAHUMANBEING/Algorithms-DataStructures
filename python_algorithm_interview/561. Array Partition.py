# 풀이1. 오름차순 풀이
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = sum([num for i, num in enumerate(nums) if i % 2 == 0])
        return result

# 풀이2. 파이썬 다운 방식
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])