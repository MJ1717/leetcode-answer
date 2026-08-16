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

      