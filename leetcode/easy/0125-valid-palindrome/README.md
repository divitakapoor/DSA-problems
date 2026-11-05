# Valid Palindrome

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

A phrase is a  **palindrome**  if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` *if it is a  **palindrome**, or* `false` *otherwise*.

 

 **Example 1:** 

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

```

 **Example 2:** 

```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

```

 **Example 3:** 

```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

```

 

 **Constraints:** 

- 1 <= s.length <= 2 * 105
- s consists only of printable ASCII characters.

## Solution

**Language:** Python  
**Runtime:** 10 ms (beats 94.75%)  
**Memory:** 13.3 MB (beats 36.91%)  
**Submitted:** 2026-11-05T18:00:53.742Z  

```py
class Solution:
    def isPalindrome(self, s):
        s=s.lower()
        result =''.join(i for i in s if i.isalnum())
        return result==result[::-1]  
        
```

---

[View on LeetCode](https://leetcode.com/problems/valid-palindrome/)