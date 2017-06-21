import math
import random

def odds(n, k, p=0.5):
    if n == k:
        c = 1
    elif k == 1:
        c = n
    else:
        c = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return c * (p ** k) * ((1 - p) ** (n - k))


def odds_ge(n, k, p=0.5):
    if n < k:
        return 0.0
    return odds(n, k, p) + odds_ge(n, k + 1, p)


def roll(dice=1):
    succ = 0
    for _ in range(dice):
        if random.randint(1, 6) > 3:
            succ += 1
    return succ


def attk(attack, defense, damage, armor):
    mos = roll(attack) - roll(defense)
    if mos < 1:
        return 0
    return max(0, mos + roll(damage) - armor)
