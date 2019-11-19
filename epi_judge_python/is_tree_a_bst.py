from test_framework import generic_test
from collections import namedtuple
from collections import deque

def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    """ 
    # Recursive approach has O(N) time and O(N) stack space complexity
    def are_keys_in_range(tree, low_range, high_range):
        if not tree:
            return True
        elif not low_range <= tree.data <= high_range:
            return False
        return (are_keys_in_range(tree.left, low_range, tree.data) and
                are_keys_in_range(tree.right, tree.data, high_range))
    return(are_keys_in_range(tree, low_range, high_range))
    """
    entry = namedtuple('entry', ('node', 'lower', 'upper'))
    bfs_queue = deque([entry(tree, low_range, high_range)])
    while bfs_queue:
        front = bfs_queue.popleft()
        if front.node:
            if not front.lower <= front.node.data <= front.upper:
                return False
            bfs_queue.append(entry(front.node.left, front.lower, front.node.data))
            bfs_queue.append(entry(front.node.right, front.node.data, front.upper))
    return True

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
