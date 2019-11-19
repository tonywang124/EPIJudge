
from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
    # Initialize the DP table
    num_combs = [[1] + [0] * final_score for _ in individual_play_scores]

    # Build the DP table 1 row at a time
    for i in range(len(num_combs)):
        for j in range(1, final_score + 1):
            include_curr_play = num_combs[i][j - individual_play_scores[i]] if j >= individual_play_scores[i] else 0
            exclude_curr_play = num_combs[i-1][j] if i >= 0 else 0
            num_combs[i][j] = include_curr_play + exclude_curr_play
    return num_combs[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
