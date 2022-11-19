"""
알고리즘 성능 평가
시간 제한 1초를 기준으로
N의  범위가 500 : O(N^3)
N의  범위가 2000 : O(N^2) -> 이중 반복문이라고 무조건 N^2 아니고 내부에 추가되는 요소가 없는지 확인해야함
N의  범위가 100,000 : O(NlogN)
N의  범위가 10,000,000 : O(N)
"""

# 수 자료형
# 정수형(양,음,0)
a = 1000
print(a)

# 실수형
a = 1000.
print(a)

# 지수 표현 방식(E=10의 지수부)
a = 72.3e2
print(a)
print(int(a))

# 계산 오차
a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

print(round(a, 4))

if round(a, 4) == 0.9:
    print(True)
else:
    print(False)

# 연산자
# 나누기(/) 사용 시 실수형으로 반환
# %(나머지), //(몫), **(거듭제곱)

# 리스트 자료형 []
n = 10
a = [0] * n
a[3] = 1
print(a)

# 슬라이싱
# 끝 인덱스를 실제 인덱스보다 1을 더 크게 설정
print(a[2:4])

# 리스트 컴프리헨션
a = [i * i for i in range(10) if i % 2 == 1]
print(a)

m = 4
n = 3
a = [[0] * m for _ in range(n)]
print(a)
a[1][1] = 3
print(a)

a = [[0] * m] * n
a[1][1] = 3
print(a)

# 리스트 함수
"""
append 1
sort NlogN
reverse N
insert N
count N
remove N
"""
a = [1, 3, 2]
a.append(2)
print("삽입 : ", a)
a.sort()
print("오름차 정렬 : ", a)
a.sort(reverse=True)
print("내림차 정렬 : ", a)
a.reverse()
print("뒤집기 : ", a)
a.insert(2, 3)
print("인덱스 2에 3 추가 : ", a)
print("3 개수 세기 : ", a.count(3))
a.remove(2)
print("2 하나만 삭제 : ", a)

# 모두 제거
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]
print(result)

# 문자열 자료형
# \ 사용하면 따옴표 안에 따옴표 사용가능
data = "Don't you know \"이코테(파이썬)\"?"
print(data)

# 문자열 연산
a = "abc"
print(a[0:2] * 3)

# 튜플 자료형 ()
# 한번 선언된 값 변경 불가
# 서로 다른 성질 데이터 묶어서 관리할 때 사용
# 해싱의 키 값으로 사용
# 리스트보다 메모리를 효율적으로 사용해야할 때 사용

# 사전 자료형
# 순차적이지 않고 key와 value의 쌍을 데이터로 가짐
# 변경 불가능한 자료형을 키로 사용할 수 있음
# 해시 테이블을 이용하므로 데이터 조회 및 수정이 O(1) 시간 소요
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
print(data)

print(data.keys())
print(list(data.values()))

for key in data.keys():
    print(data[key])

# 집합 자료형
# 중복과 순서를 허용하지 않음
# 데이터의 조회 및 수정 O(1) 시간 소요
data = set([1, 2, 1, 2, 3, 4, 4, 5])
print(data)

# 집합 자료형 연산
data2 = set([2, 4])
print(data | data2)  # 합
print(data & data2)  # 교
print(data - data2)  # 차

# 집합 자료형 함수
data = set([1, 2, 3])
print(data)
data.add(4)
data.update([5, 6])
data.remove(3)

# 기본 입출력
# input() 한 줄의 문자열을 입력 받는 함수
# map() 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용

data = list(map(int, input().split()))  # 공백을 기준으로 구분된 데이터를 입력받을 때
# a, b, c = map(int, input().split())
print(data)

# 빠르게 입력 받기
# sys.stdin.readline() 메서드 사용, 엔터도 입력되므로 rstrip() 메서드 함께 사용
import sys

data = sys.stdin.readline().rstrip()
print(data)

# 표준 출력 방법
# , 로 여러 변수 출력 가능
# 줄바꿈을 원치 않을 경우 end 속성 이용
a = 1
b = 2
print(a, b)
print(7, end=" ")
print(8, end=" ")

answer = 7
print("정답은 " + str(7) + "입니다.")

# f-string
print(f"정답은 {answer}입니다.")

# 조건문
# 들여쓰기로 구분
a = 5
if a >= 0:
    print("1")
elif a >= -10:
    print("2")
else:
    print("3")

# 조건문 간소화
score = 84
result = "Success" if score >= 80 else "Fail"
print(result)

# 반복문
# while, for
result = 0

for i in range(1, 10):  # continue를 이용한 1~9까지 홀수 합
    if i % 2 == 0:
        continue
    result += i

print(result)

# 함수
# 전역변수를 함수 내에서 사용하려면 global 붙여야하고 list는 안붙여도 됨
# 여러개의 return을 갖고 assign 해줄 수 있음

# 람다 표현식
print((lambda a, b: a + b)(3, 7))

# ex.1
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))

# ex.2
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a+b, list1, list2)
print(list(result))     # result는 map object라서 list 변환 필요

# 실전에서 유용한 표준 라이브러리
# 내장함수: sum, min, max, eval, sorted
# itertools: 반복되는 형태의 데이터 처리에 사용 ex.순열과 조합
# heapq: heap 자료구조를 제공
# bisect: binary search 기능을 제공
# collections: deque, counter 등 유용한 자료구조를 포함
# math: 수학적 기능 제공 ex. 팩토리얼, 제곱근, 최대공약수, 삼각함수, pi 등

# itertools
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)

from itertools import product
result = list(product(data, repeat=2))
print(result)

from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data, 2))

# counter
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) # 'blue'가 등장한 횟수 출력
print(counter['green']) # 'green'가 등장한 횟수 출력
print(dict(counter)) # 사전 자료형으로 반환

# 최소 공약수와 최소 공배수
import math

# 최소 공배수를 구하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

a = 21
b = 14

print(math.gcd(21, 14)) # 최대 공약수
print(lcm(21, 14)) # 최소 공배수