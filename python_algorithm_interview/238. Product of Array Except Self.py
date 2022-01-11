# 풀이1. 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        p = 1   # 곱셈 결과를 저장하는 리스트 없이 변수에 쌓아가는 방식도 가능
        # 왼쪽 곱셉
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]
        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums) - 1, - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]
        return out


