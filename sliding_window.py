class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        current = sum(nums[:k])
        max_val = current

        for i in range(k, len(nums), 1):
            current = current + nums[i] - nums[i - k]
            max_val = max(current, max_val)

        return max_val / float(k)    


class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
    
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_array = []
        current = 0
        maxx = 0

        # make 1 0, vowel array
        for i, val in enumerate(s):
            if (val in vowels):
                vowel_array += [1]
            else:
                vowel_array += [0]

        current = sum(vowel_array[:k])
        maxx = current

        for i in range(k, len(vowel_array), 1):
            current = current + vowel_array[i] - vowel_array[i-k]
            maxx = max(maxx, current)

        return maxx     


class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        left = 0
        right = 0
        zero = k
        current = 0
        maxx = 0

        while (right < len(nums)):
            
            # when i is 0
            if (nums[right] == 0):

                # when we have more zero
                if (zero > 0):
                    zero -= 1
                    current += 1
                    maxx = max(current, maxx)
                    right += 1

                # when there is no more zero
                else:
                    if (nums[left] == 0):
                        zero += 1
                    
                    current -= 1
                    left += 1

            # when i is 1
            else:
                current += 1
                maxx = max(current, maxx)            
                right += 1


        return maxx        


class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """


        left = 0
        zero = 0
        maxx = 0

        for right in range(len(nums)):
            
            # when right is 0
            if (nums[right] == 0):
                zero += 1

            # check if we exceed 1 zero in the sub array
            while (zero > 1):
                if (nums[left] == 0):
                    zero -= 1
                left += 1

            # here, we only have 1 zero
            maxx = max(maxx, right - left)

        return maxx





        
   


        
     











