# 풀이1. 스택일치 여부 판별
class Solution:
    def isValid(self, s: str) -> bool:
        ans_list = { ')' : '(', '}' : '{', ']' : '[' }
        stack = []

        # 스택 이용 예외처리 및 일치 여부 판별
        for char in s:
            if char not in ans_list:
                stack.append(char)
            elif not stack or ans_list[char] != stack.pop():    # 짝 지을 것이 없는데(stack이 비었는데) ans_list의 값이 나온 경우 + 짝이 안맞는 경우
                return False

        return len(stack) == 0  # stack에 저장된 값들이 모두 짝지어지지 않고 문자열이 끝날 수 있으므로