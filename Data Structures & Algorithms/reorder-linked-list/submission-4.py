# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        linkedlist = list()

        while cur:
            linkedlist.append(cur)
            cur = cur.next

        front = 0
        rear = len(linkedlist) - 1
        reversedlist = list()

        while front <= rear:
            reversedlist.append(linkedlist[front])

            #홀수개일때 하나만 넣어주게
            if front != rear:
                reversedlist.append(linkedlist[rear])
            front += 1
            rear -= 1

        #배열 다시 링크드리스트로 합치기
        for i in range(len(reversedlist) - 1):
            reversedlist[i].next = reversedlist[i + 1]
        reversedlist[-1].next = None

        



        