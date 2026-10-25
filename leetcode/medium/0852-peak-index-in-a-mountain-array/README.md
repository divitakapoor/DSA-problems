# Peak Index in a Mountain Array

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an integer  **mountain**  array `arr` of length `n` where the values increase to a  **peak element**  and then decrease.

Return the index of the peak element.

Your task is to solve it in `O(log(n))` time complexity.

 

 **Example 1:** 

 **Input:**  arr = [0,1,0]

 **Output:**  1

 **Example 2:** 

 **Input:**  arr = [0,2,1,0]

 **Output:**  1

 **Example 3:** 

 **Input:**  arr = [0,10,5,2]

 **Output:**  1

 

 **Constraints:** 

- 3 <= arr.length <= 105
- 0 <= arr[i] <= 106
- arr is guaranteed to be a mountain array.

## Solution

**Language:** Python  
**Runtime:** 18 ms (beats 7.99%)  
**Memory:** 21.3 MB (beats 95.35%)  
**Submitted:** 2026-10-25T11:08:22.895Z  

```py
class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        maximum=max(arr)
        for i in range(len(arr)):
            if arr[i]==maximum:
                return i
        return -1

        
```

---

[View on LeetCode](https://leetcode.com/problems/peak-index-in-a-mountain-array/)