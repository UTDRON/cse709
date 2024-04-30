'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''
def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    left, right = 0, m

    while left <= right:
        # Partition the smaller array
        partition1 = (left + right) // 2
        partition2 = (m + n + 1) // 2 - partition1

        # Calculate the maximum and minimum elements on the left side
        maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        minRight1 = float('inf') if partition1 == m else nums1[partition1]
        minRight2 = float('inf') if partition2 == n else nums2[partition2]

        # Check if the partitioning is correct
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            # Check if the total number of elements is odd or even
            if (m + n) % 2 == 0:
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            else:
                return max(maxLeft1, maxLeft2)
        elif maxLeft1 > minRight2:
            right = partition1 - 1
        else:
            left = partition1 + 1

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
    findMedianSortedArrays([1,3], [2])
    findMedianSortedArrays([1,2], [3,4])

# print(findMedianSortedArrays([1,3], [2]))     # Output: 2.00000
# print(findMedianSortedArrays([1,2], [3,4]))   # Output: 2.50000
