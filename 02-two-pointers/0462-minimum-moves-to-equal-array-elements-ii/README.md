# 462. Minimum Moves to Equal Array Elements II

| Difficulty | Pattern | Also uses | Solved on | Link |
|---|---|---|---|---|
| Medium | Two Pointers | Sorting, Math | 2026-10-09 | [LeetCode](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/) |

---

## 🧩 Problem in Simple Words
In one move you add 1 to or subtract 1 from a single element. Find the fewest moves to make all elements equal.

**Example:** `nums = [1,2,3]` → `2` because [1,2,3] → [2,2,3] → [2,2,2].

---

## 🔑 Keywords That Give It Away
| Keyword in the problem | What it tells me |
|---|---|
| "minimum moves" | optimise a total cost → think Two Pointers after sorting |
| "increment or decrement by 1" | each unit of distance costs one move |
| "equal" | everything meets at the middle value (median) |

> **Pattern trigger:** minimum moves + increment/decrement → **Sorting + Two Pointer** (median idea) (from my master sheet: "Pattern 1 Two Pointer / Sorting + Two Pointer")

---

## 🧠 Pattern Recognition
The best common value is the **median**. After sorting, pair the smallest with the largest: both must walk to the same spot, and the total walking for a pair is `nums[right] − nums[left]` wherever the meeting point is inside that gap. Add that up for every pair as the pointers close in.

---

## 🛠️ Approaches

### 1. Brute Force
- **Idea:** Try every value as the target.
- **Steps:** For each candidate value sum `|nums[i] − value|`.
- **Complexity:** Time O(n²) · Space O(1)
- **Why it's not enough:** Too slow for 10⁵.

### 2. Better — Median
- **Idea:** Sort, take the middle element, sum the distances.
- **Steps:** Sort + one pass.
- **Complexity:** Time O(n log n) · Space O(1)
- **Why it's not enough:** Correct; the pointer method below needs no median.

### 3. Optimal — Sorting + Opposite Two Pointer
- **Idea:** Sort, then add `nums[right] − nums[left]` for each pair from the outside in.
- **Steps:**
  1. Sort `nums`.
  2. `left = 0`, `right = n−1`, `res = 0`.
  3. `res += nums[right] − nums[left]`; `left++`, `right--`.
  4. Stop when `left >= right`.
- **Template adapted to this problem:**
```python
nums.sort()
left, right = 0, n - 1
while left < right:
    res += nums[right] - nums[left]
    left += 1; right -= 1
```
- **Complexity:** Time O(n log n) · Space O(1) extra

---

## ✍️ My Handwritten Notes
**462. Minimum Moves to Equal Array Elements II**

Given: int array `nums` of size n. Min moves to make all elements equal.
In one move → increment or decrement an element by **1**.

min moves ⟹ again test for **2 ptr**

eg: `nums = [1,2,3]` → op → 2
`1,2,3` ⟹ `[2 2 3]` (+1 on the 1, −1 on the 3)… ⟹ so **2**
and an element: `123 ⟹ 223 ⟹ 222`

⟹ `3 − 1 = 2` → make the 2 elements equal ⟹ 2 moves
→ `r −= 1` / `l += 1` & do the same

**#sort**

---

## 💡 Explained Simply — Dry Run
Example: `[1,10,2,9] → sorted [1,2,9,10]`

| left | right | nums[r] − nums[l] | res |
|---|---|---|---|
| 0 | 3 | 10 − 1 = 9 | 9 |
| 1 | 2 | 9 − 2 = 7 | 16 |

left ≥ right → answer 16 (all meet at a value between 2 and 9).

---

## ⚠️ Edge Cases & Common Mistakes
- Odd length: the middle element needs 0 moves (loop stops when pointers meet).
- Single element → 0.
- Values up to ±10⁹ – the sum fits in 32-bit per the problem, but use `long` in C++/Java.

---

## 💻 My Solution (Python 3)
[`solution.py`](./solution.py) · Runtime 0 ms (beats 100.0%) · Memory 20.4 MB (beats 85.39%)

```python
class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        
        nums.sort()
        n = len(nums)
        left = 0
        right = n - 1

        res = 0

        while left < right:

            res += nums[right] - nums[left]
            left += 1
            right -= 1
        
        return res
```

---

## ⏱️ Complexity
- **Time:** O(n log n) — sorting dominates; the pointer pass is O(n)
- **Space:** O(1) — in-place sort, a few variables

---

## 🔁 Similar Problems (same pattern)
- [453. Minimum Moves to Equal Array Elements](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/) — opposite trick, math answer
- [296. Best Meeting Point](https://leetcode.com/problems/best-meeting-point/) — median in 1-D
- [1703. Minimum Adjacent Swaps for K Consecutive Ones](https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/) — median again
- [2448. Minimum Cost to Make Array Equal](https://leetcode.com/problems/minimum-cost-to-make-array-equal/) — weighted median

---

## 📝 One-Line Takeaway
> Make all equal with ±1 moves → sort, and pair ends: the answer is the sum of `nums[right] − nums[left]` (median idea).
