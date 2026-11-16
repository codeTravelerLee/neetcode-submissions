# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = dict()
        cur = head

        while cur:
            if cur in visited:
                return True
            else:
                visited[cur] = 1
                cur = cur.next
                
        return False
        