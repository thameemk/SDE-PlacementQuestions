#  Project : SDE Placement Questions
#  Filename : main.py
#  Author : blacklist
#  Current modification time : Thu, 8 Sep 2022 at 10:32 pm India Standard Time
#  Last modified time : Thu, 8 Sep 2022 at 10:32 pm India Standard Time

"""
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


from typing import List


def max_profit(prices: List[int]) -> int:

    buy_at = 10000
    profit = 0
    maximum_profit = 0

    for price in prices:
        if buy_at > price:
            buy_at = price

        profit = price - buy_at

        if maximum_profit < profit:
            maximum_profit = profit

    return maximum_profit


if __name__ == '__main__':
    print(max_profit(prices=[7, 1, 5, 3, 6, 4]))
