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
        