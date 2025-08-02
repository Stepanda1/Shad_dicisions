prices = [7,6,4,3,1]

def MaxProfit(prices):
    for i in range(len(prices)):
        if min(prices) == prices[i]:
            minIndex = i
            minn = prices[i]
    maxx = 0
    for j in range(minIndex, len(prices)):
        if maxx <= prices[j]:
            maxx = prices[j]
    return maxx - minn
    
print(MaxProfit(prices))