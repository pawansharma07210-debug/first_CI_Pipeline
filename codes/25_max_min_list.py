"""Program 25: Find the Maximum and Minimum in a List."""

def find_max_min(numbers):
    """Return a tuple (maximum, minimum). Raise ValueError for an empty list."""
    if not numbers:
        raise ValueError("List cannot be empty")
    
    current_max = numbers[0]
    current_min = numbers[0]
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        if num < current_min:
            current_min = num
    return (current_max, current_min)

if __name__ == "__main__":
    nums = [4, 9, 1, 7]
    print("Max and Min:", find_max_min(nums))
