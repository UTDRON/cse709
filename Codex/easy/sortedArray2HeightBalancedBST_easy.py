'''
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
'''

# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base case: if nums is empty, return None
        if not nums:
            return None
        
        # Find the middle element of the array
        mid = len(nums) // 2
        
        # Create a TreeNode with the middle element as the value
        root = TreeNode(nums[mid])
        
        # Recursively construct the left subtree with elements to the left of the middle element
        root.left = Solution().sortedArrayToBST(nums[:mid])
        
        # Recursively construct the right subtree with elements to the right of the middle element
        root.right = Solution().sortedArrayToBST(nums[mid+1:])
        
        return root

def printTree(root):
    if root:
        printTree(root.left)
        print(root.val, end=" ")
        printTree(root.right)

sol = Solution()
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
    nums1 = [-10, -3, 0, 5, 9]
    root1 = sol.sortedArrayToBST(nums1)

    nums2 = [1, 3]
    root2 = sol.sortedArrayToBST(nums2)
    
# nums1 = [-10, -3, 0, 5, 9]
# root1 = sol.sortedArrayToBST(nums1)
# printTree(root1)
# print()

# nums2 = [1, 3]
# root2 = sol.sortedArrayToBST(nums2)
# printTree(root2)