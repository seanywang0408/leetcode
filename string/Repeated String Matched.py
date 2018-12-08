# solution O(1) time, O (1) space
class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        times = -(-len(B)//len(A))
        for i in range(times, times+2):
            if B in A*(i):
                return i
        return -1

'''
1. the answer can either be -(-len(B)//len(A)) or -(-len(B)//len(A))+1
for len(t*a) should at least >= len(b), and if the solution ever exists, 
it should have occured at t+1