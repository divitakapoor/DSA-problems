# Longest Palindrome

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given a string `s` which consists of lowercase or uppercase letters, return the length of the  **longest palindrome**  that can be built with those letters.

Letters are  **case sensitive**, for example, `"Aa"` is not considered a palindrome.

 

 **Example 1:** 

```
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

```

 **Example 2:** 

```
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

```

 

 **Constraints:** 

- 1 <= s.length <= 2000
- s consists of lowercase and/or uppercase English letters only.

## Solution

**Language:** Python  
**Runtime:** 4 ms (beats 42.46%)  
**Memory:** 12 MB (beats 95.24%)  
**Submitted:** 2026-11-06T17:02:56.352Z  

```py
class Solution:
    def longestPalindrome(self, s):
        from collections import Counter
        
        count = Counter(s)
        length = 0
        odd_found = False
        
        for c in count.values():
            if c % 2 == 0:
                length += c
            else:
                length += c - 1
                odd_found = True
        
        if odd_found:
            length += 1
        
        return length
```

---

[View on LeetCode](https://leetcode.com/problems/longest-palindrome/)