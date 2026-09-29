"""
Module containing Sections 5 to 8 for LinearAlgebra_Master_Notes.ipynb
"""

import nbformat as nbf

def get_lecture5_cells():
    cells = []
    
    sec5_md = """# Section 5: Lecture 5 — Elementary Matrices and LU Decomposition (PREP ONCE, SERVE MANY)

---

### 5.1 Summary Box & Key Formulas
> **Key Identities & Elimination Factorization:**
> - **Elementary Matrix $E$:** Formed by applying a single row operation to the identity matrix $I$. Left-multiplying $A$ by $E$ executes that exact row operation on $A$:
>   $$R_j \\to R_j - c R_i \\iff E_{ij} = I - c \\mathbf{e}_j \\mathbf{e}_i^T$$
> - **Elementary Inverse $E^{-1}$:** Undoes the operation with the opposite sign:
>   $$(E_{ij})^{-1} = I + c \\mathbf{e}_j \\mathbf{e}_i^T$$
> - **The $A = LU$ Decomposition (No Row Swaps):**
>   $$E_k \\cdots E_2 E_1 A = U \\implies A = (E_1^{-1} E_2^{-1} \\cdots E_k^{-1}) U = LU$$
>   - $L$ is strictly **Lower Triangular** with $1$'s on the main diagonal (unit lower triangular).
>   - Below the diagonal, entry $l_{ij}$ holds the exact multiplier used to eliminate entry $(i, j)$: $l_{ij} = \\frac{a_{ij}^{(i-1)}}{\\text{pivot}_i}$.
>   - $U$ is strictly **Upper Triangular** (Row Echelon Form before back-substitution).
> - **Solving $Ax = b$ via Forward & Back Substitution:**
>   1. **Forward Substitution:** Solve $L \\mathbf{c} = \\mathbf{b}$ for $\\mathbf{c}$ (top-down, $O(n^2/2)$ operations).
>   2. **Back Substitution:** Solve $U \\mathbf{x} = \\mathbf{c}$ for $\\mathbf{x}$ (bottom-up, $O(n^2/2)$ operations).
> - **Complexity Advantage:** Elimination costs $\\frac{1}{3}n^3$ operations. Once factorized, each new right-hand side costs only $n^2$ operations!
> - **Symmetric Matrix Pivots:** For $A = \\begin{bmatrix} a & a & a \\\\ a & b & b \\\\ a & b & c \\end{bmatrix}$, three pivots exist iff $a \\ne 0$, $b \\ne a$, and $c \\ne b$.
"""
    cells.append(nbf.v4.new_markdown_cell(sec5_md))

    c5_1_md = """### 5.2 Concept 1: Elementary Matrices and $A = LU$ Factorization

#### Intuition in Plain Words
In Lecture 4, we did row operations step by step by hand. In Lecture 5, we realize that **every row operation is just multiplication by a matrix $E$**.
Even better: while each elementary step $E$ has minus signs ($R_2 - 3R_1$), its inverse $E^{-1}$ has plus signs ($R_2 + 3R_1$).
When we multiply the inverses together in order to build $L = E_1^{-1} E_2^{-1} \\dots E_k^{-1}$, a miracle of linear algebra occurs: **the multipliers fall directly into place without interfering with each other!** No extra work is needed to invert or multiply.

#### The Magic of $L$: Why Multipliers Fall in Place
Suppose we do two elimination steps on a $3 \\times 3$ matrix:
1. $R_2 \\to R_2 - l_{21} R_1 \\implies E_{21} = \\begin{bmatrix} 1 & 0 & 0 \\\\ -l_{21} & 1 & 0 \\\\ 0 & 0 & 1 \\end{bmatrix}, \\quad E_{21}^{-1} = \\begin{bmatrix} 1 & 0 & 0 \\\\ l_{21} & 1 & 0 \\\\ 0 & 0 & 1 \\end{bmatrix}$
2. $R_3 \\to R_3 - l_{32} R_2 \\implies E_{32} = \\begin{bmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & -l_{32} & 1 \\end{bmatrix}, \\quad E_{32}^{-1} = \\begin{bmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & l_{32} & 1 \\end{bmatrix}$
When we multiply the inverses:
$$L = E_{21}^{-1} E_{32}^{-1} = \\begin{bmatrix} 1 & 0 & 0 \\\\ l_{21} & 1 & 0 \\\\ 0 & l_{32} & 1 \\end{bmatrix}$$
The multipliers simply sit in their corresponding entries below the diagonal!
*(Note: If you multiply the $E$'s directly, cross-terms appear: $E_{32} E_{21}$ has fill-in $l_{32} l_{21}$. That is why $A = LU$ is vastly superior to $U = MA$.)*
"""
    cells.append(nbf.v4.new_markdown_cell(c5_1_md))

    # Diagram 13: Elementary Matrix & LU Visualizer
    c5_2_code = """# Diagram 13: Elementary Matrix and LU Visualizer (A, L, U Heatmaps and Substitution Flow)
A_sym = Matrix([
    [2, 1, 1],
    [4, 5, 2],
    [2, -1, 4]
])

L_mat, U_mat, _ = A_sym.LUdecomposition()

print("Matrix A:")
display(A_sym)
print("Lower Triangular Factor L (Unit Diagonal with Multipliers):")
display(L_mat)
print("Upper Triangular Factor U (Pivots on Diagonal):")
display(U_mat)
assert L_mat * U_mat == A_sym, "LU decomposition failed!"
print("Checked L * U == A: TRUE")

# Visual Heatmap
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
matrices = [(np.array(A_sym).astype(float), 'A (Original)'), 
            (np.array(L_mat).astype(float), 'L (Multipliers)'), 
            (np.array(U_mat).astype(float), 'U (Upper Triangular)')]

for idx, (m, title) in enumerate(matrices):
    ax = axes[idx]
    im = ax.imshow(m, cmap='Blues')
    ax.set_title(f'Diagram 13: {title}', fontweight='bold')
    for i in range(3):
        for j in range(3):
            ax.text(j, i, f'{m[i, j]:.0f}', ha='center', va='center', fontsize=12, fontweight='bold',
                    color='black' if abs(m[i, j]) < 3 else 'white')
plt.tight_layout()
plt.show()
"""
    cells.append(nbf.v4.new_code_cell(c5_2_code))

    lec5_worked_md = """### 5.8 Lecture 5 Preserved Worked Examples

#### Example 1: Robotics Engineer Recovering Forgotten Matrix A (Lab 5 Q.8)
After three row operations:
$$E_1: R_2 \\to R_2 - R_1, \\quad E_2: R_3 \\to R_3 - 2R_1, \\quad E_3: R_3 \\to R_3 + R_2$$
The matrix became:
$$U = \\begin{bmatrix} 2 & 1 & 3 \\\\ 0 & 4 & 5 \\\\ 0 & 0 & 6 \\end{bmatrix}$$
To recover $A$ without elimination:
$$E_3 E_2 E_1 A = U \\implies A = E_1^{-1} E_2^{-1} E_3^{-1} U$$
Inverses:
$$E_1^{-1} = \\begin{bmatrix} 1 & 0 & 0 \\\\ 1 & 1 & 0 \\\\ 0 & 0 & 1 \\end{bmatrix}, \\quad E_2^{-1} = \\begin{bmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 2 & 0 & 1 \\end{bmatrix}, \\quad E_3^{-1} = \\begin{bmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & -1 & 1 \\end{bmatrix}$$
Multiplying:
$$A = \\begin{bmatrix} 2 & 1 & 3 \\\\ 2 & 5 & 8 \\\\ 4 & -2 & 7 \\end{bmatrix}$$

#### Example 2: Three Stage Lamps & LU Color Mixing (Lab 5 Q.9)
$$M = \\begin{bmatrix} 1 & 0 & 1 \\\\ 0 & 1 & 1 \\\\ 0 & 1 & 0 \\end{bmatrix} \\implies L = \\begin{bmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 1 & 1 \\end{bmatrix}, \\quad U = \\begin{bmatrix} 1 & 0 & 1 \\\\ 0 & 1 & 1 \\\\ 0 & 0 & -1 \\end{bmatrix}$$
1. **Amber $(4, 3, 1)^T$:** Solve $Lc = (4, 3, 1)^T \\implies c = (4, 3, -2)^T$. Then $Ux = c \\implies x = (2, 1, 2)^T$. Physically valid dials!
2. **Sage $(2, 3, 2)^T$:** $c = (2, 3, -1)^T \\implies x = (1, 2, 1)^T$. Valid!
3. **Pure Blue $(0, 0, 1)^T$:** $c = (0, 0, 1)^T \\implies x = (1, 1, -1)^T$. Mathematically unique, but **physically impossible** because lamp dial 3 cannot have negative brightness $(-1)$.
"""
    cells.append(nbf.v4.new_markdown_cell(lec5_worked_md))

    lec5_worked_code = """# SymPy Verification of Lab 5 Worked Examples
U_robot = Matrix([[2, 1, 3], [0, 4, 5], [0, 0, 6]])
E1_inv = Matrix([[1, 0, 0], [1, 1, 0], [0, 0, 1]])
E2_inv = Matrix([[1, 0, 0], [0, 1, 0], [2, 0, 1]])
E3_inv = Matrix([[1, 0, 0], [0, 1, 0], [0, -1, 1]])
A_robot = E1_inv * E2_inv * E3_inv * U_robot
print("Recovered Matrix A for Robotics Engineer:")
display(A_robot)
assert A_robot == Matrix([[2, 1, 3], [2, 5, 8], [4, -2, 7]]), "Recovery Failed!"

# Three Stage Lamps LU Solution
M_lamp = Matrix([[1, 0, 1], [0, 1, 1], [0, 1, 0]])
L_lamp, U_lamp, _ = M_lamp.LUdecomposition()
b_amber = Matrix([4, 3, 1])
b_sage = Matrix([2, 3, 2])
b_blue = Matrix([0, 0, 1])

x_amb = M_lamp.LUsolve(b_amber)
x_sag = M_lamp.LUsolve(b_sage)
x_blu = M_lamp.LUsolve(b_blue)

print("\\nStage Lamp Solutions:")
print("Amber (4,3,1):", x_amb.T)
print("Sage (2,3,2):", x_sag.T)
print("Pure Blue (0,0,1):", x_blu.T, "<- Contains -1! Physically impossible.")
"""
    cells.append(nbf.v4.new_code_cell(lec5_worked_code))

    lec5_selftest_md = """### 5.10 Lecture 5 Self-Test Block

1. **Question 1:** Why is LU decomposition not unique unless the diagonal of $L$ is specified?
   <details><summary><b>View Answer</b></summary>
   If $A = LU$, you can insert any invertible diagonal matrix $D$: $A = (L D)(D^{-1} U) = L' U'$. To make it unique, we mandate that $L$ has $1$'s on its diagonal (unit lower triangular), which leaves the pivots on the diagonal of $U$.
   </details>

2. **Question 2:** If $A$ is a tridiagonal matrix (nonzeros only on main diagonal and immediately above/below), what are the zero patterns of $L$ and $U$?
   <details><summary><b>View Answer</b></summary>
   $L$ has nonzeros only on the main diagonal and one subdiagonal below it. $U$ has nonzeros only on the main diagonal and one superdiagonal above it. No fill-in occurs anywhere else!
   </details>
"""
    cells.append(nbf.v4.new_markdown_cell(lec5_selftest_md))
    
    return cells

