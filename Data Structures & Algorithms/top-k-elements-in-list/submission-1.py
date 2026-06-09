class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        mostCom=count.most_common(k)
        res=[]
        for num, cnt in mostCom:
            res.append(num)
        return res
