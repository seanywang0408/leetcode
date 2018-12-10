# my recursive version. O(n) time, O(n) space
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _minDepth(node):
            if not node: return 0
            d_l = _minDepth(node.left)
            d_r = _minDepth(node.right)
            if d_r * d_l != 0:
                return min(d_r, d_l)+1  
            else: 
                return max(d_r, d_l)+1
        return _minDepth(root)