# my recursive version. O(n) time, O(n) space
class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def heightBalanced(node):
            if not node:
                return 0, True
            h_l, b_l = heightBalanced(node.left)
            h_r, b_r = heightBalanced(node.right)
            if not (b_l and b_r) or abs(h_l-h_r)>1: return max(h_l, h_r)+1, False
            return max(h_l, h_r)+1, True

        h, b = heightBalanced(root)
        return b