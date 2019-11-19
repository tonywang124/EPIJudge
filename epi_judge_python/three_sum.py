from test_framework import generic_test


def has_three_sum(A, t):
    # Start by sorting
    A.sort()
    for i in range(len(A)):
        sub_target = t - A[i]
        j, k = 0, len(A) - 1
        while j <= k:
            remainder = A[j] + A[k]
            if remainder < sub_target:
                j += 1
            elif remainder == sub_target:
                return True
            else:
                k -= 1
    return False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
