from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        def rangeRob(nums,start,end):
            if start == end:
                return nums[start]
            
            dp = [0] * len(nums)
            
            dp[start] = nums[start]
            dp[start + 1] = max(nums[start],nums[start + 1])
            
            for i in range(start + 2,end + 1):
                dp[i]  = max(dp[i - 1],dp[i - 2] + nums[i])

            return dp[end]

        res1 = rangeRob(nums,0,n-2)
        res2 = rangeRob(nums,1,n-1)

        return max(res1,res2)