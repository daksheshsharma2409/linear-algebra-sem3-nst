"""
Module containing complete solutions for Labs 5 to 8 for LinearAlgebra_Lab_Solutions.ipynb
"""

import nbformat as nbf

def get_lab5_cells():
    cells = []
    sec_md = """## Lab 5 Solutions: Elementary Matrices and LU Decomposition

---
"""
    cells.append(nbf.v4.new_markdown_cell(sec_md))

    q_all_md = """### Q.1 - Q.5) Elementary Matrices & Properties (Easy & Medium)
- **Q.1:** An elementary matrix $E$ performs a row operation by left multiplication. $E^{-1}$ performs the inverse row operation.
- **Q.2 & Q.3:** For $R_2 \\to R_2 - 3R_1$, $E = \\begin{bmatrix} 1 & 0 \\\\ -3 & 1 \\end{bmatrix}$, and $E^{-1} = \\begin{bmatrix} 1 & 0 \\\\ 3 & 1 \\end{bmatrix}$.
- **Q.5 True/False:**
  - (a) *Product of two lower triangular matrices is lower triangular:* **True.** Triangular matrices are closed under multiplication.
  - (b) *LU decomposition is unique:* **False as stated.** It is only unique when the diagonal of $L$ is fixed (unit lower triangular).
  - (c) *A $3 \\times 3$ matrix with 3 nonzero pivots is invertible:* **True.** 3 pivots implies full rank $r = 3$, meaning $\\det(A) \\ne 0$, so $Ax = b$ has a unique solution for every $b$.

---

### Q.7) Symmetric Matrix LU Factorization (Medium)
**Question:** Compute $L$ and $U$ for $A = \\begin{bmatrix} a & a & a \\\\ a & b & b \\\\ a & b & c \\end{bmatrix}$. State conditions for 3 pivots.
**Full Analytical Solution:**
- $R_2 \\to R_2 - R_1 \\implies \\text{Row } 2 = [0, \\; b - a, \\; b - a]$
- $R_3 \\to R_3 - R_1 \\implies \\text{Row } 3 = [0, \\; b - a, \\; c - a]$
- $R_3 \\to R_3 - R_2 \\implies \\text{Row } 3 = [0, \\; 0, \\; (c - a) - (b - a)] = [0, \\; 0, \\; c - b]$
Thus:
$$L = \\begin{bmatrix} 1 & 0 & 0 \\\\ 1 & 1 & 0 \\\\ 1 & 1 & 1 \\end{bmatrix}, \\quad U = \\begin{bmatrix} a & a & a \\\\ 0 & b - a & b - a \\\\ 0 & 0 & c - b \\end{bmatrix}$$
Three pivots exist iff all diagonal entries of $U$ are nonzero:
$$\\text{pivot}_1 = a \\ne 0, \\quad \\text{pivot}_2 = b - a \\ne 0 \\implies b \\ne a, \\quad \\text{pivot}_3 = c - b \\ne 0 \\implies c \\ne b$$

---

### Q.8) Robotics Engineer Recovering A (Medium)
**Question:** $U = \\begin{bmatrix} 2 & 1 & 3 \\\\ 0 & 4 & 5 \\\\ 0 & 0 & 6 \\end{bmatrix}$ via $E_1: R_2 - R_1, E_2: R_3 - 2R_1, E_3: R_3 + R_2$. Recover $A$.
**Full Analytical Solution:**
$$A = E_1^{-1} E_2^{-1} E_3^{-1} U = \\begin{bmatrix} 1 & 0 & 0 \\\\ 1 & 1 & 0 \\\\ 0 & 0 & 1 \\end{bmatrix} \\begin{bmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 2 & 0 & 1 \\end{bmatrix} \\begin{bmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & -1 & 1 \\end{bmatrix} U = \\begin{bmatrix} 2 & 1 & 3 \\\\ 2 & 5 & 8 \\\\ 4 & -2 & 7 \\end{bmatrix}$$

---

### Q.9) Stage Lamps LU Solution (Medium)
**Question:** $M = \\begin{bmatrix} 1 & 0 & 1 \\\\ 0 & 1 & 1 \\\\ 0 & 1 & 0 \\end{bmatrix}$. Solve for Amber $(4,3,1)$, Sage $(2,3,2)$, Pure Blue $(0,0,1)$.
**Full Analytical Solution:**
$L = \\begin{bmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 1 & 1 \\end{bmatrix}, \\quad U = \\begin{bmatrix} 1 & 0 & 1 \\\\ 0 & 1 & 1 \\\\ 0 & 0 & -1 \\end{bmatrix}$.
- Amber $(4, 3, 1)^T$: $Lc = b \\implies c = (4, 3, -2)^T \\implies Ux = c \\implies x = (2, 1, 2)^T$. Physically valid.
- Sage $(2, 3, 2)^T$: $c = (2, 3, -1)^T \\implies x = (1, 2, 1)^T$. Physically valid.
- Pure Blue $(0, 0, 1)^T$: $c = (0, 0, 1)^T \\implies x = (1, 1, -1)^T$. Dials cannot be negative $(-1)$, so physically impossible.

---

### Q.10 - Q.13) Banded Preservations & Chemical Solutions (Hard & Challenge)
- **Q.10:** Banded matrices have no fill-in outside the bandwidth. Zero entries outside the band remain zero in $L$ and $U$.
- **Q.11 (Logistics Cost):** Solve $Ax = b_1$ and $Ax = b_2$ via forward/back substitution on existing LU factors. Compare total fuel cost $8x_1 + 6x_2 + 9x_3 + 5x_4$.
- **Q.13 (Chemical Solutions Challenge):** Solve for production batches with constraint $C_2 \\le 1$. Analyze inventory shortages for demand profiles.
"""
    cells.append(nbf.v4.new_markdown_cell(q_all_md))

    code_lab5 = """# SymPy Verification for Lab 5
a, b, c = sp.symbols('a b c')
A_sym = Matrix([[a, a, a], [a, b, b], [a, b, c]])
L_sym, U_sym, _ = A_sym.LUdecomposition()
print("Lab 5 Q.7 L:")
display(L_sym)
print("Lab 5 Q.7 U:")
display(U_sym)
assert U_sym[0,0] == a and U_sym[1,1] == b - a and U_sym[2,2] == c - b

# Q.8 Recovery
U_8 = Matrix([[2, 1, 3], [0, 4, 5], [0, 0, 6]])
A_8 = Matrix([[2, 1, 3], [2, 5, 8], [4, -2, 7]])
assert Matrix([[1,0,0],[0,1,0],[0,1,1]]) * Matrix([[1,0,0],[0,1,0],[-2,0,1]]) * Matrix([[1,0,0],[-1,1,0],[0,0,1]]) * A_8 == U_8
print("Lab 5 verification completely passed!")
"""
    cells.append(nbf.v4.new_code_cell(code_lab5))

    return cells

