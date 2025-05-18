class Solution(object):
    def maximumWealth(self, accounts):
        sum_accounts=[]
        sum_total = 0
        max_account = 0
        for a in accounts:
            if len(accounts) == 1:
                for q in a:
                    max_account+=q
                return max_account
            else:
                if sum_total > 0:
                    sum_total=0
                for c in a:
                    sum_total+=c
                sum_accounts.append(sum_total)
        for i in range(1, len(sum_accounts)):
            if sum_accounts[i-1] >= sum_accounts[i] and sum_accounts[i-1] > max_account:
                max_account = sum_accounts[i-1]
        return max_account

solution = Solution()
accounts = [[6,59,64,19,30,76,71,86,90,25,56,17,19,72,61,56,24,40,35,39,67,28,52,11,82,72,8,82,81,47]]

solution.maximumWealth(accounts=accounts)

