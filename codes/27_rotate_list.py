"""Program 27: Rotate a List by K Positions."""

def rotate_list(items, k):
    """Rotate items to the right by k positions and return a new list."""
    if not items:
        return []
    n = len(items)
    effective_k = k % n
    if effective_k == 0:
        return list(items)
    return list(items[-effective_k:]) + list(items[:-effective_k])

if __name__ == "__main__":
    print("Rotated:", rotate_list([1, 2, 3, 4, 5], 2))
