class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return ''.join(result)
    

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
      


        def is_multiple_of(x, long_string):
            if len(long_string) % len(x) != 0:
                return False

            times = len(long_string) // len(x)
            tmp = ""

            for i in range(times):
                tmp += x

            return tmp == long_string    



        if len(str1) >= len(str2):
            minimum_length = len(str2)
            minimum_str = str2
        else:
            minimum_length = len(str1)
            minimum_str = str1
        

        result = ""
        
        for i in range(1, minimum_length + 1):
            

            test = minimum_str[0:i]
            if (is_multiple_of(test, str1) and is_multiple_of(test,str2)):
                result = test

        return result

       
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        # find max num of candies
        max_candy = 0
        for candy in candies:
            if (candy >= max_candy):
                max_candy = candy

        list_length = len(candies)
        result = [0] * list_length

        # go thru the loop, and check condition
        for i, candy in enumerate(candies): #enumerate returns (index, value)
            if (candy + extraCandies >= max_candy):
                result[i] = True
            else:
                result[i] = False    

        return result        


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        def adjacent_empty(i, flowerbed):
            left_i = i-1
            right_i = i+1

            # when we can plant it
            if (flowerbed[i] == 0):
                if (left_i == -1):
                    # when flowerbed size is only 1
                    if (len(flowerbed) == 1):
                        return flowerbed[i] == 0
                        
                    return flowerbed[right_i] == 0

                elif (right_i == len(flowerbed)):
                    return flowerbed[left_i] == 0

                else:
                    return flowerbed[left_i] == 0 and flowerbed[right_i] == 0


            # when we cannot plan it
            else:
                return False        


        for i in range(len(flowerbed)):
            if (n == 0):
                break

            else:
                if (adjacent_empty(i, flowerbed)):
                    flowerbed[i] = 1
                    n -= 1

        return n == 0    


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

        s_to_list = list(s)

        tmp_letter = []
        tmp_index = []

        # traverse the list and get the vowels
        for i, val in enumerate(s_to_list):
            if (val in vowels):
                tmp_letter += [val]
                tmp_index += [i]

        # traverse the reverse tmp_letter and add back
        tmp_letter.reverse()
        for i in range(len(tmp_index)):
            s_to_list[tmp_index[i]] = tmp_letter[i]


        # convert list into string
        return "".join(s_to_list)        


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        # split and make into list
        split_s = s.split()
        list_s = list(split_s)

        result = []

        # traverse the list in reverse
        for i in range(len(list_s) - 1, -1, -1):
            result += [list_s[i]]

        # make into string then return
        return " ".join(result)


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # prefix array
        prefix_array = [0] * len(nums)
        for i in range(len(prefix_array)):
            if (i == 0):
                prefix_array[i] = 1
            else:
                prefix_array[i] = nums[i-1] * prefix_array[i-1]

        # suffix array
        suffix_array = [0] * len(nums)
        for i in range(len(suffix_array) - 1, -1, -1):
            if (i == len(suffix_array) - 1):
                suffix_array[i] = 1
            else:
                suffix_array[i] = nums[i+1] * suffix_array[i+1] 

        # update nums array
        for i in range(len(nums)):
            nums[i] = prefix_array[i] * suffix_array[i]

        return nums     

   
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        first = float('inf')
        second = float('inf')

        for i, val in enumerate(nums):
            if (val < first):
                first = val

            if (val < second and val > first):
                second = val

            if (val > second):
                return True

        return False


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        letter_array = []
        index_array = []

        current = "test"

        for i, val in enumerate(chars):
            if (current != val):
                current = val

                # update tmp arrays
                letter_array += [val]
                index_array += [i]

        result = ""
        for i in range(len(letter_array)):
            # add letter
            result += letter_array[i]

            # add number
            if (i == len(index_array) - 1):
                count_number = len(chars) - index_array[i]
            else:
                count_number = index_array[i+1] - index_array[i]

            if (count_number != 1):
                result += str(count_number)

        for i in range(len(result)):
            chars[i] = result[i]

        return len(result)      

      

       

        

    