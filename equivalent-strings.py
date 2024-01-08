from functools import lru_cache
a = input()
b = input()

@lru_cache(maxsize=None)
def are_equivalent(a, b):
    if a == b:
        return "YES"
    
    if len(a) % 2 != 0:
        return "NO"


    half_len = len(a) // 2
    a1, a2 = a[:half_len], a[half_len:]
    b1, b2 = b[:half_len], b[half_len:]

    if (are_equivalent(a1, b1) == "YES" and are_equivalent(a2, b2) == "YES") or (are_equivalent(a1, b2) == "YES" and are_equivalent(a2, b1) == "YES"):
        return "YES"
    
    return "NO"

print(are_equivalent(a, b))
