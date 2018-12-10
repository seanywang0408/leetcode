# my recursive version O(n) time, O(n) space (the number of recursive call is bound by the height of the tree)
# better to treat current node in iteration and recursion. (more conveniant and faster to run)
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def symmetric(left, right):
            result = [False, False]
            for index, (i, j) in enumerate([(left.left, right.right), (left.right, right.left)]):
                if i and j:
                    if i.val==j.val:  result[index] = symmetric(i, j)
                    else: result[index] = False
                elif not i and not j:
                    result[index] = True
                else: result[index] = False
            return result[0] and result[1]
                
        if (not root) or (not root.left and not root.right): return True
        if not root.left or not root.right: return False
        if root.left.val!=root.right.val: return False
        return symmetric(root.left, root.right)

 # faster recursive solution
 class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPiar = self.isMirror(left.right, right.left)
            return outPair and inPiar
        else:
            return False
