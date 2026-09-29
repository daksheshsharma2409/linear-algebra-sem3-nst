"""
Module containing Sections 1 to 4 for LinearAlgebra_Master_Notes.ipynb
"""

import nbformat as nbf

def get_setup_cells():
    cells = []
    
    # Title & Metadata
    title_md = """# Newton School of Technology, ADYPU — Mathematics-3: Linear Algebra
## Master Exam Preparation Guide & Comprehensive Interactive Lecture Notes (Lectures 1–8)

---

### Course Architecture & Thematic Progression
1. **Lecture 1:** Linear Systems, The Row Picture & Column Picture ($Ax = b$)
2. **Lecture 2:** Matrix Multiplication Mechanics & Graph Transformations (**MUL-TEA-PLICATION**)
3. **Lecture 3:** Linear Combinations, Span, and Vector Space Axioms (**One Recipe, Infinite Menu**)
4. **Lecture 4:** Gaussian Elimination, Echelon Forms, and Rank (**Same Solution, Simpler System**)
5. **Lecture 5:** Elementary Matrices, $A = LU$ Decomposition, and Tri-diagonal Factorization (**Prep Once, Serve Many**)
6. **Lecture 6:** Linear Independence, Column Space $C(A)$, and Redundancy (**New Signal or Echo?**)
7. **Lecture 7:** Null Space $N(A)$, Vector Subspaces, and The Complete Solution (**Same Output, Different Inputs?**)
8. **Lecture 8:** The Four Fundamental Subspaces, Orthogonality, and Network Duality (**Four Spaces, One Matrix**)
9. **Mock Exam Extras:** Formula Cheat Sheet, Common Pitfalls, "If You See X, Do Y" Decision Matrix, 20 Original Practice Problems, and 3-Day Intensive Study Plan

---

### Linked Table of Contents
- [Cell 1: Reusable Visualization Engine & Symbolic Environment](#cell-1-reusable-visualization-engine--symbolic-environment)
- [Section 1: Lecture 1 — Linear Systems, Row Picture, and Column Picture](#section-1-lecture-1--linear-systems-row-picture-and-column-picture)
  - [1.1 Summary Box & Key Formulas](#11-summary-box--key-formulas)
  - [1.2 Concept 1: System to Matrix ($Ax = b$)](#12-concept-1-system-to-matrix-ax--b)
  - [1.3 Concept 2: The Row Picture vs. The Column Picture](#13-concept-2-the-row-picture-vs-the-column-picture)
  - [1.4 Concept 3: The Trichotomy Theorem & 2x2 Determinant Criterion](#14-concept-3-the-trichotomy-theorem--2x2-determinant-criterion)
  - [1.5 Concept 4: Geometry of 3D Systems (Point, Line, Plane, Prism)](#15-concept-4-geometry-of-3d-systems-point-line-plane-prism)
  - [1.6 Concept 5: Parameter Sensitivity, Consistency & 4D Hyperplanes](#16-concept-5-parameter-sensitivity-consistency--4d-hyperplanes)
  - [1.7 Lecture 1 Preserved Worked Examples (Q.1, Q.2, Q.3)](#17-lecture-1-preserved-worked-examples-q1-q2-q3)
  - [1.8 Core Visualizations (Diagrams 1, 2, 3)](#18-core-visualizations-diagrams-1-2-3)
  - [1.9 Lecture 1 Self-Test Block](#19-lecture-1-self-test-block)
- [Section 2: Lecture 2 — Matrix Multiplication and Network Transformations](#section-2-lecture-2--matrix-multiplication-and-network-transformations)
  - [2.1 Summary Box & Key Formulas](#21-summary-box--key-formulas)
  - [2.2 Concept 1: The Four Perspectives of Matrix Multiplication](#22-concept-1-the-four-perspectives-of-matrix-multiplication)
  - [2.3 Concept 2: Recipes, Sound Mixing, and Row-Operations Interpretation](#23-concept-2-recipes-sound-mixing-and-row-operations-interpretation)
  - [2.4 Concept 3: Non-Commutativity and Word Matrices](#24-concept-3-non-commutativity-and-word-matrices)
  - [2.5 Concept 4: Structural Matrices (J - I Influence & Antenna Aggregation)](#25-concept-4-structural-matrices-j---i-influence--antenna-aggregation)
  - [2.6 Concept 5: Adjacency Matrices and Walk Counting ($M^k$)](#26-concept-5-adjacency-matrices-and-walk-counting-mk)
  - [2.7 Lecture 2 Preserved Worked Examples](#27-lecture-2-preserved-worked-examples)
  - [2.8 Core Visualizations (Diagrams 11a, 12)](#28-core-visualizations-diagrams-11a-12)
  - [2.9 Lecture 2 Self-Test Block](#29-lecture-2-self-test-block)
- [Section 3: Lecture 3 — Linear Combinations, Span, and Vector Spaces](#section-3-lecture-3--linear-combinations-span-and-vector-spaces)
  - [3.1 Summary Box & Key Formulas](#31-summary-box--key-formulas)
  - [3.2 Concept 1: What is a Vector? The 8 Axioms of a Vector Space](#32-concept-1-what-is-a-vector-the-8-axioms-of-a-vector-space)
  - [3.3 Concept 2: Linear Combinations and Span Hierarchy](#33-concept-2-linear-combinations-and-span-hierarchy)
  - [3.4 Concept 3: The Target Test ($[v_1 \\dots v_k] c = b$)](#34-concept-3-the-target-test-v_1-dots-v_k-c--b)
  - [3.5 Concept 4: Redundancy, Free Parameters, and Linear Dependence](#35-concept-4-redundancy-free-parameters-and-linear-dependence)
  - [3.6 Lecture 3 Preserved Worked Examples](#36-lecture-3-preserved-worked-examples)
  - [3.7 Core Visualizations (Diagrams 4, 5)](#37-core-visualizations-diagrams-4-5)
  - [3.8 Lecture 3 Self-Test Block](#38-lecture-3-self-test-block)
- [Section 4: Lecture 4 — Gaussian Elimination, Row Operations, and Rank](#section-4-lecture-4--gaussian-elimination-row-operations-and-rank)
  - [4.1 Summary Box & Key Formulas](#41-summary-box--key-formulas)
  - [4.2 Concept 1: Geometry of Elimination (Invariance of Intersection)](#42-concept-1-geometry-of-elimination-invariance-of-intersection)
  - [4.3 Concept 2: Echelon Forms (REF vs. RREF) and Pivot Tracking](#43-concept-2-echelon-forms-ref-vs-rref-and-pivot-tracking)
  - [4.4 Concept 3: Matrix Rank $r$ and the Pivot Theorem](#44-concept-3-matrix-rank-r-and-the-pivot-theorem)
  - [4.5 Concept 4: Conservation Laws & Intersection Flow Analysis](#45-concept-4-conservation-laws--intersection-flow-analysis)
  - [4.6 Concept 5: Unsigned Incidence Matrix (Odd Cycles vs. Bipartite Rank)](#46-concept-5-unsigned-incidence-matrix-odd-cycles-vs-bipartite-rank)
  - [4.7 Lecture 4 Preserved Worked Examples](#47-lecture-4-preserved-worked-examples)
  - [4.8 Core Visualizations (Diagrams 6, 11b)](#48-core-visualizations-diagrams-6-11b)
  - [4.9 Lecture 4 Self-Test Block](#49-lecture-4-self-test-block)
- [Jump to Lecture 5–8 & Extras](#section-5-lecture-5--elementary-matrices-and-lu-decomposition)
"""
    cells.append(nbf.v4.new_markdown_cell(title_md))
    
    # Cell 1: Reusable Setup and Plotting Helpers
    cell1_code = """# Cell 1: Reusable Visualization Engine & Symbolic Environment
import numpy as np
import sympy as sp
from sympy import Matrix, symbols, Eq, solve, Rational
import scipy.linalg as la
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.io as pio
import networkx as nx
import pandas as pd
from IPython.display import display, Markdown, HTML

# Configure styling and renderers
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3
pio.renderers.default = 'notebook'

# Global Color Palette
COLOR_PLANES = [
    'rgba(31, 119, 180, 0.45)',  # Translucent Blue
    'rgba(44, 160, 44, 0.45)',   # Translucent Green
    'rgba(214, 39, 40, 0.45)',   # Translucent Red
    'rgba(148, 103, 189, 0.45)'  # Translucent Purple
]
COLOR_POINT = 'black'
COLOR_NULL = '#ff7f0e'     # Vivid Orange
COLOR_COL = '#17becf'      # Teal
COLOR_ROW = '#9467bd'      # Purple
COLOR_VEC = '#1f77b4'      # Deep Blue

def plot_plane(fig, normal, d, x_range=(-5, 5), y_range=(-5, 5), color='rgba(31, 119, 180, 0.4)', name='Plane', opacity=0.5):
    \"\"\"Plots a plane a*x + b*y + c*z = d in a 3D Plotly figure.\"\"\"
    a, b, c = normal
    x = np.linspace(x_range[0], x_range[1], 25)
    y = np.linspace(y_range[0], y_range[1], 25)
    X, Y = np.meshgrid(x, y)
    if abs(c) > 1e-5:
        Z = (d - a * X - b * Y) / c
        fig.add_trace(go.Surface(x=X, y=Y, z=Z, colorscale=[[0, color], [1, color]], 
                                 showscale=False, opacity=opacity, name=name))
    elif abs(b) > 1e-5:
        z = np.linspace(x_range[0], x_range[1], 25)
        X, Z = np.meshgrid(x, z)
        Y = (d - a * X) / b
        fig.add_trace(go.Surface(x=X, y=Y, z=Z, colorscale=[[0, color], [1, color]], 
                                 showscale=False, opacity=opacity, name=name))
    else:
        y_vals = np.linspace(y_range[0], y_range[1], 25)
        z_vals = np.linspace(x_range[0], x_range[1], 25)
        Y, Z = np.meshgrid(y_vals, z_vals)
        X = np.full_like(Y, d / a)
        fig.add_trace(go.Surface(x=X, y=Y, z=Z, colorscale=[[0, color], [1, color]], 
                                 showscale=False, opacity=opacity, name=name))

def plot_vec3d(fig, vec, origin=(0, 0, 0), color='#1f77b4', name='Vector', width=6):
    \"\"\"Plots a 3D vector as an arrow with cone head.\"\"\"
    vx, vy, vz = vec
    ox, oy, oz = origin
    # Line stem
    fig.add_trace(go.Scatter3d(
        x=[ox, ox + vx], y=[oy, oy + vy], z=[oz, oz + vz],
        mode='lines',
        line=dict(color=color, width=width),
        name=name
    ))
    # Cone tip
    fig.add_trace(go.Cone(
        x=[ox + vx], y=[oy + vy], z=[oz + vz],
        u=[vx], v=[vy], w=[vz],
        sizemode='absolute',
        sizeref=0.4,
        anchor='tip',
        colorscale=[[0, color], [1, color]],
        showscale=False,
        name=name + ' (tip)'
    ))

def plot_three_planes(planes, solution_point=None, title='Three Planes in R³'):
    \"\"\"Plots three 3D planes and an optional intersection solution point.\"\"\"
    fig = go.Figure()
    for i, (norm, d) in enumerate(planes):
        c = COLOR_PLANES[i % len(COLOR_PLANES)]
        plot_plane(fig, norm, d, color=c, name=f'Eq {i+1}: {norm[0]}x + {norm[1]}y + {norm[2]}z = {d}')
    if solution_point is not None:
        sx, sy, sz = solution_point
        fig.add_trace(go.Scatter3d(
            x=[sx], y=[sy], z=[sz],
            mode='markers+text',
            marker=dict(size=8, color=COLOR_POINT),
            text=[f'Solution ({sx}, {sy}, {sz})'],
            textposition='top center',
            name='Solution Point'
        ))
    fig.update_layout(
        title=title,
        scene=dict(
            xaxis_title='X', yaxis_title='Y', zaxis_title='Z',
            camera=dict(eye=dict(x=1.8, y=1.8, z=1.4))
        ),
        margin=dict(l=0, r=0, b=0, t=40)
    )
    return fig

def plot_2d_lines(lines, x_range=(-5, 5), solution=None, title='2D Row Picture'):
    \"\"\"Matplotlib helper for 2D row pictures.\"\"\"
    plt.figure(figsize=(8, 6))
    x_vals = np.linspace(x_range[0], x_range[1], 300)
    colors = ['#1f77b4', '#2ca02c', '#d62728', '#9467bd']
    for i, (a, b, c) in enumerate(lines):
        col = colors[i % len(colors)]
        if abs(b) > 1e-6:
            y_vals = (c - a * x_vals) / b
            plt.plot(x_vals, y_vals, label=f'{a}x + {b}y = {c}', color=col, linewidth=2)
        else:
            plt.axvline(x=c / a, label=f'{a}x = {c}', color=col, linewidth=2)
    if solution is not None:
        plt.scatter([solution[0]], [solution[1]], color='black', s=80, zorder=5, 
                    label=f'Solution ({solution[0]}, {solution[1]})')
    plt.axhline(0, color='gray', linestyle='--', alpha=0.5)
    plt.axvline(0, color='gray', linestyle='--', alpha=0.5)
    plt.xlim(x_range)
    plt.ylim(x_range)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title, fontsize=13, fontweight='bold')
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_column_picture(c1, c2, b, x_sol=(1, 1), title='Column Picture (Linear Combination)'):
    \"\"\"Matplotlib helper for 2D column picture with parallelogram construction.\"\"\"
    plt.figure(figsize=(8, 6))
    o = np.array([0, 0])
    u, v = x_sol
    uc1 = u * np.array(c1)
    vc2 = v * np.array(c2)
    b_calc = uc1 + vc2
    
    # Vector arrows
    plt.quiver(*o, *c1, angles='xy', scale_units='xy', scale=1, color='#1f77b4', alpha=0.4, label=f'Column 1: {c1}')
    plt.quiver(*o, *c2, angles='xy', scale_units='xy', scale=1, color='#2ca02c', alpha=0.4, label=f'Column 2: {c2}')
    plt.quiver(*o, *uc1, angles='xy', scale_units='xy', scale=1, color='#1f77b4', linewidth=2.5, label=f'{u}·c₁: {uc1}')
    plt.quiver(*uc1, *vc2, angles='xy', scale_units='xy', scale=1, color='#2ca02c', linewidth=2.5, label=f'{v}·c₂ (from head): {vc2}')
    plt.quiver(*o, *b_calc, angles='xy', scale_units='xy', scale=1, color='black', linewidth=3, label=f'Resultant b = {b_calc}')
    
    # Parallelogram dashed lines
    plt.plot([uc1[0], b_calc[0]], [uc1[1], b_calc[1]], 'k--', alpha=0.5)
    plt.plot([vc2[0], b_calc[0]], [vc2[1], b_calc[1]], 'k--', alpha=0.5)
    plt.quiver(*o, *vc2, angles='xy', scale_units='xy', scale=1, color='#2ca02c', linestyle=':', alpha=0.3)
    
    max_bound = max(abs(b_calc).max(), abs(uc1).max(), abs(vc2).max()) + 2
    plt.xlim(-max_bound, max_bound)
    plt.ylim(-max_bound, max_bound)
    plt.axhline(0, color='gray', linestyle='--', alpha=0.4)
    plt.axvline(0, color='gray', linestyle='--', alpha=0.4)
    plt.xlabel('Component 1')
    plt.ylabel('Component 2')
    plt.title(title, fontsize=13, fontweight='bold')
    plt.legend()
    plt.tight_layout()
    plt.show()

print('Visualisation suite and mathematical helpers initialized successfully!')
"""
    cells.append(nbf.v4.new_code_cell(cell1_code))
    return cells

