# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        array = list()

        while cur:
            array.append(cur)
            cur = cur.next

        del array[-n]

        for i in range(len(array) - 1):
            array[i].next = array[i+1]

        if array:
            array[-1].next = None
            return array[0]
        
        return None


        