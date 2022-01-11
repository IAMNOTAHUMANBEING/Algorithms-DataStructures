import sys

# 풀이1. 완전탐색 -> 시간초과

# 풀이2. 저점과 현재값과의 차이 계산
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        max = prices[0]
        result = 0

        for i in range(1, len(prices)-1):
            if min > prices[i]:
                max = prices[i]
                min = prices[i]
            elif max < prices[i]:
                max = prices[i]
                if result < (max - min):
                    result = max - min

        if max < prices[-1]:
            max = prices[-1]
            if result < (max - min):
                result = max - min

        return result

# 풀이3. 풀이2 개선
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        # 최솟값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(price, min_price)
            profit = max(profit, price - min_price)

        return profit