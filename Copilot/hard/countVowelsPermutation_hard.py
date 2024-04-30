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
def countStrings(n):
    MOD = int(1e9) + 7
    dp = [[0] * 5 for _ in range(n + 1)]
    dp[1] = [1] * 5

    for i in range(2, n + 1):
        dp[i][0] = (dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]) % MOD
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD
        dp[i][2] = (dp[i - 1][1] + dp[i - 1][3]) % MOD
        dp[i][3] = dp[i - 1][2] % MOD
        dp[i][4] = (dp[i - 1][2] + dp[i - 1][3]) % MOD

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
    countStrings(1)
    countStrings(2)
    countStrings(5)

# print(countStrings(1))  # Output: 5
# print(countStrings(2))  # Output: 10
# print(countStrings(5))  # Output: 68