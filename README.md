# MERGE

## Algorithm
1. Sort the input array by the first index(low) of interval.
2. Merge the interval one by one. If the current interval and the last interval do not overlap, append the current interval to result. Else merge and update the last interval in result.

## Boundaries
If given input is empty, an empty output will be returned.

If any of these checks failed, user defined InputError will be raised:

* Check each interval has only two entries, the first is low and the second is high.
* Check low is less than high for each interval. (Not "less or equal")




## Complexity Analysis
Assume we have N intervals to merge.
Sort(Python build-in sort use Timsort) takes O(NlogN) time and no additional space. 
Merge one by one takes O(N) time and O(N) space, since it generate the result.

Therefore, overall time complexity would be O(NlogN), space complexity would be O(N).

## For tremendous input size
This algorithm can be easily implemented mapreduce-wise. We can partition the input array into subarrays and apply MERGE to each subarray.