'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''
def searchMatrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        num = matrix[mid // n][mid % n]
        
        if num == target:
            return True
        elif num < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# Example usage:
import sys

if len(sys.argv) < 2:
    num_simulations = 1
else:
    if sys.argv[1] == "1":
        num_simulations = 1
    else:
        num_simulations = 10000000

for _ in range(num_simulations):
    matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target1 = 3
    searchMatrix(matrix1, target1)

    matrix2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target2 = 13
    searchMatrix(matrix2, target2)

# matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
# target1 = 3
# print(searchMatrix(matrix1, target1))  # Output: True

# matrix2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
# target2 = 13
# print(searchMatrix(matrix2, target2))  # Output: False