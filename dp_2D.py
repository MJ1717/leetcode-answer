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

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [ [0] * (m + 1) for _ in range(n + 1) ]

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                # when we have same char, we get the each best
                # optimal solution from (one char back) each
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1

                # same as above, since we cannnot add one more, we
                # want to keep the best ideal solution for current ij.
                # and best ideal solution will be based on
                # which on is better? when we didnt see first text one less
                # or second text one less?
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                

        return dp[-1][-1]

        