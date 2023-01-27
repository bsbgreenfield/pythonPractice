def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    answer = 0
    if start and 0 <= start <= len(nums)-1:
        start_point = start
    else:
        start_point = 0

    if end and 0 <= end <= len(nums)-1:
        end_point = end + 1
    else:
        end_point = len(nums)

    for num in nums[start_point: end_point]:
        answer += num

    return answer