# my version O(node） time, O(1) space
class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        slow, fast = head, head.next
        while fast and fast.next:
            tmp = fast.next
            slow.next, tmp.next, fast.next = tmp, slow.next, tmp.next
            fast, slow = fast.next, slow.next
        return head
