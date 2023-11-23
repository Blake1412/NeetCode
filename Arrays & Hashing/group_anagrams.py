from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    grouped_anagrams = defaultdict(list)
    for s in strs:
        chars = [0] * 26
        for char in s:
            chars[ord(char) - ord("a")] += 1
        grouped_anagrams[tuple(chars)].append(s)
    return grouped_anagrams.values()



