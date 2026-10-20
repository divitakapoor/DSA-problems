# Minimum Size Subarray Sum

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an array of positive integers `nums` and a positive integer `target`, return  *the  **minimal length**  of a  **subarray**  whose sum is greater than or equal to*  `target`. If there is no such subarray, return `0` instead.

 

 **Example 1:** 

```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

```

 **Example 2:** 

```
Input: target = 4, nums = [1,4,4]
Output: 1

```

 **Example 3:** 

```
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

```

 

 **Constraints:** 

- 1 <= target <= 109
- 1 <= nums.length <= 105
- 1 <= nums[i] <= 104

 

 **Follow up:**  If you have figured out the `O(n)` solution, try coding another solution of which the time complexity is `O(n log(n))`.

## Solution

**Language:** Python  
**Runtime:** 28 ms (beats 31.22%)  
**Memory:** 20.2 MB (beats 16.27%)  
**Submitted:** 2026-10-20T12:47:04.410Z  

```py
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        l=0
        sum=0
        minlength=float("inf")
        for r in range(n):
            sum=sum+nums[r]
            while sum>=target:
                minlength=min(minlength,r-l+1)
                sum=sum-nums[l]
                l+=1
        if minlength == float("inf"):
            return 0

        return minlength






        
```

---

[View on LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/)