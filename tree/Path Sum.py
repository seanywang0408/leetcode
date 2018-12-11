# my recursive version
class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def _hasPathSum(node):
            if not node: return []
            pre = _hasPathSum(node.left)+_hasPathSum(node.right)
            # pre = list(set(pre))
            if pre==[]: 
                pre.append(node.val)
            else: 
                for i in range(len(pre)):
                    pre[i]+=node.val
            return pre
        return (sum in _hasPathSum(root))
                