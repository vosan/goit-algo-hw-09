from time import perf_counter
from coins import find_coins_greedy, find_min_coins


def bench(fn, amount):
    t0 = perf_counter()
    _ = fn(amount)
    return perf_counter() - t0


for a in [10 ** 3, 10 ** 4, 10 ** 5]:
    tg = bench(find_coins_greedy, a)
    td = bench(find_min_coins, a)
    print(f"amount={a:>6} | greedy: {tg * 1e6:8.1f} µs | dp: {td * 1e6:8.1f} µs")
