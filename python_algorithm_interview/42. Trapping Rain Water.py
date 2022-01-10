# 완전탐색
def trap(self, height: List[int]) -> int:
    result = 0
    for j in range(max(height)):
        start = 0
        count = 0
        for i in height:
            if i > j:
                start += 1
                if start == 2:
                    result += count
                    start = 1
                    count = 0
            else:
                if start == 1:
                    count += 1
    return result
# 시간 초과

# 투 포인터를 최대로 이동
def trap2(self, height: List[int]) -> int:
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(left_max, height[left]), max(right_max, height[right])

        if left_max <= right_max :  # 포인터를 반복할 때마다 동시에 움직이면 가장 높은 부분이 정중앙에 있음을 보장할 수 없으므로 모든 칸을 탐색하기 전에 반복문이 멈춤
            volume += right_max - height[right]
            right -= 1
        else:
            volume += left_max - height[left]
            left += 1

    return volume

# 스택 쌓기
def trap3(self, height: List[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼낸다
            bottom = stack.pop()

            if not len(stack):
                break

            # 이전과의 차이만큼 물 높이 처리
            width = i - stack[-1] - 1
            vertical = min(height[i], height[stack[-1]]) - height[bottom]

            volume += width * vertical

        stack.append(i)
    return volume

