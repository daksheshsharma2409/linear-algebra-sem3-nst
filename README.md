# linear-algebra-sem3-nst

Linear Algebra course materials with lecture notes and lab solutions in Jupyter notebooks.

## Installation

```bash
# Create virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Launch Jupyter
jupyter notebook

# Navigate to notebooks/
# - LinearAlgebra_Master_Notes.ipynb
# - LinearAlgebra_Lab_Solutions.ipynb
```

## Regenerate Notebooks

```bash
python scripts/generate_master_notes.py
python scripts/generate_lab_solutions.py
```
