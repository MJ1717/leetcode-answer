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


from collections import deque

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """

        def is_collision(old, new):
            if (new * old > 0):
                return False
            if (old < 0 and new > 0):
                return False
            if (old > 0 and new < 0):
                return True

        result = []

        for i in range(len(asteroids)):
            current = asteroids[i]

            if (len(result) == 0):
                result.append(current)
                continue

            result.append(current)

            new = result[len(result) - 1]
            old = result[len(result) - 2]
            while (is_collision(old, new)):
                if (abs(new) > abs(old)):
                    result.pop()
                    result.pop()
                    result.append(new)
                elif (abs(new) < abs(old)):
                    result.pop()
                    break
                else:
                    result.pop()
                    result.pop()
                    break
                new = result[len(result) - 1]
                old = result[len(result) - 2]

        return result





            


        