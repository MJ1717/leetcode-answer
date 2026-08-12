import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)

        for i in range(k):
            if (i == k - 1):
                return heapq.heappop_max(nums)

            heapq.heappop_max(nums)


import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1
        self.heap = []
        

    def popSmallest(self) -> int:
        if (len(self.heap) != 0):
            return heapq.heappop(self.heap)
        
        else:
            res = self.current
            self.current += 1
            return res
        

    def addBack(self, num: int) -> None:
        if (num < self.current):
            if (num not in self.heap):
                heapq.heappush(self.heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)



import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        pairs = []
        for i in range(len(nums1)):
            pairs.append([nums1[i], nums2[i]])

        def get_second_element(x):
            return x[1]

        pairs.sort(key = get_second_element, reverse = True)

        current_sum = 0
        heap = []

        for i in range(k):
            current_sum += pairs[i][0]
            heapq.heappush(heap, pairs[i][0])

        maxx = current_sum * pairs[k-1][1]

        right = k

        while (right < len(pairs)):
            right_nums1 = pairs[right][0]
            right_nums2 = pairs[right][1]

            prev_smallest = heapq.heappop(heap)

            heapq.heappush(heap, right_nums1)
            current_sum = current_sum - prev_smallest + right_nums1

            maxx = max(maxx, current_sum * right_nums2)

            right += 1

        return maxx

