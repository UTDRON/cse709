'''
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

 

Example 1:
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:
Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] <= 99
'''
from typing import List
def isToeplitzMatrix(matrix: List[List[int]]) -> bool:
    m = len(matrix)
    n = len(matrix[0])
    
    for i in range(m-1):
        for j in range(n-1):
            if matrix[i][j] != matrix[i+1][j+1]:
                return False
    return True

# Test cases
print(isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))  # Output: True
print(isToeplitzMatrix([[1,2],[2,2]]))                    # Output: False