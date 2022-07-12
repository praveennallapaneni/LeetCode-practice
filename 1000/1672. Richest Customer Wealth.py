class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        maxMoney = 0
        
        for person in range(len(accounts)):
            money = 0 
            for bank in accounts[person]:
                money += bank
            
            maxMoney = max(maxMoney, money)

        return maxMoney
