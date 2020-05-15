"""
Problem Link : "https://leetcode.com/problems/maximum-sum-circular-subarray/"

"""

class MaximumSumCircularSubarray:

    def maxSubarraySum(self, nums):
        total_sum = max_sum = nums[0]

        for i in range(1, len(nums)):
            total_sum = max(nums[i], total_sum + nums[i])
            max_sum = max(max_sum, total_sum)

        return max_sum

    def maxSubarraySumCircular(self, A) -> int:
        original_subarray_sum = self.maxSubarraySum(A)

        sum_array = sum(A)
        negative_temp_array = []
        for each in A:
            negative_temp_array.append(-each)

        negative_subarray_sum = self.maxSubarraySum(negative_temp_array)

        if negative_subarray_sum + sum_array > original_subarray_sum and negative_subarray_sum + sum_array != 0:
            return negative_subarray_sum + sum_array
        return original_subarray_sum

obj = MaximumSumCircularSubarray()
print(obj.maxSubarraySumCircular([3, -2, 2, -3]))
print(obj.maxSubarraySumCircular([3, -1, 2, -1]))
print(obj.maxSubarraySumCircular([-2, -3, -1]))
print(obj.maxSubarraySumCircular([5, -3, 5]))
print(obj.maxSubarraySumCircular([1, -2, 3, -2]))