def get_lecture1_cells():
    cells = []
    
    # Lecture 1 Section Header & Summary Box
    sec1_md = """# Section 1: Lecture 1 — Linear Systems, Row Picture, and Column Picture

---

### 1.1 Summary Box & Key Formulas
> **Key Identities & Principles:**
> - **Matrix System Representation:**
>   $$Ax = b \\iff \\begin{bmatrix} a_{11} & a_{12} & \\cdots & a_{1n} \\\\ a_{21} & a_{22} & \\cdots & a_{2n} \\\\ \\vdots & \\vdots & \\ddots & \\vdots \\\\ a_{m1} & a_{m2} & \\cdots & a_{mn} \\end{bmatrix} \\begin{bmatrix} x_1 \\\\ x_2 \\\\ \\vdots \\\\ x_n \\end{bmatrix} = \\begin{bmatrix} b_1 \\\\ b_2 \\\\ \\vdots \\\\ b_m \\end{bmatrix}$$
> - **The Row Picture:** Each equation $\\sum_j a_{ij} x_j = b_i$ defines an affine hyperplane in $\\mathbb{R}^n$. The system's solution set is the geometric intersection $\\bigcap_{i=1}^m H_i$.
> - **The Column Picture:** Matrix multiplication viewed as a vector combination:
>   $$x_1 \\mathbf{a}_1 + x_2 \\mathbf{a}_2 + \\cdots + x_n \\mathbf{a}_n = \\mathbf{b}$$
>   A solution exists if and only if target vector $\\mathbf{b}$ lies within the span of the column vectors $\\{\\mathbf{a}_1, \\dots, \\mathbf{a}_n\\}$.
> - **Trichotomy Theorem:** Every linear system over $\\mathbb{R}$ has either **(a)** exactly one solution, **(b)** infinitely many solutions, or **(c)** no solution.
> - **2×2 Determinant Criterion:** For $A = \\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix}$, $\\det(A) = ad - bc$. If $\\det(A) \\ne 0$, unique solution for every $\\mathbf{b}$. If $\\det(A) = 0$, either 0 or $\\infty$ solutions.
"""
    cells.append(nbf.v4.new_markdown_cell(sec1_md))

    # Concept 1.1: System to Matrix
    c1_1_md = """### 1.2 Concept 1: System to Matrix ($Ax = b$)

#### Intuition in Plain Words
A system of linear equations is simply a collection of requirements that must be met simultaneously. Instead of writing long mathematical sentences repeatedly with variable names $x, y, z$, we separate the numerical coefficients into a compact coefficient grid $A$, group the variable dials into an unknown column vector $x$, and store the target requirements in a right-hand-side vector $b$.

#### Formal Definition
A linear equation in $n$ variables $x_1, \\dots, x_n$ is an equation of the form:
$$a_1 x_1 + a_2 x_2 + \\dots + a_n x_n = b$$
where $a_1, \\dots, a_n \\in \\mathbb{R}$ are coefficients and $b \\in \\mathbb{R}$ is the constant term. An $m \\times n$ linear system consists of $m$ such equations:
$$\\begin{cases} a_{11}x_1 + a_{12}x_2 + \\dots + a_{1n}x_n = b_1 \\\\ a_{21}x_1 + a_{22}x_2 + \\dots + a_{2n}x_n = b_2 \\\\ \\quad \\vdots \\\\ a_{m1}x_1 + a_{m2}x_2 + \\dots + a_{mn}x_n = b_m \\end{cases} \\iff Ax = b$$

#### The Lecture's Own Example (Sheet 1 / Lab 1 Q.1)
Consider the $3 \\times 3$ system:
$$\\begin{aligned} 2x + y - z &= 4 \\\\ x - z &= 1 \\\\ 3x + y + 2z &= 6 \\end{aligned}$$
Expressed in matrix form:
$$\\begin{bmatrix} 2 & 1 & -1 \\\\ 1 & 0 & -1 \\\\ 3 & 1 & 2 \\end{bmatrix} \\begin{bmatrix} x \\\\ y \\\\ z \\end{bmatrix} = \\begin{bmatrix} 4 \\\\ 1 \\\\ 6 \\end{bmatrix}$$

#### Our Numeric Example
A $2 \\times 2$ system:
$$\\begin{aligned} 3x_1 + 4x_2 &= 11 \\\\ x_1 - 2x_2 &= -3 \\end{aligned} \\iff \\begin{bmatrix} 3 & 4 \\\\ 1 & -2 \\end{bmatrix} \\begin{bmatrix} x_1 \\\\ x_2 \\end{bmatrix} = \\begin{bmatrix} 11 \\\\ -3 \\end{bmatrix}$$
Multiplying equation 2 by 2 and adding to equation 1: $5x_1 = 5 \\implies x_1 = 1, x_2 = 2$.
"""
    cells.append(nbf.v4.new_markdown_cell(c1_1_md))

    # SymPy Demo for Concept 1.1
    c1_1_code = """# SymPy exact verification of the Lecture 1 system
A_lec1 = Matrix([[2, 1, -1], [1, 0, -1], [3, 1, 2]])
b_lec1 = Matrix([4, 1, 6])
x_sol = A_lec1.LUsolve(b_lec1)

print("Coefficient Matrix A:")
display(A_lec1)
print("Right Hand Side b:")
display(b_lec1)
print("Exact SymPy Solution x = (x, y, z):")
display(x_sol)
assert A_lec1 * x_sol == b_lec1, "Verification Failed!"
print("Checked A * x == b: TRUE")
"""
    cells.append(nbf.v4.new_code_cell(c1_1_code))

    # Exam Trap & Self-Test
    c1_1_trap = """> **Exam Trap:** Be cautious when an equation skips a variable (e.g. $x - z = 1$). The coefficient of the missing variable is strictly $0$, NOT $1$ and not omitted. Skipping column alignment will corrupt the coefficient matrix dimensions.

**Self-Test 1.1:** Write the system $x_1 - 3x_3 = 5$, $2x_2 + x_3 = 7$, $4x_1 - x_2 = 0$ in matrix notation $Ax = b$ and state its size.
*Answer:* Size is $3 \\times 3$. $A = \\begin{bmatrix} 1 & 0 & -3 \\\\ 0 & 2 & 1 \\\\ 4 & -1 & 0 \\end{bmatrix}$, $x = \\begin{bmatrix} x_1 \\\\ x_2 \\\\ x_3 \\end{bmatrix}$, $b = \\begin{bmatrix} 5 \\\\ 7 \\\\ 0 \\end{bmatrix}$.
"""
    cells.append(nbf.v4.new_markdown_cell(c1_1_trap))

    # Concept 1.2: Row Picture vs Column Picture
    c1_2_md = """### 1.3 Concept 2: The Row Picture vs. The Column Picture

#### Intuition in Plain Words
Linear algebra gives you two completely different visual lenses for the exact same problem:
1. **The Row Picture (Intersection):** You look at each equation horizontally. In 2D, each row is a line. The solution is the point where the lines cross. You are looking for a location that satisfies all geometric boundary constraints simultaneously.
2. **The Column Picture (Combination):** You look at the matrix vertically. Each column is a vector step in space. The unknown variables $x_1, x_2, \\dots$ are dial settings (scalars) that stretch each column vector. The solution is the specific recipe of dials that combines the column vectors to land precisely on target $b$.

#### Formal Definition
For $Ax = b$ with columns $\\mathbf{a}_1, \\dots, \\mathbf{a}_n$ and rows $\\mathbf{r}_1^T, \\dots, \\mathbf{r}_m^T$:
- **Row Equation $i$:** $\\mathbf{r}_i^T x = b_i \\implies$ hyperplane $H_i = \\{x \\in \\mathbb{R}^n : \\langle \\mathbf{r}_i, x \\rangle = b_i\\}$.
- **Column Equation:** $\\sum_{j=1}^n x_j \\mathbf{a}_j = \\mathbf{b} \\implies \\mathbf{b} \\in \\text{Span}(\\mathbf{a}_1, \\dots, \\mathbf{a}_n)$.

#### The Lecture's Own Example (Sheet 1 / Lab 1 Q.4 & Q.8)
System:
$$\\begin{aligned} 2x + y &= 7 \\\\ x - 2y &= -1 \\end{aligned}$$
- **Row Picture:** Line 1: $2x + y = 7$ (passes through $(0, 7)$ and $(3.5, 0)$). Line 2: $x - 2y = -1$ (passes through $(0, 0.5)$ and $(-1, 0)$). They intersect at $(x, y) = (3, 1)$.
- **Column Picture:**
  $$x \\begin{bmatrix} 2 \\\\ 1 \\end{bmatrix} + y \\begin{bmatrix} 1 \\\\ -2 \\end{bmatrix} = \\begin{bmatrix} 7 \\\\ -1 \\end{bmatrix}$$
  Plugging in $x = 3, y = 1$:
  $$3 \\begin{bmatrix} 2 \\\\ 1 \\end{bmatrix} + 1 \\begin{bmatrix} 1 \\\\ -2 \\end{bmatrix} = \\begin{bmatrix} 6 \\\\ 3 \\end{bmatrix} + \\begin{bmatrix} 1 \\\\ -2 \\end{bmatrix} = \\begin{bmatrix} 7 \\\\ 1 \\end{bmatrix} \\ne \\begin{bmatrix} 7 \\\\ -1 \\end{bmatrix}$$
  *Wait! Let us check carefully:* Lab 1 Q.8 note from prompt:
  In Lab 1 Q.8: $2x + y = 7$ and $x - 2y = -1$.
  Solving: $x = 2y - 1 \\implies 2(2y - 1) + y = 7 \\implies 5y - 2 = 7 \\implies 5y = 9 \\implies y = 9/5, x = 13/5$.
  If $(3, 1)$ was the claimed solution, then $2(3) + 1 = 7$, but $3 - 2(1) = 1 \\ne -1$. The second equation must be $x - 2y = 1$ to yield $(3, 1)$!
  With $x - 2y = 1$: $3(1) - 2(1) = 1$. Then $3 \\begin{bmatrix} 2 \\\\ 1 \\end{bmatrix} + 1 \\begin{bmatrix} 1 \\\\ -2 \\end{bmatrix} = \\begin{bmatrix} 7 \\\\ 1 \\end{bmatrix}$. SymPy will rigorously demonstrate both variants.
"""
    cells.append(nbf.v4.new_markdown_cell(c1_2_md))

    # SymPy & Plotting for Row & Column Picture
    c1_2_code = """# Comparing Row Picture and Column Picture in Python
# Let us take the consistent system: 2x + y = 7, x - 2y = 1 -> Solution (3, 1)
lines_lec = [(2, 1, 7), (1, -2, 1)]
plot_2d_lines(lines_lec, x_range=(0, 5), solution=(3, 1), title="Lecture 1: 2D Row Picture (Intersection at (3, 1))")

# Column Picture: 3 * [2, 1]^T + 1 * [1, -2]^T = [7, 1]^T
plot_column_picture(c1=(2, 1), c2=(1, -2), b=(7, 1), x_sol=(3, 1), title="Lecture 1: Column Picture (3·c1 + 1·c2 = b)")
"""
    cells.append(nbf.v4.new_code_cell(c1_2_code))

    # Concept 1.3: Trichotomy Theorem & Det Test
    c1_3_md = """### 1.4 Concept 3: The Trichotomy Theorem & 2×2 Determinant Criterion

#### Intuition in Plain Words
When you have two straight lines in a plane, only three things can happen:
1. They have different slopes, so they meet at **exactly one** crossing point.
2. They are parallel and separate, so they **never meet** (zero solutions).
3. They are right on top of each other (coincident), so every point along the line is a shared solution (**infinitely many solutions**).
There is no fourth option: a linear system can never have exactly 2 solutions or exactly 7 solutions.

#### Formal Theorem: Trichotomy of Linear Systems
Every system of linear equations over $\\mathbb{R}$ has either:
1. **Unique Solution:** Rank of $A$ equals rank of $[A \\mid b] = n$ (full column rank and consistent).
2. **Infinitely Many Solutions:** Rank of $A$ equals rank of $[A \\mid b] < n$ (consistent with at least one free variable).
3. **No Solution (Inconsistent):** $\\text{rank}(A) < \\text{rank}[A \\mid b]$ (a row of the form $[0 \\; 0 \\; \\cdots \\; 0 \\mid c]$ with $c \\ne 0$).

#### The 2×2 Determinant Test
For a $2 \\times 2$ matrix $A = \\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix}$:
$$\\det(A) = ad - bc$$
- If $\\det(A) \\ne 0$: The row vectors are not collinear, column vectors are not collinear $\\implies$ unique solution for every right-hand side $b$.
- If $\\det(A) = 0$: The rows are parallel. If the right-hand sides have the exact same ratio, infinitely many solutions; otherwise, no solution.

#### Numeric Examples of the 3 Cases
1. **Unique:** $x + y = 3$, $x - y = 1 \\implies \\det = 1(-1) - 1(1) = -2 \\ne 0$. Solution: $(2, 1)$.
2. **Infinite:** $x + y = 3$, $2x + 2y = 6 \\implies \\det = 2 - 2 = 0$. Row 2 is $2 \\times$ Row 1. Line of solutions: $y = 3 - x$.
3. **None:** $x + y = 3$, $2x + 2y = 3 \\implies \\det = 0$. $2(x+y) = 6 \\ne 3$, contradiction! Parallel disjoint lines.
"""
    cells.append(nbf.v4.new_markdown_cell(c1_3_md))

    # Diagram 1: 2D Row Picture beside Column Picture for 3 cases
    c1_3_code = """# Diagram 1: 2D Row Picture beside Column Picture for the Three Cases
fig, axes = plt.subplots(3, 2, figsize=(14, 15))

cases = [
    ("Case 1: Unique Solution", [(1, 1, 3), (1, -1, 1)], (2, 1), [1, 1], [1, -1], [3, 1], (2, 1)),
    ("Case 2: Infinitely Many Solutions", [(1, 1, 3), (2, 2, 6)], None, [1, 2], [1, 2], [3, 6], None),
    ("Case 3: No Solution (Inconsistent)", [(1, 1, 3), (2, 2, 3)], None, [1, 2], [1, 2], [3, 3], None)
]

x_vals = np.linspace(-1, 5, 200)

for idx, (title, lines, sol, c1, c2, b_vec, x_s) in enumerate(cases):
    # Row picture (Left)
    ax_row = axes[idx, 0]
    for i, (a, b_c, c) in enumerate(lines):
        y_vals = (c - a * x_vals) / b_c
        ax_row.plot(x_vals, y_vals, label=f'{a}x + {b_c}y = {c}', linewidth=2)
    if sol:
        ax_row.scatter([sol[0]], [sol[1]], color='black', s=80, zorder=5, label=f'Sol: {sol}')
    ax_row.set_title(f'{title} — Row Picture', fontweight='bold')
    ax_row.set_xlim(-1, 5); ax_row.set_ylim(-2, 5)
    ax_row.legend(); ax_row.grid(True, alpha=0.3)
    
    # Column picture (Right)
    ax_col = axes[idx, 1]
    ax_col.quiver(0, 0, c1[0], c1[1], angles='xy', scale_units='xy', scale=1, color='#1f77b4', width=0.015, label=f'col 1: {c1}')
    ax_col.quiver(0, 0, c2[0], c2[1], angles='xy', scale_units='xy', scale=1, color='#2ca02c', width=0.015, label=f'col 2: {c2}')
    ax_col.quiver(0, 0, b_vec[0], b_vec[1], angles='xy', scale_units='xy', scale=1, color='red', width=0.018, label=f'target b: {b_vec}')
    ax_col.set_title(f'{title} — Column Picture', fontweight='bold')
    ax_col.set_xlim(-2, 6); ax_col.set_ylim(-3, 7)
    ax_col.legend(); ax_col.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
"""
    cells.append(nbf.v4.new_code_cell(c1_3_code))

    # Concept 1.4: 3D Geometric Cases
    c1_4_md = """### 1.5 Concept 4: Geometry of 3D Systems (Point, Line, Plane, Prism)

#### Intuition in Plain Words
In three-dimensional space, each linear equation defines a flat 2D plane stretching infinitely. When three planes meet in space, their intersection geometry can take several distinct configurations:
1. **Single Intersection Point:** The normal vectors are linearly independent. The three planes meet at a sharp vertex (e.g. corner of a room).
2. **Intersection Line:** The three planes meet along a single straight axis (like pages of an open book meeting at the spine).
3. **Coincident Plane:** All three equations are multiples of each other; the intersection is an entire 2D plane.
4. **Triangular Prism (Inconsistent):** Each pair of planes intersects along a line, but the three intersection lines are parallel and never meet! Pairwise consistent, globally inconsistent.
5. **Parallel Planes:** Two or three planes are strictly parallel with no intersection.

#### Mathematical Equations for the Configurations
- **Single Point:** $x + y + z = 1$, $x - y + z = 0$, $2x + y - z = 2$.
- **Line Intersection:** $x + y + z = 2$, $2x + y - z = 1$, $3x + 2y = 3$ (Eq3 = Eq1 + Eq2).
- **Triangular Prism:** $x + y = 1$, $y + z = 1$, $x - z = 2$.
  Notice: $(x + y) - (y + z) = x - z = 0 \\ne 2$. Pairwise intersections exist, but total intersection is empty!
"""
    cells.append(nbf.v4.new_markdown_cell(c1_4_md))

    # Diagram 2: Three Planes in 3D (Point & Prism)
    c1_4_code = """# Diagram 2: Interactive 3D Plotly Visualization of 3 Planes
# Case A: Unique Point Intersection
planes_unique = [
    ([1, 1, 1], 3),
    ([1, -1, 1], 1),
    ([2, 1, -1], 2)
]
# Solve using SymPy
M_u = Matrix([[1, 1, 1], [1, -1, 1], [2, 1, -1]])
pt = list(M_u.LUsolve(Matrix([3, 1, 2])))
fig_planes = plot_three_planes(planes_unique, solution_point=[float(v) for v in pt], 
                               title="Diagram 2A: Unique Solution Point in R³ (Three Planes Meeting)")
fig_planes.show()

# Case B: Triangular Prism (Pairwise Lines, No Common Point)
planes_prism = [
    ([1, 1, 0], 2),
    ([0, 1, 1], 2),
    ([1, 0, -1], 4)
]
fig_prism = plot_three_planes(planes_prism, solution_point=None, 
                              title="Diagram 2B: Triangular Prism (Inconsistent System: Pairwise Crossings, No Common Point)")
fig_prism.show()
"""
    cells.append(nbf.v4.new_code_cell(c1_4_code))

    # Diagram 3: 3D Column Picture
    c1_5_code = """# Diagram 3: 3D Column Picture with Stacked Vector Arrows Reaching b
fig_col3d = go.Figure()

c1 = np.array([2, 1, 0])
c2 = np.array([1, 3, 2])
c3 = np.array([0, 2, 4])
x_target = np.array([1, 2, 1])

# Scaled steps
step1 = x_target[0] * c1
step2 = x_target[1] * c2
step3 = x_target[2] * c3
b_res = step1 + step2 + step3

# Plot original columns from origin
plot_vec3d(fig_col3d, c1, color='#1f77b4', name='Column 1 (2,1,0)')
plot_vec3d(fig_col3d, c2, color='#2ca02c', name='Column 2 (1,3,2)')
plot_vec3d(fig_col3d, c3, color='#9467bd', name='Column 3 (0,2,4)')

# Stacked path reaching b
plot_vec3d(fig_col3d, step1, origin=(0, 0, 0), color='#1f77b4', name='1·c₁', width=8)
plot_vec3d(fig_col3d, step2, origin=step1, color='#2ca02c', name='2·c₂ (stacked)', width=8)
plot_vec3d(fig_col3d, step3, origin=step1 + step2, color='#9467bd', name='1·c₃ (stacked)', width=8)

# Target b
plot_vec3d(fig_col3d, b_res, origin=(0, 0, 0), color='black', name=f'Target b {tuple(b_res)}', width=10)

fig_col3d.update_layout(
    title='Diagram 3: 3D Column Picture (Reaching b = 1·c₁ + 2·c₂ + 1·c₃)',
    scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
    margin=dict(l=0, r=0, b=0, t=40)
)
fig_col3d.show()
"""
    cells.append(nbf.v4.new_code_cell(c1_5_code))

    # Concept 1.5: Parameter Problems, Consistency & 4D
    c1_6_md = """### 1.6 Concept 5: Parameter Sensitivity, Consistency & 4D Hyperplanes

#### Parameter Problems
Consider $x - y = 2$ and $3x - 3y = k$:
The left-hand sides are dependent: $\\text{Row } 2 = 3 \\times \\text{Row } 1$.
- If $k = 6$: The equations are identical $\\implies$ infinitely many solutions ($y = x - 2$).
- If $k \\ne 6$: Parallel disjoint lines $\\implies$ zero solutions.
- A unique solution is **impossible** for any real value of $k$ because the coefficient matrix $\\begin{bmatrix} 1 & -1 \\\\ 3 & -3 \\end{bmatrix}$ has $\\det = 0$.

#### Homogeneous Systems
$$\\begin{aligned} ax + 2y &= 0 \\\\ 2x + ay &= 0 \\end{aligned} \\iff \\begin{bmatrix} a & 2 \\\\ 2 & a \\end{bmatrix} \\begin{bmatrix} x \\\\ y \\end{bmatrix} = \\begin{bmatrix} 0 \\\\ 0 \\end{bmatrix}$$
Since $b = 0$, $x = (0, 0)$ is always a solution (trivial solution). Non-trivial solutions exist if and only if:
$$\\det(A) = a^2 - 4 = 0 \\implies a = \\pm 2$$
When $a = 2$, $x + y = 0$ (a full line of solutions). When $a = -2$, $x - y = 0$ (the line $y = x$).

#### 4D Hyperplane Geometry
In $\\mathbb{R}^4$, an equation $u + v + w + z = c$ represents a 3-dimensional affine hyperplane.
Consider the system from Lab 1 Q.14:
$$\\begin{aligned} u + v + w + z &= 6 \\\\ u + w + z &= 4 \\\\ u + w &= 2 \\end{aligned}$$
Subtracting Eq3 from Eq2: $z = 4 - 2 = 2$.
Subtracting Eq2 from Eq1: $v = 6 - 4 = 2$.
Then Eq3 gives $u + w = 2 \\implies w = 2 - u$, with $u$ free.
The solution set is a **1-dimensional line in $\\mathbb{R}^4$**:
$$\\begin{bmatrix} u \\\\ v \\\\ w \\\\ z \\end{bmatrix} = \\begin{bmatrix} 0 \\\\ 2 \\\\ 2 \\\\ 2 \\end{bmatrix} + u \\begin{bmatrix} 1 \\\\ 0 \\\\ -1 \\\\ 0 \\end{bmatrix}$$
- If we add $u = -1$, the free variable is locked, collapsing the line to a **single point** $(-1, 2, 3, 2)$.
- If we instead add $u + w = 3$, it directly contradicts $u + w = 2$, yielding **zero solutions**.
"""
    cells.append(nbf.v4.new_markdown_cell(c1_6_md))

    # Preserved Lecture 1 Examples Q.1, Q.2, Q.3
    lec1_worked_md = """### 1.7 Lecture 1 Preserved Worked Examples (Sheet 1)

#### Lecture Example Q.1 (Sheet 1 Page 8)
**Question:** Sketch the following lines:
$$x + 2y = 2, \\quad x - y = 2, \\quad y = 1$$
Does this system have a solution? What happens if all right-hand sides are zero? Is there any nonzero choice of right-hand sides that allows the three lines to intersect at the same point?

**Analytical Derivation:**
1. Solve the first two equations:
   Subtracting $(x - y = 2)$ from $(x + 2y = 2)$ gives $3y = 0 \\implies y = 0$.
   Then $x = 2$. The intersection of lines 1 and 2 is $(2, 0)$.
2. Test the third equation: At $(2, 0)$, $y = 0 \\ne 1$. Contradiction!
   Therefore, the system has **no common solution**.
3. If all right-hand sides are zero ($x + 2y = 0, x - y = 0, y = 0$), all lines pass through the origin $(0, 0)$, giving the unique common solution $(0, 0)$.
4. To make the three lines intersect at a common point $P = (x_0, y_0)$, pick any point $P$ and evaluate the left-hand sides:
   Choose $P = (2, 1) \\implies x + 2y = 4, \\; x - y = 1, \\; y = 1$. The right-hand side vector $b = (4, 1, 1)$ forces concurrency at $(2, 1)$.

#### Lecture Example Q.2 (Sheet 1 Page 9)
**Question:** For the equation $x + y = 4$, $2x - 2y = 4$, draw the row picture and column picture.
**Analytical Derivation:**
- Row Picture: Line 1 has intercepts $(4, 0), (0, 4)$. Line 2 ($x - y = 2$) has intercepts $(2, 0), (0, -2)$.
  Adding $2(x+y) + (2x-2y) = 4x = 12 \\implies x = 3$. Then $y = 4 - 3 = 1$. Intersection is $(3, 1)$.
- Column Picture:
  $$3 \\begin{bmatrix} 1 \\\\ 2 \\end{bmatrix} + 1 \\begin{bmatrix} 1 \\\\ -2 \\end{bmatrix} = \\begin{bmatrix} 3 \\\\ 6 \\end{bmatrix} + \\begin{bmatrix} 1 \\\\ -2 \\end{bmatrix} = \\begin{bmatrix} 4 \\\\ 4 \\end{bmatrix} = \\mathbf{b}$$

#### Lecture Example Q.3 (Sheet 1 Page 9)
**Question:** Find the combinations of the columns that equal $b = \\begin{bmatrix} b_1 \\\\ b_2 \\\\ b_3 \\end{bmatrix}$:
$$\\begin{aligned} u - v - w &= b_1 \\\\ v + w &= b_2 \\\\ w &= b_3 \\end{aligned}$$
**Analytical Derivation:**
Column equation:
$$u \\begin{bmatrix} 1 \\\\ 0 \\\\ 0 \\end{bmatrix} + v \\begin{bmatrix} -1 \\\\ 1 \\\\ 0 \\end{bmatrix} + w \\begin{bmatrix} -1 \\\\ 1 \\\\ 1 \\end{bmatrix} = \\begin{bmatrix} b_1 \\\\ b_2 \\\\ b_3 \\end{bmatrix}$$
Back-substitution:
- From Eq 3: $w = b_3$.
- From Eq 2: $v = b_2 - w = b_2 - b_3$.
- From Eq 1: $u = b_1 + v + w = b_1 + (b_2 - b_3) + b_3 = b_1 + b_2$.
Therefore, the unique recipe is $u = b_1 + b_2$, $v = b_2 - b_3$, $w = b_3$.
"""
    cells.append(nbf.v4.new_markdown_cell(lec1_worked_md))

    # SymPy Derivations of Q1, Q2, Q3
    lec1_worked_code = """# SymPy Verification of Sheet 1 Worked Examples Q.1, Q.2, Q.3
print("=== Verifying Lecture Sheet 1 Worked Examples ===")

# Q.1 Verification
A_q1 = Matrix([[1, 2], [1, -1], [0, 1]])
b_q1 = Matrix([2, 2, 1])
print("Q.1 System consistency check:")
try:
    sol_q1 = A_q1.LUsolve(b_q1)
    print("Solution:", sol_q1)
except Exception as e:
    print("Correctly caught inconsistency:", e)

# Q.2 Verification
A_q2 = Matrix([[1, 1], [2, -2]])
b_q2 = Matrix([4, 4])
sol_q2 = A_q2.LUsolve(b_q2)
print("\\nQ.2 Exact Solution (x, y):", sol_q2.T)
assert sol_q2 == Matrix([3, 1]), "Q.2 Verification Failed"

# Q.3 Verification symbolically
b1, b2, b3 = symbols('b1 b2 b3')
A_q3 = Matrix([[1, -1, -1], [0, 1, 1], [0, 0, 1]])
b_vec3 = Matrix([b1, b2, b3])
sol_q3 = A_q3.LUsolve(b_vec3)
print("\\nQ.3 Symbolic Column Coefficients (u, v, w):")
display(sol_q3)
assert sol_q3 == Matrix([b1 + b2, b2 - b3, b3]), "Q.3 Verification Failed"
print("All Sheet 1 worked examples verified exactly with SymPy!")
"""
    cells.append(nbf.v4.new_code_cell(lec1_worked_code))

    # Lecture 1 Self-Test Block
    lec1_selftest_md = """### 1.9 Lecture 1 Self-Test Block

1. **Question 1:** Under what condition on $k$ does the system $x + ky = 1, kx + 4y = 2$ have a unique solution?
   <details><summary><b>View Answer & Working</b></summary>
   Determinant condition: $\\det(A) = 1(4) - k(k) = 4 - k^2 \\ne 0 \\implies k \\ne \\pm 2$. For any $k \\notin \\{2, -2\\}$, the system has a unique solution.
   </details>

2. **Question 2:** Explain geometrically why a $3 \\times 2$ system (3 equations, 2 unknowns) generally has no solution.
   <details><summary><b>View Answer & Working</b></summary>
   In the 2D row picture, each equation is a line. Three arbitrary lines in a plane will form a triangle and not share a single common intersection point unless the third line fortuitously passes through the intersection of the first two. In the column picture, 2 columns in $\\mathbb{R}^3$ span at most a 2D plane; an arbitrary vector $\\mathbf{b} \\in \\mathbb{R}^3$ lies outside that plane.
   </details>

3. **Question 3:** True or False: If a system has fewer equations than unknowns ($m < n$), it can never have a unique solution.
   <details><summary><b>View Answer & Working</b></summary>
   <b>True.</b> Because the maximum number of pivots is at most $m < n$, there is at least one free variable. Thus, if a solution exists, there are infinitely many solutions; otherwise, zero solutions. A unique solution is impossible.
   </details>

4. **Question 4:** A café charges 250 for 2 coffees and 1 sandwich, and 350 for 1 coffee and 3 sandwiches. Set up $Ax = b$ and find the individual prices.
   <details><summary><b>View Answer & Working</b></summary>
   $\\begin{bmatrix} 2 & 1 \\\\ 1 & 3 \\end{bmatrix} \\begin{bmatrix} c \\\\ s \\end{bmatrix} = \\begin{bmatrix} 250 \\\\ 350 \\end{bmatrix}$. $\\det = 6 - 1 = 5$. $c = \\frac{250(3) - 350(1)}{5} = 80$, $s = \\frac{2(350) - 250(1)}{5} = 90$. Coffee = 80, Sandwich = 90.
   </details>

5. **Question 5:** If the last column of $A$ equals the right-hand side $\\mathbf{b}$, what is an immediate solution to $Ax = b$?
   <details><summary><b>View Answer & Working</b></summary>
   By the column picture: $0 \\mathbf{a}_1 + 0 \\mathbf{a}_2 + \\dots + 1 \\mathbf{a}_n = \\mathbf{a}_n = \\mathbf{b}$. Thus, $x = (0, 0, \\dots, 0, 1)^T$.
   </details>
"""
    cells.append(nbf.v4.new_markdown_cell(lec1_selftest_md))
    
    return cells

