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
    # Find the starting and ending positions
    start = None
    end = None
    empty_count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                start = (i, j)
            elif grid[i][j] == 2:
                end = (i, j)
            elif grid[i][j] == 0:
                empty_count += 1

    # Define the directions for movement
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Define a recursive function to explore all possible paths
    def dfs(grid, i, j, count):
        # Base cases
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == -1:
            return 0
        if (i, j) == end:
            return count == empty_count + 1

        # Mark the current position as visited
        temp = grid[i][j]
        grid[i][j] = -1

        # Explore all possible directions
        result = 0
        for dx, dy in directions:
            result += dfs(grid, i + dx, j + dy, count + 1)

        # Restore the grid
        grid[i][j] = temp

        return result

    # Start the recursive exploration from the starting position
    return dfs(grid, start[0], start[1], 0)

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