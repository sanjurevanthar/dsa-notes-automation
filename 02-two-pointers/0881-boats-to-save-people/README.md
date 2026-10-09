# 881. Boats to Save People

| Difficulty | Pattern | Also uses | Solved on | Link |
|---|---|---|---|---|
| Medium | Two Pointers | Greedy, Sorting | 2026-10-09 | [LeetCode](https://leetcode.com/problems/boats-to-save-people/) |

---

## 🧩 Problem in Simple Words
Each boat holds at most 2 people and a total weight up to `limit`. Find the fewest boats needed to carry everyone.

**Example:** `people = [3,2,2,1], limit = 3` → `3` because (1,2), (2), (3).

---

## 🔑 Keywords That Give It Away
| Keyword in the problem | What it tells me |
|---|---|
| "minimum number of boats" | minimise → Greedy + Two Pointers |
| "at most two" | a pair at a time → pointers at both ends |
| "limit" | pair sum compared with a limit, like a target |

> **Pattern trigger:** minimum + at most 2 + limit → **Sorting + Greedy + Two Pointer** (from my master sheet: "Sorting + Greedy → "sort → greedy selection"; Pair + sorted → Two Pointer")

---

## 🧠 Pattern Recognition
The heaviest person must take a boat anyway. Try to pair them with the lightest person. If they fit together, great (both leave). If not, the heavy person goes alone, because nobody lighter than the lightest could fit either. Sorting makes 'lightest' and 'heaviest' sit at the two ends.

---

## 🛠️ Approaches

### 1. Brute Force
- **Idea:** Try all pairings.
- **Steps:** Try to match each person with every other unused person.
- **Complexity:** Time O(n²) or worse · Space O(n)
- **Why it's not enough:** n up to 5×10⁴.

### 2. Optimal — Sort + Greedy Two Pointer
- **Idea:** Heaviest always sails; take the lightest along if they fit.
- **Steps:**
  1. Sort `people`.
  2. `left = 0`, `right = n−1`, `boats = 0`.
  3. While `left <= right`: if `people[left] + people[right] <= limit` then `left++`.
  4. Always `right--` and `boats++`.
- **Template adapted to this problem:**
```python
people.sort()
left, right, boats = 0, n - 1, 0
while left <= right:
    if people[left] + people[right] <= limit:
        left += 1          # lightest rides along
    right -= 1             # heaviest always leaves
    boats += 1
```
- **Complexity:** Time O(n log n) · Space O(1) extra

---

## ✍️ My Handwritten Notes
**881. Boats to Save People**

Given: `people[i]` → weight of i-th person. Infinite no. of boats, each can carry max **limit**.
- boat → max limit
- → at most 2 at a time
  } both should be true

Min no. of boats to carry.

**minimum** → keyword → try **2 pointer**

eg: `people = [1, 2]`, `limit = 3` ⟹ sort `[1, 2]`; 2 ppl → add ⟹ 3 ✔ ⟹ append to list & `r −= 1`, `l += 1`

First idea: if sum `>= limit` then `r −= 1`, else `l += 1` ⟹ **this fails**

But if 2 added `<= limit` (then try increasing left to max the limit)
If heavy → single person → single boat so → `r −= 1` & `boat += 1`

---

## 💡 Explained Simply — Dry Run
Example: `[3,2,2,1], limit = 3 → sorted [1,2,2,3]`

| left | right | pair sum | boats |
|---|---|---|---|
| 0 | 3 | 1+3 = 4 > 3 → 3 goes alone | 1 |
| 0 | 2 | 1+2 = 3 ≤ 3 → both go | 2 |
| 1 | 1 | 2+2 = 4 > 3 → single (left == right) | 3 |

---

## ⚠️ Edge Cases & Common Mistakes
- `left == right` is the last person alone – needs `<=` in the loop.
- Someone as heavy as `limit` always rides alone.
- My first idea (move `left` when the sum is too small, without counting boats) failed – every step must count one boat and always remove the heaviest.

---

## 💻 My Solution (Python 3)
[`solution.py`](./solution.py) · Runtime 51 ms (beats 62.86%) · Memory 25.1 MB (beats 81.53%)

```python
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        
        people.sort()
        n = len(people)

        left = 0
        right = n - 1
        res = 0

        while left <= right:

            if people[left] + people[right] <= limit:
                left += 1

            right -= 1
            res += 1 
        
        return res
```

---

## ⏱️ Complexity
- **Time:** O(n log n) — sort + one pointer pass
- **Space:** O(1) — just indices (sort in place)

---

## 🔁 Similar Problems (same pattern)
- [167. Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) — opposite pointers on sorted
- [455. Assign Cookies](https://leetcode.com/problems/assign-cookies/) — sort + greedy matching
- [2491. Divide Players Into Teams of Equal Skill](https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/) — pair smallest with largest
- [1679. Max Number of K-Sum Pairs](https://leetcode.com/problems/max-number-of-k-sum-pairs/) — count pairs with pointers

---

## 📝 One-Line Takeaway
> Pair the heaviest with the lightest: if they fit, both go; if not, the heavy one goes alone.
