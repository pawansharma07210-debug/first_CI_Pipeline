"""Program 26: Find the Sum of Elements in a List."""

def sum_of_list(numbers):
    """Return the sum of elements in a list using a loop. Empty list gives 0."""
    total = 0
    for num in numbers:
        total += num
    return total

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print("Sum:", sum_of_list(nums))
