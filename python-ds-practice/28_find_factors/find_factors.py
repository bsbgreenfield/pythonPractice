def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    factors = {1, num}
    for integer in range(2, num - 1):
        if integer not in factors and num % integer == 0:
            factors.add(integer)
            factors.add(int(num/integer))
    answer = list(factors)
    answer.sort()
    return answer


find_factors(12291098232)