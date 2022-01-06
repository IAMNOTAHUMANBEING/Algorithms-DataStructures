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

def isPalindrome(self, s:str) -> bool:

