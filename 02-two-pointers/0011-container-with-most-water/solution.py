class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        left = 0
        right = len(height) - 1

        res = 0

        while left < right:

            x_length = right - left
            y_length = min(height[left], height[right])

            res = max(res, x_length * y_length)

            if height[left] > height[right]:
                right -= 1

            else:
                left += 1
        
        return res
