'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9   

'''
class Solution:
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []

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
    nums1 = [2, 7, 11, 15]
    target1 = 9
    Solution().twoSum(nums1, target1)

    nums2 = [3, 2, 4]
    target2 = 6
    Solution().twoSum(nums2, target2)

    nums3 = [3, 3]
    target3 = 6
    Solution().twoSum(nums3, target3)

# nums1 = [2, 7, 11, 15]
# target1 = 9
# print(Solution().twoSum(nums1, target1))  # Output: [0, 1]

# nums2 = [3, 2, 4]
# target2 = 6
# print(Solution().twoSum(nums2, target2))  # Output: [1, 2]

# nums3 = [3, 3]
# target3 = 6
# print(Solution().twoSum(nums3, target3))  # Output: [0, 1]
