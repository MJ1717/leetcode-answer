class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        maxx = 0
        last_altitude = 0

        for i, val in enumerate(gain):
            last_altitude += val
            maxx = max(maxx, last_altitude)

        return maxx    

        
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum = [0] * len(nums)
        right_sum = [0] * len(nums)
        pivot_index = -1

        for i in range(len(nums)):
            if (i == 0):
                left_sum[i] = 0
            else:
                left_sum[i] = left_sum[i-1] + nums[i - 1]

        for i in range(len(nums) - 1, -1, -1):
            if (i == len(nums) - 1):
                right_sum[i] = 0
            else:
                right_sum[i] = right_sum[i+1] + nums[i + 1]

        for i in range(len(left_sum)):
            if (left_sum[i] == right_sum[i]):
                pivot_index = i
                return pivot_index

        return pivot_index       
