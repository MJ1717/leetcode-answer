class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        result = []
        star = 0

        for i in range(len(s) - 1, -1, -1):
            if (s[i] == "*"):
                star += 1
            else:
                if (star == 0):
                    result += s[i]
                else:
                    star -= 1

        return "".join(reversed(result))

        