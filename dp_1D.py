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



class Solution:
    def rob(self, nums: List[int]) -> int:

        # edge case
        if (len(nums) == 0):
            return 0
        if (len(nums) == 1):
            return nums[0]
        if (len(nums) == 2):
            return max(nums[0], nums[1])

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return max(dp[-1], dp[-2])      



class Solution:
    def numTilings(self, n: int) -> int:

        # edge case
        if (n == 1):
            return 1
        if (n == 2):
            return 2

        full = [0] * (n + 1)
        gap = [0] * (n + 1)

        gap[1] = 1
        gap[2] = 2

        full[1] = 1
        full[2] = 2

        for i in range(3, n+1):
            full[i] = full[i-1] + full[i-2] + (2 * gap[i-2])
            gap[i] = full[i-1] + gap[i-1]

        return full[n] % (10**9 + 7)


        
        