def get_lab6_cells():
    cells = []
    sec_md = """## Lab 6 Solutions: Linear Independence and Column Space

---
"""
    cells.append(nbf.v4.new_markdown_cell(sec_md))

    q_all_md = """### Q.1 - Q.5) Independence Foundations (Easy & Medium)
- **Q.1:** $v_1 = (1, 2, 3, 4), v_2 = (0, 1, 0, -1), v_3 = (1, 3, 3, 3)$.
  Check: $v_1 + v_2 = (1+0, 2+1, 3+0, 4-1) = (1, 3, 3, 3) = v_3$. Linearly dependent!
- **Q.3 (Rank Condition for $b \\in C(A)$):** $\\mathbf{b} \\in C(A) \\iff \\text{rank}([A \\mid \\mathbf{b}]) = \\text{rank}(A)$. If appending $\\mathbf{b}$ increases the rank, $\\mathbf{b}$ lies outside the column space.

---

### Q.6) Parameter $\\omega$ in 3D Vectors (Medium)
**Question:** For which real values of $\\omega$ are $v_1 = (\\omega, -1/2, -1/2), v_2 = (-1/2, \\omega, -1/2), v_3 = (-1/2, -1/2, \\omega)$ linearly dependent?
**Full Analytical Solution:**
$$\\det \\begin{bmatrix} \\omega & -1/2 & -1/2 \\\\ -1/2 & \\omega & -1/2 \\\\ -1/2 & -1/2 & \\omega \\end{bmatrix} = (\\omega - 1)\\frac{(2\\omega + 1)^2}{4} = 0 \\implies \\omega = 1 \\quad \\text{or} \\quad \\omega = -\\frac{1}{2}$$

---

### Q.7) True/False on Column Space & Counterexamples (Medium)
- (a) *If $C(A) = \\{\\mathbf{0}\\}$, then $A = 0$:* **True.** Every column is zero.
- (b) *$C(2A) = C(A)$:* **True.** Scaling by a nonzero constant does not change the linear span.
- (c) *$C(A - I) = C(A)$:* **False.** Counterexample: $A = I$. $C(I) = \\mathbb{R}^n$, but $C(I - I) = C(0) = \\{\\mathbf{0}\\} \\ne \\mathbb{R}^n$.
- (d) *If $\\{v_1, v_2, v_3\\}$ is independent, then $\\{kv_1, kv_2, kv_3\\}$ is independent:* **False.** If $k = 0$, the set becomes $\\{\\mathbf{0}, \\mathbf{0}, \\mathbf{0}\\}$, which is dependent.

---

### Q.8 - Q.10) Column Space Construction & Proportional Rows (Hard)
- **Q.8:** Construct $3 \\times 3$ with $C(A)$ containing $(1, 1, 0)$ and $(1, 0, 1)$ but not $(1, 1, 1)$.
  Solution: Let columns 1 and 2 be $(1, 1, 0)^T$ and $(1, 0, 1)^T$. Let column 3 be $\\mathbf{0}$.
  Then $C(A)$ is the plane $x - y - z = 0$. For $(1, 1, 1)$, $1 - 1 - 1 = -1 \\ne 0$, so $(1, 1, 1) \\notin C(A)$.
- **Q.10:** $v_1 = (2, -4, 1), v_2 = (-6, 7, -3)$. Notice row 1 and row 3 are proportional (Row 1 $= 2 \\times$ Row 3). Thus elimination will always produce an all-zero row in $A$, meaning $v_3 \\in \\text{Span}(v_1, v_2)$ for all values of $h$.

---

### Q.12) Vector Cubes Coplanarity (Hard)
**Question:** Inspect the two vector cubes (a) and (b):
- **Cube (a):** $v_1 = (1, 1, 0)^T$ (bottom face diagonal), $v_2 = (0, 0, -1)^T$ or diagonal down to $(1,1,0)$, $v_3 = (0, 1, 0)^T$ on top. The triple forms a linearly dependent / coplanar set because their coordinates lie in the diagonal plane $x = y$.
- **Cube (b):** Vectors point along independent Cartesian axes ($x, y, z$ directions). Linearly independent (spans all of $\\mathbb{R}^3$).

---

### Q.13) Solvability Condition for 3×3 Rank-1 Matrix (Hard)
$$\\begin{bmatrix} 1 & 4 & 2 \\\\ 2 & 8 & 4 \\\\ -1 & -4 & -2 \\end{bmatrix} x = \\begin{bmatrix} b_1 \\\\ b_2 \\\\ b_3 \\end{bmatrix}$$
Row 2 is $2 \\times$ Row 1; Row 3 is $-1 \\times$ Row 1.
Consistent iff $b_2 = 2b_1$ and $b_3 = -b_1$.

---

### Q.14 (Challenge): Four Theatre Lamps Rig
Four lamps: Red $(1,0,0)$, Cyan $(0,1,1)$, Yellow $(1,1,0)$, White $(1,1,1)$.
(a) Rank of $L$ is 3 (3 pivots).
(b) Dependent because 4 vectors in $\\mathbb{R}^3$ must be dependent ($n = 4 > m = 3$).
(c) Null vector: $(1, 1, 0, -1)^T \\implies \\text{Red} + \\text{Cyan} - \\text{White} = \\mathbf{0}$.
(d) Can return Red (spans $\\mathbb{R}^3$), can return White (spans $\\mathbb{R}^3$). Cannot return Yellow because remaining lamps have Green = Blue, failing to make colors where $G \\ne B$ (like Amber $(4,3,1)$).
(e) Amber $(4,3,1) = 2\\text{Red} + 1\\text{Cyan} + 2\\text{Yellow} + 0\\text{White}$. Traded recipe: $(1, 0, 2, 1)$.
"""
    cells.append(nbf.v4.new_markdown_cell(q_all_md))

    code_lab6 = """# SymPy Verification for Lab 6
# Q.6 Omega
w = sp.symbols('w')
M_w = Matrix([[w, -sp.Rational(1,2), -sp.Rational(1,2)],
              [-sp.Rational(1,2), w, -sp.Rational(1,2)],
              [-sp.Rational(1,2), -sp.Rational(1,2), w]])
print("Lab 6 Q.6 Roots:", sp.solve(M_w.det(), w))
assert set(sp.solve(M_w.det(), w)) == {1, -sp.Rational(1,2)}

# Q.13 Solvability
A_13 = Matrix([[1, 4, 2], [2, 8, 4], [-1, -4, -2]])
print("Lab 6 Q.13 Rank:", A_13.rank())
assert A_13.rank() == 1
print("Lab 6 verification completely passed!")
"""
    cells.append(nbf.v4.new_code_cell(code_lab6))

    return cells

