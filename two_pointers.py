class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        current_index = 0
        last_index = len(nums) - 1

        while (current_index <= last_index):
            if (nums[current_index] == 0):
                for i in range(current_index, last_index, 1):
                    current_val = nums[i]
                    next_val = nums[i+1]

                    # swap
                    nums[i] = next_val
                    nums[i+1] = current_val

                last_index -= 1

            else:

                current_index += 1


    def moveZeroes(nums):
        slow = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[slow], nums[i] = nums[i], nums[slow]
                slow += 1        


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # edge case
        if (len(s) == 0):
            return True
        
        s_index = 0
        tmp_str = ""

        for i, val in enumerate(t):
            if (val == s[s_index]):
                # dont want to go out of bound
                if (s_index < len(s) - 1):
                    s_index += 1
                
                tmp_str += val

        return s == tmp_str         


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_vol = 0
        left_pointer = 0
        right_pointer = len(height) - 1

        while (left_pointer < right_pointer):
            length = right_pointer - left_pointer
            heightt = min(height[left_pointer], height[right_pointer])
            current_volume = length * heightt    

            if (current_volume > max_vol):
                max_vol = current_volume

            if (height[left_pointer] < height[right_pointer]):
                left_pointer += 1
            else:
                right_pointer -= 1     

        return max_vol           


class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        sorted_array = sorted(nums)
        left_pointer = 0
        right_pointer = len(sorted_array) - 1
        output = 0

        while (left_pointer < right_pointer):
            sum = sorted_array[left_pointer] + sorted_array[right_pointer]
            if (sum == k):
                output += 1
                left_pointer += 1
                right_pointer -= 1

            else:
                if (sum > k):
                    right_pointer -= 1
                else:
                    left_pointer += 1

        return output         





