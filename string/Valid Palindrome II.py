# my version O(n) time, O(1) space
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s)-1
        changed = False
        while l<r:
            if s[l]!=s[r]:
                one = s[:l]+s[l+1:]
                two = s[:r]+s[r+1:]
                break
            l+=1; r-=1
        if l>=r :return True
        return one==one[::-1] or two==two[::-1]


# simpler one O(n) time, O(1) space
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True