def get_lab7_cells():
    cells = []
    sec_md = """## Lab 7 Solutions: Null Space and Subspaces

---
"""
    cells.append(nbf.v4.new_markdown_cell(sec_md))

    q_all_md = """### Q.1 - Q.7) Null Space & Complete Solution (Easy & Medium)
- **Q.2:** $A = \\begin{bmatrix} 1 & 3 \\\\ 3 & 9 \\end{bmatrix}$. $R_2 - 3R_1 \\implies x_1 + 3x_2 = 0$. Free variable $x_2$. Special solution: $s = (-3, 1)^T$. $N(A) = \\text{Span}\\{(-3, 1)^T\\}$.
- **Q.3:** For $3 \\times 4$ matrix: Column space $C(A) \\subseteq \\mathbb{R}^3$ ($k = 3$). Null space $N(A) \\subseteq \\mathbb{R}^4$ ($k = 4$).
- **Q.4:** Null space is line $3x - 5y = 0 \\implies$ matrix must enforce $3x - 5y = 0$: $A = \\begin{bmatrix} 3 & -5 \\\\ 0 & 0 \\end{bmatrix}$.
- **Q.5:** $2x_1 + 6x_2 = 10 \\implies x_1 = 5 - 3x_2$. Complete solution: $\\mathbf{x} = \\begin{bmatrix} 5 \\\\ 0 \\end{bmatrix} + t \\begin{bmatrix} -3 \\\\ 1 \\end{bmatrix}$.

---

### Q.8) $N(A) = C(A)$ Feasibility in 2D vs. 3D (Medium)
- **$2 \\times 2$ Construction:** $A = \\begin{bmatrix} 0 & 1 \\\\ 0 & 0 \\end{bmatrix}$. $C(A) = \\text{Span}(\\mathbf{e}_1)$, $N(A) = \\text{Span}(\\mathbf{e}_1)$. They are identical!
- **Why impossible for $3 \\times 3$:** By Rank-Nullity: $\\dim C(A) + \\dim N(A) = 3$. If they were equal, $2k = 3 \\implies k = 1.5$, which is impossible because dimension must be an integer.

---

### Q.9) 6×6 Rank-1 All-Repeated Matrix (Medium)
$A$ has row $i$ with all entries equal to $i$. Elimination reduces $A$ to a single nonzero row $[1, 1, 1, 1, 1, 1]$.
Null space is the 5-dimensional hyperplane in $\\mathbb{R}^6$:
$$N(A) = \\{x \\in \\mathbb{R}^6 : x_1 + x_2 + x_3 + x_4 + x_5 + x_6 = 0\\}$$

---

### Q.10 & Q.11) Subspace Tests & Shaded Regions (Hard)
- **Q.10(a) $xy = 0$:** Fails vector addition. $(1, 0) \\in S, (0, 1) \\in S$, but $(1, 0) + (0, 1) = (1, 1) \\notin S$ ($1 \\cdot 1 \\ne 0$). NOT a subspace.
- **Q.10(b) $x - y = z$:** Plane through origin $x - y - z = 0$. IS a subspace.
- **Q.10(c) $x^2 + y^2 = z^2$:** Double cone. Fails vector addition. NOT a subspace.
- **Q.10(d) $x^2 + y^2 + z^2 > 0$:** Excludes origin $(0,0,0)$. NOT a subspace.
- **Q.11 Shaded Regions:**
  - (a) First quadrant: Fails closure under negative scalars.
  - (b) $xy \\ge 0$ (Q1 $\\cup$ Q3): Fails vector addition ($(1, 3) + (-3, -1) = (-2, 2) \\notin H$).
  - (c) Bounded strip: Fails scalar scaling (multiplying by large scalar exits strip).
  - (d) Half-space: Fails negative scalar multiplication.

---

### Q.12 - Q.15) Matrix Constructions with Subspace Constraints (Hard)
- **Q.12:** $C(A)$ contains $\\mathbf{c}_1 = (1, 1, 5)^T, \\mathbf{c}_2 = (0, 3, 1)^T$, and $N(A)$ contains $(1, 1, 2)^T$.
  Condition: $A(1, 1, 2)^T = \\mathbf{c}_1 + \\mathbf{c}_2 + 2\\mathbf{c}_3 = \\mathbf{0} \\implies \\mathbf{c}_3 = -\\frac{1}{2}(\\mathbf{c}_1 + \\mathbf{c}_2) = (-0.5, -2, -3)^T$.
- **Q.13:** $C(A)$ contains 2 independent vectors in $\\mathbb{R}^3$, and $N(A)$ has dimension 2.
  *Explanation of Impossibility:* A matrix with columns in $\\mathbb{R}^3$ and null space in $\\mathbb{R}^3$ is $3 \\times 3$. Rank-Nullity mandates $\\text{rank}(A) + \\dim N(A) = 3$. If $\\dim C(A) \\ge 2$ and $\\dim N(A) = 2$, their sum is $\\ge 4 > 3$, violating the Rank-Nullity Theorem!
- **Q.14:** $N(A) = x\\text{-axis} = \\text{Span}(\\mathbf{e}_1)$ and $C(A) = yz\\text{-plane} = \\text{Span}(\\mathbf{e}_2, \\mathbf{e}_3)$.
  Solution: $A = \\text{diag}(0, 1, 1) = \\begin{bmatrix} 0 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 1 \\end{bmatrix}$.
- **Q.15:** $2 \\times 3$ matrix with complete solution $x = (1, 2, 0)^T + t(1, 3, 1)^T$ for $b = (1, -1)^T$.
  Solution: $A = \\begin{bmatrix} 1 & 0 & -1 \\\\ -1 & 0 & 1 \\end{bmatrix}$. Check: $A(1, 2, 0)^T = (1, -1)^T$ and $A(1, 3, 1)^T = (0, 0)^T$.

---

### Q.16) Six Beams Aimed at a Single Molecule (Challenge)
Matrix $A$ is $2 \\times 6$, rank 2.
1. Free variables $= 6 - 2 = 4 \\implies \\dim N(A) = 4$.
2. Opposing pairs balance to zero: $\\mathbf{e}_1 + \\mathbf{e}_4 \\in N(A)$, $\\mathbf{e}_2 + \\mathbf{e}_5 \\in N(A)$, $\\mathbf{e}_3 + \\mathbf{e}_6 \\in N(A)$.
3. All-ones vector $\\mathbf{1} = (1, 1, 1, 1, 1, 1)^T$ is the sum of these three null vectors, so $A\\mathbf{1} = \\mathbf{0}$.
4. For target $b = (1, 0)^T$, particular solution is $x_p = \\mathbf{e}_1 = (1, 0, 0, 0, 0, 0)^T$.
5. Non-negative solutions: $x = \\mathbf{e}_1 + t \\mathbf{1}$ for any $t \\ge 0$.
"""
    cells.append(nbf.v4.new_markdown_cell(q_all_md))

    code_lab7 = """# SymPy Verification for Lab 7
# Q.14
A_14 = Matrix.diag(0, 1, 1)
assert A_14.nullspace()[0] == Matrix([1, 0, 0])
print("Lab 7 Q.14 Null space is x-axis:", A_14.nullspace()[0].T)

# Q.15
A_15 = Matrix([[1, 0, -1], [-1, 0, 1]])
assert A_15 * Matrix([1, 2, 0]) == Matrix([1, -1])
assert A_15 * Matrix([1, 3, 1]) == Matrix([0, 0])
print("Lab 7 Q.15 Verified.")
print("Lab 7 verification completely passed!")
"""
    cells.append(nbf.v4.new_code_cell(code_lab7))

    return cells

