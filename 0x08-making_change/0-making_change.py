#!/usr/bin/python3
"""makeChange function definition"""


def makeChange(coins, total):
    """determines the fewest number of coins needed to meet a total"""
    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if total == 0:
            break
        # Use as many of the largest coin as possible
        num_coins = total // coin
        count += num_coins
        total -= num_coins * coin

    # If the total couldn't be made with the given coins
    if total != 0:
        return -1
    return count
