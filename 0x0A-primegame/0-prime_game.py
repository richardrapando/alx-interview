#!/usr/bin/python3
"""Prime game module"""


def isWinner(x, nums):
    '''Prime game determining the winner'''
    import math

    def is_prime(n):
        """Checking for a prime number"""
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        val = math.isqrt(n)
        for d in range(3, val + 1, 2):
            if n % d == 0:
                return False
        return True

    def gen_prime(prime_lis):
        """Generating a prime number from a list"""
        prime = []
        for val in prime_lis:
            if is_prime(val):
                prime.append(val)
        return prime

    playe = ['X', 'Y']
    player = {'X': 0,  'Y': 0}
    for i in range(x):
        number = nums[i]
        num_lis = range(1, number)
        prime = gen_prime(num_lis)
        number = ((len(prime) + 1) % 2)
        player[playe[number]] += 1
    if player['X'] > player['Y']:
        return "Maria"
    return "Ben"
