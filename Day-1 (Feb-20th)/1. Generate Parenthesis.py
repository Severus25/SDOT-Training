# Leetcode - 22
def backtrack(current, open_count, close_count):
        # Base case: If the current combination has reached the desired length (2 * n),
        # add it to the result list.
        if len(current) == 2 * n:
            result.append(current)
            return

        # If the number of open parentheses is less than n,
        # add an open parenthesis and backtrack.
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)

        # If the number of close parentheses is less than the number of open parentheses,
        # add a close parenthesis and backtrack.
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    result = []
    # Start the backtracking with an empty current combination and initial counts of open and close parentheses.
    backtrack('', 0, 0)
    return result
