def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [i, seen[diff]]
        else:
            seen[num] = i