def get_lecture6_cells():
    cells = []
    
    sec6_md = """# Section 6: Lecture 6 — Linear Independence, Column Space, and Redundancy (NEW SIGNAL OR ECHO?)

---

### 6.1 Summary Box & Key Formulas
> **Key Independence & Column Space Identities:**
> - **Linear Independence Definition:**
>   $$\\sum_{i=1}^n c_i \\mathbf{v}_i = \\mathbf{0} \\iff c_1 = c_2 = \\dots = c_n = 0$$
>   Equivalently, $A \\mathbf{x} = \\mathbf{0}$ has **only the trivial solution $\\mathbf{x} = \\mathbf{0}$**.
> - **The Column Space $C(A)$:**
>   $$C(A) = \\text{Span}(\\text{columns of } A) = \\{A \\mathbf{x} : \\mathbf{x} \\in \\mathbb{R}^n\\} \\subseteq \\mathbb{R}^m$$
> - **Rank Solvability Criterion:**
>   $$\\mathbf{b} \\in C(A) \\iff \\text{rank}([A \\mid \\mathbf{b}]) = \\text{rank}(A)$$
> - **The Pivot Theorem for Independence:**
>   - Columns of $A$ are linearly independent $\\iff$ Every column is a pivot column $\\iff \\text{rank}(A) = n$.
>   - If $n > m$ (more columns than rows), the columns are **ALWAYS linearly dependent**.
> - **Basis of $C(A)$:** The pivot columns of the **original matrix $A$** (NOT the columns of $U$ or $R$!) form a basis for $C(A)$.
"""
    cells.append(nbf.v4.new_markdown_cell(sec6_md))

    c6_1_md = """### 6.2 Concept 1: Linear Independence Definition and Geometric Redundancy

#### Intuition in Plain Words
A set of vectors is linearly independent if every vector brings a brand new, genuine direction to the table. If one vector is just an "echo" (a mixture of the others), it is redundant.
In an audio mixer, if microphone 3 simply picks up a mix of microphone 1 and 2, dial 3 is redundant: turning it up gives no new acoustic signals that couldn't already be produced by dials 1 and 2.
"""
    cells.append(nbf.v4.new_markdown_cell(c6_1_md))

    # Diagram 7: Column Space C(A) as a Plane in R^3
    c6_2_code = """# Diagram 7: Column Space C(A) in R³ with Pivot Columns and Redundant Column
fig_c7 = go.Figure()

col1 = np.array([1, 0, 1])
col2 = np.array([0, 1, 1])
col3 = col1 + col2  # (1, 1, 2) redundant
col4 = 2*col1 + col2 # (2, 1, 3) redundant

# Plane C(A)
s = np.linspace(-2, 2, 10)
t = np.linspace(-2, 2, 10)
S, T = np.meshgrid(s, t)
PX = S * col1[0] + T * col2[0]
PY = S * col1[1] + T * col2[1]
PZ = S * col1[2] + T * col2[2]

fig_c7.add_trace(go.Surface(
    x=PX, y=PY, z=PZ,
    colorscale=[[0, 'rgba(23, 190, 207, 0.45)'], [1, 'rgba(23, 190, 207, 0.45)']],
    showscale=False, opacity=0.45, name='Column Space C(A) (2D Plane in R³)'
))

plot_vec3d(fig_c7, col1, color='#1f77b4', name='Col 1 (Pivot)', width=7)
plot_vec3d(fig_c7, col2, color='#2ca02c', name='Col 2 (Pivot)', width=7)
plot_vec3d(fig_c7, col3, color='#d62728', name='Col 3 = Col 1 + Col 2 (Redundant)', width=6)
plot_vec3d(fig_c7, col4, color='#9467bd', name='Col 4 = 2·Col 1 + Col 2 (Redundant)', width=6)

fig_c7.update_layout(
    title='Diagram 7: Column Space C(A) in R³ Spanned by Pivot Columns (Redundant Columns Lie in Plane)',
    scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
    margin=dict(l=0, r=0, b=0, t=40)
)
fig_c7.show()
"""
    cells.append(nbf.v4.new_code_cell(c6_2_code))

    lec6_worked_md = """### 6.6 Lecture 6 Preserved Worked Examples

#### Example 1: Robot Movement Mechanisms (Lab 6 Q.14 Easy-Hard)
$$A = \\begin{bmatrix} 1 & 0 & 1 & 2 \\\\ 0 & 1 & 1 & 1 \\\\ 1 & 1 & 2 & 3 \\end{bmatrix}$$
1. Column relations: $\\mathbf{a}_3 = \\mathbf{a}_1 + \\mathbf{a}_2$, $\\mathbf{a}_4 = 2\\mathbf{a}_1 + \\mathbf{a}_2$.
2. Rank is 2. Controls 3 and 4 are completely redundant.
3. The smallest number of controls needed to preserve all capabilities is **2** (keeping controls 1 and 2).

#### Example 2: The Stage Lamps Challenge & The Trade Argument (Lab 6 Q.14 Challenge)
Four lamps: Red $(1,0,0)$, Cyan $(0,1,1)$, Yellow $(1,1,0)$, White $(1,1,1)$.
$$L = \\begin{bmatrix} 1 & 0 & 1 & 1 \\\\ 0 & 1 & 1 & 1 \\\\ 0 & 1 & 0 & 1 \\end{bmatrix}$$
- Linear dependence relation: $\\text{White} = \\text{Red} + \\text{Cyan} \\implies \\text{Red} + \\text{Cyan} - \\text{White} = \\mathbf{0}$.
- **Returning White:** Leaves $\\{\\text{Red}, \\text{Cyan}, \\text{Yellow}\\}$, which has $\\det = -1 \\ne 0 \\implies$ spans all of $\\mathbb{R}^3$.
- **Returning Red:** Leaves $\\{\\text{Cyan}, \\text{Yellow}, \\text{White}\\}$, which has $\\det = -1 \\ne 0 \\implies$ also spans all of $\\mathbb{R}^3$.
- **Returning Yellow:** DISASTER! The remaining lamps $\\{\\text{Red}, \\text{Cyan}, \\text{White}\\}$ all have green component equal to blue component ($G = B$). Thus they can only make colors on the plane $y = z$. Amber $(4, 3, 1)$ has $G = 3 \\ne B = 1$, so it is impossible without Yellow!
"""
    cells.append(nbf.v4.new_markdown_cell(lec6_worked_md))

    lec6_worked_code = """# SymPy Verification of Lab 6 Challenge
L_theatre = Matrix([
    [1, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 1, 0, 1]
])
print("Theatre Rig Matrix L:")
display(L_theatre)
print("Rank of L:", L_theatre.rank())
print("Nullspace of L (Trade vector):", L_theatre.nullspace()[0].T)

# Test amber (4, 3, 1) with original recipe (2, 1, 2, 0)
b_amber = Matrix([4, 3, 1])
x_orig = Matrix([2, 1, 2, 0])
assert L_theatre * x_orig == b_amber, "Orig recipe failed"

# Trade 1 Red and 1 Cyan for 1 White: (2-1, 1-1, 2, 0+1) = (1, 0, 2, 1)
x_traded = Matrix([1, 0, 2, 1])
assert L_theatre * x_traded == b_amber, "Traded recipe failed"
print("Both recipes successfully produce Amber:", (L_theatre*x_orig).T, "==", (L_theatre*x_traded).T)
"""
    cells.append(nbf.v4.new_code_cell(lec6_worked_code))

    lec6_selftest_md = """### 6.9 Lecture 6 Self-Test Block

1. **Question 1:** If the column space $C(A)$ contains only the zero vector $\\{\\mathbf{0}\\}$, what can you conclude about $A$?
   <details><summary><b>View Answer</b></summary>
   $A$ must be the zero matrix. Because $A \\mathbf{e}_j = \\text{Col } j(A) = \\mathbf{0}$ for every standard basis vector $\\mathbf{e}_j$, all entries of $A$ are zero.
   </details>

2. **Question 2:** True or False: If $\\{\\mathbf{v}_1, \\mathbf{v}_2, \\mathbf{v}_3\\}$ is linearly independent, then $\\{k\\mathbf{v}_1, k\\mathbf{v}_2, k\\mathbf{v}_3\\}$ is also linearly independent for all real numbers $k$.
   <details><summary><b>View Answer</b></summary>
   <b>False.</b> If $k = 0$, the set becomes $\\{\\mathbf{0}, \\mathbf{0}, \\mathbf{0}\\}$, which is immediately linearly dependent. It is only true for $k \\ne 0$.
   </details>
"""
    cells.append(nbf.v4.new_markdown_cell(lec6_selftest_md))
    
    return cells

