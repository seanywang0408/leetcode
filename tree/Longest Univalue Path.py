# my recursive version. O(n) time, O(n) space
# list can be refered in function
class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0

        def _longest(node):
            if not node: return None, 0, 0
            l_val, l_last_length, l_result = _longest(node.left)
            r_val, r_last_length, r_result = _longest(node.right)       
            if l_val==r_val==node.val:
                last_length = max(l_last_length,r_last_length)+1
                result = max(l_result, r_result, l_last_length+r_last_length+1)                
            else:
                if l_val==node.val:
                    last_length = l_last_length+1
                elif r_val==node.val:
                    last_length = r_last_length+1
                else:
                    last_length = 1
                result = max(last_length, l_result, r_result)
            return node.val, last_length, result
        _, _, result = _longest(root)
        return result-1



# solution
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        longest = [0]
        def traverse(node):
            if not node:
                return 0
            left_len, right_len = traverse(node.left), traverse(node.right)
            left = (left_len + 1) if node.left and node.left.val == node.val else 0
            right = (right_len + 1) if node.right and node.right.val == node.val else 0
            longest[0] = max(longest[0], left + right)
            return max(left, right)
        traverse(root)
        return longest[0]