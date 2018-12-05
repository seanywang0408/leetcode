# my version
# slow and fast pointer

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        if nums==[]:
            return 0
        l = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                l += 1
                nums[l]=nums[i]
        return l+1

