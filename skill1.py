def arithmetic_arranger(problems, display_answers=False):
    # 1. Check too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes = []
    results = []

    for problem in problems:
        parts = problem.split()

        if len(parts) != 3:
            return "Error: Invalid format."

        first, operator, second = parts

        # 2. Check operator
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # 3. Check digits
        if not (first.isdigit() and second.isdigit()):
            return "Error: Numbers must only contain digits."

        # 4. Check length
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."

        # 5. Format problem
        width = max(len(first), len(second)) + 2  # +2 for operator and space

        top = first.rjust(width)
        bottom = operator + second.rjust(width - 1)
        dash = "-" * width

        first_line.append(top)
        second_line.append(bottom)
        dashes.append(dash)

        if display_answers:
            if operator == "+":
                answer = str(int(first) + int(second))
            else:
                answer = str(int(first) - int(second))
            results.append(answer.rjust(width))

    # 6. Combine with four spaces
    arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(dashes)

    if display_answers:
        arranged_problems += "\n" + "    ".join(results)

    return arranged_problems
