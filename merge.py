from Error import InputError

"""
Main module of merge.
"""
__author__ = "Yinchi Wexort Luo"
__email__ = "yinchi.luo@gmail.com"


def merge(list_to_merge):
    if not list_to_merge:
        return []

    if not is_valid_input(list_to_merge):
        raise InputError('invalid input')

    # inplace sort input list according to the low (first entry) of each interval
    list_to_merge.sort(key=lambda ls: ls[0])

    res = []
    for i in range(len(list_to_merge)):
        interval = list_to_merge[i]
        if not res:  # init res
            res.append(interval)

        # If the current interval in the input and the last interval of the result do not overlap, append the current interval from input to result
        # Else merge the current interval into the last interval of the result.
        if not is_overlapping(interval, res[-1]):
            res.append(interval)
        else:
            res[-1] = merge_interval(res[-1], interval)
    return res


def merge_interval(interval_a, interval_b):
    return [min(interval_a[0], interval_b[0]), max(interval_a[1], interval_b[1])]


def is_overlapping(interval_a, interval_b):
    if interval_a[0] > interval_b[0]:
        interval_a, interval_b = interval_b, interval_a
    return interval_a[1] >= interval_b[0]


def is_valid_input(input):
    for interval in input:
        if not is_valid_interval(interval):
            return False
    return True


def is_valid_interval(interval):
    return len(interval) == 2 and interval[0] < interval[1]