def get_lecture7_cells():
    cells = []
    
    sec7_md = """# Section 7: Lecture 7 — Null Space, Subspaces, and Complete Solutions (SAME OUTPUT, DIFFERENT INPUTS?)

---

### 7.1 Summary Box & Key Formulas
> **Key Null Space & Subspace Identities:**
> - **The Null Space $N(A)$:**
>   $$N(A) = \\{\\mathbf{x} \\in \\mathbb{R}^n : A \\mathbf{x} = \\mathbf{0}\\} \\subseteq \\mathbb{R}^n$$
>   *Ambient home:* $N(A)$ lives in the input home $\\mathbb{R}^n$, while $C(A)$ lives in the output home $\\mathbb{R}^m$.
> - **Dimension of Null Space (Nullity):**
>   $$\\dim N(A) = \\text{nullity}(A) = n - r = \\text{number of free variables}$$
> - **The Complete Solution Theorem:**
>   $$\\mathbf{x} = \\mathbf{x}_p + \\mathbf{x}_n = \\mathbf{x}_p + c_1 \\mathbf{s}_1 + \\dots + c_{n-r} \\mathbf{s}_{n-r}$$
>   - $\\mathbf{x}_p$ is any **particular solution** to $A \\mathbf{x}_p = \\mathbf{b}$ (obtained by setting all free variables to $0$).
>   - $\\mathbf{x}_n \\in N(A)$ is the general solution to the homogeneous system $A \\mathbf{x} = \\mathbf{0}$.
> - **The Three Subspace Requirements:** A subset $S \\subseteq \\mathbb{R}^n$ is a subspace iff:
>   1. Contains the zero vector: $\\mathbf{0} \\in S$.
>   2. Closed under vector addition: $\\mathbf{u}, \\mathbf{v} \\in S \\implies \\mathbf{u} + \\mathbf{v} \\in S$.
>   3. Closed under scalar multiplication: $\\mathbf{u} \\in S, c \\in \\mathbb{R} \\implies c\\mathbf{u} \\in S$.
"""
    cells.append(nbf.v4.new_markdown_cell(sec7_md))

    c7_1_md = """### 7.2 Concept 1: The Machine Metaphor (Input Home vs. Output Home)

A matrix $A_{m \\times n}$ is a machine that processes inputs from $\\mathbb{R}^n$ and outputs results into $\\mathbb{R}^m$:
- **Output side (Column Space $C(A) \\subseteq \\mathbb{R}^m$):** Answers *"What can the machine make?"*
- **Input side (Null Space $N(A) \\subseteq \\mathbb{R}^n$):** Answers *"What can the machine NOT see?"*
If $N(A)$ contains nonzero vectors, the machine has "blind spots": adding any null vector $\\mathbf{x}_n$ to your input dial leaves the output completely unchanged:
$$A(\\mathbf{x}_p + \\mathbf{x}_n) = A\\mathbf{x}_p + A\\mathbf{x}_n = \\mathbf{b} + \\mathbf{0} = \\mathbf{b}$$
"""
    cells.append(nbf.v4.new_markdown_cell(c7_1_md))

    # Diagram 9: Complete Solution Geometry (Affine vs. Null Line)
    c7_2_code = """# Diagram 9: Complete Solution Geometry — Affine Solution Line vs. Null Space Line
# System: 2x + 6y = 10 -> x_p = (5, 0), null direction s = (-3, 1)
# x(t) = (5, 0) + t*(-3, 1) = (5 - 3t, t)
t_vals = np.linspace(-2, 3, 100)

null_x = -3 * t_vals
null_y = 1 * t_vals

sol_x = 5 - 3 * t_vals
sol_y = 1 * t_vals

plt.figure(figsize=(9, 6))
# Null space line (passes through origin)
plt.plot(null_x, null_y, color='#ff7f0e', linewidth=2.5, linestyle='--', label='Null Space N(A): 2x + 6y = 0 (Line through Origin)')
# Complete solution line (shifted by x_p)
plt.plot(sol_x, sol_y, color='#1f77b4', linewidth=3, label='Complete Solution: x = xp + t·xn (Affine Line 2x + 6y = 10)')

# Points
plt.scatter([0], [0], color='#ff7f0e', s=100, zorder=5, label='Origin (0, 0)')
plt.scatter([5], [0], color='black', s=120, zorder=5, label='Particular Solution xp = (5, 0)')

# Shift vector xp
plt.quiver(0, 0, 5, 0, angles='xy', scale_units='xy', scale=1, color='black', width=0.012, label='Shift Vector xp')

plt.xlim(-8, 8)
plt.ylim(-3, 4)
plt.axhline(0, color='gray', linestyle=':', alpha=0.5)
plt.axvline(0, color='gray', linestyle=':', alpha=0.5)
plt.xlabel('x₁')
plt.ylabel('x₂')
plt.title('Diagram 9: Affine Solution Line Parallel to Null Space Line Shifted by xp', fontsize=12, fontweight='bold')
plt.legend()
plt.tight_layout()
plt.show()
"""
    cells.append(nbf.v4.new_code_cell(c7_2_code))

    # Diagram 10: Six-Beam Laser Challenge
    c7_3_code = """# Diagram 10: Six-Beam Laser Challenge — Quiver & Null-Space Balancing Vectors (Lab 7 Q.16)
# Directions: u1=(1,0), u2=(s2,-s2), u3=(-s2,-s2), u4=(-1,0), u5=(-s2,s2), u6=(s2,s2)
s2 = np.sqrt(2)/2
dirs = [
    (1, 0, '1: (1, 0)'),
    (s2, -s2, '2: (√2/2, -√2/2)'),
    (-s2, -s2, '3: (-√2/2, -√2/2)'),
    (-1, 0, '4: (-1, 0)'),
    (-s2, s2, '5: (-√2/2, √2/2)'),
    (s2, s2, '6: (√2/2, √2/2)')
]

plt.figure(figsize=(8, 8))
# Molecule at center
plt.scatter([0], [0], color='gold', s=400, edgecolors='black', linewidth=2, zorder=5, label='Molecule (Target b)')

for u, v, lbl in dirs:
    # Quivers pointing toward center from outside
    plt.quiver(-u*2, -v*2, u*1.8, v*1.8, angles='xy', scale_units='xy', scale=1, 
               color='#d62728', width=0.015, headwidth=4)
    plt.text(-u*2.2, -v*2.2, lbl, fontsize=11, fontweight='bold', ha='center', va='center')

plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.axhline(0, color='gray', linestyle=':', alpha=0.5)
plt.axvline(0, color='gray', linestyle=':', alpha=0.5)
plt.title('Diagram 10: Six-Beam Laser Setup Aimed at Molecule (Lab 7 Q.16)', fontsize=13, fontweight='bold')
plt.legend()
plt.tight_layout()
plt.show()
"""
    cells.append(nbf.v4.new_code_cell(c7_3_code))

    # Diagram 14: Subspace Test Gallery
    c7_4_code = """# Diagram 14: Subspace-Test Gallery — Failing Sets with Specific Counterexamples (Lab 7 Q.10 & Q.11)
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Region (a): First Quadrant x >= 0, y >= 0 (Fails negative scalars)
ax = axes[0, 0]
ax.fill_between([0, 4], 0, 4, color='lightblue', alpha=0.5, label='Set H: Q1 (x≥0, y≥0)')
ax.scatter([2], [2], color='green', s=80, label='u = (2, 2) ∈ H')
ax.scatter([-2], [-2], color='red', s=80, label='(-1)·u = (-2, -2) ∉ H')
ax.quiver(0, 0, 2, 2, angles='xy', scale_units='xy', scale=1, color='green', width=0.015)
ax.quiver(0, 0, -2, -2, angles='xy', scale_units='xy', scale=1, color='red', width=0.015)
ax.set_title('(a) First Quadrant: Fails Negative Scalars', fontweight='bold')
ax.set_xlim(-3, 4); ax.set_ylim(-3, 4); ax.legend(); ax.grid(True, alpha=0.3)

# Region (b): Q1 U Q3: xy >= 0 (Fails Vector Addition)
ax = axes[0, 1]
ax.fill_between([0, 4], 0, 4, color='lightblue', alpha=0.5)
ax.fill_between([-4, 0], -4, 0, color='lightblue', alpha=0.5, label='Set H: xy ≥ 0')
ax.scatter([1, -3], [3, -1], color='green', s=80, label='u=(1,3), v=(-3,-1) ∈ H')
ax.scatter([-2], [2], color='red', s=100, label='u + v = (-2, 2) ∉ H (xy = -4 < 0)')
ax.set_title('(b) Q1 ∪ Q3 (xy ≥ 0): Fails Addition', fontweight='bold')
ax.set_xlim(-4, 4); ax.set_ylim(-4, 4); ax.legend(); ax.grid(True, alpha=0.3)

# Region (c): Strip |y - x| <= 1 (Fails Scalar Multiplication)
ax = axes[1, 0]
x_s = np.linspace(-4, 4, 100)
ax.fill_between(x_s, x_s - 1.5, x_s + 1.5, color='lightblue', alpha=0.5, label='Set H: Strip |y - x| ≤ 1.5')
ax.scatter([1], [1], color='green', s=80, label='u = (1, 1) ∈ H')
ax.scatter([0], [1], color='green', s=80, label='v = (0, 1) ∈ H')
ax.scatter([0], [3], color='red', s=100, label='3·v = (0, 3) ∉ H (Exits Strip!)')
ax.set_title('(c) Diagonal Strip: Fails Scaling', fontweight='bold')
ax.set_xlim(-4, 4); ax.set_ylim(-4, 4); ax.legend(); ax.grid(True, alpha=0.3)

# Region (d): Non-linear Curve / Cone xy = 0 (Axes union)
ax = axes[1, 1]
ax.axhline(0, color='blue', linewidth=4, label='Set H: x-axis ∪ y-axis (xy = 0)')
ax.axvline(0, color='blue', linewidth=4)
ax.scatter([2, 0], [0, 3], color='green', s=80, label='u=(2,0), v=(0,3) ∈ H')
ax.scatter([2], [3], color='red', s=100, label='u + v = (2, 3) ∉ H (xy = 6 ≠ 0)')
ax.set_title('(d) Axes Union xy = 0: Fails Addition', fontweight='bold')
ax.set_xlim(-4, 4); ax.set_ylim(-4, 4); ax.legend(); ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
"""
    cells.append(nbf.v4.new_code_cell(c7_4_code))

    lec7_selftest_md = """### 7.10 Lecture 7 Self-Test Block

1. **Question 1:** Why is the set $S = \\{x \\in \\mathbb{R}^3 : x_1 + x_2 + x_3 = 1\\}$ NOT a subspace of $\\mathbb{R}^3$?
   <details><summary><b>View Answer</b></summary>
   It does not contain the zero vector $\\mathbf{0} = (0, 0, 0)^T$ because $0 + 0 + 0 = 0 \\ne 1$. (It is an affine plane, not a linear subspace).
   </details>

2. **Question 2:** Can a $3 \\times 3$ matrix have its null space equal to its column space?
   <details><summary><b>View Answer</b></summary>
   <b>No.</b> By Rank-Nullity, $\\dim C(A) + \\dim N(A) = 3$. If they were equal, say $\\dim = k$, then $2k = 3 \\implies k = 1.5$, which is impossible since dimension must be an integer. (For $2 \\times 2$, $\\begin{bmatrix} 0 & 1 \\\\ 0 & 0 \\end{bmatrix}$ has $C(A) = N(A) = \\text{Span}(\\mathbf{e}_1)$).
   </details>
"""
    cells.append(nbf.v4.new_markdown_cell(lec7_selftest_md))
    
    return cells

