class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        
        skill.sort()

        n = len(skill)

        left = 0
        right = n - 1

        equal = skill[left] + skill[right]

        teams = []

        while left < right:

            if skill[left] + skill[right] == equal:
                teams.append((skill[left], skill[right]))
                left += 1
                right -= 1
            
            else:
                return -1
        
        total_chemistry = sum(i*j for i,j in teams)
        return total_chemistry
