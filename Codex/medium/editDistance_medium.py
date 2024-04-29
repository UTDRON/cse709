'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
'''
def minDistance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill the dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    return dp[m][n]

# Example usage:

import sys

if len(sys.argv) < 2:
    num_simulations = 1
else:
    if sys.argv[1] == "1":
        num_simulations = 1
    else:
        num_simulations = 100000

for _ in range(num_simulations):
    word1 = "horse"
    word2 = "ros"
    minDistance(word1, word2)

    word1 = "intention"
    word2 = "execution"
    minDistance(word1, word2)

    word1 = "aquickbrownfoxjumpedoverthelazydogs"
    word2 = "catreegoatapaperedoguntheracheliam"
    minDistance(word1, word2)


# word1 = "horse"
# word2 = "ros"
# print(minDistance(word1, word2))  # Output: 3

# word1 = "intention"
# word2 = "execution"
# print(minDistance(word1, word2))  # Output: 5

# word1 = "aquickbrownfoxjumpedoverthelazydogs"
# word2 = "catreegoatapaperedoguntheracheliam"
# print(minDistance(word1, word2))  