from test_framework import generic_test
from collections import OrderedDict

def intersect_two_sorted_arrays(A, B):
    # Better empirical runtime: O(k * logk) where k == len(intersection)
    # If the intersection approaches max(N, M), then runtime approaches N log N
    # Much better performance assuming k much smaller than max(N, M)
    return [val for val in sorted(set(A).intersection(set(B)))]

"""
#This solution has better theoretical runtime: O(N + M).
    set_A = OrderedDict()
    set_B = OrderedDict()
    for i in A:
        set_A[i] = True
    for j in B:
        set_B[j] = True
    return [val for val in set_A if val in set_B]
"""

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intersect_sorted_arrays.py",
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
