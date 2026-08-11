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