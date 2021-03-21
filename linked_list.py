# 21. Merge Two Sorted Lists
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        head = result
        while l1 and l2:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next
        if l1:
            head.next = l1
        elif l2:
            head.next = l2
        
        return result.next

#========================================================================================================

# 19. Remove Nth Node From End of List
 
     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
         result = ListNode(0,head)
         left = result
         right = result

         while n >= 0:
             right = right.next
             n -= 1
            
        while right:
            right = right.next
            left = left.next
        
        left.next = left.next.next
        return result.next
        