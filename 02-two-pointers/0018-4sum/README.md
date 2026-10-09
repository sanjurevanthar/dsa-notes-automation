# 18. 4Sum

| Difficulty | Pattern | Also uses | Solved on | Link |
|---|---|---|---|---|
| Medium | Two Pointers | Sorting | 2026-10-09 | [LeetCode](https://leetcode.com/problems/4sum/) |

---

## 🧩 Problem in Simple Words
Find all different groups of four numbers (different positions) that add up to `target`. No repeated groups in the answer.

**Example:** `nums = [1,0,-1,0,-2,2], target = 0` → `[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]`.

---

## 🔑 Keywords That Give It Away
| Keyword in the problem | What it tells me |
|---|---|
| "quadruplets" | four numbers → two loops + two pointers |
| "unique" | sort and skip duplicates (or use a set) |
| "== target" | target sum → Two Pointer on sorted array |

> **Pattern trigger:** quadruplets + target → **Sort + Two Pointer** (from my master sheet: "3Sum / 4Sum → Sort + Two Pointer")

---

## 🧠 Pattern Recognition
Every extra number adds one more outer loop. 2Sum = pointers, 3Sum = 1 loop + pointers, 4Sum = 2 loops + pointers. This is the K-Sum pattern from my sheet.

---

## 🛠️ Approaches

### 1. Brute Force
- **Idea:** Four nested loops.
- **Steps:** Check every 4 numbers, store sorted tuples in a set.
- **Complexity:** Time O(n⁴) · Space O(n)
- **Why it's not enough:** n up to 200 → 1.6 billion checks.

### 2. Optimal — Sorting + 2 Loops + Two Pointer
- **Idea:** Sort, fix `i` and `j`, then two-pointer `left`/`right` for the remaining pair.
- **Steps:**
  1. Sort `nums`.
  2. Loops `i`, then `j > i`.
  3. `left = j+1`, `right = n-1`.
  4. Sum equal → save quadruplet, move both; smaller → `left++`; bigger → `right--`.
- **Template adapted to this problem:**
```python
nums.sort()
for i in range(n):
    for j in range(i + 1, n):
        left, right = j + 1, n - 1
        while left < right:
            s = nums[i] + nums[j] + nums[left] + nums[right]
            if s == target: save; left += 1; right -= 1
            elif s < target: left += 1
            else: right -= 1
```
- **Complexity:** Time O(n³) · Space O(n) for results

---

## ✍️ My Handwritten Notes
**18. 4Sum**

`nums` → n. Return array → unique **quadruplets** *(circled)* → keyword: **2 pointer**

`nums[a] nums[b] nums[c] nums[d]`, `0 ≤ a,b,c,d < n`
`nums[a] + nums[b] + nums[c] + nums[d] == target`

eg: `nums = [1,0,-1,0,-2,2]`, `target = 0`

**2 loop & 2 pointer** ⟹ ✔

---

## 💡 Explained Simply — Dry Run
Example: `[1,0,-1,0,-2,2], target = 0 → sorted [-2,-1,0,0,1,2]`

| i | j | left / right | sum → action |
|---|---|---|---|
| -2 (0) | -1 (1) | l=2,r=5 | -2-1+0+2 = -1 → left++ (twice, to idx 4) |
| -2 | -1 | l=4,r=5 | -2-1+1+2 = 0 → save [-2,-1,1,2] |
| -2 | 0 (2) | l=3,r=5 | -2+0+0+2 = 0 → save [-2,0,0,2] |
| -1 (1) | 0 (2) | l=3,r=5 | -1+0+0+2 = 1 → right-- |
| -1 | 0 | l=3,r=4 | -1+0+0+1 = 0 → save [-1,0,0,1] |

---

## ⚠️ Edge Cases & Common Mistakes
- `[2,2,2,2,2]`, target 8 → `[[2,2,2,2]]` (duplicates must collapse).
- Values up to 10⁹: in Python no overflow, in C++/Java use `long`.
- My code uses a `set` for uniqueness (accepted, but only beats ~7% on time). Skipping equal `i`/`j` values (the commented lines in my code) would prune a lot of repeated work.
- Fewer than 4 numbers → empty result.

---

## 💻 My Solution (Python 3)
[`solution.py`](./solution.py) · Runtime 773 ms (beats 6.56%) · Memory 19.4 MB (beats 56.56%)

```python
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
```

---

## ⏱️ Complexity
- **Time:** O(n³) — two loops × a two-pointer sweep
- **Space:** O(n) — result set

---

## 🔁 Similar Problems (same pattern)
- [15. 3Sum](https://leetcode.com/problems/3sum/) — one loop less
- [16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/) — closest version
- [454. 4Sum II](https://leetcode.com/problems/4sum-ii/) — HashMap split into two halves
- [167. Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) — base case

---

## 📝 One-Line Takeaway
> K-Sum = (K−2) loops + one two-pointer sweep on the sorted array.
