#!/usr/bin/python
import os,sys

def get_best_profit(stock_prices_yesterday):
    profit_list = stock_prices_yesterday.split()
    min_price = int(profit_list[0])
    max_profit = 0
    for current_price in profit_list:
        int_cur = int(current_price)
        min_price = min(min_price, int_cur)
        max_profit = max(max_profit, int_cur- min_price)
    return max_profit


def main():
    stock_prices_yesterday = []
    for line in sys.stdin:
        stock_prices_yesterday.append(line)

    best_profit = get_best_profit(stock_prices_yesterday[0])
    print best_profit

if __name__ == "__main__":
    main()
