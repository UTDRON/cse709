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

    def dfs(matrix, i, j, memo):
        if memo[i][j]:
            return memo[i][j]

        longest_path = 1
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                longest_path = max(longest_path, 1 + dfs(matrix, ni, nj, memo))

        memo[i][j] = longest_path
        return longest_path

    m, n = len(matrix), len(matrix[0])
    memo = [[0] * n for _ in range(m)]
    max_length = 0

    for i in range(m):
        for j in range(n):
            max_length = max(max_length, dfs(matrix, i, j, memo))

    return max_length

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
