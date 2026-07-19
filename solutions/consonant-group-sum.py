VOWELS = set("aeiou")

# Character value: 'a'=81, 'b'=82, ..., 'z'=106  (ord(ch) - 16)
#
# Examples:
# Input: "letter"  → consonant groups: "l"=92, "tt"=200, "r"=98  → Output: 200
# Input: "aeiou"   → no consonant groups                          → Output: 0
# Input: "bcdf"    → one consonant group "bcdf"=82+83+84+86=335   → Output: 335


def consonant_group_sum(s: str) -> int:
    max_sum = group_sum = 0
    diff = ord('a') - 81
    for ch in s:
        if ch not in VOWELS:
            group_sum += ord(ch) - diff
            max_sum = max(max_sum, group_sum)
        else:
            group_sum = 0
    return max_sum
