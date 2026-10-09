class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        
        people.sort()
        n = len(people)

        left = 0
        right = n - 1
        res = 0

        while left <= right:

            if people[left] + people[right] <= limit:
                left += 1

            right -= 1
            res += 1 
        
        return res
