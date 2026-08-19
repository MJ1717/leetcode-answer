class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        array = [[0], [0], ['a','b','c'], ['d','e','f'], ['g','h','i'], ['j','k','l'], ['m','n','o'], ['p','q','r','s'], ['t','u','v'], ['w','x','y','z']]

        def backtrack(index, path):
            # base case
            if (len(path) == len(digits)):
                s = "".join(path[:])
                result.append(s)
                return

            for letter in digits_array[index]:
                path.append(letter)

                backtrack(index + 1, path)

                path.pop()

        digits_array = []
        result = []

        for val in digits:
            int_num = int(val)
            digits_array.append(array[int_num])

        backtrack(0, [])

        return result



class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]: 
        array = [0,1,2,3,4,5,6,7,8,9]
        result = []

        def backtrack(index, path):
            #base case
            if (len(path) == k):
                if (sum(path) == n):
                    result.append(path[:])
                return
            if (index >= len(array)):
                return

            #include this index number
            path.append(array[index])
            backtrack(index + 1, path)

            path.pop()

            #not include this number
            backtrack(index + 1, path)

        backtrack(1, [])
        return result