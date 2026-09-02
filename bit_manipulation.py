class Solution:
    def countBits(self, n: int) -> List[int]:

        result = [0] * (n+1)
        for i in range(1, n+1):
            result[i] = result[i // 2] + (i % 2)

        return result


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        result = 0

        for val in nums:
            result = result ^ val

        return result
            

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:

        def put_zero(string, num):
            current_len = len(string)

            while (current_len < num):
                string = "0" + string
                current_len += 1

            return string

        a_bin = bin(a)[2:]
        b_bin = bin(b)[2:]
        c_bin = bin(c)[2:]

        max_length = max(len(a_bin), len(b_bin), len(c_bin))

        a_bin = put_zero(a_bin, max_length)
        b_bin = put_zero(b_bin, max_length)
        c_bin = put_zero(c_bin, max_length)

        count = 0

        for i in range(len(a_bin)):
            if (c_bin[i] == '1'):
                if (a_bin[i] != '1' and b_bin[i] != '1'):
                    count += 1
            
            elif (c_bin[i] == '0'):
                if (a_bin[i] == '1'):
                    count += 1
                if (b_bin[i] == '1'):
                    count += 1

        return count
            

        