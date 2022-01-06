import collections
import re
from typing import Deque

# 풀이1. 리스트로 변환
def isPalindrome(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():  # isalnum()은 영문자, 숫자 여부를 판별하는 함수
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop() != strs.pop(0):
            return False

    return True

# 풀이2. 데크 자료형을 이용한 최적화

def isPalindrome2(self, s:str) -> bool:
    # 자료형 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

# 풀이3. 슬라이싱 사용

def isPalindrome3(self, s:str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1] # 문자열 뒤집기

