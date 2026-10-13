"""Program 23: Sort a List Without Using sort()."""

def bubble_sort(numbers):
    """Return a new sorted list in ascending order without modifying the original."""
    arr = list(numbers)
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    nums = [5, 2, 9, 1]
    print("Sorted list:", bubble_sort(nums))
