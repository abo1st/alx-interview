#!/usr/bin/python3
"""0. Prime Game - The game between Maria and Ben"""


def isWinner(x, nums):
    """x - rounds
    nums - numbers list
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    az = [1 for x in range(sorted(nums)[-1] + 1)]
    az[0], az[1] = 0, 0
    for iz in range(2, len(az)):
        rm_multiples(az, iz)

    for iz in nums:
        if sum(az[0:iz + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """removes multiple
    of primes
    """
    for iz in range(2, len(ls)):
        try:
            ls[iz * x] = 0
        except (ValueError, IndexError):
            break
