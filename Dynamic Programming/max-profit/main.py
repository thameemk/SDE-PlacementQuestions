#  Project : SDE Placement Questions
#  Filename : main.py
#  Author : blacklist
#  Current modification time : Thu, 8 Sep 2022 at 10:32 pm India Standard Time
#  Last modified time : Thu, 8 Sep 2022 at 10:32 pm India Standard Time

"""
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


def max_profit(prices: list[int]) -> int:
    # todo - not correct
    maximum_profit = 0
    for i in range(1, len(prices)):
        current_profit = prices[i] - prices[i - 1]
        if prices[i] > prices[i - 1]:
            maximum_profit = max(current_profit, maximum_profit)

    return maximum_profit


if __name__ == '__main__':
    print(max_profit(prices=[7, 1, 5, 3, 6, 4]))
