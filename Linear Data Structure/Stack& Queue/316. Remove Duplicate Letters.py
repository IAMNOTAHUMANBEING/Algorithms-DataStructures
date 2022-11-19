# 풀이1. 재귀를 이용한 풀이
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 집합으로 알파벳 순 정렬
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            # 전체 집합과 접미사 집합이 일치할 때 분리 진행
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))

        return '' # 빈 문자열인 경우

# 풀이2. 스택을 이용한 문자 제거
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, stack = collections.Counter(s), []

        for char in s:
            counter[char] -= 1
            if char in stack:   # 원칙적으론 스택은 검색기능이 없음
                continue
            # 이전 문자보다 앞선 문자이고 뒤에 붙일 문자가 남아있다면 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(char)

        return ''.join(stack)

