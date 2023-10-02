import sympy as sp

def solve_quadratic_equation(coefficients):
    solutions = []

    for a, b, c in coefficients:
        # Define the variables and the quadratic equation
        x = sp.symbols('x')
        equation = a * x**2 + b * x + c - 100

        # Solve the quadratic equation
        quadratic_solutions = sp.solve(equation, x)

        # Add the solutions to the list
        solutions.extend(quadratic_solutions)

    return solutions

# Example usage:
coefficients = [(1, -30, 229), (2, 5, -105)]
solutions = solve_quadratic_equation(coefficients)

print("Solutions to 100 = ax^2 + bx + c:")
for solution in solutions:
    print(f"x = {solution}")
