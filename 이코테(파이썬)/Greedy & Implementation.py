# 그리디 알고리즘
# 현재 상황에서 지금 당장 좋은 것만 고르는 방법
# 단순히 가장 좋아보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는지 정당성을 검토가 중요

# <문제> 거스름 돈
n = 1260
count = 0

array = [500, 100, 50, 10]  # 큰 단위 화폐부터 차례대로 확인

for coin in array:
    count += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)

# 시간 복잡도: O(화폐의 종류), 금액과 무관

# <1이 될 때까지>

N, K = map(int, input().split()) # 입력값 int로 바꾸는 방법
count = 0

# while True:
#     if N % K == 0 and K != 1:
#         if N == 1:
#             break
#         N = N / K
#         count = count + 1
#     else:
#         if N == 1:
#             break
#         N = N - 1
#         count = count + 1
# 
# print(count)

# 한번 반복할 때 나누기와 빼기 동시에 수행하는 빠른 풀이
while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (N // K) * K   # 뺴서 나누어질 수 있는 수 찾는 테크닉
    count += N - target
    N = target
    if N < K:   # 더이상 나눌 수 없음
        break
    count += 1
    N //= K

count += N-1
print(count)

# <문제> 곱하기 혹은 더하기

S = input()
result = int(S[0])
for i in S[1:]:
    if result * int(i) > result + int(i):
        result = result * int(i)
    else:
        result = result + int(i)

print(result)

# <문제> 모험가 길드
count = 0

h = list(map(int, input().split()))
h.sort()
num = 0

for i in h:
    num += 1
    if i <= num:
        count += 1
        num = 0

print(count)

# 구현: 시뮬레이션과 완전탐색
# 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정 -> 풀이를 떠올리기는 쉽지만 소스코드로 옮기기 어려운 문제를 지칭
# 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제
# 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
# 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
# 적잘한 라이브러리를 찾아서 사용해야 하는 문제

# 2차원 공간은 행렬과 방향벡터를 이용함

# <문제> 상하좌우
n = int(input())
order = input().split()
loc_x = 1
loc_y = 1
temp_x = 0
temp_y = 0

for i in order:
    temp_x = loc_x
    temp_y = loc_y
    if i == 'L':
        loc_y -= 1
    elif i == 'R':
        loc_y += 1
    elif i == 'U':
        loc_x -= 1
    else:
        loc_x += 1
    if loc_x > n or loc_y > n or loc_x < 1 or loc_y < 1:
        loc_x = temp_x
        loc_y = temp_y

print(loc_x, loc_y)

# 다른 풀이
# 필요한 요소들을 리스트로 만들어두고 상황마다 불러와서 사용하는 방법, 확장성 더 좋음.
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:    # for 안에서 초기화한 변수 밖에서 참조 가능
        continue
    x, y = nx, ny

print(x, y)

# <문제> 시각

n = int(input())
count1 = 0
count2 = 0
result = 0

for i in range(60):
    if '3' in str(i): count1 += 1

for i in range(60):
    if '3' in str(i):
        count2 += 60
    else:
        count2 += count1

for i in range(n+1):
    if '3' in str(i) :
        result += 3600
    else:
        result += count2

print(result)

# 다른 풀이

h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)

# <문제> 왕실의 나이트
loc = input()
x = ord(loc[0]) - 96  # ord: 아스키 코드를 int로 바꾸는 함수
y = int(loc[1])
count = 0
dx = [2, 2, -2, -2, -1, 1, -1, 1]
dy = [-1, 1, -1, 1, 2, 2, -2, -2]

for i in range(8):
    nx = x + dx[i]  # x, y를 사용하면 반복문이 돌면서 자리를 이동하게 됨
    ny = y + dy[i]
    if nx > 8 or ny > 8 or nx < 1 or ny < 1:
        continue
    count += 1

print(count)

# <문제> 문자열 재정렬

s = input()
result = ""
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
s_int = 0
s_chr = []

for i in s:
    if i in num:
        s_int += int(i)
    else:
        s_chr.append(i)

s_chr.sort()

for i in s_chr:
    result += i

if s_int != 0:
    result += (str(s_int))

print(result)

# 다른 풀이

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():     # 알파벳인지 확인하는 함수 존재
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:      # 0일 때 고려 안해주면 숫자 없을 경우 문자열 뒤에 0이 붙게 됨
    result.append(str(value))

print(''.join(result))  # 리스트 요소를 문자열로 출력하는 방법

