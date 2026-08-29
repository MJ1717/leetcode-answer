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


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        hold = [0] * len(prices)
        cash = [0] * len(prices)
        hold[0] = - prices[0]

        for i in range(1, len(prices)):
            hold[i] = max(hold[i-1], cash[i-1] - prices[i])
            cash[i] = max(cash[i-1], hold[i-1] + prices[i] - fee)

        return cash[-1]


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # word1 -> empty string
        for i in range(n + 1):
            dp[i][0] = i

        # empty string -> word2
        for j in range(m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                # same character
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                # different character
                else:
                    delete = dp[i - 1][j]
                    insert = dp[i][j - 1]
                    replace = dp[i - 1][j - 1]

                    dp[i][j] = 1 + min(delete, insert, replace)

        return dp[n][m]

