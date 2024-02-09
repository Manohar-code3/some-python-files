from constraint import Problem


def eight_queens():
    problem = Problem()

    # Define the variables for each column, representing the row where a queen is placed.
    for i in range(8):
        problem.addVariable(i, range(8))

    # Define the constraints to ensure queens don't threaten each other.
    for i in range(8):
        for j in range(i + 1, 8):
            problem.addConstraint(lambda x, y, i=i, j=j: x !=
                                  y and abs(x - y) != j - i, (i, j))

    # Find a solution
    solutions = problem.getSolutions()

    return solutions


def print_solution(solution):
    for i in range(8):
        row = [solution[j] for j in range(8) if j == i]
        print(" ".join("Q" if i == row[0] else "." for i in range(8)))


solutions = eight_queens()
if solutions:
    print("Solution found:")
    print_solution(solutions[0])
else:
    print("No solution found.")