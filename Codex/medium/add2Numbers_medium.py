'''
you are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

'''

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            # Get the values of the current nodes or 0 if node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Create a new node with the sum digit and attach it to the result linked list
            current.next = ListNode(digit)
            current = current.next
            
            # Move to the next nodes if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next

# Helper function to convert a list to a linked list
def list_to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linked_list_to_list(l):
    result = []
    while l:
        result.append(l.val)
        l = l.next
    return result

# Example usage:
sol = Solution()

import sys

if len(sys.argv) < 2:
    num_simulations = 1
else:
    if sys.argv[1] == "1":
        num_simulations = 1
    else:
        num_simulations = 1000000
    
for _ in range(num_simulations):
    # Example 1
    l1 = list_to_linked_list([2, 4, 3])
    l2 = list_to_linked_list([5, 6, 4])
    result = sol.addTwoNumbers(l1, l2)

    # Example 2
    l1 = list_to_linked_list([0])
    l2 = list_to_linked_list([0])
    result = sol.addTwoNumbers(l1, l2)

    # Example 3
    l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = list_to_linked_list([9, 9, 9, 9])
    result = sol.addTwoNumbers(l1, l2)


# # Example 1
# l1 = list_to_linked_list([2, 4, 3])
# l2 = list_to_linked_list([5, 6, 4])
# result = sol.addTwoNumbers(l1, l2)
# print(linked_list_to_list(result))  # Output: [7, 0, 8]

# # Example 2
# l1 = list_to_linked_list([0])
# l2 = list_to_linked_list([0])
# result = sol.addTwoNumbers(l1, l2)
# print(linked_list_to_list(result))  # Output: [0]

# # Example 3
# l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
# l2 = list_to_linked_list([9, 9, 9, 9])
# result = sol.addTwoNumbers(l1, l2)
# print(linked_list_to_list(result))  # Output: [8, 9, 9, 9, 0, 0, 0, 1]