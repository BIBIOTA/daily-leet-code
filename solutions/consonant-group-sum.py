from collections import defaultdict

VOWELS = set("aeiou")
BASE_VALUE = 81  # a -> 81, b -> 82, ...

# Examples:
# Input: "letter"  → consonant groups: ["l"]=92, ["tt"]=200, ["r"]=98  → Output: 200
# Input: "aeiou"   → no consonant groups                                → Output: 0


def consonant_group_sum(s: str) -> int:
    groups = defaultdict(list)
    groups_index = 0
    for ch in s:
        if ch not in VOWELS:
            groups[groups_index].append(ch)
        else:
            groups_index += 1
    base_value_diff = ord('a') - BASE_VALUE
    max_sum = 0
    for group in groups.values():
        current_sum = sum(ord(ch) - base_value_diff for ch in group)
        max_sum = max(current_sum, max_sum)
    return max_sum