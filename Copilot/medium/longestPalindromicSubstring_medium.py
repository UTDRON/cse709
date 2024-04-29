'''
Given a string s, return the longest 
palindromic
 
substring
 in s.
A string is palindromic if it reads the same forward and backward.
 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''
def longestPalindrome(s):
    n = len(s)
    if n < 2:
        return s
    
    start = 0
    max_len = 1
    
    def expandAroundCenter(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    for i in range(n):
        len1 = expandAroundCenter(i, i)
        len2 = expandAroundCenter(i, i + 1)
        curr_len = max(len1, len2)
        
        if curr_len > max_len:
            max_len = curr_len
            start = i - (curr_len - 1) // 2
    
    return s[start:start + max_len]

# Example usage:
import sys

if len(sys.argv) < 2:
    num_simulations = 1
else:
    if sys.argv[1] == "1":
        num_simulations = 1
    else:
        num_simulations = 1000000

for _ in range(num_simulations):
    longestPalindrome("babad")
    longestPalindrome("cbbd")
    longestPalindrome("simsimepaninapemjayn")

# print(longestPalindrome("babad"))  # Output: "bab" or "aba"
# print(longestPalindrome("cbbd"))   # Output: "bb"
# print(longestPalindrome("simsimepaninapemjayn"))   # Output: "mepaninapem"