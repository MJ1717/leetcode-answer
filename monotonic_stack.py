class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures) -1, -1, -1):
            current_temperature = temperatures[i]

            # while stack is not empty, and not satisfying the condition
            while (stack and current_temperature >= stack[-1][0]):
                stack.pop()

            # here it is either, stack is empty or satisfying the condition
            if (len(stack) != 0):
                result[i] = stack[-1][1] - i

            stack.append([current_temperature, i])

        return result



class StockSpanner:

    def __init__(self):
        self.stack = []
        self.day = 0
        

    def next(self, price: int) -> int:
        self.day += 1

        while (self.stack and price >= self.stack[-1][0]):
            self.stack.pop()
        
        # if stack is empty
        if (not self.stack):
            span = self.day
    
        # there is element
        else:
            last_day = self.stack[-1][1]
            span = self.day - last_day

        self.stack.append([price, self.day])

        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
            

        