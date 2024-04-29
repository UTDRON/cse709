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

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        
        # Initialize a 2D boolean table to store if substrings are palindromic
        dp = [[False] * n for _ in range(n)]
        
        # Initialize variables to keep track of the longest palindrome
        start, max_length = 0, 1
        
        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True
        
        # Check for substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2
        
        # Check for substrings of length > 2
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    max_length = length
        
        # Return the longest palindromic substring
        return s[start:start + max_length]

sol = Solution()
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
    sol.longestPalindrome("babad")
    sol.longestPalindrome("cbbd")
    sol.longestPalindrome("simsimepaninapemjayn")


# print(sol.longestPalindrome("babad"))  # Output: "bab" or "aba"
# print(sol.longestPalindrome("cbbd"))   # Output: "bb"
# print(sol.longestPalindrome("simsimepaninapemjayn"))   # Output: "mepaninapem"