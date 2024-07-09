def check_brackets(string):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}
    open_brackets = set(['(', '{', '['])

    # Iterate through each character in the input string
    for char in string:
        # If the character is an open bracket, push it onto the stack
        if char in open_brackets:
            stack.append(char)
        # If the character is a closing bracket
        elif char in bracket_pairs:
            # Check if the stack is empty or the top of the stack doesn't match the current closing bracket
            if not stack or stack.pop()!= bracket_pairs[char]:
                return "Not symmetric"
    # If the stack is empty after iterating through the entire string, the brackets are symmetric
    if not stack:
        return "Symmetric"
    else:
        return "Not symmetric"

# Test cases
print(check_brackets("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # Symmetric
print(check_brackets("( 23 ( 2 - 3);"))  # Not symmetric
print(check_brackets("( 11 }"))  # Not symmetric