# mine



#  Kadane's algorithm, O(n)
class Solution:
    # @param A, a list of integers
    # @return an integer
    # 6:57
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        for num in A[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)

        return maxSum

        # curSum = num if curSum<0 else cunrSum+num (should break down the array if the subarray has decreased to minus
        #                                            to prevent affection on next subarray)
        # maxSum = 