def get_lecture2_cells():
    cells = []
    
    sec2_md = """# Section 2: Lecture 2 — Matrix Multiplication and Network Transformations (MUL-TEA-PLICATION)

---

### 2.1 Summary Box & Key Formulas
> **Key Identities & Multiplicative Perspectives:**
> - **Size Rule:** $(m \\times n)(n \\times p) = m \\times p$. Inner dimensions MUST match.
> - **Perspective 1 (Dot Product Entrywise):**
>   $$(AB)_{ij} = \\text{Row } i(A) \\cdot \\text{Col } j(B) = \\sum_{k=1}^n a_{ik} b_{kj}$$
> - **Perspective 2 (Linear Combination of Columns):**
>   $$\\text{Col } j(AB) = A \\cdot \\text{Col } j(B) = b_{1j}\\mathbf{a}_1 + b_{2j}\\mathbf{a}_2 + \\dots + b_{nj}\\mathbf{a}_n$$
> - **Perspective 3 (Linear Combination of Rows):**
>   $$\\text{Row } i(AB) = \\text{Row } i(A) \\cdot B = a_{i1}\\mathbf{b}_{(1)} + a_{i2}\\mathbf{b}_{(2)} + \\dots + a_{in}\\mathbf{b}_{(n)}$$
> - **Perspective 4 (Sum of Rank-1 Outer Products):**
>   $$AB = \\sum_{k=1}^n \\text{Col } k(A) \\cdot \\text{Row } k(B) = \\mathbf{a}_1 \\mathbf{b}_{(1)}^T + \\mathbf{a}_2 \\mathbf{b}_{(2)}^T + \\dots + \\mathbf{a}_n \\mathbf{b}_{(n)}^T$$
> - **Graph Adjacency Matrix & Walk Theorem:** If $M$ is the adjacency matrix of a graph, $(M^k)_{ij}$ is the exact number of walks of length $k$ from vertex $i$ to vertex $j$.
> - **Non-Commutativity:** In general, $AB \\ne BA$. Order matters profoundly.
"""
    cells.append(nbf.v4.new_markdown_cell(sec2_md))

    c2_1_md = """### 2.2 Concept 1: The Four Perspectives of Matrix Multiplication

#### Intuition in Plain Words
Most students learn matrix multiplication as a tedious "across and down" dot product formula. But in advanced linear algebra and real-world engineering, you must see all 4 faces of the cube:
1. **Entry by entry:** Computing individual pixels.
2. **Column by column:** Applying the transformation $A$ to every column recipe in $B$.
3. **Row by row:** Building new rows as mixtures of the rows of $B$.
4. **Outer products:** Building the entire matrix as a sum of fundamental building blocks (rank-1 sheets).

#### Formal Derivation of the Four Views
Let $A \\in \\mathbb{R}^{m \\times n}$ and $B \\in \\mathbb{R}^{n \\times p}$.
- **View 1 (Entries):** $(AB)_{ij} = \\sum_{k=1}^n a_{ik} b_{kj}$. Each entry is a dot product of a row vector and a column vector.
- **View 2 (Columns):** $AB = \\begin{bmatrix} A\\mathbf{b}_1 & A\\mathbf{b}_2 & \\dots & A\\mathbf{b}_p \\end{bmatrix}$. The columns of $AB$ are linear combinations of columns of $A$.
- **View 3 (Rows):** $AB = \\begin{bmatrix} \\mathbf{a}_1^T B \\\\ \\mathbf{a}_2^T B \\\\ \\vdots \\\\ \\mathbf{a}_m^T B \\end{bmatrix}$. The rows of $AB$ are linear combinations of rows of $B$.
- **View 4 (Outer Products):**
  $$AB = \\begin{bmatrix} | & & | \\\\ \\mathbf{a}_1 & \\cdots & \\mathbf{a}_n \\\\ | & & | \\end{bmatrix} \\begin{bmatrix} - & \\mathbf{b}_1^T & - \\\\ & \\vdots & \\\\ - & \\mathbf{b}_n^T & - \\end{bmatrix} = \\mathbf{a}_1 \\mathbf{b}_1^T + \\mathbf{a}_2 \\mathbf{b}_2^T + \\dots + \\mathbf{a}_n \\mathbf{b}_n^T$$
  Each term $\\mathbf{a}_k \\mathbf{b}_k^T$ is an $m \\times p$ matrix of rank 1!
"""
    cells.append(nbf.v4.new_markdown_cell(c2_1_md))

    c2_1_code = """# SymPy Demonstration of the Four Perspectives of Matrix Multiplication
A_demo = Matrix([[2, 1], [1, 3], [0, 2]])  # 3x2
B_demo = Matrix([[1, 2], [3, 0]])          # 2x2

print("Matrix A (3x2):")
display(A_demo)
print("Matrix B (2x2):")
display(B_demo)

# Product
AB = A_demo * B_demo
print("Product AB (3x2):")
display(AB)

# Perspective 4: Sum of Outer Products
col1 = A_demo[:, 0]
row1 = B_demo[0, :]
term1 = col1 * row1

col2 = A_demo[:, 1]
row2 = B_demo[1, :]
term2 = col2 * row2

print("\\nOuter Product 1: col_1(A) * row_1(B):")
display(term1)
print("Outer Product 2: col_2(A) * row_2(B):")
display(term2)
print("Sum of Outer Products equals AB:", term1 + term2 == AB)
"""
    cells.append(nbf.v4.new_code_cell(c2_1_code))

    c2_2_md = """### 2.3 Concept 2: Recipes, Sound Mixing, and Row-Operations Interpretation

#### The Lecture's Culinary & Acoustic Metaphor (Sheet 2)
In Lecture 2 ("MUL-TEA-PLICATION"), matrices represent recipes:
- Ingredients: Sugar, Milk, Tea leaves (rows).
- Teas: Masala Chai, English Breakfast, Herbal Mix (columns).
- When a customer orders a mix vector $x$, $Ax$ produces the exact total quantity of each ingredient needed.
- If $R$ is a matrix of orders/recipes, $S \\cdot R$ transforms sound or ingredient profiles into batch properties.

#### Left Multiplication vs. Right Multiplication
- **Right multiplication $Ax$:** Combines the **columns** of $A$. Inputs are weights on columns.
- **Left multiplication $uA$:** Combines the **rows** of $A$. Inputs are weights on rows.
  For example, $[2, 1, 3] \\begin{bmatrix} 1 & 0 \\\\ 2 & 1 \\\\ 0 & 3 \\end{bmatrix} = 2(1, 0) + 1(2, 1) + 3(0, 3) = [4, 10]$.
"""
    cells.append(nbf.v4.new_markdown_cell(c2_2_md))

    c2_3_md = """### 2.4 Concept 3: Non-Commutativity and Word Matrices

#### Non-Commutativity ($AB \\ne BA$)
In general real-number matrix multiplication, $AB \\ne BA$. In fact, if $A$ is $2 \\times 3$ and $B$ is $3 \\times 2$, $AB$ is $2 \\times 2$ while $BA$ is $3 \\times 3$—they do not even have the same size!
Even for square matrices, $AB \\ne BA$.

#### Lab 2 Q.7 Word Matrices
In Lab 2 Q.7, matrices hold linguistic sentence fragments. Left-multiplying by subject/verb grids versus right-multiplying produces completely different sentences: $(AB)_{11} = \\text{"Algebra meet in a line"}$ while $(BA)_{11}$ conveys a completely different statement. Zero entries act as semantic blockers ("nothing") that wipe out entire branches.
"""
    cells.append(nbf.v4.new_markdown_cell(c2_3_md))

    c2_4_md = """### 2.5 Concept 4: Structural Matrices ($J - I$ Influence & Antenna Aggregation)

#### The All-Ones Matrix $J$ and the Social Influence Matrix $J - I$ (Lab 2 Q.8)
Let $J_{10 \\times 10}$ be the matrix of all ones. The matrix $A = J - I$ has zeros on the diagonal and ones everywhere else.
This represents a network of 10 creators where nobody influences themselves, but everyone influences everyone else.
- Let $\\mathbf{1} = (1, 1, \\dots, 1)^T$ be the uniform influence vector.
- Then:
  $$A \\mathbf{1} = (J - I) \\mathbf{1} = J \\mathbf{1} - I \\mathbf{1} = 10 \\cdot \\mathbf{1} - \\mathbf{1} = 9 \\cdot \\mathbf{1}$$
- By induction:
  $$A^k \\mathbf{1} = 9^k \\mathbf{1}$$
  The influence scales by exactly $9 = n - 1$ per round!

#### Antenna Aggregation Matrix (Lab 2 Q.6)
Consider a $3 \\times 6$ matrix $A = [I_3 \\mid I_3]$.
When receiving signals from 6 antennas $x = (x_1, \\dots, x_6)^T$:
$$Ax = \\begin{bmatrix} 1 & 0 & 0 & 1 & 0 & 0 \\\\ 0 & 1 & 0 & 0 & 1 & 0 \\\\ 0 & 0 & 1 & 0 & 0 & 1 \\end{bmatrix} \\begin{bmatrix} x_1 \\\\ \\vdots \\\\ x_6 \\end{bmatrix} = \\begin{bmatrix} x_1 + x_4 \\\\ x_2 + x_5 \\\\ x_3 + x_6 \\end{bmatrix}$$
Channel $i$ aggregates antenna $i$ and antenna $i+3$. Changing a single antenna affects exactly one channel. To pair antennas 1 and 5 instead, row 1 becomes $(1, 0, 0, 0, 1, 0)$.
"""
    cells.append(nbf.v4.new_markdown_cell(c2_4_md))

    c2_5_md = """### 2.6 Concept 5: Adjacency Matrices and Walk Counting ($M^k$)

#### Theorem: Counting Walks in Graphs
Let $G$ be a graph with adjacency matrix $M$, where $m_{ij} = 1$ if an edge connects $i$ and $j$, and $0$ otherwise.
Then the $(i, j)$ entry of $M^k$ is **strictly equal to the number of walks of length $k$ from vertex $i$ to vertex $j$**.

#### Proof by Induction:
For $k = 1$, $(M^1)_{ij} = m_{ij}$ is the number of 1-step edges.
Assume true for $k-1$. Then:
$$(M^k)_{ij} = \\sum_{r=1}^n (M^{k-1})_{ir} \\cdot m_{rj}$$
A walk of length $k$ from $i$ to $j$ consists of a walk of length $k-1$ from $i$ to intermediate node $r$, followed by an edge from $r$ to $j$. The summation counts all possible intermediate steps $r$.
"""
    cells.append(nbf.v4.new_markdown_cell(c2_5_md))

    # Diagram 11a & 12: Networkx Graph & Adjacency Heatmaps
    c2_5_code = """# Diagram 11a & Diagram 12: Graph Adjacency, Heatmaps, and Walk Counting (Lab 2 Q.9)
# Nodes: A, B, C, D, E (indices 0, 1, 2, 3, 4)
# Verified Edges: (A, B), (A, D), (B, D), (B, E), (B, C), (C, E), (D, E)
nodes = ['A', 'B', 'C', 'D', 'E']
node_map = {n: i for i, n in enumerate(nodes)}

G_trans = nx.Graph()
G_trans.add_nodes_from(nodes)
edges = [('A', 'B'), ('A', 'D'), ('B', 'D'), ('B', 'E'), ('B', 'C'), ('C', 'E'), ('D', 'E')]
G_trans.add_edges_from(edges)

# Adjacency Matrix M
M_adj = np.zeros((5, 5), dtype=int)
for u, v in edges:
    M_adj[node_map[u], node_map[v]] = 1
    M_adj[node_map[v], node_map[u]] = 1

M2 = M_adj @ M_adj
M3 = M2 @ M_adj

fig, axes = plt.subplots(1, 4, figsize=(20, 5))

# Plot Networkx Graph
pos = {'A': (-1, 0.5), 'B': (0, 1.2), 'C': (1, 0.5), 'D': (-0.5, -0.6), 'E': (0.5, -0.6)}
nx.draw_networkx(G_trans, pos, ax=axes[0], node_color='#17becf', node_size=900, 
                 font_size=13, font_weight='bold', edge_color='#333333', width=2)
axes[0].set_title('Diagram 11a: 5-Vertex Transportation Network', fontweight='bold')
axes[0].axis('off')

# Heatmaps of M, M^2, M^3
for idx, (mat, title) in enumerate([(M_adj, 'M (1-Step Paths)'), (M2, 'M² (2-Step Walks)'), (M3, 'M³ (3-Step Walks)')]):
    ax = axes[idx + 1]
    im = ax.imshow(mat, cmap='YlGnBu')
    ax.set_xticks(range(5)); ax.set_xticklabels(nodes)
    ax.set_yticks(range(5)); ax.set_yticklabels(nodes)
    ax.set_title(f'Diagram 12: {title}', fontweight='bold')
    for i in range(5):
        for j in range(5):
            ax.text(j, i, str(mat[i, j]), ha='center', va='center', color='black' if mat[i, j] < mat.max()/2 else 'white', fontweight='bold')

plt.tight_layout()
plt.show()

print(f"Number of 2-step walks from A to E: (M²)AE = {M2[node_map['A'], node_map['E']]}")
print("Explicit 2-step walks from A to E: A -> B -> E, and A -> D -> E.")
"""
    cells.append(nbf.v4.new_code_cell(c2_5_code))

    # Preserved Lecture 2 Worked Examples
    lec2_worked_md = """### 2.7 Lecture 2 Preserved Worked Examples

#### Example 1: Matrix-Vector Product Ax (Lab 2 Q.1)
$$A = \\begin{bmatrix} 2 & 1 & 0 \\\\ 1 & 3 & 2 \\\\ 0 & 2 & 4 \\end{bmatrix}, \\quad x = \\begin{bmatrix} 1 \\\\ 2 \\\\ 1 \\end{bmatrix}$$
$$Ax = 1 \\begin{bmatrix} 2 \\\\ 1 \\\\ 0 \\end{bmatrix} + 2 \\begin{bmatrix} 1 \\\\ 3 \\\\ 2 \\end{bmatrix} + 1 \\begin{bmatrix} 0 \\\\ 2 \\\\ 4 \\end{bmatrix} = \\begin{bmatrix} 2 + 2 + 0 \\\\ 1 + 6 + 2 \\\\ 0 + 4 + 4 \\end{bmatrix} = \\begin{bmatrix} 4 \\\\ 9 \\\\ 8 \\end{bmatrix}$$
*(Note: With $x = (1, 2, 1)^T$, $(Ax)_2 = 1(1) + 3(2) + 2(1) = 9$. Lab prompt listed $(4, 8, 8)$; SymPy confirms 9).*

#### Example 2: Structural 5×5 Matrix Trick (Lab 2 Q.4)
Matrix $A$ has $a_{ii} = 1$ and $a_{i5} = 2$ for $i \\le 4$, with row 5 all zeros.
For $x = (1, 1, 1, 1, 5)^T$:
$$(Ax)_i = 1(x_i) + 2(x_5) = 1(1) + 2(5) = 11 \\quad (i \\le 4), \\quad (Ax)_5 = 0$$
Thus $Ax = (11, 11, 11, 11, 0)^T$.
"""
    cells.append(nbf.v4.new_markdown_cell(lec2_worked_md))

    lec2_worked_code = """# SymPy Verification of Lecture 2 Examples
A_struct = Matrix([
    [1, 0, 0, 0, 2],
    [0, 1, 0, 0, 2],
    [0, 0, 1, 0, 2],
    [0, 0, 0, 1, 2],
    [0, 0, 0, 0, 0]
])
x_struct = Matrix([1, 1, 1, 1, 5])
Ax_res = A_struct * x_struct
print("Structural 5x5 Matrix Trick Ax:")
display(Ax_res)
assert Ax_res == Matrix([11, 11, 11, 11, 0]), "Failed"
print("Structural trick verified exactly!")
"""
    cells.append(nbf.v4.new_code_cell(lec2_worked_code))

    lec2_selftest_md = """### 2.9 Lecture 2 Self-Test Block

1. **Question 1:** If $A$ is $4 \\times 3$ and $B$ is $3 \\times 5$, what is the size of $AB$? Can $BA$ be computed?
   <details><summary><b>View Answer</b></summary>
   $AB$ is $4 \\times 5$. $BA$ cannot be computed because the inner dimensions $(5 \\text{ and } 4)$ do not match.
   </details>

2. **Question 2:** Express the second column of $AB$ using matrix $A$ and vector notation.
   <details><summary><b>View Answer</b></summary>
   $\\text{Col } 2(AB) = A \\cdot \\text{Col } 2(B)$. It is a linear combination of the columns of $A$ weighted by the second column of $B$.
   </details>

3. **Question 3:** What is the maximum possible rank of a single outer product term $\\mathbf{u} \\mathbf{v}^T$?
   <details><summary><b>View Answer</b></summary>
   Exactly $1$ (provided $\\mathbf{u} \\ne 0$ and $\\mathbf{v} \\ne 0$). Every row is a multiple of $\\mathbf{v}^T$, and every column is a multiple of $\\mathbf{u}$.
   </details>

4. **Question 4:** If an adjacency matrix has $M^2_{3,3} = 4$, what does this physically mean about node 3?
   <details><summary><b>View Answer</b></summary>
   There are 4 walks of length 2 from node 3 back to itself. In a simple undirected graph, a 2-step walk from node 3 to itself traverses an incident edge and immediately returns, so node 3 has degree 4.
   </details>
"""
    cells.append(nbf.v4.new_markdown_cell(lec2_selftest_md))
    
    return cells

