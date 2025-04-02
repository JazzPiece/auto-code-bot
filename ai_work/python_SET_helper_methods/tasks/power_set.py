def power_set(s):
    from itertools import chain, combinations
    return set(chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

s = {1, 2, 3}
print(power_set(s))