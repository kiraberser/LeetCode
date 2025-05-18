class Solution:
    def running_sum(self, nums):
        for i in range(1, len(nums)):
            nums[i]+=nums[i-1]
        print(nums)
        return nums

solution = Solution()
solution.running_sum(nums=[1,2,3,4])