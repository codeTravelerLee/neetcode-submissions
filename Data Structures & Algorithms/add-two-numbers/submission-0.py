# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        array = list()
        curl1 = l1
        curl2 = l2
        carry = 0

        while curl1 or curl2 or carry:
            v1 = curl1.val if curl1 else 0
            v2 = curl2.val if curl2 else 0
            total = v1 + v2 + carry
        
            array.append(ListNode(total % 10))
            carry = total // 10

            curl1 = curl1.next if curl1 else None
            curl2 = curl2.next if curl2 else None
        
        for i in range(len(array) - 1):
            array[i].next = array[i+1]
        array[-1].next = None 

        return array[0]