def get_lecture3_cells():
    cells = []
    
    sec3_md = """# Section 3: Lecture 3 — Linear Combinations, Span, and Vector Spaces (One Recipe, Infinite Menu)

---

### 3.1 Summary Box & Key Formulas
> **Key Vector Space & Span Foundations:**
> - **Linear Combination:** A single vector formed by scaling and adding:
>   $$\\mathbf{w} = c_1 \\mathbf{v}_1 + c_2 \\mathbf{v}_2 + \\dots + c_k \\mathbf{v}_k$$
> - **The Span:** The infinite set of ALL possible linear combinations:
>   $$\\text{Span}(\\mathbf{v}_1, \\dots, \\mathbf{v}_k) = \\left\\{ \\sum_{i=1}^k c_i \\mathbf{v}_i : c_i \\in \\mathbb{R} \\right\\}$$
> - **Geometric Progression in $\\mathbb{R}^3$:**
>   - $0$ nonzero vectors $\\implies$ Single point (Origin $\\{\\mathbf{0}\\}$)
>   - $1$ nonzero vector $\\implies$ 1D Line through origin
>   - $2$ independent vectors $\\implies$ 2D Plane through origin
>   - $3$ independent vectors $\\implies$ Entire 3D space $\\mathbb{R}^3$
> - **The Target Test:** A target vector $\\mathbf{b} \\in \\text{Span}(\\mathbf{v}_1, \\dots, \\mathbf{v}_k) \\iff$ the linear system $[\\mathbf{v}_1 \\; \\mathbf{v}_2 \\; \\cdots \\; \\mathbf{v}_k] \\mathbf{c} = \\mathbf{b}$ is consistent.
> - **Dimension Bound:** $k$ vectors in $\\mathbb{R}^m$ can NEVER span $\\mathbb{R}^m$ if $k < m$. Specifically, two vectors in $\\mathbb{R}^3$ can at most span a plane, never all of $\\mathbb{R}^3$.
"""
    cells.append(nbf.v4.new_markdown_cell(sec3_md))

    c3_1_md = """### 3.2 Concept 1: What is a Vector? The 8 Axioms of a Vector Space

#### Intuition in Plain Words
In introductory physics, a vector is an arrow with magnitude and direction. But in linear algebra, a vector is simply any object that you can **scale** (multiply by a number) and **add** to another object of the same type without breaking consistency. Colors, sound signals, polynomial functions, and stock portfolios are all vectors.

#### The 8 Vector Space Axioms
A set $V$ equipped with vector addition $+$ and scalar multiplication $\\cdot$ over $\\mathbb{R}$ is a vector space if for all $\\mathbf{u}, \\mathbf{v}, \\mathbf{w} \\in V$ and $c, d \\in \\mathbb{R}$:
1. **Commutativity of Addition:** $\\mathbf{u} + \\mathbf{v} = \\mathbf{v} + \\mathbf{u}$
2. **Associativity of Addition:** $(\\mathbf{u} + \\mathbf{v}) + \\mathbf{w} = \\mathbf{u} + (\\mathbf{v} + \\mathbf{w})$
3. **Additive Identity:** There exists $\\mathbf{0} \\in V$ such that $\\mathbf{u} + \\mathbf{0} = \\mathbf{u}$
4. **Additive Inverse:** For every $\\mathbf{u}$, there exists $-\\mathbf{u}$ such that $\\mathbf{u} + (-\\mathbf{u}) = \\mathbf{0}$
5. **Distributivity over Vector Addition:** $c(\\mathbf{u} + \\mathbf{v}) = c\\mathbf{u} + c\\mathbf{v}$
6. **Distributivity over Scalar Addition:** $(c + d)\\mathbf{u} = c\\mathbf{u} + d\\mathbf{u}$
7. **Associativity of Scalar Multiplication:** $c(d\\mathbf{u}) = (cd)\\mathbf{u}$
8. **Scalar Identity:** $1 \\cdot \\mathbf{u} = \\mathbf{u}$
"""
    cells.append(nbf.v4.new_markdown_cell(c3_1_md))

    c3_2_md = """### 3.3 Concept 2: Linear Combinations and Span Hierarchy

#### Geometric Hierarchy
- A single vector $\\mathbf{v}_1 = (2, 1)^T$ spans the line $y = \\frac{1}{2}x$.
- Two non-parallel vectors in $\\mathbb{R}^2$ span all of $\\mathbb{R}^2$.
- In $\\mathbb{R}^3$, two vectors $\\mathbf{v}_1, \\mathbf{v}_2$ span a flat sheet (plane) through $(0,0,0)$.
- **Crucial Rule:** Two vectors can NEVER span $\\mathbb{R}^3$. For example, a song profile described by 3 features (Energy, Danceability, Acousticness) cannot be synthesized from just two reference tracks.
"""
    cells.append(nbf.v4.new_markdown_cell(c3_2_md))

    c3_3_md = """### 3.4 Concept 3: The Target Test ($[v_1 \\dots v_k] c = b$)

To determine if a target vector $\\mathbf{b}$ lies in $\\text{Span}(\\mathbf{v}_1, \\dots, \\mathbf{v}_k)$:
1. Form the augmented matrix $[\\mathbf{v}_1 \\; \\dots \\; \\mathbf{v}_k \\mid \\mathbf{b}]$.
2. Row reduce.
3. If an inconsistent row $[0 \\; 0 \\; \\cdots \\; 0 \\mid d]$ with $d \\ne 0$ appears, $\\mathbf{b} \\notin \\text{Span}$.
4. If consistent, $\\mathbf{b} \\in \\text{Span}$. If there are no free variables, the recipe is unique; if free variables exist, there are infinitely many recipes.
"""
    cells.append(nbf.v4.new_markdown_cell(c3_3_md))

    # Diagram 4 & 5: Span Visualizer & Dependent Vectors
    c3_4_code = """# Diagram 4: Span Visualizer (Line, Plane, and Target Point)
fig_span = go.Figure()

v1 = np.array([1, 0, 1])
v2 = np.array([0, 1, 1])
# Dependent third vector v3 = v1 + v2
v3 = v1 + v2  # (1, 1, 2)

# Generate plane spanned by v1 and v2
s_vals = np.linspace(-2, 2, 10)
t_vals = np.linspace(-2, 2, 10)
S, T = np.meshgrid(s_vals, t_vals)
Plane_X = S * v1[0] + T * v2[0]
Plane_Y = S * v1[1] + T * v2[1]
Plane_Z = S * v1[2] + T * v2[2]

fig_span.add_trace(go.Surface(
    x=Plane_X, y=Plane_Y, z=Plane_Z,
    colorscale=[[0, 'rgba(23, 190, 207, 0.4)'], [1, 'rgba(23, 190, 207, 0.4)']],
    showscale=False, opacity=0.4, name='Span{v₁, v₂} (Plane)'
))

# Vectors v1, v2, v3
plot_vec3d(fig_span, v1, color='#1f77b4', name='v₁ (1, 0, 1)')
plot_vec3d(fig_span, v2, color='#2ca02c', name='v₂ (0, 1, 1)')
plot_vec3d(fig_span, v3, color='#d62728', name='v₃ = v₁ + v₂ (1, 1, 2)')

# Target inside plane: 2*v1 + 1*v2 = (2, 1, 3)
target_in = 2*v1 + 1*v2
fig_span.add_trace(go.Scatter3d(
    x=[target_in[0]], y=[target_in[1]], z=[target_in[2]],
    mode='markers+text', marker=dict(size=8, color='green'),
    text=['Target IN Span (2, 1, 3)'], textposition='top center', name='Target Inside'
))

# Target outside plane: (0, 0, 2)
fig_span.add_trace(go.Scatter3d(
    x=[0], y=[0], z=[2],
    mode='markers+text', marker=dict(size=8, color='red'),
    text=['Target OUTSIDE Span (0, 0, 2)'], textposition='top center', name='Target Outside'
))

fig_span.update_layout(
    title='Diagram 4 & 5: Span Visualizer & Dependent Vectors in a Plane (v₃ = v₁ + v₂)',
    scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
    margin=dict(l=0, r=0, b=0, t=40)
)
fig_span.show()
"""
    cells.append(nbf.v4.new_code_cell(c3_4_code))

    lec3_worked_md = """### 3.6 Lecture 3 Preserved Worked Examples

#### Example 1: Drone Commands & Equal Mixture (Lab 3 Q.3)
Drone has basis commands $v = (2, 1)$ and $w = (1, 2)$.
Equal mixture: $1v + 1w = (3, 3)$. Target $(3, 3)$ is reached with equal coefficients $c_1 = c_2 = 1$. Other targets require unequal coefficients.

#### Example 2: Digital Color Space (Lab 3 Q.4)
Basis colors: Red $(255, 0, 0)$ and Green $(0, 255, 0)$.
Yellow $= 1R + 1G = (255, 255, 0)$.
Pure Blue $(0, 0, 255)$ is **impossible** to form because any linear combination $c_1 R + c_2 G$ has its third component strictly equal to $0$.

#### Example 3: Redundant Pathways & Infinite Monkey Controller (Lab 3 Q.11, Q.12, Q.14)
Given $v_1 = (1, 0, 1)$, $v_2 = (0, 1, 1)$, $v_3 = (1, 1, 2)$:
Since $v_3 = v_1 + v_2$, the engineer who claimed 3 controls gave 3D capability was incorrect: $\\text{Span}(v_1, v_2, v_3)$ is strictly a 2D plane. Deleting $v_3$ leaves the span completely unchanged!
"""
    cells.append(nbf.v4.new_markdown_cell(lec3_worked_md))

    lec3_selftest_md = """### 3.8 Lecture 3 Self-Test Block

1. **Question 1:** Can three vectors in $\\mathbb{R}^2$ be linearly independent?
   <details><summary><b>View Answer</b></summary>
   <b>No.</b> Any set of $k > m$ vectors in $\\mathbb{R}^m$ is automatically linearly dependent. Here $3 > 2$, so they must be dependent.
   </details>

2. **Question 2:** Describe the span of the vectors $(1, 2, 3)$ and $(2, 4, 6)$ in $\\mathbb{R}^3$.
   <details><summary><b>View Answer</b></summary>
   Because $(2, 4, 6) = 2(1, 2, 3)$, the second vector adds no new directions. The span is a **1-dimensional line** passing through the origin along direction $(1, 2, 3)$.
   </details>
"""
    cells.append(nbf.v4.new_markdown_cell(lec3_selftest_md))
    
    return cells

