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
        # 스택에 값이 있는 상태에서 높이가 이전보다 높아지는 경우 반복하여 이전 위치 탐색
        while stack and height[i] > height[stack[-1]]:
            # 이전 높이 꺼내기(조희가 아니라 꺼내는 이유: 변곡점을 만나면 스택에 저장된 이전 위치들을 탐색하며 처리 가능한 물 처리하고 지금 층에서 불가능한 위치들은 남겨둠)
            bottom = stack.pop()
            
            # 좌측에서 물을 막아줄 칸이 없는 경우 
            if not len(stack):
                break

            # 이전과의 차이만큼 물 처리
            width = i - stack[-1] - 1
            vertical = min(height[i], height[stack[-1]]) - height[bottom] # 물을 가두는 두 기둥 중 낮은 기둥만큼 물이 차니까

            volume += width * vertical
            
        stack.append(i)
    return volume

