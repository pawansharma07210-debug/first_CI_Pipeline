"""Program 22: Check Anagram Strings."""

def is_anagram(first, second):
    """Return True if two strings are anagrams, ignoring case and spaces."""
    cleaned_first = "".join(ch.lower() for ch in first if not ch.isspace())
    cleaned_second = "".join(ch.lower() for ch in second if not ch.isspace())
    
    char_count = {}
    for ch in cleaned_first:
        char_count[ch] = char_count.get(ch, 0) + 1
    for ch in cleaned_second:
        if ch not in char_count:
            return False
        char_count[ch] -= 1
        if char_count[ch] < 0:
            return False
    return all(v == 0 for v in char_count.values())

if __name__ == "__main__":
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    print("Is anagram:", is_anagram(s1, s2))
