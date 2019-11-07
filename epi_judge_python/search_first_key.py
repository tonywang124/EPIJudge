from test_framework import generic_test
import bisect

def search_first_of_k(A, k):
    l, u, result = 0, len(A)-1, -1
    while l <= u:
        pivot = l + (abs(u - l) // 2) # Prevents overflow
        if A[pivot] == k:
            result = pivot
            u = pivot - 1
        elif A[pivot] > k:
            u = pivot - 1
        else:
            l = pivot + 1
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
