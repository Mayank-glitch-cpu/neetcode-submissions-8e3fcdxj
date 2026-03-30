class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        buy=0
        sell=0
        profit=0
        for i in range(len(prices)):
            if prices[buy]<=prices[sell]:
                profit= prices[sell]-prices[buy]
                max_profit= max(profit,max_profit)
                sell+=1
                print('sell index at i ',i,'',sell)
                print('MaxProfit ',max_profit)
            else:
                buy =sell
                sell+=1
                print('Buy index at i ','',buy)
                print('sell index at i ',i,'',sell)
        print('Final Max Profit',max_profit)
        return max_profit