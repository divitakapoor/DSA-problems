# Second Largest Digit in a String

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an alphanumeric string `s`, return  *the  **second largest**  numerical digit that appears in* `s` *, or* `-1` *if it does not exist*.

An  **alphanumeric**  string is a string consisting of lowercase English letters and digits.

 

 **Example 1:** 

```
Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.

```

 **Example 2:** 

```
Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit. 

```

 

 **Constraints:** 

- 1 <= s.length <= 500
- s consists of only lowercase English letters and digits.

## Solution

**Language:** Python  
**Runtime:** 11 ms (beats 59.84%)  
**Memory:** 12.3 MB (beats 52.13%)  
**Submitted:** 2026-10-31T17:29:10.435Z  

```py
class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        largest=-1
        second=-1
        for i in s:
            if i.isdigit():
                num=int(i)
                if num>largest:
                    second=largest
                    largest=num
                elif num<largest and num>second:
                    second=num
        return second


```

---

[View on LeetCode](https://leetcode.com/problems/second-largest-digit-in-a-string/)