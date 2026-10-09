# 16. 3Sum Closest

| Difficulty | Pattern | Also uses | Solved on | Link |
|---|---|---|---|---|
| Medium | Two Pointers | Sorting | 2026-10-09 | [LeetCode](https://leetcode.com/problems/3sum-closest/) |

---

## 🧩 Problem in Simple Words
Pick three numbers at different positions so their sum is as close as possible to `target`. Return that sum (not the numbers).

**Example:** `nums = [-1,2,1,-4], target = 1` → `2` because -1 + 2 + 1 = 2 is only 1 away from 1.

---

## 🔑 Keywords That Give It Away
| Keyword in the problem | What it tells me |
|---|---|
| "closest" | we track the smallest distance |sum − target| |
| "three integers" | fix one, two-pointer the other two |
| "target" | compare the sum to target to decide which pointer moves |

> **Pattern trigger:** closest + target + triplet → **Sort + Two Pointer** (from my master sheet: "3Sum / 4Sum → Sort + Two Pointer; keyword "closest"")

---

## 🧠 Pattern Recognition
It is 3Sum with a twist: instead of `== 0` we keep the best (closest) sum seen so far. After sorting, if the current sum is below the target we need a bigger sum (`left++`), otherwise a smaller one (`right--`).

---

## 🛠️ Approaches

### 1. Brute Force
- **Idea:** Try all triples.
- **Steps:** 3 loops, keep the sum with the smallest `abs(sum - target)`.
- **Complexity:** Time O(n³) · Space O(1)
- **Why it's not enough:** Works for n ≤ 500 but is slow.

### 2. Optimal — Sorting + Two Pointer
- **Idea:** Sort, fix `i`, move `left`/`right` based on sum vs target, and update the closest sum each step.
- **Steps:**
  1. Sort `nums`, `closest = inf`.
  2. For each `i`: `left = i+1`, `right = n-1`.
  3. `s = nums[i] + nums[left] + nums[right]`. If `s == target` return it.
  4. If `abs(s - target) < abs(closest - target)` update `closest`.
  5. `s < target` → `left++`, else `right--`.
- **Template adapted to this problem:**
```python
nums.sort(); closest = inf
for i in range(n):
    left, right = i + 1, n - 1
    while left < right:
        s = nums[i] + nums[left] + nums[right]
        if s == target: return s
        if abs(s - target) < abs(closest - target): closest = s
        if s < target: left += 1
        else: right -= 1
```
- **Complexity:** Time O(n²) · Space O(1) extra

---

## ✍️ My Handwritten Notes
**16. 3Sum Closest**

Given: array `nums` → n, integer `target`.
3 **distinct** indices → `nums[indices]` is closest to target. Return the sum of the closest sum.

target sum ⟹ **2 ptr** *(circled)*

Thinking: `nums = [-1, 2, 1, -4]`, `t = 1`
- `-1 + 2 - 4 = -3`; `-3 - 1 = -4` → closest sum *(distance)*
- closest = if `abs(target - closest sum)` is smaller → **update** closest sum

---

## 💡 Explained Simply — Dry Run
Example: `[-1,2,1,-4], target = 1 → sorted [-4,-1,1,2]`

| i | left | right | sum → closest |
|---|---|---|---|
| 0 | 1 | 3 | -4-1+2 = -3 → closest -3, left++ |
| 0 | 2 | 3 | -4+1+2 = -1 → closest -1, left++ |
| 1 | 2 | 3 | -1+1+2 = 2 → closest 2 (distance 1), right-- |

Pointers meet → answer 2.

---

## ⚠️ Edge Cases & Common Mistakes
- `[0,0,0]`, target 1 → 0.
- Return immediately when the sum equals target (distance 0).
- Start `closest` with `inf` (careful: `float('inf')` in Python).

---

## 💻 My Solution (Python 3)
[`solution.py`](./solution.py) · Runtime 389 ms (beats 44.97%) · Memory 19.6 MB (beats 16.54%)

```python
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
```

---

## ⏱️ Complexity
- **Time:** O(n²) — outer loop × two-pointer sweep (sort is n log n)
- **Space:** O(1) — only a few variables (sort in place)

---

## 🔁 Similar Problems (same pattern)
- [15. 3Sum](https://leetcode.com/problems/3sum/) — same skeleton, exact target
- [18. 4Sum](https://leetcode.com/problems/4sum/) — add another loop
- [259. 3Sum Smaller](https://leetcode.com/problems/3sum-smaller/) — count triplets under target
- [167. Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) — base two-pointer step

---

## 📝 One-Line Takeaway
> 'Closest' = same sorted two-pointer sweep, but keep the sum whose distance to target is smallest.
