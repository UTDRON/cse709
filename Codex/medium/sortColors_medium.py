'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
'''

def sortColors(nums):
    # Initialize pointers for the three regions: red, white, and blue
    red, white, blue = 0, 0, len(nums) - 1
    
    while white <= blue:
        if nums[white] == 0:
            # Swap nums[white] and nums[red], move white and red pointers forward
            nums[white], nums[red] = nums[red], nums[white]
            white += 1
            red += 1
        elif nums[white] == 1:
            # Move white pointer forward
            white += 1
        else:
            # Swap nums[white] and nums[blue], move blue pointer backward
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1
    
    return nums

# Example usage:
import sys

if len(sys.argv) < 2:
    num_simulations = 1
else:
    if sys.argv[1] == "1":
        num_simulations = 1
    else:
        num_simulations = 1000000

for _ in range(num_simulations):
    nums1 = [2, 0, 2, 1, 1, 0]
    sortColors(nums1)  

    nums2 = [2, 0, 1]
    sortColors(nums2)  

    
# nums1 = [2, 0, 2, 1, 1, 0]
# print(sortColors(nums1))  # Output: [0, 0, 1, 1, 2, 2]

# nums2 = [2, 0, 1]
# print(sortColors(nums2))  # Output: [0, 1, 2]
