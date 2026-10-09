# 453. Minimum Moves to Equal Array Elements

| Difficulty | Pattern | Also uses | Solved on | Link |
|---|---|---|---|---|
| Medium | Two Pointers | — | 2026-10-09 | [LeetCode](https://leetcode.com/problems/minimum-moves-to-equal-array-elements/) |

---

## 🧩 Problem in Simple Words
In one move you add 1 to every element except one. Find the fewest moves to make all elements equal.

**Example:** `nums = [1,2,3]` → `3` because [1,2,3] → [2,3,3] → [3,4,3] → [4,4,4].

---

## 🔑 Keywords That Give It Away
| Keyword in the problem | What it tells me |
|---|---|
| "minimum moves" | my first guess was Two Pointers, but there is nothing to pair up here |
| "increment n−1 elements" | same as decreasing 1 element by 1 → turns into a math/sum problem |

> **Pattern trigger:** minimum moves + n−1 elements incremented → **Math / Number Theory** (not Two Pointers) (from my master sheet: "Section "Math / Number Theory" (the sheet lists this problem under Two Pointer, but the trick is math)")

---

## 🧠 Pattern Recognition
Adding 1 to n−1 elements is the same, in terms of differences, as **subtracting 1 from the one left out**. So every move can only lower one element relative to the rest, and all numbers must come down to the minimum. Total moves = sum of (each number − min) = `sum(nums) − n × min(nums)`. Two pointers does not help because every move touches almost all elements.

---

## 🛠️ Approaches

### 1. Brute Force
- **Idea:** Simulate the moves.
- **Steps:** Repeat: leave out the max, add 1 to the others, until all equal.
- **Complexity:** Time O(n × answer) – huge · Space O(1)
- **Why it's not enough:** Answer can be ~10⁹.

### 2. Optimal — Math (reverse thinking)
- **Idea:** Think of each move as decreasing one element by 1 → everything must come down to `min`.
- **Steps:**
  1. `smallest = min(nums)`.
  2. Moves needed = `sum(nums) − n × smallest`.
  3. Return it.
- **Template adapted to this problem:**
```python
smallest = min(nums)
return sum(nums) - len(nums) * smallest
```
- **Complexity:** Time O(n) · Space O(1)

---

## ✍️ My Handwritten Notes
**453. Minimum Moves to Equal Array Elements**

Given: `nums` of size n. Min no. of moves to make all array elements equal.
In one move → `n-1` elements incremented by 1.

**minimum moves** → chance of 2 ptr *but not sure*

`[1, 2, 3]` → `3 - 1 = 2`   *(1 to be 3 ⟹ 2)*
⟹ 2 ✗ — **2 ptr does not work**
⟹ mathematical exp → `min_val = 1`, `sum ⟹ 6`
so → o/p = 3 = `6 - 1 × len(nums)` = `6 - 1 × 3` = 3

*I don't have a clear idea here ⟹ **explain** (circled)*

---

## 💡 Explained Simply — Dry Run
Example: `[1,2,3]`

| step | array | what happens | moves |
|---|---|---|---|
| 0 | [1,2,3] | min = 1, sum = 6, n = 3 | — |
| 1 | [2,3,3] | left out the 3 at index 2 (others +1) | 1 |
| 2 | [3,4,3] | left out the 3 at index 2 | 2 |
| 3 | [4,4,4] | all equal | 3 |
| formula |  | 6 − 3×1 = 3 | 3 |

---

## ⚠️ Edge Cases & Common Mistakes
- All equal → 0 (`[1,1,1]`).
- Single element → 0.
- Negative numbers work (the min can be negative; use a large int where needed in C++).
- Mistake I noted: expecting Two Pointers. Ask: does a move touch only 2 positions? Here it touches n−1.

---

## 💻 My Solution (Python 3)
[`solution.py`](./solution.py) · Runtime 0 ms (beats 100.0%) · Memory 20.4 MB (beats 74.97%)

```python
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        
        smallest = min(nums)
        return sum(nums) - len(nums)*smallest
```

---

## ⏱️ Complexity
- **Time:** O(n) — one pass for min and one for sum
- **Space:** O(1) — two numbers

---

## 🔁 Similar Problems (same pattern)
- [462. Minimum Moves to Equal Array Elements II](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/) — ±1 on one element → median
- [1658. Minimum Operations to Reduce X to Zero](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/) — rethink the problem backwards
- [1217. Minimum Cost to Move Chips](https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/) — parity / math trick
- [1000. Minimum Cost to Merge Stones](https://leetcode.com/problems/minimum-cost-to-merge-stones/) — hard follow-up (DP)

---

## 📝 One-Line Takeaway
> 'Increase n−1 elements' = 'decrease 1 element' → answer is `sum − n × min`. Think math, not pointers.
