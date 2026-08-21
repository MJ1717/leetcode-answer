class Solution:
    def tribonacci(self, n: int) -> int:
        
        # edge case
        if (n == 0):
            return 0
        if (n == 1):
            return 1
        if (n == 2):
            return 1

        current = 0
        last_1 = 1
        last_2 = 1
        last_3 = 0

        count = 0

        while (count <= n - 3):
            current = last_3 + last_2 + last_1

            #for next iteration
            last_3, last_2, last_1 = last_2, last_1, current
            count += 1

        return current


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
  
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        return min(dp[len(cost) - 1], dp[len(cost) - 2])