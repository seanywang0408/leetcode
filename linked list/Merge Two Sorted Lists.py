# my solution, O(node) time, O(1) space
class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        
        if l1.val>l2.val:
            n2, n1 = l1, l2            
        else:
            n1, n2 = l1, l2
        head = n1
        
        while n1.next:
            if n2.val<=n1.next.val:
                n1.next, n2.next, n2 = n2, n1.next, n2.next
            n1 = n1.next
            if not n2:break

        if not n1.next:
            n1.next = n2
        return head