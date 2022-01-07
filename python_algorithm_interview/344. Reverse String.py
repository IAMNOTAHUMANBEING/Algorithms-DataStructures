# 투 포인터를 이용한 스왑

def reverseString(self, s:List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# 파이썬다운 방식

def reverseString2(self, s:List[str]) -> None:
    s.reverse()
    # reverse는 리스트에만 제공되기 때문에 문자열인 경우 슬라이싱을 이용
    # 그러나 이 문제는 공간복잡도가 O(1)로 제한 되기 때문에 s = s[::-1]가 안됨
    # s[:] = s[::-1]을 이용해서 연산 전의 주소를 그대로 사용해야함

