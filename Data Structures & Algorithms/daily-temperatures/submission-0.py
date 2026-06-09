class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        ans=[0]* len(temperatures)

        for i, a in enumerate(temperatures):
            while stack and a>temperatures[stack[-1]]:
                prevIdx=stack.pop()
                ans[prevIdx]=i-prevIdx
            stack.append(i) 
        return ans 
