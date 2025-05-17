class Solution(object):
  def twoSum(self, nums, target):
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])
            return [i, j]
          
solution = Solution()
solution.twoSum(nums=[10, 5, 11, 15, 7, 4], target=9)
