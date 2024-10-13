import numpy as np

def latexMatrix(matrix):
    # Start the LaTeX tabular environment
    latex_code = "\\begin{pmatrix}\n"

    # Add each row of the matrix to the LaTeX code
    for row in matrix:
        latex_code += " & ".join(map(str, row)) + " \\\\\n"

    # End the LaTeX tabular environment
    latex_code += "\\end{pmatrix}"

    print(latex_code)

def latexVector(vector, orientation):
    if orientation not in ['column', 'row']:
        raise ValueError("Orientation must be 'column' or 'row'")

    # Start the LaTeX tabular environment
    if orientation == 'column':
        latex_code = "\\begin{pmatrix}\n"
        for element in vector:
            latex_code += f"{element} \\\\\n"
    else:  # orientation == 'row'
        latex_code = "\\begin{pmatrix}\n"
        latex_code += " & ".join(map(str, vector)) + " \\\\\n"

    # End the LaTeX tabular environment
    latex_code += "\\end{pmatrix}"

    print(latex_code)
