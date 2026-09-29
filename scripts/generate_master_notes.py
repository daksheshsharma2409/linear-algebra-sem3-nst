"""
Script to assemble notebooks/LinearAlgebra_Master_Notes.ipynb
"""

import nbformat as nbf
from master_sections_1_4 import (
    get_setup_cells,
    get_lecture1_cells,
    get_lecture2_cells,
    get_lecture3_cells,
    get_lecture4_cells
)
from master_sections_5_8 import (
    get_lecture5_cells,
    get_lecture6_cells,
    get_lecture7_cells,
    get_lecture8_cells
)
from master_extras import get_extras_cells

def build_master_notebook():
    nb = nbf.v4.new_notebook()
    all_cells = []
    
    # 1. Setup & Titles
    all_cells.extend(get_setup_cells())
    
    # 2. Lectures 1 - 4
    all_cells.extend(get_lecture1_cells())
    all_cells.extend(get_lecture2_cells())
    all_cells.extend(get_lecture3_cells())
    all_cells.extend(get_lecture4_cells())
    
    # 3. Lectures 5 - 8
    all_cells.extend(get_lecture5_cells())
    all_cells.extend(get_lecture6_cells())
    all_cells.extend(get_lecture7_cells())
    all_cells.extend(get_lecture8_cells())
    
    # 4. Mock Exam Extras
    all_cells.extend(get_extras_cells())
    
    nb.cells = all_cells
    
    # Metadata
    nb.metadata = {
        "kernelspec": {
            "display_name": "Python 3 (linalg-venv)",
            "language": "python",
            "name": "linalg-venv"
        },
        "language_info": {
            "name": "python",
            "version": "3.11"
        }
    }
    
    out_path = 'notebooks/LinearAlgebra_Master_Notes.ipynb'
    with open(out_path, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
        
    print(f"Successfully generated {out_path} with {len(all_cells)} cells!")

if __name__ == '__main__':
    build_master_notebook()
