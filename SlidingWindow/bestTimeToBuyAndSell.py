# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a 
# different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.

prices = [7,1,5,3,6,4]

def maxProfit(prices:list[int]) -> int:
    maxProfit = 0   # default case 
    l = 0           # left pointer = buy
    r = l + 1       # right pointer = sell
    while l != len(prices)-1 :
        min = prices[l]
        max = prices[r]
        profit = max - min
        
        if profit > maxProfit: 
            maxProfit = profit
        # If no profit will return his base value = 0
        r +=1 # Increment the right pointer,
        
        if r > len(prices)-1:
            l += 1
            r = l + 1 #  it's time based, so the right pointer should always be after left pointer 
    return maxProfit

def solution(prices:list[int]) -> int:
    maxProfit = 0   # default case 
    l = 0           # left pointer = buy
    r = 1      # right pointer = sell
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else :
            l = r # prices[l] > prices[r] r is lower than l 
            # actual lowest price is found and we want to shif the left pointer to it to avoid to test others that we know will have a lo
        r += 1
    return maxP
         

print("Max profit is: ",maxProfit(prices))

