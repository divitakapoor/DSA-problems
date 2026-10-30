# Longest Consecutive Sequence

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an unsorted array of integers `nums`, return  *the length of the longest consecutive elements sequence.* 

You must write an algorithm that runs in `O(n)` time.

 

 **Example 1:** 

```
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

```

 **Example 2:** 

```
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

```

 **Example 3:** 

```
Input: nums = [1,0,1,2]
Output: 3

```

 

 **Constraints:** 

- 0 <= nums.length <= 105
- -109 <= nums[i] <= 109

## Solution

**Language:** Python  
**Runtime:** 55 ms (beats 55.98%)  
**Memory:** 26.8 MB (beats 80.20%)  
**Submitted:** 2026-10-30T15:10:34.956Z  

```py
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        count =0
        longest=0
        for i in s:
            if i-1 not in s :
                count =1
                while i+1 in s:
                    i+=1
                    count+=1
                longest=max(longest,count)
        return longest
        
```

---

[View on LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/)