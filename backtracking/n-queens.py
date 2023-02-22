def solve_n_queens(n):
    def backtracking(solutionB, row, results):
        if row == n:
            results.append(solutionB[:])
            return

        for j in range(n):
            if is_valid_move(row, j, solutionB):
                solutionB[row] = j
                backtracking(solutionB, row + 1, results)

    def is_valid_move(proposed_row, proposed_col, solutionI):
        for row in range(proposed_row):
            old_row = row
            old_col = solutionI[row]
            diagonal_offset = proposed_row - old_row
            if old_col == proposed_col or old_col == proposed_col - diagonal_offset or old_col == proposed_col + diagonal_offset:
                return False
        return True

    result = []
    solution = [-1] * n
    backtracking(solution, 0, result)

    return result


if __name__ == '__main__':
    for i in range(1, 10):
        print(solve_n_queens(i))