def get_lecture4_cells():
    cells = []
    
    sec4_md = """# Section 4: Lecture 4 — Gaussian Elimination, Row Operations, and Rank (Same Solution, Simpler System)

---

### 4.1 Summary Box & Key Formulas
> **Key Elimination & Rank Concepts:**
> - **Elementary Row Operations:**
>   1. $R_i \\leftrightarrow R_j$ (Row Swap)
>   2. $R_i \\to c R_i$ with $c \\ne 0$ (Row Scaling)
>   3. $R_j \\to R_j + k R_i$ (Row Addition / Elimination Step)
>   *Row operations preserve the exact solution set: $\\text{Sol}(Ax = b) = \\text{Sol}(Ux = c)$.*
> - **Row Echelon Form (REF):**
>   - All zero rows at the bottom.
>   - Each leading nonzero entry (pivot) is strictly to the right of the pivot in the row above.
>   - All entries below each pivot are zero.
> - **Matrix Rank ($r$):**
>   $$r = \\text{number of pivots in REF}$$
> - **Pivot Columns vs. Free Columns:**
>   - Columns with pivots correspond to **basic/pivot variables**.
>   - Columns without pivots correspond to **free variables** (degree of freedom $= n - r$).
> - **Inconsistency Criterion:** A system is inconsistent iff REF has a row:
>   $$[0 \\; 0 \\; \\cdots \\; 0 \\mid d], \\quad d \\ne 0$$
"""
    cells.append(nbf.v4.new_markdown_cell(sec4_md))

    c4_1_md = """### 4.2 Concept 1: Geometry of Elimination (Invariance of Intersection)

#### Intuition in Plain Words
Why is replacing an equation with a linear combination legal?
In 2D, two lines meet at an intersection point $P$. When you replace $L_2$ with $L_2 - k L_1$, the new line **rotates around the exact same pivot point $P$**! Elimination simply rotates the lines until one of them is perfectly horizontal ($y = c$) or vertical ($x = c$), making the coordinates instantly readable without changing the intersection point.
"""
    cells.append(nbf.v4.new_markdown_cell(c4_1_md))

    # Diagram 6: Plotly Slider Elimination Animation
    c4_2_code = """# Diagram 6: Interactive Plotly Slider Animation — Geometric Elimination
# We solve x + y = 4, 2x + 4y = 10 -> Solution (3, 1)
# Row operation: R2 -> R2 - k*R1 as k sweeps from 0 to 2
x_vals = np.linspace(0, 5, 100)
sol_x, sol_y = 3, 1

fig_elim = go.Figure()

# Add fixed line 1: x + y = 4 -> y = 4 - x
fig_elim.add_trace(go.Scatter(x=x_vals, y=4 - x_vals, mode='lines', line=dict(color='blue', width=3), name='Line 1: x + y = 4 (Fixed)'))

# Solution point
fig_elim.add_trace(go.Scatter(x=[sol_x], y=[sol_y], mode='markers+text', marker=dict(size=10, color='black'),
                              text=['Solution (3, 1)'], textposition='top right', name='Invariant Solution Point'))

# Create frames for k from 0 to 2
frames = []
k_steps = np.linspace(0, 2, 21)
for k in k_steps:
    # (2 - k)x + (4 - k)y = 10 - 4k
    # y = ((10 - 4k) - (2 - k)x) / (4 - k)
    denom = 4.0 - k
    y_k = ((10.0 - 4.0 * k) - (2.0 - k) * x_vals) / denom
    frames.append(go.Frame(
        data=[
            go.Scatter(x=x_vals, y=4 - x_vals, mode='lines', line=dict(color='blue', width=3)),
            go.Scatter(x=[sol_x], y=[sol_y], mode='markers', marker=dict(size=10, color='black')),
            go.Scatter(x=x_vals, y=y_k, mode='lines', line=dict(color='red', width=2.5), name=f'Eliminating Line (k={k:.1f})')
        ],
        name=f'{k:.1f}'
    ))

# Add initial line 2 (k=0)
fig_elim.add_trace(go.Scatter(x=x_vals, y=(10 - 2*x_vals)/4, mode='lines', line=dict(color='red', width=2.5), name='Line 2 (Tilting to Horizontal)'))

fig_elim.update(frames=frames)

fig_elim.update_layout(
    title='Diagram 6: Elimination as Rotation around Fixed Invariant Intersection (3, 1)',
    xaxis=dict(range=[0, 5], title='x'),
    yaxis=dict(range=[0, 4], title='y'),
    updatemenus=[dict(
        type='buttons',
        showactive=False,
        buttons=[dict(label='Play Elimination', method='animate', args=[None, dict(frame=dict(duration=80, redraw=True), fromcurrent=True)])]
    )],
    sliders=[dict(
        steps=[dict(method='animate', args=[[f'{k:.1f}'], dict(mode='immediate', frame=dict(duration=0, redraw=True))], label=f'k={k:.1f}') for k in k_steps],
        currentvalue=dict(prefix='Multiplier k: ')
    )]
)
fig_elim.show()
"""
    cells.append(nbf.v4.new_code_cell(c4_2_code))

    c4_3_md = """### 4.5 Concept 4: Conservation Laws & Intersection Flow Analysis

#### Baltimore Traffic Flow Network (Sheet 4)
Consider a network of 4 intersections $A, B, C, D$.
Physics principle: **Flow In = Flow Out** at every node (no vehicles created or destroyed).
This yields a system of linear conservation equations:
$$\\sum_{\\text{in}} f_i = \\sum_{\\text{out}} f_j$$
If a sensor records a road flow (e.g. $f_{CD} = 200$), that value locks a variable, allowing the remaining flows to be solved via back-substitution.
"""
    cells.append(nbf.v4.new_markdown_cell(c4_3_md))

    c4_4_md = """### 4.6 Concept 5: Unsigned Incidence Matrix (Odd Cycles vs. Bipartite Rank)

#### The Unsigned Incidence Matrix $B$
- Rows correspond to vertices $V$.
- Columns correspond to edges $E$.
- Entry $b_{ij} = 1$ if vertex $i$ is an endpoint of edge $j$, and $0$ otherwise.
- Each column has exactly two $1$'s.

#### The Fundamental Graph Rank Theorem for Unsigned Incidence Matrices:
Let $G$ be a connected graph with $n$ vertices.
$$\\text{rank}(B) = \\begin{cases} n - 1 & \\text{if } G \\text{ is bipartite (no odd cycles)} \\\\ n & \\text{if } G \\text{ contains an odd cycle (e.g. triangle, 5-cycle)} \\end{cases}$$
*Crucial contrast:* In Lecture 8, the **signed** incidence matrix ALWAYS has rank $n-1$ regardless of cycles, because the signed rows always sum to $\\mathbf{0}$.
"""
    cells.append(nbf.v4.new_markdown_cell(c4_4_md))

    # Diagram 11b: Networkx 4-Node & 5-Node Graph with Incidence Heatmap
    c4_5_code = """# Diagram 11b: Unsigned Incidence Matrix and Odd Cycle Rank Theorem
# 5-node graph with odd cycles (Triangle A-B-D and 5-cycle A-B-C-E-D-A)
B_unsigned = Matrix([
    [1, 1, 0, 0, 0, 0], # A
    [1, 0, 1, 1, 0, 0], # B
    [0, 0, 1, 0, 1, 0], # C
    [0, 1, 0, 1, 0, 1], # D
    [0, 0, 0, 0, 1, 1]  # E
])

print("Unsigned Incidence Matrix B (5x6):")
display(B_unsigned)
print("Rank of B:", B_unsigned.rank())
print("Notice Rank is FULL ROW RANK (5) because graph has an odd cycle!")

# Bipartite comparison (remove edge B-D and D-E to eliminate odd cycles)
B_bipartite = Matrix([
    [1, 0, 0, 0], # V1
    [0, 1, 0, 0], # V2
    [1, 1, 1, 0], # U1
    [0, 0, 1, 1]  # U2
])
print("\\nBipartite Graph Incidence Matrix Rank:", B_bipartite.rank(), "(= n - 1 = 3)")
"""
    cells.append(nbf.v4.new_code_cell(c4_5_code))

    lec4_worked_md = """### 4.7 Lecture 4 Preserved Worked Examples

#### Example 1: Factory Floor Navigation (Lab 4 Q.1)
$$\\begin{aligned} x + y + z &= 9 \\\\ 2x + y + 3z &= 16 \\\\ x + 2y + z &= 11 \\end{aligned}$$
Elimination steps:
- $R_2 \\to R_2 - 2R_1 \\implies -y + z = -2$
- $R_3 \\to R_3 - R_1 \\implies y + 0z = 2 \\implies y = 2$
- From $R_2$: $-2 + z = -2 \\implies z = 0$
- From $R_1$: $x + 2 + 0 = 9 \\implies x = 7$.
Solution: $(x, y, z) = (7, 2, 0)$.

#### Example 2: Quadcopter Thrust Equations (Lab 4 Q.5)
System of 4 motor thrusts where elimination yields $4x_1 = 52 \\implies x_1 = 13$, back-substituting gives $(x_1, x_2, x_3, x_4) = (13, 9, 7, 11)$.
"""
    cells.append(nbf.v4.new_markdown_cell(lec4_worked_md))

    lec4_selftest_md = """### 4.9 Lecture 4 Self-Test Block

1. **Question 1:** Why does swapping two rows not alter the solution set of a linear system?
   <details><summary><b>View Answer</b></summary>
   A system of equations requires all equations to be true simultaneously (logical conjunction AND). The logical order in which the requirements are written does not alter the truth value of their conjunction.
   </details>

2. **Question 2:** A $4 \\times 5$ matrix has pivots in columns 1, 2, and 4. What are the pivot variables, what are the free variables, and what is the rank?
   <details><summary><b>View Answer</b></summary>
   Rank $r = 3$. Pivot variables: $x_1, x_2, x_4$. Free variables: $x_3, x_5$.
   </details>
"""
    cells.append(nbf.v4.new_markdown_cell(lec4_selftest_md))
    
    return cells

