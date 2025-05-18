class Solution(object):
    def maximumWealth(self, accounts):
        return max(sum(acc)for acc in accounts)

solution = Solution()
accounts = [[6,59,64,19,30,76,71,86,90,25,56,17,19,72,61,56,24,40,35,39,67,28,52,11,82,72,8,82,81,47][2,5,6,75,43,2,2]]

solution.maximumWealth(accounts=accounts)

