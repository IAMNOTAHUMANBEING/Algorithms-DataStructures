# 완전탐색 -> 시간초과

# dict 이용
def threeSum(self, nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()
    for i in range(len(nums) - 2):  # 리스트 길이가 3보다 작아지는 예외
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]
        new_nums = nums[i + 1:]

        nums_map = {}
        for j, num in enumerate(new_nums):
            if j > 1 and nums_map[num] > 2:  # 같은 수 끼리 조합 될 때 같은 수가 연속해서 나오는 경우
                continue
            if target - num in nums_map:
                result.append([nums[i], num, target - num])
                del (nums_map[target - num])  # 조합을 찾으면 키를 지워서 연속으로 조합되는 경우 제외
            nums_map[num] += 1
    return result

# default dict 이용하여 개선
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 2):  # 리스트 길이가 3보다 작아지는 예외
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]

            nums_map = defaultdict(int)
            for j in range(i + 1, len(nums)):
                num = nums[j]
                if nums_map[num] > 1:
                    continue
                if nums_map[target - num] > 0:
                    result.append([nums[i], num, target - num])
                    nums_map[num] += 1
                nums_map[num] += 1
        return result

# 투 포인터로 합 계산
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 간격을 좁혀가며 합 sum 계산
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # sum = 0인 경우이므로 정답 및 스킵 처리
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results