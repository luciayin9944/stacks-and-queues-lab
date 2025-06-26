def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    # TODO: Implement stack logic to validate parentheses
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        if char not in pairs:
            stack.append(char)
            continue
        if not stack or stack.pop() != pairs[char]:
            return False
        
    return True if not stack else False
            
        
