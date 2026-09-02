# Examples:
# - "letter" -> 200
# - "aeiou" -> 0
# - "bcdf" -> 335


def consonant_group_sum(s: str) -> int:
    """回傳字串中連續子音群組的最高分數。"""
    diff = ord('a') - 81
    vowels = set('aeiou')
    max_result = result = 0
    for ch in s:
        if ch not in vowels:
            result += ord(ch) - diff
            max_result = max(max_result, result)
        else:
            max_result = max(max_result, result)
            result = 0
    return max_result
