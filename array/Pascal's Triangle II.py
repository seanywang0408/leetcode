# Pascal's Triangle II

# my version
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rlist = [1]*(rowIndex+1)
        for i in range(1, rowIndex+1):
            tmp1 = 1
            for j in range(i-1):
                tmp2 = rlist[j+1]
                rlist[j+1] += tmp1
                tmp1 = tmp2            
        return rlist

# genius version
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row


