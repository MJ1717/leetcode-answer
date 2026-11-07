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


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort(key = lambda x : x[0])
        result = []
        result.append([intervals[0][0], intervals[0][1]])
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            current_start = intervals[i][0]
            current_end = intervals[i][1]

            if (current_start <= prev_end):
                longest = max(result[-1][1], current_end)
                result[-1][1] = longest
                prev_end = longest
            
            else:
                result.append([current_start, current_end])
                prev_end = current_end

        return result   



class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        new_start = newInterval[0]
        new_end = newInterval[1]

        result = []
        inserted = False

        for i in range(len(intervals)):

            start = intervals[i][0]
            end = intervals[i][1]

            if (end < new_start):
                result.append(intervals[i])

            elif (start > new_end):
                if (not inserted):
                    result.append([new_start, new_end])
                    inserted = True

                result.append(intervals[i])

            else:
                new_start = min(new_start, start)
                new_end = max(new_end, end)

        if (not inserted):
            result.append([new_start, new_end])

        return result