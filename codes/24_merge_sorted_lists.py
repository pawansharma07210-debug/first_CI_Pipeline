"""Program 24: Merge Two Sorted Lists."""

def merge_sorted_lists(list1, list2):
    """Return one merged sorted list containing all elements of both sorted lists."""
    merged = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    while i < len(list1):
        merged.append(list1[i])
        i += 1
    while j < len(list2):
        merged.append(list2[j])
        j += 1
    return merged

if __name__ == "__main__":
    l1 = [1, 3, 5]
    l2 = [2, 4]
    print("Merged:", merge_sorted_lists(l1, l2))
