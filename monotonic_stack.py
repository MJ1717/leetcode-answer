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

            

        