# 15. 3Sum

| Difficulty | Pattern | Also uses | Solved on | Link |
|---|---|---|---|---|
| Medium | Two Pointers | Sorting | 2026-10-09 | [LeetCode](https://leetcode.com/problems/3sum/) |

---

## 🧩 Problem in Simple Words
Given an array, find all groups of three numbers (at different positions) that add up to 0. The answer must not contain the same triplet twice.

**Example:** `nums = [-1,0,1,2,-1,-4]` → `[[-1,-1,2],[-1,0,1]]` because -1 + -1 + 2 = 0 and -1 + 0 + 1 = 0.

---

## 🔑 Keywords That Give It Away
| Keyword in the problem | What it tells me |
|---|---|
| "triplets" | three numbers → fix one, find the other two (pair) with two pointers |
| "sum == 0" | target sum → Two Pointers on a sorted array |
| "no duplicate triplets" | sort first so equal numbers sit together and can be skipped |

> **Pattern trigger:** triplet + target sum → **Sort + Two Pointer** (from my master sheet: "3Sum / 4Sum → Sort + Two Pointer")

---

## 🧠 Pattern Recognition
Two Sum on a sorted array is solved with two pointers. 3Sum is the same thing wrapped in one loop: fix the first number `nums[i]`, then the other two must add to `-nums[i]`, which is a Two Sum II problem on the rest of the array. Sorting also puts duplicates next to each other so they are easy to skip.

---

## 🛠️ Approaches

### 1. Brute Force
- **Idea:** Check every triple.
- **Steps:** Three nested loops, put sorted triples in a set.
- **Complexity:** Time O(n³) · Space O(n)
- **Why it's not enough:** n up to 3000 → too slow.

### 2. Better — HashMap
- **Idea:** Fix `i`, use a hash set to look for the third number.
- **Steps:** For each pair `(i, j)` look for `-(a+b)` in a set.
- **Complexity:** Time O(n²) · Space O(n)
- **Why it's not enough:** Handling duplicates is messy.

### 3. Optimal — Sorting + Two Pointer (fix one, two-pointer the rest)
- **Idea:** Sort. For each `i`, run left/right pointers on the part after `i`.
- **Steps:**
  1. Sort `nums`.
  2. Loop `i`. If `nums[i] == nums[i-1]` skip it (avoid duplicate triplets).
  3. `left = i+1`, `right = n-1`.
  4. Sum too small → `left++`; too big → `right--`; equal → save the triplet and move both.
  5. Return the saved triplets.
- **Template adapted to this problem:**
```python
nums.sort()
for i in range(n):
    if i > 0 and nums[i] == nums[i-1]: continue   # skip duplicate first number
    left, right = i + 1, n - 1
    while left < right:
        s = nums[i] + nums[left] + nums[right]
        if s == 0:   save; left += 1; right -= 1
        elif s < 0:  left += 1
        else:        right -= 1
```
- **Complexity:** Time O(n²) · Space O(n) for the result / sort

---

## ✍️ My Handwritten Notes
**15. 3Sum**

Given: `nums`. Return all triplets `nums[i], nums[j], nums[k]` with `i, j, k` all not equal and `nums[i] + nums[j] + nums[k] == 0`.

Example: `nums = [-1,0,1,2,-1,-4]` → `[[-1,-1,2],[-1,0,1]]`

- If **triplet** & **target sum** (both circled) → so try **2 pointer**
- Sort → `-4, -1, -1, 0, 1, 2`
- Take `-4` (`l = 1`, `r = 2`... *[unclear, probably left = index 1, right = last]*)
  - `-4 -1 + 2 = -3`
  - `-4 + 0 + 2 = -2`
  - `-4 + 1 + 2 = -1` → break *(no triplet with -4)*
- **Skip duplicates** → if `nums[i] == nums[i-1]` → continue

---

## 💡 Explained Simply — Dry Run
Example: `[-1,0,1,2,-1,-4] → sorted [-4,-1,-1,0,1,2]`

| i | left | right | sum / action |
|---|---|---|---|
| -4 | 1 | 5 | -4-1+2 = -3 → too small, left++ |
| -4 | 2 | 5 | -4-1+2 = -3 → left++ |
| -4 | 3 | 5 | -4+0+2 = -2 → left++ |
| -4 | 4 | 5 | -4+1+2 = -1 → left++, pointers meet |
| -1 (idx1) | 2 | 5 | -1-1+2 = 0 → save [-1,-1,2] |
| -1 (idx1) | 3 | 4 | -1+0+1 = 0 → save [-1,0,1] |
| -1 (idx2) | — | — | same as previous i → skipped |

---

## ⚠️ Edge Cases & Common Mistakes
- `[0,0,0]` → `[[0,0,0]]`; `[0,1,1]` → `[]`.
- Forgetting to skip duplicates gives repeated triplets (my code uses a `set` as a safety net, which works but costs extra time/memory; skipping duplicates after a hit is faster).
- Never reuse the same index – `left` starts at `i+1`.

---

## 💻 My Solution (Python 3)
[`solution.py`](./solution.py) · Runtime 775 ms (beats 24.23%) · Memory 23.6 MB (beats 7.37%)

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        n = len(nums)

        nums.sort()

        res = set()

        for i in range(n):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            first = nums[i]

            left = i + 1
            right = n - 1

            while left < right:

                second = nums[left]
                third = nums[right]

                if first + second + third == 0:
                    res.add((first, second, third))
                    right -= 1
                    left += 1
                
                elif first + second + third <= 0:
                    left += 1
                
                else:
                    right -= 1
            

        return [list(triplet) for triplet in res]
```

---

## ⏱️ Complexity
- **Time:** O(n²) — sort is n log n, then n iterations × an O(n) two-pointer sweep
- **Space:** O(n) — result set + sort

---

## 🔁 Similar Problems (same pattern)
- [16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/) — same loop, track the closest sum
- [18. 4Sum](https://leetcode.com/problems/4sum/) — one more outer loop
- [167. Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) — the inner two-pointer step
- [259. 3Sum Smaller](https://leetcode.com/problems/3sum-smaller/) — count instead of collect

---

## 📝 One-Line Takeaway
> Triplet + target → sort, fix one number, and two-pointer the rest; skip equal neighbours to avoid duplicates.
