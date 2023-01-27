def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    open_count = 0
    close_count = 0
    is_valid = False
    if parens[0] == ")":
        return False
    for char in parens:
        if char == '(':
            open_count += 1
            is_valid = False
        else:
            close_count += 1
            is_valid = False
        if close_count == open_count:
            open_count = 0
            close_count = 0
            is_valid = True
    if is_valid:
        return True
    else:
        return False


