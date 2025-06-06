# This is script to calculate the longest substring in an array!!


def longest_substring(s: str) -> int:
    if s is None:
        raise ValueError("The string is empty!!")
    
    char_map = {}
    start = 0
    max_len = 0
    
    for end in range(len(s)):
        char = s[end]

        if char in char_map and char_map[char] >= start:
            start = char_map[char] + 1
        
        char_map[char] = end

        max_len = max(max_len, end-start+1)
    
    return max_len

print(longest_substring("abcabcbb"))  # Output: 3 ("abc")
print(longest_substring("bbbbb"))     # Output: 1 ("b")
print(longest_substring("pwwkew"))    # Output: 3 ("wke")
