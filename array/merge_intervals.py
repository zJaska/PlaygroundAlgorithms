# It's a common problem where we need to produce in output an array without overlapping intervals

from typing import List

def merge_array(intervals: List[List[int]])  -> List[int] :
    """
    We assume that the arrays are ordered in an ascending manner
    """

    if not intervals:
        raise ValueError("Intervals is empty!!")
    
    intervals.sort(key=lambda x: x[0]) # to be sure, we reorder on left value of interval

    merged = intervals[0]

    for current in intervals[1:]:
        last = intervals[-1]
        if current[0] <= last[1]:
            merged[-1] = [last[0], max(current[1], last[1])]
        else:
            merged.append(current)

    return merged