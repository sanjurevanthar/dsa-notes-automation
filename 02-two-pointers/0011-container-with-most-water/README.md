# 11. Container With Most Water

| Difficulty | Pattern | Also uses | Solved on | Link |
|---|---|---|---|---|
| Medium | Two Pointers | Greedy | 2026-10-09 | [LeetCode](https://leetcode.com/problems/container-with-most-water/) |

---

## 🧩 Problem in Simple Words
You get an array of heights. Each number is a vertical line standing on the x-axis. Pick two lines so that, together with the floor, they hold the most water. Return that maximum amount.

**Example:** `height = [1,8,6,2,5,4,8,3,7]` → `49` because lines at index 1 (height 8) and index 8 (height 7) give width 7 × height 7 = 49.

---

## 🔑 Keywords That Give It Away
| Keyword in the problem | What it tells me |
|---|---|
| "maximum" | we want the best pair → try Two Pointers / Greedy |
| "two lines" | a pair of positions → left and right pointers |
| "array of heights" | pair at both ends, shrink inward |

> **Pattern trigger:** maximum + pair of lines → **Two Pointers** (from my master sheet: "Pair + sorted → Two Pointer; keywords "maximize/minimize"")

---

## 🧠 Pattern Recognition
Area = width × height. Width is biggest when the pointers are at the two ends. Moving inward always makes the width smaller, so the only way to get a bigger area is to find a **taller shorter-side**. So we always move the pointer on the *shorter* line. (The array is not sorted here, but the greedy argument replaces sorting.)

---

## 🛠️ Approaches

### 1. Brute Force
- **Idea:** Try every pair of lines.
- **Steps:** Two loops `i < j`, area = (j-i) × min(h[i],h[j]), keep the max.
- **Complexity:** Time O(n²) · Space O(1)
- **Why it's not enough:** n is up to 10⁵, so 10¹⁰ pairs is too slow.

### 2. Optimal — Opposite Direction Two Pointer + Greedy move
- **Idea:** Start at both ends. Compute area, then move the pointer at the shorter line inward.
- **Steps:**
  1. `left = 0`, `right = n-1`, `res = 0`.
  2. Width = `right - left`, height = `min(h[left], h[right])`. Update `res`.
  3. If `h[left] > h[right]` move `right` left, else move `left` right.
  4. Stop when they meet.
- **Template adapted to this problem:**
```python
left, right = 0, n - 1
while left < right:
    area = (right - left) * min(h[left], h[right])
    res = max(res, area)
    # move the shorter side
    if h[left] > h[right]: right -= 1
    else: left += 1
```
- **Complexity:** Time O(n) · Space O(1)

---

## ✍️ My Handwritten Notes
**11. Container With Most Water**

Given: int array `height` of length n. Line i goes from `(i, 0)` to `(i, height[i])`, so `height[i]` is a vertical line of that height. Return the max amount of water that can be held.

Example: `height = [1,8,6,2,5,4,8,3,7]` → output `49` *(hand-drawn bar chart of the example)*

- area = l × b → l = y-axis, b = x-axis
- Keyword: **maximum / minimum** → think of **2 ptr** first
- `l = 0`, `r = n-1 = 8` → `b = 8 - 0 = 8`
- `l = min(yaxis = 1, 7) = 1` → `A = 8`
- `l++` → `l = min(8, 7) = 7` → `8 - 1 = 7` → `49` ✔ *(continues…)*

---

## 💡 Explained Simply — Dry Run
Example: `[1,8,6,2,5,4,8,3,7]`

| left | right | width × min height | best |
|---|---|---|---|
| 0 | 8 | 8 × min(1,7) = 8 | 8 |
| 1 | 8 | 7 × min(8,7) = 49 | 49 |
| 1 | 7 | 6 × min(8,3) = 18 | 49 |
| 1 | 6 | 5 × min(8,8) = 40 | 49 |

… keep moving the shorter side; 49 is never beaten.

---

## ⚠️ Edge Cases & Common Mistakes
- `[1,1]` → 1 (smallest input, width 1).
- Heights of `0` give area 0 – fine.
- Mistake: moving the *taller* pointer. That can only shrink the area.

---

## 💻 My Solution (Python 3)
[`solution.py`](./solution.py) · Runtime 55 ms (beats 71.63%) · Memory 29.6 MB (beats 39.24%)

```python
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
```

---

## ⏱️ Complexity
- **Time:** O(n) — each pointer moves inward at most n times
- **Space:** O(1) — only a few variables

---

## 🔁 Similar Problems (same pattern)
- [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) — two pointers + max from each side
- [167. Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) — opposite pointers on a sorted array
- [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) — compare from both ends
- [881. Boats to Save People](https://leetcode.com/problems/boats-to-save-people/) — sort + move one end per step

---

## 📝 One-Line Takeaway
> Two lines → start at both ends and always move the **shorter** one, because only a taller short-side can improve the area.
