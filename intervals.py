class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda i : i[0])

        dp = [0] * len(intervals)

        dp[0] = 0
        prev = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if (start < prev):
                prev = min(prev, end)
                dp[i] = dp[i - 1] + 1
            else:
                prev = end
                dp[i] = dp[i - 1]

        return dp[-1]


        