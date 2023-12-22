from bisect import insort_left
from collections import defaultdict


def topKFrequent(nums: list[int], k: int) -> list[int]:
    most_frequent = [None] * k
    frequencies = defaultdict(int)
    frequencies[None] = 0

    for num in nums:
        frequencies[num] += 1
    for num, freq in frequencies.items():
        if freq > frequencies[most_frequent[0]]:
            most_frequent = most_frequent[1:]
            insort_left(most_frequent, num, key=lambda x: frequencies[x])
    return most_frequent
