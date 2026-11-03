# Valid Anagram

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

 

 **Example 1:** 

 **Input:**  s = "anagram", t = "nagaram"

 **Output:**  true

 **Example 2:** 

 **Input:**  s = "rat", t = "car"

 **Output:**  false

 

 **Constraints:** 

- 1 <= s.length, t.length <= 5 * 104
- s and t consist of lowercase English letters.

 

 **Follow up:**  What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

## Solution

**Language:** Python  
**Runtime:** 19 ms (beats 62.12%)  
**Memory:** 12.2 MB (beats 97.52%)  
**Submitted:** 2026-11-03T18:09:10.601Z  

```py
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        freq1 = {}
        freq2 = {}

        for ch in s:
            freq1[ch] = freq1.get(ch, 0) + 1

        for ch in t:
            freq2[ch] = freq2.get(ch, 0) + 1

        return freq1 == freq2
        
```

---

[View on LeetCode](https://leetcode.com/problems/valid-anagram/)