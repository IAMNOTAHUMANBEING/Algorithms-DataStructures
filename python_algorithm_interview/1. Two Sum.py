# 1. 브루트 포스로 계산
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if num[i] + num[j] == target:
                return [i, j]
            
# 2. in을 이용한 탐색
def twoSum2(self, nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return nums.index(n), nums[i + 1:].index(complement) + (i + 1)

# 시간 복잡도는 풀이1과 같은 O(n^2)이지만 in이 매번 비교하는 것보다 빠르다.

# 3. 첫번째 수를 뺀 결과 키 조회
def twoSum3(self, nums: List[int], target: int) -> List[int]:
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i
    
    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:    # 같은 인덱스인 경우 예외처리 필요
            return nums.index(num), nums_map[target - num]

# 4. 조회 구조 개선

def twoSum4(self, nums: List[int], target: int) -> List[int]:
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:    
            return i, nums_map[target-num]
        nums_map[num] = i

# 5. 투 포인터 이용
def twoSum5(self, nums: List[int], target: int) -> List[int]:
    nums.sort()
    left, right = 0, len(nums) - 1
    while not left == right:
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return left, right

# 인덱스를 구해야하므로 sort를 사용해야 하는 알고리즘으로는 풀 수 없음
