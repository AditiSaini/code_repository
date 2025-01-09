from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = l1
        pointer2 = l2
        carry = remainder = 0
        val1 = pointer1.val if pointer1 is not None else 0
        val2 = pointer2.val if pointer2 is not None else 0
        head = ListNode(0)
        result = head
        while pointer1 is not None or pointer2 is not None or carry>0:
            val1 = pointer1.val if pointer1 is not None else 0
            val2 = pointer2.val if pointer2 is not None else 0
            remainder = total = val1 + val2 + carry
            if total>9:
                carry = int(total/10)
                remainder = total%10
            else:
                carry = 0
            result.next = ListNode(remainder)
            result = result.next
            val1 = val2 = 0
            if pointer1 is not None:
                pointer1 = pointer1.next
            if pointer2 is not None:
                pointer2 = pointer2.next
        return head.next

def create_linked_list(numbers):
    dummy = ListNode()
    current = dummy
    for num in numbers:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(node):
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    print(" -> ".join(result))


l1_values = [2, 4, 3]  # Represents the number 342
l2_values = [5, 6, 4]  # Represents the number 465
l1_values = [9,9,9,9,9,9,9]
l2_values = [9,9,9,9]
#Create linked lists
l1 = create_linked_list(l1_values)
l2 = create_linked_list(l2_values)
solution = Solution()
result = solution.addTwoNumbers(l1, l2)
print_linked_list(result)