'''
You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Example 1:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:
Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
1 <= m * n <= 20
-1 <= grid[i][j] <= 2
There is exactly one starting cell and one ending cell.
'''
def uniquePathsIII(grid):
    def dfs(i, j, visited, visited_count):
        nonlocal total_paths
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == -1 or visited[i][j]:
            return
        if grid[i][j] == 2:
            if visited_count == empty_count + 1:  # All non-obstacle squares visited
                total_paths += 1
            return
        visited[i][j] = True
        visited_count += 1
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            dfs(ni, nj, visited, visited_count)
        visited[i][j] = False  # Backtrack
        visited_count -= 1

    m, n = len(grid), len(grid[0])
    start_i, start_j = None, None
    end_i, end_j = None, None
    empty_count = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                start_i, start_j = i, j
            elif grid[i][j] == 2:
                end_i, end_j = i, j
            elif grid[i][j] == 0:
                empty_count += 1

    total_paths = 0
    visited = [[False] * n for _ in range(m)]
    dfs(start_i, start_j, visited, 0)
    return total_paths

# Test cases
import sys

if len(sys.argv) < 2:
    num_simulations = 1
else:
    if sys.argv[1] == "1":
        num_simulations = 1
    else:
        num_simulations = 100000

for _ in range(num_simulations):
    # Example 1
    uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])

    # Example 2
    uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]])

    # Example 3
    uniquePathsIII([[0,1],[2,0]])


# print(uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))  # Output: 2
# print(uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))  # Output: 4
# print(uniquePathsIII([[0,1],[2,0]]))  # Output: 0
