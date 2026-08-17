# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n

        while (True):
            mid = (left + right) // 2

            if (guess(mid) == 0):
                return mid

            elif (guess(mid) == 1):
                left = mid + 1

            else:
                right = mid - 1


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        sorted_potions = sorted(potions)
        result = []

        for i in range(len(spells)):
            left = 0
            right = len(potions) - 1
            
            spell_val = spells[i]

            while (left <= right):
                mid = (left + right) // 2
                mid_value = sorted_potions[mid] * spell_val

                if (mid_value >= success):
                    right = mid - 1
                else:
                    left = mid + 1
            
            result.append(len(sorted_potions) - left)

        return result


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        # edge case
        if (len(nums) == 1):
            return left
        if (nums[left] > nums[left + 1]):
            return left
        if (nums[right] > nums[right - 1]):
            return right

        while (left <= right):
            # base case
            if (left == right):
                return left

            # recursive case
            mid = (left + right) // 2
            mid_value = nums[mid]

            # if left is greater, meaning that there is local max on left
            if (mid - 1 >= 0):
                if (nums[mid - 1] > mid_value):
                    right = mid - 1
                    continue

            # if right is greater, meaning that there is local max on right
            if (mid + 1 <= len(nums) - 1):
                if (nums[mid + 1] > mid_value):
                    left = mid + 1
                    continue

            # when nothing is satisfied, current is max
            return mid

      