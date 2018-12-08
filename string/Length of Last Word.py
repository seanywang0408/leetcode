# my version
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = len(s)-1
        while p>=0 and not s[p].isalpha(): p-=1
        count = 0
        while p>=0 and s[p].isalpha():
            p-=1; count+=1
        return count

# use str.split()
# str.split() split by all kinds of blank char, including ' ', '\n', '\t' ,'\0' by default
# if given char, there can be only one
# at the end of string lies a '\0', we can't use str.split(' ') here
# which leads to suggestion that we'd better use str.split() by default, giving no params
 class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        if words == []:return 0
        else: return len(words[-1])