def get_lecture8_cells():
    cells = []
    
    sec8_md = """# Section 8: Lecture 8 — The Four Fundamental Subspaces and Network Duality (FOUR SPACES, ONE MATRIX)

---

### 8.1 Summary Box & Key Formulas
> **The Big Picture: Dimensions, Bases & Orthogonality:**
> - For any $m \\times n$ matrix $A$ of rank $r$:
>   | Subspace | Notation | Ambient Space | Dimension | Basis Construction |
>   | :--- | :---: | :---: | :---: | :--- |
>   | **Column Space** | $C(A)$ | $\\mathbb{R}^m$ | $r$ | Pivot columns of original matrix $A$ |
>   | **Row Space** | $C(A^T)$ | $\\mathbb{R}^n$ | $r$ | Nonzero rows of REF $U$ (or $R$) |
>   | **Null Space** | $N(A)$ | $\\mathbb{R}^n$ | $n - r$ | Special solutions to $Ax = 0$ |
>   | **Left Null Space** | $N(A^T)$ | $\\mathbb{R}^m$ | $m - r$ | Special solutions to $A^T y = 0$ (rows of $E$ eliminating to zero) |
> - **Orthogonality of Fundamental Subspaces:**
>   $$C(A^T) \\perp N(A) \\quad \\text{in } \\mathbb{R}^n \\qquad \\text{and} \\qquad C(A) \\perp N(A^T) \\quad \\text{in } \\mathbb{R}^m$$
> - **The Fredholm Alternative (Solvability Condition):**
>   $$A \\mathbf{x} = \\mathbf{b} \\text{ is solvable } \\iff \\mathbf{b} \\in C(A) \\iff \\mathbf{y}^T \\mathbf{b} = 0 \\quad \\forall \\mathbf{y} \\in N(A^T)$$
> - **Network Graph Incidence Matrix $A$ (Signed: Rows = Edges, Cols = Nodes):**
>   - $N(A) = \\text{Span}(\\mathbf{1})$ (Constant node potentials, dim 1 for connected graph).
>   - $N(A^T)$ = Loop currents / Kirchhoff's Current Law (dim $m - n + 1$).
>   - $C(A) \\perp N(A^T) \\iff$ Kirchhoff's Voltage Law (KVL around any closed loop $\\sum_{\\text{loop}} \\Delta V_i = 0$).
"""
    cells.append(nbf.v4.new_markdown_cell(sec8_md))

    # Diagram 8: The Two-Panel Four-Subspace Big Picture
    c8_1_code = """# Diagram 8: The Big Picture — Two-Panel Fundamental Subspaces Diagram with Right Angles Marked
fig, (ax_in, ax_out) = plt.subplots(1, 2, figsize=(14, 6))

# Left Panel: Input Home R^n
ax_in.plot([-3, 3], [0, 0], color='#9467bd', linewidth=4, label='Row Space C(Aᵀ) (dim r)')
ax_in.plot([0, 0], [-3, 3], color='#ff7f0e', linewidth=4, label='Null Space N(A) (dim n - r)')
# Right angle mark
ax_in.plot([0, 0.4, 0.4, 0], [0.4, 0.4, 0, 0], color='black', linewidth=1.5)
ax_in.scatter([0], [0], color='black', s=100, zorder=5)
ax_in.text(0.1, 0.1, '90° (⊥)', fontsize=12, fontweight='bold')
ax_in.set_title('Input Home ℝⁿ: Row Space ⊥ Null Space\\ndim C(Aᵀ) + dim N(A) = n', fontsize=12, fontweight='bold')
ax_in.set_xlim(-4, 4); ax_in.set_ylim(-4, 4); ax_in.legend(loc='upper right'); ax_in.axis('off')

# Right Panel: Output Home R^m
ax_out.plot([-3, 3], [0, 0], color='#17becf', linewidth=4, label='Column Space C(A) (dim r)')
ax_out.plot([0, 0], [-3, 3], color='#d62728', linewidth=4, label='Left Null Space N(Aᵀ) (dim m - r)')
# Right angle mark
ax_out.plot([0, 0.4, 0.4, 0], [0.4, 0.4, 0, 0], color='black', linewidth=1.5)
ax_out.scatter([0], [0], color='black', s=100, zorder=5)
ax_out.text(0.1, 0.1, '90° (⊥)', fontsize=12, fontweight='bold')
ax_out.set_title('Output Home ℝᵐ: Column Space ⊥ Left Null Space\\ndim C(A) + dim N(Aᵀ) = m', fontsize=12, fontweight='bold')
ax_out.set_xlim(-4, 4); ax_out.set_ylim(-4, 4); ax_out.legend(loc='upper right'); ax_out.axis('off')

plt.suptitle('Diagram 8: The Fundamental Theorem of Linear Algebra — Geometric Orthogonality', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
"""
    cells.append(nbf.v4.new_code_cell(c8_1_code))

    # Diagram 11c: Water Grid Network
    c8_2_code = """# Diagram 11c: Water Grid Network Graph with Spanning Tree & Loop Flows (Lab 8 Q.18)
# Junctions: v1..v5, Pipes: e1..e6
G_water = nx.DiGraph()
G_water.add_nodes_from(['v1', 'v2', 'v3', 'v4', 'v5'])
water_edges = [
    ('v1', 'v2', 'e1'),
    ('v2', 'v3', 'e2'),
    ('v3', 'v1', 'e3'),
    ('v3', 'v4', 'e4'),
    ('v4', 'v5', 'e5'),
    ('v5', 'v3', 'e6')
]
for u, v, l in water_edges:
    G_water.add_edge(u, v, label=l)

pos_water = {
    'v1': (-2, 0),
    'v2': (-1, 1),
    'v3': (0, 0),
    'v4': (1, 1),
    'v5': (2, 0)
}

plt.figure(figsize=(10, 5))
# Draw nodes
nx.draw_networkx_nodes(G_water, pos_water, node_color='#17becf', node_size=1200)
nx.draw_networkx_labels(G_water, pos_water, font_size=13, font_weight='bold')

# Spanning tree edges (e1, e2, e4, e5) in blue
tree_edges = [('v1', 'v2'), ('v2', 'v3'), ('v3', 'v4'), ('v4', 'v5')]
nx.draw_networkx_edges(G_water, pos_water, edgelist=tree_edges, edge_color='#1f77b4', width=3, arrows=True, arrowsize=20)

# Loop-closing edges (e3, e6) in orange dashed
loop_edges = [('v3', 'v1'), ('v5', 'v3')]
nx.draw_networkx_edges(G_water, pos_water, edgelist=loop_edges, edge_color='#ff7f0e', width=3, style='dashed', arrows=True, arrowsize=20)

# Edge labels
edge_labels = {(u, v): d['label'] for u, v, d in G_water.edges(data=True)}
nx.draw_networkx_edge_labels(G_water, pos_water, edge_labels=edge_labels, font_size=12, font_weight='bold')

plt.title('Diagram 11c: Six Pipes Water Grid — Spanning Tree (Solid Blue) and Independent Loops (Dashed Orange)', fontweight='bold')
plt.axis('off')
plt.tight_layout()
plt.show()
"""
    cells.append(nbf.v4.new_code_cell(c8_2_code))

    lec8_worked_md = """### 8.7 Lecture 8 Preserved Worked Examples

#### Example 1: Solvability Condition via Left Null Space (Lab 8 Q.9)
$$A = \\begin{bmatrix} 1 & 2 & -2 \\\\ 2 & 5 & -4 \\\\ 4 & 9 & -8 \\end{bmatrix}$$
Elimination on $[A \\mid I]$:
- $R_2 \\to R_2 - 2R_1 \\implies [0, 1, 0 \\mid -2, 1, 0]$
- $R_3 \\to R_3 - 4R_1 \\implies [0, 1, 0 \\mid -4, 0, 1]$
- $R_3 \\to R_3 - R_2 \\implies [0, 0, 0 \\mid -2, -1, 1]$
Left null vector is $\\mathbf{y} = (-2, -1, 1)^T$.
By the Fredholm Alternative, $Ax = b$ is solvable iff:
$$\\mathbf{y}^T \\mathbf{b} = 0 \\iff -2b_1 - b_2 + b_3 = 0 \\iff b_3 = 2b_1 + b_2$$

#### Example 2: Parametric Rank Analysis (Lab 8 Q.12)
$$M = \\begin{bmatrix} 1 & 0 & 0 \\\\ 0 & r - 2 & 2 \\\\ 0 & s - 1 & r + 2 \\\\ 0 & 0 & 3 \\end{bmatrix}$$
- Row 1 has a pivot in col 1; Row 4 has a pivot in col 3 ($3 \\ne 0$). These two rows are independent for **all** $r, s$.
- Thus $\\text{rank}(M) \\ge 2$ always. **Rank 1 is IMPOSSIBLE.**
- For rank 2: column 2 must contain zero pivots, requiring $r - 2 = 0 \\implies r = 2$ and $s - 1 = 0 \\implies s = 1$.
  When $r = 2, s = 1$, row 2 is $[0, 0, 2]$ and row 3 is $[0, 0, 4]$, both parallel to row 4 $[0, 0, 3]$. Rank is exactly 2.
"""
    cells.append(nbf.v4.new_markdown_cell(lec8_worked_md))

    lec8_worked_code = """# SymPy Verification of Lab 8 Worked Examples
A_solv = Matrix([[1, 2, -2], [2, 5, -4], [4, 9, -8]])
y_left = A_solv.T.nullspace()[0]
print("Left null vector y spanning N(A^T):")
display(y_left)

b1, b2, b3 = symbols('b1 b2 b3')
cond_solv = y_left.dot(Matrix([b1, b2, b3]))
print("Solvability condition:", cond_solv, "= 0")
assert solve(cond_solv, b3)[0] == 2*b1 + b2, "Condition derivation failed!"
print("Fredholm solvability verified exactly!")
"""
    cells.append(nbf.v4.new_code_cell(lec8_worked_code))

    lec8_selftest_md = """### 8.9 Lecture 8 Self-Test Block

1. **Question 1:** If $A$ is $5 \\times 7$ with rank 4, what are the dimensions of all four fundamental subspaces?
   <details><summary><b>View Answer</b></summary>
   - $\\dim C(A) = r = 4$
   - $\\dim C(A^T) = r = 4$
   - $\\dim N(A) = n - r = 7 - 4 = 3$
   - $\\dim N(A^T) = m - r = 5 - 4 = 1$
   </details>

2. **Question 2:** If $AB = 0$, prove that the column space of $B$ is contained in the null space of $A$.
   <details><summary><b>View Answer</b></summary>
   Let $\\mathbf{y} \\in C(B)$. Then $\\mathbf{y} = B \\mathbf{x}$ for some $\\mathbf{x}$. Multiplying by $A$:
   $A \\mathbf{y} = A(B\\mathbf{x}) = (AB)\\mathbf{x} = 0\\mathbf{x} = \\mathbf{0}$.
   Therefore, $\\mathbf{y} \\in N(A)$. Hence, $C(B) \\subseteq N(A)$.
   </details>

3. **Question 3:** Can two $3 \\times 3$ matrices of rank 2 multiply to give the zero matrix ($AB = 0$)?
   <details><summary><b>View Answer</b></summary>
   <b>No.</b> If $AB = 0$, then $C(B) \\subseteq N(A)$, which implies $\\dim C(B) \\le \\dim N(A)$. Here $\\dim C(B) = 2$, but $\\dim N(A) = 3 - \\text{rank}(A) = 3 - 2 = 1$. Since $2 \\not\\le 1$, this is impossible.
   </details>
"""
    cells.append(nbf.v4.new_markdown_cell(lec8_selftest_md))
    
    return cells

print("master_sections_5_8.py initialized successfully.")
