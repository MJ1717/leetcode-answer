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