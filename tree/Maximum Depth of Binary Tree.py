# my recursive version. O(n) time, O(n) space
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _maxDepth(node):
            if not node: return 0
            return max(_maxDepth(node.left), _maxDepth(node.right))+1
        return _maxDepth(root)