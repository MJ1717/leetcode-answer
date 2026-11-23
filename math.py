class Solution:
    def isPalindrome(self, x: int) -> bool:
        listt = list(str(x))

        left = 0
        right = len(listt) - 1

        while (left < right):
            if (listt[left] != listt[right]):
                return False

            left += 1
            right -= 1

        return True



class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result = 0

        for i in range(len(digits)):
            result += digits[i] * (10 ** (len(digits) - 1 - i))

        result += 1

        result = str(result)
        tmp = []
        for val in result:
            tmp.append(int(val))

        return tmp



class Solution:
    def mySqrt(self, x: int) -> int:
        
        left = 0
        right = x

        while (left <= right):

            mid = (left + right) // 2
            root = mid * mid

            if (root == x):
                return mid

            elif (root > x):
                right = mid - 1

            elif (root < x):
                left = mid + 1

        return right