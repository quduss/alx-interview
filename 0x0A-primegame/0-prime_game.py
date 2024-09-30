#!/usr/bin/python3
'''
solution for solving the prime game
'''


def is_prime(x):
    '''
    Checks if x is a prime number
    '''
    if x == 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def isWinner(n, nums):
    '''
    Solves the prime game between Maria an Ben
    '''
    if n <= 0 or len(nums) == 0 or len(nums) < n:
        return None
    result = {"Maria": 0, "Ben": 0}
    for i in range(n):
        primes = []
        for j in range(1, nums[i] + 1):
            if is_prime(j):
                primes.append(j)
        if len(primes) % 2 == 0:
            result['Ben'] += 1
        else:
            result['Maria'] += 1
    if result['Maria'] > result['Ben']:
        return 'Maria'
    elif result['Maria'] < result['Ben']:
        return 'Ben'
    else:
        return None
