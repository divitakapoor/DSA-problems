# Jewels and Stones

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so `"a"` is considered a different type of stone from `"A"`.

 

 **Example 1:** 

```
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

```

 **Example 2:** 

```
Input: jewels = "z", stones = "ZZ"
Output: 0

```

 

 **Constraints:** 

- 1 <= jewels.length, stones.length <= 50
- jewels and stones consist of only English letters.
- All the characters of jewels are unique.

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 24.71%)  
**Memory:** 11.9 MB (beats 98.77%)  
**Submitted:** 2026-11-04T15:55:50.493Z  

```py
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        fre={}
        count =0
        for i in stones:
            fre[i]=fre.get(i,0)+1
        for i in jewels:
            if i in fre:
                count =count+fre[i]
        return count 

        
```

---

[View on LeetCode](https://leetcode.com/problems/jewels-and-stones/)