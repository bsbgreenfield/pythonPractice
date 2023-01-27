def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    result_one = {digit: str(num1).count(digit) for digit in str(num1)}
    result_two = {digit: str(num2).count(digit) for digit in str(num2)}

    if result_one == result_two:
        return True
    else:
        return False