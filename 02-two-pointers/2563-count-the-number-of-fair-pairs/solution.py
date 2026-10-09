class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        n = len(nums)
        nums.sort()

        def count_less_than(target: int) -> int :

            left = 0
            right = n - 1

            res = 0

            while left < right:

                if nums[left] + nums[right] < target:

                    res += (right - left)
                    left += 1
                
                else:
                    right -= 1
                
            return res
        
        return count_less_than(upper + 1) - count_less_than(lower)
