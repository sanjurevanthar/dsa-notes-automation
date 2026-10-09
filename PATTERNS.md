# 🚀 DSA Pattern-Wise Master Sheet
*(User's personal reference — originally created with ChatGPT. Source of truth for pattern names, keywords, templates.)*

## Contents
- Master DSA Patterns (1–40)
- Sliding Window master idea
- Sections 1–29: pattern details (problems, core idea, recognition keywords, templates, complexity)
- Section 30: Quick Pattern Recognition table (memorize this)

---

## 📌 Master DSA Patterns
| # | Pattern | Priority |
|---|---|---|
| 1 | Hashing / Frequency Map | ⭐⭐⭐⭐⭐ |
| 2 | Two Pointers | ⭐⭐⭐⭐⭐ |
| 3 | Sliding Window | ⭐⭐⭐⭐⭐ |
| 4 | Prefix Sum | ⭐⭐⭐⭐⭐ |
| 5 | Difference Array | ⭐⭐⭐ |
| 6 | Kadane's Algorithm | ⭐⭐⭐⭐ |
| 7 | Binary Search | ⭐⭐⭐⭐⭐ |
| 8 | Binary Search on Answer | ⭐⭐⭐⭐⭐ |
| 9 | Sorting + Greedy | ⭐⭐⭐⭐⭐ |
| 10 | Fast & Slow Pointers | ⭐⭐⭐⭐ |
| 11 | Stack | ⭐⭐⭐⭐⭐ |
| 12 | Monotonic Stack | ⭐⭐⭐⭐⭐ |
| 13 | Monotonic Queue / Deque | ⭐⭐⭐⭐ |
| 14 | Heap / Priority Queue | ⭐⭐⭐⭐⭐ |
| 15 | Top K Elements | ⭐⭐⭐⭐⭐ |
| 16 | Merge Intervals | ⭐⭐⭐⭐ |
| 17 | Cyclic Sort | ⭐⭐⭐⭐ |
| 18 | Linked List Reversal | ⭐⭐⭐⭐ |
| 19 | Tree DFS | ⭐⭐⭐⭐⭐ |
| 20 | Tree BFS | ⭐⭐⭐⭐⭐ |
| 21 | Tree Construction / Recursion | ⭐⭐⭐⭐ |
| 22 | BST Patterns | ⭐⭐⭐⭐ |
| 23 | Graph DFS | ⭐⭐⭐⭐⭐ |
| 24 | Graph BFS | ⭐⭐⭐⭐⭐ |
| 25 | Multi-Source BFS | ⭐⭐⭐⭐ |
| 26 | Topological Sort | ⭐⭐⭐⭐⭐ |
| 27 | Union Find / DSU | ⭐⭐⭐⭐ |
| 28 | Shortest Path | ⭐⭐⭐⭐⭐ |
| 29 | Backtracking | ⭐⭐⭐⭐⭐ |
| 30 | 1D Dynamic Programming | ⭐⭐⭐⭐⭐ |
| 31 | 2D Dynamic Programming | ⭐⭐⭐⭐⭐ |
| 32 | Knapsack DP | ⭐⭐⭐⭐⭐ |
| 33 | LCS / String DP | ⭐⭐⭐⭐ |
| 34 | LIS / Subsequence DP | ⭐⭐⭐⭐ |
| 35 | Interval DP | ⭐⭐⭐ |
| 36 | Greedy | ⭐⭐⭐⭐⭐ |
| 37 | Trie | ⭐⭐⭐⭐ |
| 38 | Bit Manipulation | ⭐⭐⭐⭐ |
| 39 | Matrix / Grid | ⭐⭐⭐⭐⭐ |
| 40 | Divide & Conquer | ⭐⭐⭐⭐ |

Extra folder numbers for detailed sections not in the 40: `41-string`, `42-math-number-theory`, `43-linked-list`, `44-matrix` (use 39 for grid traversal problems, 44 for pure matrix manipulation).

---

## 🔥 Sliding Window — Master Idea
**Expand right → maintain window state → if invalid, move left → update answer/count.**

Used for subarrays/substrings, especially: longest, shortest, count, fixed K, at most K, exactly K, at least K, frequencies, window constraints.

User's saved references: Sliding Window Patterns (LeetCode), Complete Sliding Window Pattern Sheet / Revision, DSA All Pattern-Wise Master Sheet, C++ STL Containers Cheat Sheet, 50+ Useful C++ Functions.

---

## 🟢 1. Two Pointer
**Problems:** 11 Container With Most Water · 15 3Sum · 16 3Sum Closest · 18 4Sum · 167 Two Sum II · 453 Minimum Moves to Equal Array Elements · 462 Minimum Moves to Equal Array Elements II · K-Sum pattern · 1679 Max Number of K-Sum Pairs · 2491 Divide Players Into Teams of Equal Skill · 2563 Count the Number of Fair Pairs · 2401 Longest Nice Subarray

**All approaches:** Two Pointer · Sorting + Two Pointer · HashMap · Binary Search
**Core idea:** Move left and right based on whether the current condition is too small/large.
**Approach name:** Opposite Direction Two Pointer
**🔑 Keywords:** sorted array · pair · triplet · closest · target sum · maximize/minimize
**Steps:**
```
sort
left = 0
right = n-1
while left < right:
    check condition
    move left/right
```
**Complexity:** O(n log n) after sorting, or O(n) if already sorted.

## 🟢 2. Sliding Window (Variable Size)
**Problems:** 3 Longest Substring Without Repeating Characters · 209 Minimum Size Subarray Sum · 395 Longest Substring with At Least K Repeating Characters · 424 Longest Repeating Character Replacement · 713 Subarray Product Less Than K · 904 Fruit Into Baskets · 1004 Max Consecutive Ones III · 1343 Number of Sub-arrays of Size K · 1438 Longest Continuous Subarray · 1456 Maximum Number of Vowels · 2390 Removing Stars (stack pattern) · 2405 Optimal Partition of String · 2461 Maximum Sum of Distinct Subarrays · 2958 Longest Subarray With at Most K Frequency · 3305 Vowels + K Consonants I · 3306 Vowels + K Consonants II · 3254/3255 Power of K-Size Subarrays · 3708 Longest Fibonacci Subarray · 4032 Longest Subarray With at Most K Distinct Prime Factors

**Core idea:** Maintain a valid window `[left ... right]`. Expand with right; shrink with left when invalid.
**Approach:** Variable Size Sliding Window
**🔑 Keywords:** longest substring · shortest subarray · at most K · exactly K · frequency · consecutive · window of size K
```cpp
left = 0;
for (int right = 0; right < n; right++) {
    add(nums[right]);
    while (window_invalid) {
        remove(nums[left]);
        left++;
    }
    update_answer();
}
```
**Complexity:** O(n)

## 🟢 3. Fixed Size Sliding Window
**Problems:** 1343 Number of Sub-arrays of Size K · 1456 Maximum Number of Vowels in a Substring of Given Length · 2090 K Radius Subarray Averages · 3254 Find the Power of K-Size Subarrays I · 3255 … II · 2461 Maximum Sum of Distinct Subarrays With Length K
**Core idea:** Window size must remain exactly K.
```cpp
if (right - left + 1 > k)
    remove(nums[left++]);
```
**Complexity:** O(n)

## 🟢 4. HashMap / HashSet
**Problems:** Two Sum pattern (1) · 128 Longest Consecutive Sequence · duplicate pattern (217) · 2195 Append K Integers · 2295 Replace Elements in an Array · 2442 Count Distinct Integers After Reverse Operations · 287 Find the Duplicate Number · 347 Top K Frequent Elements · 451 Sort Characters By Frequency · 523 Continuous Subarray Sum · 560 Subarray Sum Equals K · 692 Top K Frequent Words · 792 Number of Matching Subsequences · 1343 fixed-window frequency · 1657-type / 2085-type frequency · 2958 At Most K Frequency · 3016 Minimum Number of Pushes · 3305/3306 Vowels · 3747 Count Distinct Integers After Removing Zeros · 3761 Mirror Pairs · 3889 Mirror Frequency Distance
**Core idea:** Store value → frequency · value → index · prefix → frequency · character → frequency
**🔑 Keywords:** frequency · duplicate · count · occurrence · lookup · complement · last position
**Complexity:** Average O(n)

## 🟢 5. Prefix Sum
**Problems:** 523 Continuous Subarray Sum · 525 Contiguous Array · 560 Subarray Sum Equals K · 2270 Number of Ways to Split Array · 3747-type prefix counting · 3969 Valid Subarrays With Matching Sum Digits
**Core idea:** For `prefix[j] - prefix[i] = target`, use a HashMap.
**🔑 Keywords:** subarray sum · range sum · sum equals K · divisible by K · count subarrays
**Complexity:** O(n)

## 🟢 6. Binary Search
**Problems:** 33 Search in Rotated Sorted Array · 34 Find First and Last Position · 81 Search in Rotated Sorted Array II · 153 Find Minimum in Rotated Sorted Array · 162 Find Peak Element · 540 Single Element in a Sorted Array · 852 Peak Index in a Mountain Array · 1901 Find a Peak Element II · 2517 Maximum Tastiness of Candy Basket · 3720 Lexicographically Smallest Permutation Greater Than Target · 3932 Count K-th Roots in a Range · 4032-type optimization
**Core idea:** Search space is monotonic: `left ---- mid ---- right`
**🔑 Keywords:** sorted · minimum possible · maximum possible · first/last · peak · rotated · answer optimization
**Complexity:** O(log n); binary search on answer: O(n log answer)

## 🟢 7. Sorting
**Problems:** 75 Sort Colors · 912 Sort an Array · 215 Kth Largest Element · 347 Top K Frequent Elements · 451 Sort Characters By Frequency · 692 Top K Frequent Words · 324 Wiggle Sort II · 2149 Rearrange Array Elements by Sign · 2295 Replace Elements · 2491 Divide Players · 2563 Fair Pairs · 3760 Maximum Substrings · 3818 Minimum Prefix Removal
**Core idea:** Sort first when ordering simplifies the problem.
**🔑 Keywords:** smallest/largest · pair/triplet · frequency ordering · intervals · greedy after sorting
**Complexity:** O(n log n)

## 🟢 8. Stack / Monotonic Stack
**Problems:** 20 Valid Parentheses-type · 42 Trapping Rain Water-type · 84 Largest Rectangle-type · 150 Evaluate Reverse Polish Notation · 394 Decode String · 402 Remove K Digits · 503 Next Greater Element II · 556 Next Greater Element III · 678 Valid Parenthesis String · 739 Daily Temperatures · 921 Minimum Add to Make Parentheses Valid · 1209 Remove All Adjacent Duplicates II · 1381-type custom stack · 2390 Removing Stars · 2104 Sum of Subarray Ranges · 3746 Minimum String Length After Balanced Removals
**Core idea:** Use a stack when the previous/next greater/smaller element matters.
**🔑 Keywords:** next greater · next smaller · remove elements · parentheses · nested · previous greater · monotonic
**Complexity:** Usually O(n)

## 🟢 9. Greedy
**Problems:** 45 Jump Game II · 55 Jump Game · 738 Monotone Increasing Digits · 769 Max Chunks To Make Sorted · 846 Hand of Straights · 1338 Reduce Array Size to Half · 1481 Least Number of Unique Integers · 2244 Minimum Rounds · 2870 Minimum Operations to Make Array Empty · 3016 Minimum Number of Pushes · 324-type sorting/greedy · 3974 Maximum Total Sum · 3979 Maximum Valid Pair Sum
**Core idea:** Make the best local decision that leads to the global optimum.
**🔑 Keywords:** minimum operations · maximum possible · choose largest/smallest · scheduling · intervals · jumps
**Complexity:** Usually O(n) or O(n log n)

## 🟢 10. Backtracking
**Problems:** 17 Letter Combinations of Phone Number · 22 Generate Parentheses · 39 Combination Sum · 40 Combination Sum II · 46 Permutations · 47 Permutations II · 77 Combinations · 78 Subsets · 90 Subsets II · 131 Palindrome Partitioning · 216 Combination Sum III · 301-type parentheses · 491 Non-decreasing Subsequences · 698 Partition to K Equal Sum Subsets · 784 Letter Case Permutation · 980-type grid backtracking · 473 Matchsticks to Square
**Core idea:** choose → explore → undo
**🔑 Keywords:** all combinations · all permutations · all subsets · generate · partition · choose K
**Complexity:** Usually exponential: O(2ⁿ) / O(n!)

## 🟢 11. Dynamic Programming
**Problems:** 62 Unique Paths · 63 Unique Paths II · 64 Minimum Path Sum · 70-type Climbing Stairs · string DP · 198-type House Robber · 300 Longest Increasing Subsequence · 322 Coin Change · 377 Combination Sum IV · 416 Partition Equal Subset Sum · 494 Target Sum · 518 Coin Change II · 698 Partition to K Equal Sum Subsets · 901-type state problems · 152 Maximum Product Subarray · 1749 Maximum Absolute Sum · 3693 Climbing Stairs II · 3708 Longest Fibonacci Subarray
**Core idea:** Break into overlapping subproblems. `dp[state] = best/count answer for state`
**🔑 Keywords:** maximum/minimum · number of ways · choose/not choose · subsequence · paths · target sum · coin
**Complexity:** Usually O(n), O(n²), or O(n × target)

## 🟢 12. Linked List
**Problems:** 2 Add Two Numbers · 19 Remove Nth Node From End · 24 Swap Nodes in Pairs · 82 Remove Duplicates II · 92 Reverse Linked List II · 138-type Copy List · 142 Linked List Cycle II · 143 Reorder List · 148 Sort List · 206-type Reverse Linked List · 2095 Delete Middle Node · 2130 Maximum Twin Sum · 237 Delete Node · 2487 Remove Nodes · 3217 Delete Nodes Present in Array
**Core patterns:** Fast & Slow Pointer · Dummy Node · Reverse Linked List · Merge · Cycle Detection
**🔑 Keywords:** linked list · cycle · nth from end · reverse · middle · reorder
**Complexity:** Usually O(n)

## 🟢 13. Binary Tree / BST
**Problems:** 94-type inorder · 102 Binary Tree Level Order Traversal · 107 Level Order Traversal II · 1161 Maximum Level Sum · 129 Sum Root to Leaf Numbers · 222 Count Complete Tree Nodes · 230 Kth Smallest Element in BST · 2471 Minimum Operations to Sort Binary Tree by Level · 2583 Kth Largest Sum in Binary Tree
**Core patterns:** DFS · BFS · Inorder · Preorder · Postorder · Level Order
**🔑 Keywords:** tree · level · depth · path · root-to-leaf · BST · kth smallest/largest
**Complexity:** O(n)

## 🟢 14. Graph / Grid
**Problems:** 200 Number of Islands · 547 Number of Provinces · 2471-type tree/graph traversal · 2257 Count Unguarded Cells · 3969-type grid · 1901 Peak Element II
**Core patterns:** DFS · BFS · Flood Fill · Connected Components · Matrix traversal
**🔑 Keywords:** islands · connected · adjacent · grid · province · path
**Complexity:** Usually O(V + E) or O(rows × cols)

## 🟢 15. Bit Manipulation ⭐ (user has worked heavily here)
**Problems:** 137 Single Number II · 260 Single Number III · 421 Maximum XOR · 477 Total Hamming Distance · 1318 Minimum Flips OR · 1780 Sum of Powers of Three · 1980 Find Unique Binary String · 2044 Maximum Bitwise OR Subsets · 2997 Minimum Operations XOR Equal K · 3702 Longest Subsequence With Non-Zero XOR · 3918 Sum of Primes… · 4036 Lexicographically Largest String… · 2401 Longest Nice Subarray
**Know:** `n & 1` · `n >> 1` · `n << 1` · `a ^ b` · `a & b` · `a | b` · `~a`
**Tricks:**
```cpp
x ^ x = 0;  x ^ 0 = x;
n > 0 && (n & (n - 1)) == 0   // power of 2
n | (1 << i)                  // set bit
n & ~(1 << i)                 // clear bit
n & (1 << i)                  // check bit
```
**Complexity:** Usually O(n × bits) → effectively O(n)

## 🟢 16. String
**Problems:** 3 Longest Substring Without Repeating · 43 Multiply Strings · 151 Reverse Words · 2904 Beautiful String · 1839 Longest Beautiful Substring · 2405 Optimal Partition · 2981 Special Substring · 3016 Minimum Pushes · 3720 Lexicographically Smallest Permutation · 3746 Balanced Removals · 3756 Concatenate Non-Zero Digits · 3760 Maximum Substrings · 4036 Lexicographically Largest String · 3305/3306 Vowel Substrings
**Common techniques:** Frequency array · HashMap · Sliding Window · Stack · Two Pointer · String building · Lexicographical comparison

## 🟢 17. Math / Number Theory
**Problems:** 7 Reverse Integer · 29 Divide Two Integers · 43 Multiply Strings · 172 Factorial Trailing Zeroes · 453 Minimum Moves · 462 Minimum Moves II · 1780 Sum of Powers of Three · 3918 Sum of Primes · 3974 Maximum Total Sum · 3979 Maximum Valid Pair Sum · 3747 Distinct Integers · 3932 K-th Roots · 3723 Maximum Sum of Squares
**Must know:** GCD · LCM · Prime · Sieve · Modulo · Power · Binary conversion · Decimal ↔ Binary · Decimal ↔ Hexadecimal

## 🟢 18. Heap / Priority Queue
**Problems:** 215 Kth Largest Element · 347 Top K Frequent Elements · 692 Top K Frequent Words · 2583 Kth Largest Sum · 3759 Count Elements With K Greater Values · 3974 Maximum Total Sum
**Core idea (K largest):** min-heap holding only K elements
```cpp
priority_queue<int, vector<int>, greater<int>> pq;
```
**🔑 Keywords:** top K · kth largest · kth smallest · most frequent · continuously select min/max
**Complexity:** Usually O(n log k)

## 🟢 19. Prefix / Suffix
**Problems:** 238 Product of Array Except Self · 53 Maximum Subarray · 2270 Number of Ways to Split Array · 3121 Special Characters II · 3818 Minimum Prefix Removal · 3918-type prefix calculations
**Core idea:** Precompute information from left/right (`prefix[i]`, `suffix[i]`). Useful when each element needs info from both sides.

## 🟢 20. Interval / Range
**Problems:** 56-type Merge Intervals · 57-type Insert Interval · 986-type Interval List · 1029-type scheduling · 1235-type weighted scheduling · 2563 Fair Pairs · 2270 Split Array
**Pattern:** sort by start → compare current with previous → merge/update
**Complexity:** O(n log n)

## 🟢 21. Matrix
**Problems:** 48 Rotate Image · 54-type Spiral Matrix · 64 Minimum Path Sum · 73 Set Matrix Zeroes · 74 Search a 2D Matrix · 1161-type level/grid · 1901 Peak Element II · 200 Number of Islands · 2257 Count Unguarded Cells
**Important patterns:** Row/column traversal · Boundary traversal · DFS/BFS · Matrix binary search · In-place marking

## 🟢 22. Recursion
**Problems:** 17 · 22 · 39 · 40 · 46 · 47 · 77 · 78 · 90 · 131 · 216 · 491 · 698 · 784
**Core formula:**
```
function(state):
    if base_case:
        return
    choose
    function(next_state)
    undo
```

## 🟢 23. Monotonic / Order Patterns
**Problems:** 739 Daily Temperatures · 503 Next Greater Element II · 556 Next Greater Element III · 2104 Sum of Subarray Ranges · 402 Remove K Digits · 738 Monotone Increasing Digits · 1839 Longest Beautiful Substring · 2414 Alphabetical Continuous Substring
**Recognition:** next greater · next smaller · previous greater · previous smaller · monotonic · increasing/decreasing → **🔥 Monotonic Stack**

## 🟢 24. XOR / Prefix XOR
**Problems:** 136-type Single Number · 137 Single Number II · 260 Single Number III · 421 Maximum XOR · 477 Total Hamming Distance · 2044 Maximum OR · 2997 XOR Equal K · 3702 Non-Zero XOR
**Core rules:** `a ^ a = 0` · `a ^ 0 = a` · `a ^ b = b ^ a`

## 🟢 25. HashMap + Prefix Sum ⭐ (very important combined pattern)
**Problems:** 523 Continuous Subarray Sum · 525 Contiguous Array · 560 Subarray Sum Equals K · 974-type Subarrays Divisible by K · 1248-type Nice Subarrays
```cpp
unordered_map<int,int> mp;
mp[0] = 1;
int prefix = 0;
for (int x : nums) {
    prefix += x;
    if (mp.count(prefix - k))
        ans += mp[prefix - k];
    mp[prefix]++;
}
```

## 🟢 26. HashMap + Sliding Window ⭐
**Problems:** 3 · 424 · 904 · 1004 · 1438 · 1456 · 2461 · 2958 · 3305 · 3306
**Recognition:** substring/subarray + frequency + at most K + longest/shortest → **Sliding Window + HashMap**

## 🟢 27. Sorting + Greedy ⭐
**Problems:** 846 · 1296 · 1338 · 1481 · 1679 · 2244 · 2491 · 2563 · 2517 · 3974
**Recognition:** If sorting creates an obvious order of decisions: sort → greedy selection

## 🟢 28. Sorting + Two Pointer ⭐
**Problems:** 15 3Sum · 16 3Sum Closest · 18 4Sum · 1679 K-Sum Pairs · 2491 Divide Players · 2563 Fair Pairs · 2517 Maximum Tastiness
```cpp
sort(nums.begin(), nums.end());
int left = 0;
int right = nums.size() - 1;
while (left < right) {
    ...
}
```

## 🟢 29. DFS / BFS
**DFS problems:** 200 Number of Islands · 547 Number of Provinces · 102 Binary Tree Level Order · 107 Level Order II · 129 Sum Root to Leaf · 1161 Maximum Level Sum
**BFS recognition:** level · minimum steps · shortest path · nearest · distance
**DFS recognition:** connected · explore all · island · component · tree traversal

---

## 🟢 30. Quick Pattern Recognition 🔥 (memorize)
| Question says | Think |
|---|---|
| Pair + sorted | Two Pointer |
| 3Sum / 4Sum | Sort + Two Pointer |
| Longest substring | Sliding Window |
| At most K | Sliding Window |
| Exactly K | AtMost(K) − AtMost(K−1) |
| Frequency | HashMap |
| Subarray Sum K | Prefix Sum + HashMap |
| Sorted array | Binary Search |
| Rotated sorted | Binary Search |
| Top K | Heap |
| Next Greater | Monotonic Stack |
| Parentheses | Stack |
| Generate all | Backtracking |
| All subsets | Backtracking |
| All permutations | Backtracking |
| Number of ways | DP |
| Min/Max choices | DP / Greedy |
| Tree level | BFS |
| Tree path | DFS |
| Islands | DFS/BFS |
| Connected components | DFS/BFS |
| XOR | Bit Manipulation |
| Single Number | XOR |
| Prime range | Sieve |
| GCD | Euclidean Algorithm |
| Matrix rotation | Matrix / In-place |
| Intervals | Sort + Greedy |
| Kth largest | Heap / Quickselect |
| Lexicographically smallest | Greedy / Stack / Two Pointer depending on problem |
