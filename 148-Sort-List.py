class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        right = slow.next
        left = head
        slow.next = None

        left = self.sortList(left)
        right = self.sortList(right)

        return self.mergeSort(left,right)

    def mergeSort(self,left,right):
        dummy = ListNode(0)
        temp = dummy

        while left and right:
            if right.val < left.val:
                temp.next = right
                right = right.next
            else:
                temp.next = left
                left = left.next

            temp = temp.next

        if right:
            temp.next = right
        else:
            temp.next = left

        return dummy.next

