class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums.sort()
        n = len(nums)

        left = 0
        right = n - 1
        res = 0

        while left < right:

            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                res += 1
            
            elif nums[left] + nums[right] <= k:
                left += 1
            
            else:
                right -= 1
        
        return res
