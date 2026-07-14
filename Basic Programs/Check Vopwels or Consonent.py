def check_vowel_or_consonant(char):
    char = char.lower()
    if not char.isalpha() or len(char) != 1:
        return "Invalid input (Please enter a single alphabet letter)"
    
    if char in 'aeiou':
        return "Vowel"
    else:
        return "Consonant"

# Example
print(check_vowel_or_consonant('E'))  # Output: Vowel
print(check_vowel_or_consonant('z'))  # Output: Consonant