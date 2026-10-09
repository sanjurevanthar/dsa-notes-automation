# 02. Two Pointers

**Core idea:** Move left and right based on whether the current condition is too small/large.
**Approach:** Opposite Direction Two Pointer (usually after sorting)
**🔑 Keywords:** sorted array · pair · triplet · closest · target sum · maximize/minimize

```
sort
left = 0
right = n-1
while left < right:
    check condition
    move left/right
```
**Complexity:** O(n log n) after sorting, or O(n) if already sorted.

## ✅ Solved Problems
| # | Problem | Difficulty | Trigger keywords | Date |
|---|---|---|---|---|
| 11 | [Container With Most Water](./0011-container-with-most-water/README.md) | Medium | max area, two lines | 2026-10-09 |
| 15 | [3Sum](./0015-3sum/README.md) | Medium | triplets sum 0, no duplicates | 2026-10-09 |
| 16 | [3Sum Closest](./0016-3sum-closest/README.md) | Medium | closest to target, triplet | 2026-10-09 |
| 18 | [4Sum](./0018-4sum/README.md) | Medium | quadruplets sum to target | 2026-10-09 |
| 167 | [Two Sum II - Input Array Is Sorted](./0167-two-sum-ii-input-array-is-sorted/README.md) | Medium | sorted pair target | 2026-10-09 |
| 453 | [Minimum Moves to Equal Array Elements](./0453-minimum-moves-to-equal-array-elements/README.md) | Medium | n-1 elements +1 = math | 2026-10-09 |
| 462 | [Minimum Moves to Equal Array Elements II](./0462-minimum-moves-to-equal-array-elements-ii/README.md) | Medium | ±1 moves to equal, median | 2026-10-09 |
| 881 | [Boats to Save People](./0881-boats-to-save-people/README.md) | Medium | min boats, at most 2 per boat | 2026-10-09 |
| 1679 | [Max Number of K-Sum Pairs](./1679-max-number-of-k-sum-pairs/README.md) | Medium | pairs sum to k | 2026-10-09 |
| 2491 | [Divide Players Into Teams of Equal Skill](./2491-divide-players-into-teams-of-equal-skill/README.md) | Medium | pairs with equal sum | 2026-10-09 |
| 2563 | [Count the Number of Fair Pairs](./2563-count-the-number-of-fair-pairs/README.md) | Medium | count pairs with sum in range | 2026-10-09 |

## 📌 Notes
- 3Sum / 4Sum / 3Sum Closest = (K−2) loops + one two-pointer sweep.
- 453 looks like Two Pointers but the real trick is math (`sum − n × min`).
- Full reference: [PATTERNS.md](../PATTERNS.md)
