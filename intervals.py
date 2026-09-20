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


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key = lambda i : i[0])

        merge_count = 1
        prev = points[0][1]

        for i in range(1, len(points)):
            start, end = points[i]

            if (start <= prev):
                prev = min(prev, end)

            else:
                prev = end
                merge_count += 1

        return merge_count


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:

        if (len(nums) == 0):
            return []

        tmp = [[nums[0]]]
        prev = nums[0]

        for i in range(1, len(nums)):
            val = nums[i]

            if (val == (prev + 1)):
                tmp[-1].append(val)
            else:
                tmp.append([val])

            prev = val

        result = []

        for i in range(len(tmp)):
            if (len(tmp[i]) != 1):
                first_element = tmp[i][0]
                last_element = tmp[i][-1]

                string = str(first_element) + "->" + str(last_element)
                result.append(string)

            else:
                first_element = tmp[i][0]
                string = str(first_element)

                result.append(string)

        return result


            
        