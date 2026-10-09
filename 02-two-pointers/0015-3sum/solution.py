class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        n = len(nums)

        nums.sort()

        res = set()

        for i in range(n):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            first = nums[i]

            left = i + 1
            right = n - 1

            while left < right:

                second = nums[left]
                third = nums[right]

                if first + second + third == 0:
                    res.add((first, second, third))
                    right -= 1
                    left += 1
                
                elif first + second + third <= 0:
                    left += 1
                
                else:
                    right -= 1
            

        return [list(triplet) for triplet in res]
                
