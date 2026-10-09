class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        
        nums.sort()
        n = len(nums)
        left = 0
        right = n - 1

        res = 0

        while left < right:

            res += nums[right] - nums[left]
            left += 1
            right -= 1
        
        return res
