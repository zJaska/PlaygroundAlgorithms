# In this script we implement kadane's algorithm 
# Kadane’s algorithm computes the maximum subarray sum of a given array A.

from typing import List

def kadane_algorithm(array_element: List[float] ) -> float:

    if array_element is None:
        raise ValueError("Array is empty")

    max_sum = current_sum = array_element[0]


    for number in (array_element[1:]):
        if(current_sum<0):
            current_sum=number
        else:
            current_sum+=number

        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum
            
        


