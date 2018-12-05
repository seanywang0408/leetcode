
# Cyclic Replacements ?

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums) 
        k = k % length
        T = n//k
            
        for i in range(k):
            if T*k+i<length:
                tmp = nums[T*k+i]
                nums[T*k+i] = nums[(T-1)*k+i]
            for j in range(T-1, 0, -1):
                nums[j*k+i]=nums[(j-1)*k+i]
            nums[i]=


# Using Reverse
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]