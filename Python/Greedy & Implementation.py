import time
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

n = input()
h = list(map(int, input().split()))
h.reverse()
# 1 1 2 2 3

for
print(count)