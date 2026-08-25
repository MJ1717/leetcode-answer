class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [ [0] * n for _ in range(m) ]

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                
                # very top, all start with 1
                if (i == 0):
                    dp[i][j] = 1
                    continue

                # very left, all start with 1
                if (j == 0):
                    dp[i][j] = 1
                    continue

                # else case
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]

