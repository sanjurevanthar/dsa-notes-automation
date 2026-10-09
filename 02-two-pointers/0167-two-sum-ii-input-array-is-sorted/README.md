# 167. Two Sum II - Input Array Is Sorted

| Difficulty | Pattern | Also uses | Solved on | Link |
|---|---|---|---|---|
| Medium | Two Pointers | Binary Search | 2026-10-09 | [LeetCode](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) |

---

## 🧩 Problem in Simple Words
The array is already sorted (smallest to largest). Find two numbers that add up to `target` and return their positions (counting from 1).

**Example:** `numbers = [2,7,11,15], target = 9` → `[1,2]` because 2 + 7 = 9.

---

## 🔑 Keywords That Give It Away
| Keyword in the problem | What it tells me |
|---|---|
| "sorted / non-decreasing" | order lets us decide which pointer to move |
| "two numbers … target" | pair + target → Two Pointers |
| "constant extra space" | no HashMap allowed → two pointers |

> **Pattern trigger:** sorted + pair + target → **Two Pointer** (from my master sheet: "Pair + sorted → Two Pointer")

---

## 🧠 Pattern Recognition
Sum too big? Move the right pointer to a smaller number. Sum too small? Move the left pointer to a bigger number. Sorted order makes that decision always safe. This is the base of 3Sum, 4Sum and every K-Sum.

---

## 🛠️ Approaches

### 1. Brute Force
- **Idea:** Check every pair.
- **Steps:** Two loops.
- **Complexity:** Time O(n²) · Space O(1)
- **Why it's not enough:** n up to 30,000 → slow.

### 2. Better — Binary Search
- **Idea:** For each `i`, binary search for `target - numbers[i]`.
- **Steps:** n × log n.
- **Complexity:** Time O(n log n) · Space O(1)
- **Why it's not enough:** Works, but two pointers is simpler and faster.

### 3. Optimal — Opposite Direction Two Pointer
- **Idea:** `left` at the start, `right` at the end; move whichever side fixes the sum.
- **Steps:**
  1. `left = 0`, `right = n-1`.
  2. If `sum == target` return `[left+1, right+1]`.
  3. If `sum > target` → `right--`.
  4. Else `left++`.
- **Template adapted to this problem:**
```python
left, right = 0, n - 1
while left < right:
    s = nums[left] + nums[right]
    if s == target: return [left + 1, right + 1]
    elif s > target: right -= 1
    else: left += 1
```
- **Complexity:** Time O(n) · Space O(1)

---

## ✍️ My Handwritten Notes
**167. Two Sum II – input array sorted**

- 1-indexed array
- sorted → non-decreasing ⟹ ascending

Find 2 numbers such that `nums[x] + nums[y] = target`, `1 ≤ x < y ≤ nums.length`.
Return indices of those 2 numbers as array `[x, y]`.

Key words ⟹ **target** ⟹ **2 ptr**

eg: `[2, 7, 11, 15]`, `target = 9`
- `2 + 15 → 17 != 9 & > 9`
- `2 + 11 → 13 != 9 & > 9`
- `2 + 7 → 9 == 9` ✔
- `l →`  `r →` return both

---

## 💡 Explained Simply — Dry Run
Example: `[2,7,11,15], target = 9`

| left | right | sum | action |
|---|---|---|---|
| 0 | 3 | 17 | > 9 → right-- |
| 0 | 2 | 13 | > 9 → right-- |
| 0 | 1 | 9 | == 9 → return [1, 2] |

---

## ⚠️ Edge Cases & Common Mistakes
- Answer is 1-indexed – add 1 to both pointers.
- Negative numbers are fine (`[-1,0]`, target -1).
- `left < right` so the same element is never used twice.

---

## 💻 My Solution (Python 3)
[`solution.py`](./solution.py) · Runtime 8 ms (beats 22.24%) · Memory 22.4 MB (beats 32.63%)

```python
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        n = len(numbers)
        
        left = 0
        right = n - 1

        while left < right:

            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            
            elif numbers[left] + numbers[right] > target:
                right -= 1
            
            else:
                left += 1
        
        return []
```

---

## ⏱️ Complexity
- **Time:** O(n) — each pointer only moves one way
- **Space:** O(1) — just two indices

---

## 🔁 Similar Problems (same pattern)
- [1. Two Sum](https://leetcode.com/problems/two-sum/) — unsorted → HashMap version
- [15. 3Sum](https://leetcode.com/problems/3sum/) — this step inside a loop
- [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) — pointers from both ends
- [653. Two Sum IV - BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/) — same idea on a BST

---

## 📝 One-Line Takeaway
> Sorted + target sum → one pointer at each end; sum too big → right--, too small → left++.
