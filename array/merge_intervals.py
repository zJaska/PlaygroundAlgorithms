# It's a common problem where we need to produce in output an array without overlapping intervals

from typing import List

def merge_array(intervals: List[List[int]])  -> List[int] :
    """
    We assume that the arrays are ordered in an ascending manner
    """

    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0]) # to be sure

    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]: # Se l'ultimo ha un intervallo più a destra del current estremo sx, per forza sovrapposizione
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            merged.append(current)

    return merged