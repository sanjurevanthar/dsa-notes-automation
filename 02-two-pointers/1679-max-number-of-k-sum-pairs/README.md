# 1679. Max Number of K-Sum Pairs

| Difficulty | Pattern | Also uses | Solved on | Link |
|---|---|---|---|---|
| Medium | Two Pointers | Sorting, HashMap | 2026-10-09 | [LeetCode](https://leetcode.com/problems/max-number-of-k-sum-pairs/) |

---

## 🧩 Problem in Simple Words
Repeatedly pick two numbers that add up to `k` and remove them. Count how many times you can do this at most.

**Example:** `nums = [1,2,3,4], k = 5` → `2` because (1,4) and (2,3) both add to 5.

---

## 🔑 Keywords That Give It Away
| Keyword in the problem | What it tells me |
|---|---|
| "sum equals k" | target sum → Two Pointers |
| "two numbers" | pair → left and right |
| "maximum number of operations" | count pairs as they are removed |

> **Pattern trigger:** target + pair (+ max operations) → **Sort + Two Pointer** (from my master sheet: "Sorting + Two Pointer (1679 is listed there); also HashMap as an alternative")

---

## 🧠 Pattern Recognition
After sorting, a pair that sums to `k` has a small and a large number. Smaller sum than `k` → need a bigger number (`left++`). Bigger sum → `right--`. When equal, count one operation and move both (numbers are used up).

---

## 🛠️ Approaches

### 1. Brute Force
- **Idea:** Check each pair, mark used.
- **Steps:** Two loops and a `used` array.
- **Complexity:** Time O(n²) · Space O(n)
- **Why it's not enough:** n up to 10⁵.

### 2. Better — HashMap
- **Idea:** Count frequencies; for each x match with `k − x`.
- **Steps:** One pass with a counter map.
- **Complexity:** Time O(n) · Space O(n)
- **Why it's not enough:** Good, uses extra memory.

### 3. Optimal — Sorting + Two Pointer
- **Idea:** Sort, then move pointers from both ends depending on the pair sum.
- **Steps:**
  1. Sort `nums`.
  2. `left = 0`, `right = n−1`, `res = 0`.
  3. `sum == k` → `res++`, move both.
  4. `sum < k` → `left++`; else `right--`.
- **Template adapted to this problem:**
```python
nums.sort()
left, right, res = 0, n - 1, 0
while left < right:
    s = nums[left] + nums[right]
    if s == k: res += 1; left += 1; right -= 1
    elif s < k: left += 1
    else: right -= 1
```
- **Complexity:** Time O(n log n) · Space O(1) extra

---

## ✍️ My Handwritten Notes
**1679. Max Number of K-sum Pairs**

Given: int array `nums` & int `k`.
In one operation you can pick two numbers from the array whose sum = k & remove them.
Return max number of operations you can perform on array.

eg: `nums = [1,2,3,4]`, `k = 5` → o/p = 2

**target** & **min ops** *(circled)* ⟹ **2 ptr**

- `1 + 4 == 5` ∴ remove 4 → `ops += 1` → ①
- `2 + 3 == 5` → `ops += 1` → ②, return.

so it's the right one:
if `nums[left] + nums[right] <= k` → `left += 1`
else `right −= 1`

---

## 💡 Explained Simply — Dry Run
Example: `[1,2,3,4], k = 5`

| left | right | sum | ops |
|---|---|---|---|
| 0 | 3 | 1+4 = 5 ✔ → pair | 1 |
| 1 | 2 | 2+3 = 5 ✔ → pair | 2 |

left ≥ right → answer 2.

---

## ⚠️ Edge Cases & Common Mistakes
- No valid pair → 0.
- Same number twice (`[3,1,3,4,3]`, k=6): sorted `[1,3,3,3,4]` → (3,3) once → 1.
- Two Pointers works only after sorting – keep that in mind.

---

## 💻 My Solution (Python 3)
[`solution.py`](./solution.py) · Runtime 462 ms (beats 67.39%) · Memory 31.5 MB (beats 73.89%)

```python
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        nums.sort()
        n = len(nums)

        left = 0
        right = n - 1
        res = 0

        while left < right:

            if nums[left] + nums[right] == k:
                left += 1
                right -= 1
                res += 1
            
            elif nums[left] + nums[right] <= k:
                left += 1
            
            else:
                right -= 1
        
        return res
```

---

## ⏱️ Complexity
- **Time:** O(n log n) — sorting; pointer pass is O(n)
- **Space:** O(1) — in-place sort, a few variables

---

## 🔁 Similar Problems (same pattern)
- [167. Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) — sorted version
- [1. Two Sum](https://leetcode.com/problems/two-sum/) — HashMap version
- [2491. Divide Players Into Teams of Equal Skill](https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/) — pairs with equal sums
- [881. Boats to Save People](https://leetcode.com/problems/boats-to-save-people/) — pairs vs a limit

---

## 📝 One-Line Takeaway
> Count pairs summing to k → sort, then walk pointers inward; equal = count and move both.
