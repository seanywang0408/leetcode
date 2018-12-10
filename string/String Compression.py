# my version O(n) time, O(1) space
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if chars==[]: return 0
        pre = chars[0]
        slow = 0
        count = 1
        for fast in range(1, len(chars)):
            if chars[fast]==pre:
                count+=1
            else:
                if count!=1:      
                    for j in str(count):
                        slow+=1
                        chars[slow]=j
                slow+=1
                chars[slow]=pre=chars[fast]
                count=1
        if count!=1:
            for j in str(count):
                slow+=1
                chars[slow]=j
        return slow+1
