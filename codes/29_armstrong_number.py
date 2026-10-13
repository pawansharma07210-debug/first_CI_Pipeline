"""Program 29: Check Armstrong Number."""

def is_armstrong(number):
    """Return True if number is an Armstrong number; negative returns False."""
    if number < 0:
        return False
    digits = [int(d) for d in str(number)]
    num_digits = len(digits)
    total = sum(d ** num_digits for d in digits)
    return total == number

if __name__ == "__main__":
    num = 153
    print(f"Is {num} armstrong:", is_armstrong(num))
