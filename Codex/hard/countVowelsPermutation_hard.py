'''
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3: 

Input: n = 5
Output: 68
 

Constraints:

1 <= n <= 2 * 10^4
'''
def countVowelStrings(n):
    MOD = 10**9 + 7
    dp = [[0] * 5 for _ in range(n + 1)]
    for j in range(5):
        dp[1][j] = 1
    
    for i in range(2, n + 1):
        dp[i][0] = dp[i - 1][1]  # a can only be followed by e
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD  # e can be followed by a or i
        dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][4]) % MOD  # i can be followed by a, e, o, or u
        dp[i][3] = (dp[i - 1][2] + dp[i - 1][4]) % MOD  # o can be followed by i or u
        dp[i][4] = dp[i - 1][0]  # u can only be followed by a
    
    return sum(dp[n]) % MOD

# Test cases
import sys

if len(sys.argv) < 2:
    num_simulations = 1
else:
    if sys.argv[1] == "1":
        num_simulations = 1
    else:
        num_simulations = 10000000

for _ in range(num_simulations):
    countVowelStrings(1)
    countVowelStrings(2)
    countVowelStrings(5)

# print(countVowelStrings(1))  # Output: 5
# print(countVowelStrings(2))  # Output: 10
# print(countVowelStrings(5))  # Output: 68
