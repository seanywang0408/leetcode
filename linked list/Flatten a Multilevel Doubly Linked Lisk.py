# my recursive ! Wrong Answer
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def find_child_list(node):
            while node.next or (not node.next and node.child):
                if not node.next and node.child:
                    node.next, node.child = node.child, None
                if node.child:
                    child_tail = find_child_list(node.child)
                    node.next.prev, child_tail.next = child_tail, node.next
                    node = child_tail
                node = node.next
            return node
        if not head: return
        find_child_list(head)
        return head

# my imitative stack solution 
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None: return None
        stack=[]
        stack.append(head)
        prev = Node(0, None, None, None)
        while stack:
            pres = stack.pop()
            if pres.next:
                stack.append(pres.next)
                pres.next = None
            if pres.child:
                stack.append(pres.child)
                pres.child = None
            prev.next, pres.prev = pres, prev
            prev = pres
        head.prev = None
        return head

# stack solution
class Solution(object):
    def flatten(self, head):
        if not head:
            return
        
        dummy = Node(0,None,head,None)     
        stack = []
        stack.append(head)
        prev = dummy
        
        while stack:
            root = stack.pop()

            root.prev = prev
            prev.next = root
            
            if root.next:
                stack.append(root.next)
                root.next = None
            if root.child:
                stack.append(root.child)
                root.child = None
            prev = root        
            
        
        dummy.next.prev = None
        return dummy.next