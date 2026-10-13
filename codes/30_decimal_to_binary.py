"""Program 30: Convert Decimal to Binary Without Using bin()."""

def decimal_to_binary(number):
    """Convert non-negative integer to binary string using division by 2.
    0 returns '0'; negative raises ValueError.
    """
    if number < 0:
        raise ValueError("Negative numbers not allowed")
    if number == 0:
        return "0"
    
    bits = []
    n = number
    while n > 0:
        bits.append(str(n % 2))
        n = n // 2
    bits.reverse()
    return "".join(bits)

if __name__ == "__main__":
    print("10 in binary:", decimal_to_binary(10))
