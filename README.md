# MERGE

## Algorithm

1. Sort the input array by the first index(low) of interval.
2. Merge the interval one by one. If the current interval in the input and the last interval of the result do not overlap, append the current interval from input to result. Else merge the current interval into the last interval of the result.

## Boundaries

If the given input is empty, an empty output will be returned.

If any of these checks failed, user defined `InputError` will be raised:

* Check each interval has only two entries, the first is low and the second is high.
* Check low is less than high for each interval. (Not "less or equal")


## Complexity Analysis

Assume we have N intervals to merge.


Sort(Python build-in sort use Timsort) takes O(NlogN) time and no additional space(in place sort). 
Merge one by one takes O(N) time and O(N) space, since it generate the result.


Therefore, overall time complexity would be O(NlogN), space complexity would be O(N).

## For Tremendous Input

This algorithm can be easily implemented mapreduce-wise. We can partition the input array into subarrays and apply `MERGE` to each subarray. Afterwards we merge the `MERGED` subarray into the end result.