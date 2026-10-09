class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        
        n = len(nums)
        nums.sort()

        res = set()

        for i in range(n):
            for j in range(i+1, n):

                # if nums[j] == nums[j-1]:
                #     continue
                left = j + 1
                right = n - 1

                while left < right:

                    if nums[left] + nums[right] + nums[i] + nums[j] == target:
                        res.add((nums[i], nums[j],nums[left], nums[right]))
                        left += 1
                        right -= 1
                    
                    elif nums[left] + nums[right] + nums[i] + nums[j] < target:
                        left += 1
                    
                    else:
                        right -= 1
        
        return [list(quadruplets) for quadruplets in res]
