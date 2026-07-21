class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        first_set = set(nums1) - set(nums2)
        second_set = set(nums2) - set(nums1)

        return [list(first_set), list(second_set)]                


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        d = {}

        for i, val in enumerate(arr):
            if (val in d):
                d[val] += 1
            else:
                d[val] = 1 

        d_val_array = list(d.values())

        return len(d_val_array) == len(set(d_val_array))        


class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        # set diff
        if (set(word1) != set(word2)):
            return False

        # get occurence dict
        x_dict = {}
        y_dict = {}

        for i, val in enumerate(word1):
            if (val in x_dict.keys()):
                x_dict[val] += 1
            else:
                x_dict[val] = 1

        for i, val in enumerate(word2):
            if (val in y_dict.keys()):
                y_dict[val] += 1
            else:
                y_dict[val] = 1
                
        # values occurences diff
        if (sorted(x_dict.values()) != sorted(y_dict.values())):
            return False

        # everything satisfy
        return True    


class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # make dict with grid
        d = {}
        tmp_array = []
        for i in range(len(grid)):
            tuple_tmp_array = tuple(grid[i])
            
            if (tuple_tmp_array in d.keys()):
                d[tuple_tmp_array] += 1
            else:
                d[tuple_tmp_array] = 1

        # access to each col, and add count
        i = 0
        tmp_array = []
        count = 0
        for col_index in range(len(grid)):
            while (i < len(grid)):
                tmp_array += [grid[i][col_index]]
                i += 1
            
            # col array is ready
            tuple_tmp_array = tuple(tmp_array)
            if (tuple_tmp_array in d.keys()):
                count += d[tuple_tmp_array]

            i = 0
            tmp_array = []
        
        return count

        






        