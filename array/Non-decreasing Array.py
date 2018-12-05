# Non-decreasing Array

# my version  O(n) time, O(1) space
# need to examine four numbers aside 
class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        flag = True 
        for i in range(1, length):
            if nums[i-1]>nums[i] and flag:
                flag = False
                if i>1 and i+1<length and nums[i-2]>nums[i] and nums[i-1]>nums[i+1]:
                    return False
            elif nums[i-1]>nums[i] and not flag:
                return False
        return True

# solusion O(n) time, O(2n) space
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        one, two = nums[:], nums[:]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                one[i] = nums[i + 1]
                two[i + 1] = nums[i]
                break
        flag1 = flag2 = True
        for i in range(len(nums) - 1):
            if one[i] > one[i+1]:
                flag1 = False
                break
        for i in range(len(nums) - 1):
            if two[i] > two[i+1]:               
                flag2 = False
                break 
        return flag1 or flag2