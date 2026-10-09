# 2563. Count the Number of Fair Pairs

| Difficulty | Pattern | Also uses | Solved on | Link |
|---|---|---|---|---|
| Medium | Two Pointers | Binary Search, Sorting | 2026-10-09 | [LeetCode](https://leetcode.com/problems/count-the-number-of-fair-pairs/) |

---

## 🧩 Problem in Simple Words
Count pairs `(i, j)` with `i < j` whose sum is between `lower` and `upper` (inclusive).

**Example:** `nums = [0,1,7,4,4,5], lower = 3, upper = 6` → `6` pairs: (0,3), (0,4), (0,5), (1,3), (1,4), (1,5).

---

## 🔑 Keywords That Give It Away
| Keyword in the problem | What it tells me |
|---|---|
| "number of pairs" | count, not list → count many pairs at once |
| "lower ≤ sum ≤ upper" | a range of sums → count(≤ upper) − count(< lower) |
| "i < j" | order doesn't matter for the sum, so sorting is allowed |

> **Pattern trigger:** pairs + sum in a range → **Sort + Two Pointer (counting)** (from my master sheet: "Sorting + Two Pointer (2563 listed); Binary Search also works")

---

## 🧠 Pattern Recognition
Because the order of `i < j` doesn't change the sum, we can sort. Then, for a limit `t`, count pairs with sum `< t`: if `nums[left] + nums[right] < t`, then every index between `left+1 … right` also works with `left`, so add `right − left` at once and move `left`. Answer = pairs `< upper+1` minus pairs `< lower`.

---

## 🛠️ Approaches

### 1. Brute Force
- **Idea:** Check every pair.
- **Steps:** Two loops with the range check.
- **Complexity:** Time O(n²) · Space O(1)
- **Why it's not enough:** n up to 10⁵.

### 2. Better — Sort + Binary Search
- **Idea:** For each `i`, binary search the allowed range of partners.
- **Steps:** `bisect_left` / `bisect_right`.
- **Complexity:** Time O(n log n) · Space O(1)
- **Why it's not enough:** Works well too.

### 3. Optimal — Sorting + Two Pointer (count less-than helper)
- **Idea:** `count_less_than(t)` counts pairs with sum < t in O(n); use it twice.
- **Steps:**
  1. Sort `nums`.
  2. `count_less_than(t)`: `left = 0`, `right = n−1`; if sum `< t` add `right − left`, `left++`; else `right--`.
  3. Answer = `count_less_than(upper + 1) − count_less_than(lower)`.
- **Template adapted to this problem:**
```python
def count_less_than(t):
    left, right, res = 0, n - 1, 0
    while left < right:
        if nums[left] + nums[right] < t:
            res += right - left   # all pairs (left, left+1..right)
            left += 1
        else:
            right -= 1
    return res
return count_less_than(upper + 1) - count_less_than(lower)
```
- **Complexity:** Time O(n log n) · Space O(1) extra

---

## ✍️ My Handwritten Notes
**2563. Count the Number of Fair Pairs**

Given: 0-indexed array `nums` → n size, 2 int `lower`, `upper`.
Return the no. of fair pairs.

A fair pair: pair `(i, j)` if `0 ≤ i < j < n` & `lower ≤ nums[i] + nums[j] ≤ upper` → think of **2 ptr**

eg: `nums = [0,1,7,4,4,5]`, `lower = 3`, `upper = 6`
so all possible pair → within range **3 – 6** → `nums[i] + nums[j]`

so if `left = 0`, `right = n−1`
condition → if sum `left + right < target` → all pairs: `res += (r − l)` ↳ for upper & lower
& then lower same

return `cnt(upper) − cnt(lower)`

---

## 💡 Explained Simply — Dry Run
Example: `[0,1,7,4,4,5] → sorted [0,1,4,4,5,7], count_less_than(7) (= pairs ≤ 6)`

| left | right | sum | res |
|---|---|---|---|
| 0 | 5 | 0+7 = 7, not < 7 → right-- | 0 |
| 0 | 4 | 0+5 = 5 < 7 → +4 pairs, left++ | 4 |
| 1 | 4 | 1+5 = 6 < 7 → +3, left++ | 7 |
| 2 | 4 | 4+5 = 9 → right-- | 7 |
| 2 | 3 | 4+4 = 8 → right-- | 7 |

left ≥ right → 7 pairs with sum ≤ 6; count_less_than(3) = 1 → 7 − 1 = **6** ✔

---

## ⚠️ Edge Cases & Common Mistakes
- Use `upper + 1` so the upper bound is inclusive.
- Sorting is allowed because `i < j` doesn't affect the sum.
- Large values (±10⁹): sums up to 2×10⁹ – fine in Python, use `long` in C++/Java.
- Counts up to ~5×10⁹ → also needs 64-bit in C++/Java.

---

## 💻 My Solution (Python 3)
[`solution.py`](./solution.py) · Runtime 152 ms (beats 67.15%) · Memory 33.5 MB (beats 23.28%)

```python
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        n = len(nums)
        nums.sort()

        def count_less_than(target: int) -> int :

            left = 0
            right = n - 1

            res = 0

            while left < right:

                if nums[left] + nums[right] < target:

                    res += (right - left)
                    left += 1
                
                else:
                    right -= 1
                
            return res
        
        return count_less_than(upper + 1) - count_less_than(lower)
```

---

## ⏱️ Complexity
- **Time:** O(n log n) — sort, then two O(n) pointer passes
- **Space:** O(1) — in-place sort, a few variables

---

## 🔁 Similar Problems (same pattern)
- [167. Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) — two-pointer base
- [1679. Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/) — count pairs with sum k
- [532. K-diff Pairs in an Array](https://leetcode.com/problems/k-diff-pairs-in-an-array/) — sort + pointers on differences
- [259. 3Sum Smaller](https://leetcode.com/problems/3sum-smaller/) — the same 'add right − left' counting trick

---

## 📝 One-Line Takeaway
> Count pairs in a sum range → sort, count(sum < upper+1) − count(sum < lower), adding `right − left` at once.
