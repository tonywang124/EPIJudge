from test_framework import generic_test
import heapq

def merge_sorted_arrays(sorted_arrays):
    arrays = [iter(array) for array in sorted_arrays]
    min_heap = []
    for index, array_iter in enumerate(arrays):
        smallest = next(array_iter, None)
        if smallest is not None:
            heapq.heappush(min_heap, (smallest, index))

    result = []
    while min_heap:
        smallest, index = heapq.heappop(min_heap)
        array_iter = arrays[index]
        result.append(smallest)
        next_element = next(array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, index))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
