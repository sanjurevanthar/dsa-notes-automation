class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n = len(nums)

        nums.sort()

        closest_sum = float(inf)

        for i in range(n):

            left = i + 1
            right = n-1

            while left < right:

                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == target:

                    return target
                
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                #updating index
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum
                
