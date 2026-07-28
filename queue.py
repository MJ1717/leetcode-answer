from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.queue = deque()
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)
        
        while (self.queue and (self.queue[0] < t - 3000)):
            self.queue.popleft()
        
        return len(self.queue)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)



from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
      

        num_r = 0
        num_d = 0

        ban_r = 0
        ban_d = 0

        queue = deque(senate)
        win = ""

        for s in senate:
            if (s == "R"):
                num_r += 1
            else:
                num_d += 1

        while (queue):
            current = queue.popleft()

            if (current == "R"):
                # when D already banned this
                if (ban_r >= 1):
                    num_r -= 1
                    ban_r -= 1
                else:
                    # check if R can win
                    if (num_d == 0):
                        win = "Radiant"
                        break
                    # cant win so need to ban, and go back to queue
                    else:
                        ban_d += 1
                        queue.append(current)

            if (current == "D"):
                # when R already banned this
                if (ban_d >= 1):
                    num_d -= 1
                    ban_d -= 1
                else:
                    # check if D can win
                    if (num_r == 0):
                        win = "Dire"
                        break
                    # cant win so need to ban, and go back to queue
                    else:
                        ban_r += 1
                        queue.append(current)

        return win

            



        