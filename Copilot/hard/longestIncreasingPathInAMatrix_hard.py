'''
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

 

Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
Example 3:

Input: matrix = [[1]]
Output: 1

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
'''
def longestIncreasingPath(matrix):
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(i, j):
        if dp[i][j] != 0:
            return dp[i][j]

        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                dp[i][j] = max(dp[i][j], dfs(x, y))

        dp[i][j] += 1
        return dp[i][j]

    longest_path = 0
    for i in range(m):
        for j in range(n):
            longest_path = max(longest_path, dfs(i, j))

    return longest_path

# Test cases
import sys

if len(sys.argv) < 2:
    num_simulations = 1
else:
    if sys.argv[1] == "1":
        num_simulations = 1
    else:
        num_simulations = 1000000

for _ in range(num_simulations):
    longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])
    longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]])
    longestIncreasingPath([[1]])

# print(longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))  # Output: 4
# print(longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]))  # Output: 4
# print(longestIncreasingPath([[1]]))                     # Output: 1