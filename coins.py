DENOMINATIONS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount: int) -> dict[int, int]:
    """Return coin counts using a greedy strategy for the given amount.
    Uses denominations [50, 25, 10, 5, 2, 1]. Raises ValueError for negatives.
    """
    if amount < 0:
        raise ValueError("amount must be non-negative")
    result: dict[int, int] = {}
    remaining = amount
    for coin in DENOMINATIONS:
        if remaining == 0:
            break
        cnt, remaining = divmod(remaining, coin)
        if cnt:
            result[coin] = cnt
    return result


def find_min_coins(amount: int) -> dict[int, int]:
    """Return coin counts with the minimal total number of coins via DP.
    Uses denominations [50, 25, 10, 5, 2, 1]. Raises ValueError for negatives.
    """
    if amount < 0:
        raise ValueError("amount must be non-negative")
    if amount == 0:
        return {}

    # DP arrays: min_coins[s] = minimal coin count to make sum s; prev_coin[s] = coin used last
    inf = amount + 1
    min_coins = [0] + [inf] * amount
    prev_coin = [0] * (amount + 1)

    for coin in DENOMINATIONS:
        for s in range(coin, amount + 1):
            if min_coins[s - coin] + 1 < min_coins[s]:
                min_coins[s] = min_coins[s - coin] + 1
                prev_coin[s] = coin

    if min_coins[amount] == inf:
        raise ValueError("amount cannot be composed with given denominations")

    # Reconstruct coin counts
    result: dict[int, int] = {}
    s = amount
    while s > 0:
        c = prev_coin[s]
        result[c] = result.get(c, 0) + 1
        s -= c
    return result


print(find_coins_greedy(113))  # {50: 2, 10: 1, 2: 1, 1: 1}
print(find_min_coins(113))  # {1: 1, 2: 1, 10: 1, 50: 2}
