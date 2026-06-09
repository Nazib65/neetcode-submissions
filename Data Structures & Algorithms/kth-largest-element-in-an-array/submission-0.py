class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap=[]

        for a in nums:
            heapq.heappush(minHeap, a)
            if len(minHeap)>k:
                heapq.heappop(minHeap)
        return minHeap[0]