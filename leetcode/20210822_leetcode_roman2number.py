# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# note: realized that there's no such thing as IIV to make 3. The same is true for X and C, in which case, the code could have been much simpler

class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M':1000}        
        output = 0
        c = 0
        
        for n, i in enumerate(s):
            
            if n != 0:                
                if roman[s[n]] > roman[s[n-1]]:
                    
                    for j in s[:n][::-1]: #s[:n:-1] yields reverse of what's NOT in 0:n, thus not the same as s[:n][::-1]
                        if j == s[n-1]:
                            c += 1
                        else:
                            break
                            
                    output -= roman[s[n-1]] * c * 2
                    
                    c = 0
                    
            output += roman[i]              
            # print(n, ':', i, output)
            
        return output

    def romanToInt_simple(self, s: str) -> int:
        
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M':1000}        
        output = 0
        
        for n,i in enumerate(s):
            
            if n != 0:                
                if roman[s[n]] > roman[s[n-1]]:                    
                    output -= roman[s[n-1]] * 2
                    
            output += roman[i]
            
        return output