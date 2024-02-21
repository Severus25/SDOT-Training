# Leetcode - 46
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        p = []
        v = [False] * len(nums)
        def backtrack():
            if len(p) == len(nums):
                ans.append(p[:])
                return
            for i in range(len(nums)):
                if not v[i]:
                    v[i] = True
                    p.append(nums[i])
                    backtrack()
                    v[i] = False
                    p.pop()
        backtrack()
        return ans
