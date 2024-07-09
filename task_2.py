from collections import deque

def is_palindrome(string):
    # Remove spaces and convert to lowercase to ignore case and spaces
    string = string.replace(" ", "").lower()
    
    # Create a deque from the string characters
    char_deque = deque(string)
    
    # Compare characters from both ends of the deque
    while len(char_deque) > 1:
        if char_deque.popleft()!= char_deque.pop():
            return False
    
    return True

# Test cases
print(is_palindrome("Madam"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("A man a"))  # True
print(is_palindrome("Not a palindrome"))  # False
print(is_palindrome(" Radar"))  # True
print(is_palindrome("Level"))  # True
print(is_palindrome("Deed"))  # True
print(is_palindrome("No 'x' in Nixon"))  # True
print(is_palindrome("Was it a car or a cat I saw?"))  # True