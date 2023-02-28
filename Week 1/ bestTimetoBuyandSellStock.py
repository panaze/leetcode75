def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    maxProfit = 0
    minPrice = float('inf')

    for i in range(len(prices)):
      if minPrice > prices[i]:
        minPrice = prices[i]
      elif prices[i] - minPrice > maxProfit:
        maxProfit = prices[i] - minPrice
    return maxProfit


def main():
  prices = [7,1,5,3,6,4]
  print(maxProfit(prices))

main()
