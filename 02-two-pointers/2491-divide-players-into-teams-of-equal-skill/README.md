# 2491. Divide Players Into Teams of Equal Skill

| Difficulty | Pattern | Also uses | Solved on | Link |
|---|---|---|---|---|
| Medium | Two Pointers | HashMap | 2026-10-09 | [LeetCode](https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/) |

---

## 🧩 Problem in Simple Words
Split the players into teams of 2 so every team has the same total skill. If you can, return the sum of (skill × skill) for each team; otherwise return -1.

**Example:** `skill = [3,2,5,1,3,4]` → `22` because teams (1,5), (2,4), (3,3) each total 6 and 5 + 8 + 9 = 22.

---

## 🔑 Keywords That Give It Away
| Keyword in the problem | What it tells me |
|---|---|
| "teams of size 2" | pairs → two pointers |
| "equal total skill" | every pair must have the same sum → smallest pairs with largest |
| "-1 if not possible" | as soon as a pair differs, return -1 |

> **Pattern trigger:** pairs + equal sums → **Sort + Two Pointer** (from my master sheet: "Sorting + Two Pointer / Sorting + Greedy (2491 listed in both)")

---

## 🧠 Pattern Recognition
If all pairs sum to the same number S, the smallest player must be with the largest, the second smallest with the second largest, and so on. Sorting gives that order, and two pointers walk from the outside in. First pair sets the target sum.

---

## 🛠️ Approaches

### 1. Brute Force
- **Idea:** Try all ways of pairing.
- **Steps:** Backtracking over pairings.
- **Complexity:** Time O(n!!) · Space O(n)
- **Why it's not enough:** Explodes quickly.

### 2. Better — HashMap
- **Idea:** Target sum = total/(n/2); count frequencies and match `x` with `S − x`.
- **Steps:** Counter map.
- **Complexity:** Time O(n) · Space O(n)
- **Why it's not enough:** Also valid.

### 3. Optimal — Sorting + Two Pointer
- **Idea:** Sort, set `equal = skill[0] + skill[-1]`, then check every outside-in pair gives the same sum.
- **Steps:**
  1. Sort `skill`.
  2. `equal = skill[left] + skill[right]`.
  3. Loop: if pair sum ≠ `equal` → return -1; else add `a × b` to the answer.
  4. Move both pointers.
- **Template adapted to this problem:**
```python
skill.sort()
left, right = 0, n - 1
equal = skill[left] + skill[right]
while left < right:
    if skill[left] + skill[right] != equal: return -1
    total += skill[left] * skill[right]
    left += 1; right -= 1
```
- **Complexity:** Time O(n log n) · Space O(n) for my `teams` list (O(1) if multiplied on the fly)

---

## ✍️ My Handwritten Notes
**2491. Divide Players into Teams of Equal Skill**

Given: pos int array → `skill` (n). `skill[i]` = skill of i-th player.
Divide players → n/2 teams of size 2 that both are equal skill (team totals equal).

chemistry ⟹ product of skills of players (`skill[i]`)
Return the sum chem of team or return **−1** if not possible.

eg: `skill = [3,2,5,1,3,4]` → size 2 ∴ `(1,5), (2,4), (3,3)` → 6, 6, 6
Sum chem = 5 + 8 + 9 = **22**

**sort** ⟹ `1, 2, 3, 3, 4, 5`
create list ⟹ regular 2 ptr

process to check the if equal after sort:
so `equal = nums[left] + nums[right]`
now iterate & do the same — if `sum == equal` append to list (for chem) else **−1**

---

## 💡 Explained Simply — Dry Run
Example: `[3,2,5,1,3,4] → sorted [1,2,3,3,4,5]`

| left | right | pair sum (equal = 6) | chemistry so far |
|---|---|---|---|
| 0 | 5 | 1+5 = 6 ✔ | 5 |
| 1 | 4 | 2+4 = 6 ✔ | 13 |
| 2 | 3 | 3+3 = 6 ✔ | 22 |

---

## ⚠️ Edge Cases & Common Mistakes
- `[1,1,2,3]` → sorted pair sums 4 then 3 → `-1`.
- Two players only → always valid (`[3,4]` → 12).
- Odd counts can't happen (length is even).

---

## 💻 My Solution (Python 3)
[`solution.py`](./solution.py) · Runtime 51 ms (beats 35.35%) · Memory 31.6 MB (beats 5.05%)

```python
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
```

---

## ⏱️ Complexity
- **Time:** O(n log n) — sort, then one pointer pass
- **Space:** O(n) — `teams` list holds up to n/2 pairs

---

## 🔁 Similar Problems (same pattern)
- [1679. Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/) — pairs to a target sum
- [881. Boats to Save People](https://leetcode.com/problems/boats-to-save-people/) — pair ends of sorted array
- [1877. Minimize Maximum Pair Sum in Array](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/) — smallest + largest pairing
- [167. Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) — base pattern

---

## 📝 One-Line Takeaway
> Equal pair sums → after sorting, smallest must pair with largest; walk both ends and return -1 on the first mismatch.
