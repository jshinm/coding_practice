# Decode Ways
A message containing letters from A-Z can be encoded into numbers using the following mapping:

```
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
```

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

* "AAJF" with the grouping (1 1 10 6)
* "KJF" with the grouping (11 10 6)

Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

Example 1:

```
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
```

Example 2:

```
Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

Example 3:

```
Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with 0.
The only valid mappings with 0 are 'J' -> "10" and 'T' -> "20", neither of which start with 0.
Hence, there are no valid ways to decode this since all digits need to be mapped.
```

Example 4:

```
Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
```

Constraints:

* 1 <= s.length <= 100
* s contains only digits and may contain leading zero(s).

## Solution
The following solution is DP method using memoization where progress is being tracked in an array.

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        # inefficient method
        # for 3 digits, the possible combinations are
        # 1-1-1, 1-2, 2-1
        # for each combination, determine if string return valid conversion
        # this is finding all possible combination that sum up to the number of digits
        
        # DP method
        # make a list of possible combination at ith position, then return the last count at the list
        # check digit length of [1,2] at ith position
        # example of this is as follows
        # for s = '3442'
        # create a list such that l = [1] * len(s)
        # at i, do 1 and 2 digit check
        # if the digit is between 0 < s[i] < 10, returns l[i-1] otherwise 0
        # for the 2 digit check
        # if the digit is between 10 < s[i] < 27, returns l[i-2] otherwise 0
        # ultimately return l[-1]
        
        if s is None or s[0] == '0':
            return 0
        
        l = [1] * len(s)
        
        for i in range(1, len(s)):
            # 1-step memoization
            l[i] = l[i-1] if int(s[i]) != 0 else 0 
            # 2-step memoization
            l[i] += l[i-2 if i > 1 else 0] if 9 < int(s[i-1:i+1]) < 27 else 0 
            
        return l[-1]
```