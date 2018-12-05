

# to find if the greatest common divesor of numbers of all the existing numbers is > 1
class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        from functools import reduce
        def gcd(a,b):
            while b:
                a, b = b, a % b
            return a
        count = collections.Counter(deck).values()
        return reduce(gcd, count) > 1

        # gcd(a,b) is to find the greatest common divisor of a and b
try