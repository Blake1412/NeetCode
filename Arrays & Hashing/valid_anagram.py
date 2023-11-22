def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq_one, freq_two = {}, {}

    for i, char_one in enumerate(s):
        char_two = t[i]
        if char_one in freq_one:
            freq_one[char_one] += 1
        else:
            freq_one[char_one] = 1

        if char_two in freq_two:
            freq_two[char_two] += 1
        else:
            freq_two[char_two] = 1

    return freq_one == freq_two