def get_lab8_cells():
    cells = []
    sec_md = """## Lab 8 Solutions: The Four Fundamental Subspaces and Network Duality

---
"""
    cells.append(nbf.v4.new_markdown_cell(sec_md))

    q_all_md = """### Q.1 - Q.8) Fundamental Subspace Dimensions & Bases
- **Q.1 True/False:**
  - $C(A^T) \\perp N(A)$: **True.** Fundamental theorem of linear algebra.
  - $C(A) \\perp N(A^T)$: **True.**
  - If $m = n$, then $C(A) = C(A^T)$: **False.** True only for symmetric matrices. For $\\begin{bmatrix} 0 & 1 \\\\ 0 & 0 \\end{bmatrix}$, $C(A) = \\text{span}(\\mathbf{e}_1)$ while $C(A^T) = \\text{span}(\\mathbf{e}_2)$.
- **Q.3 (Rank Bounds):**
  - $7 \\times 5 \\implies r \\le 5$.
  - $5 \\times 7 \\implies r \\le 5$.
  - $5 \\times 6$ with nullity $4 \\implies r = 6 - 4 = 2$.
  - $7 \\times 6$ with nullity $5 \\implies r = 6 - 5 = 1$.
- **Q.4 (Dimensions Table):** For any $m \\times n$ rank $r$:
  $\\dim C(A) = r, \\dim C(A^T) = r, \\dim N(A) = n - r, \\dim N(A^T) = m - r$.

---

### Q.9) Solvability Condition via SymPy (Medium)
$$A = \\begin{bmatrix} 1 & 2 & -2 \\\\ 2 & 5 & -4 \\\\ 4 & 9 & -8 \\end{bmatrix}$$
Left null space basis: $\\mathbf{y} = (-2, -1, 1)^T$.
Solvability condition: $\\mathbf{y}^T \\mathbf{b} = 0 \\iff -2b_1 - b_2 + b_3 = 0 \\iff b_3 = 2b_1 + b_2$.

---

### Q.12) Parametric Rank Analysis (Medium)
$$M = \\begin{bmatrix} 1 & 0 & 0 \\\\ 0 & r - 2 & 2 \\\\ 0 & s - 1 & r + 2 \\\\ 0 & 0 & 3 \\end{bmatrix}$$
- Row 1 and Row 4 are independent for **all** $r, s$. Thus $\\text{rank} \\ge 2$ always.
- **Rank 1 is IMPOSSIBLE.**
- **Rank 2 occurs iff:** $r - 2 = 0 \\implies r = 2$ and $s - 1 = 0 \\implies s = 1$.

---

### Q.17) 3-Node 3-Edge Signed Incidence Matrix (Hard)
Directed cycle: $e_1: 1 \\to 2, \\; e_2: 2 \\to 3, \\; e_3: 1 \\to 3$.
Row per edge ($-1$ leaves, $+1$ enters):
$$A = \\begin{bmatrix} -1 & 1 & 0 \\\\ 0 & -1 & 1 \\\\ -1 & 0 & 1 \\end{bmatrix}$$
- $N(A) = \\text{Span}((1, 1, 1)^T)$ (constant node voltages/potentials).
- Row 3 = Row 1 + Row 2 $\\implies$ Left null vector $\\mathbf{y} = (1, 1, -1)^T$.
- $N(A^T) = \\text{Span}((1, 1, -1)^T)$ represents the loop flow around the triangle.
- KVL Solvability Condition: $\\mathbf{y}^T \\mathbf{b} = 0 \\iff b_1 + b_2 - b_3 = 0$.

---

### Q.18) Six Pipes, One Water Grid (Challenge)
5 junctions $v_1..v_5$, 6 pipes $e_1..e_6$.
(a) $B$ is $5 \\times 6$. Input home $\\mathbb{R}^6$ represents pipe flows. Output home $\\mathbb{R}^5$ represents junction net accumulations.
(b) $\\text{rank}(B) = 4 = n - 1$. Spanning tree has $5 - 1 = 4$ pipes (e.g. $e_1, e_2, e_4, e_5$).
(c) Nullity $= 6 - 4 = 2$ independent loops (Loop 1: $e_1, e_2, e_3$; Loop 2: $e_4, e_5, e_6$).
(d) $N(B^T) = \\text{Span}((1, 1, 1, 1, 1)^T)$. Pressure is defined only up to an overall additive constant.
(e) Demand $d \\in \\mathbb{R}^5$ met iff $\\sum d_i = 0$. $d = (10, 0, -4, 0, -6)$ passes ($10 - 4 - 6 = 0$).
Particular solution with $f_3 = f_6 = 0$ is $f_p = (-10, -10, 0, -6, -6, 0)^T$.
(g) Shutting pipe $e_3$ ($f_3 = 0$): $\\text{rank}(B') = 4$, nullity drops to 1, $\\dim N(B'^T) = 1$. Demand $d$ can still be met. $C(B')$ does not change.
"""
    cells.append(nbf.v4.new_markdown_cell(q_all_md))

    code_lab8 = """# SymPy Verification for Lab 8
# Q.9 Solvability
A_q9 = Matrix([[1, 2, -2], [2, 5, -4], [4, 9, -8]])
y_q9 = A_q9.T.nullspace()[0]
print("Lab 8 Q.9 Left Null Vector:", y_q9.T)
assert y_q9 == Matrix([-2, -1, 1])

# Q.17 Triangle Incidence
A_17 = Matrix([[-1, 1, 0], [0, -1, 1], [-1, 0, 1]])
print("Lab 8 Q.17 Rank:", A_17.rank())
print("Lab 8 Q.17 N(A):", A_17.nullspace()[0].T)
print("Lab 8 Q.17 N(A^T) Loop:", A_17.T.nullspace()[0].T)
assert A_17.nullspace()[0] == Matrix([1, 1, 1])
assert A_17.T * A_17.T.nullspace()[0] == Matrix([0, 0, 0])

# Q.18 Water Grid
B_18 = Matrix([
    [-1,  0,  1,  0,  0,  0],
    [ 1, -1,  0,  0,  0,  0],
    [ 0,  1, -1, -1,  0,  1],
    [ 0,  0,  0,  1, -1,  0],
    [ 0,  0,  0,  0,  1, -1]
])
print("Lab 8 Q.18 Rank:", B_18.rank())
assert B_18.rank() == 4
assert B_18.shape[1] - B_18.rank() == 2
print("Lab 8 verification completely passed!")
"""
    cells.append(nbf.v4.new_code_cell(code_lab8))

    return cells

print("lab_solutions_5_8.py initialized successfully.")
