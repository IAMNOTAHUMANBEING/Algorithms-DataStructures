# 풀이1. 스택 값 비교
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]]< temperatures[i]:
                last = stack.pop()
                result[last] = i - last
            stack.append(i)
        return result