'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
'''
def canJump(nums):
    max_reachable = 0  # Initialize the maximum reachable index
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # If the current index is beyond the maximum reachable index, return False
        if i > max_reachable:
            return False
        
        # Update the maximum reachable index
        max_reachable = max(max_reachable, i + num)
        
        # If the maximum reachable index exceeds or equals the last index, return True
        if max_reachable >= len(nums) - 1:
            return True
    
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
    canJump([2, 3, 1, 1, 4])
    canJump([3, 2, 1, 0, 4])


# nums1 = [2, 3, 1, 1, 4]
# print(canJump(nums1))  # Output: True

# nums2 = [3, 2, 1, 0, 4]
# print(canJump(nums2))  # Output: False
