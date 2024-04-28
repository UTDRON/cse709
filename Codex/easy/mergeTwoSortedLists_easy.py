'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       # Initialize a dummy node as the head of the merged list
        dummy = ListNode()
        # Pointer to traverse the merged list
        current = dummy
        
        # Traverse both lists simultaneously
        while list1 and list2:
            # Compare the values of the current nodes of list1 and list2
            if list1.val < list2.val:
                # Append the smaller node to the merged list
                current.next = list1
                # Move list1 pointer forward
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            # Move the merged list pointer forward
            current = current.next
        
        # Append the remaining nodes of list1 or list2
        current.next = list1 if list1 else list2
        
        # Return the head of the merged list (excluding the dummy node)
        return dummy.next

# Helper function to create a linked list from a list of values
def createLinkedList(values):
    head = ListNode()
    current = head
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return head.next

# Helper function to print the values of a linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


sol = Solution()

# Example1:
list1 = createLinkedList([1, 2, 4])
list2 = createLinkedList([1, 3, 4])
merged_list = sol.mergeTwoLists(list1, list2)
printLinkedList(merged_list)

# Example2:
list1 = createLinkedList([])
list2 = createLinkedList([])
merged_list = sol.mergeTwoLists(list1, list2)
printLinkedList(merged_list)

# Example3:
list1 = createLinkedList([])
list2 = createLinkedList([0])
merged_list = sol.mergeTwoLists(list1, list2)
printLinkedList(merged_list)