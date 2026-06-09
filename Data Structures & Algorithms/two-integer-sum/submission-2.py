class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={}; #val->index

        for i in range(len(nums)):
            n=nums[i]
            diff=target-n
            if diff in prevMap:
                return[prevMap[diff], i]
            prevMap[n]=i