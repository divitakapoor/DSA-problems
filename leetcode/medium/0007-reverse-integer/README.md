# Reverse Integer

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given a signed 32-bit integer `x`, return `x` *with its digits reversed*. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-231, 231 - 1]`, then return `0`.

 **Assume the environment does not allow you to store 64-bit integers (signed or unsigned).** 

 

 **Example 1:** 

```
Input: x = 123
Output: 321

```

 **Example 2:** 

```
Input: x = -123
Output: -321

```

 **Example 3:** 

```
Input: x = 120
Output: 21

```

 

 **Constraints:** 

- -231 <= x <= 231 - 1

## Solution

**Language:** Python  
**Runtime:** 20 ms (beats 45.38%)  
**Memory:** 12.2 MB (beats 76.67%)  
**Submitted:** 2026-10-31T17:49:33.312Z  

```py
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            sign=-1
        else:
            sign =1
        x=str(abs(x))
        x=x[::-1]
        result=sign*int(x)
        if result>2**31 -1 or result<-2**31:
            return 0
        return result 
```

---

[View on LeetCode](https://leetcode.com/problems/reverse-integer/)