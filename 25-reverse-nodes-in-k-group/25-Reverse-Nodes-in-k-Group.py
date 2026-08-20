# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        grp_prev = dummy

        def get_kth_node(start: ListNode, k: int):
            while start and k > 0:
                start = start.next
                k-=1
            return start

        while True:

            kth_node = get_kth_node(grp_prev,k)
            if not kth_node:
                break

            grp_next = kth_node.next

            cur = grp_prev.next
            prev = kth_node.next

            while cur!=grp_next:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            
            temp = grp_prev.next
            grp_prev.next = kth_node
            grp_prev = temp
        
        return dummy.next





            

        