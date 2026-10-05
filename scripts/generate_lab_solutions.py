"""
Script to assemble notebooks/LinearAlgebra_Lab_Solutions.ipynb
"""

import nbformat as nbf
from lab_solutions_1_4 import (
    get_lab_intro_cells,
    get_lab1_cells,
    get_lab2_cells,
    get_lab3_cells,
    get_lab4_cells
)
from lab_solutions_5_8 import (
    get_lab5_cells,
    get_lab6_cells,
    get_lab7_cells,
    get_lab8_cells
)

def build_lab_notebook():
    nb = nbf.v4.new_notebook()
    all_cells = []

    # Intro, coverage map & shared SymPy environment
    all_cells.extend(get_lab_intro_cells())

    # Labs 1 to 4
    all_cells.extend(get_lab1_cells())
    all_cells.extend(get_lab2_cells())
    all_cells.extend(get_lab3_cells())
    all_cells.extend(get_lab4_cells())

    # Labs 5 to 8
    all_cells.extend(get_lab5_cells())
    all_cells.extend(get_lab6_cells())
    all_cells.extend(get_lab7_cells())
    all_cells.extend(get_lab8_cells())

    nb.cells = all_cells

    # Metadata
    nb.metadata = {
        "kernelspec": {
            "display_name": "Python 3 (linalg-venv)",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.11"
        }
    }

    out_path = 'notebooks/LinearAlgebra_Lab_Solutions.ipynb'
    with open(out_path, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)

    print(f"Successfully generated {out_path} with {len(all_cells)} cells!")


if __name__ == '__main__':
    build_lab_notebook()
