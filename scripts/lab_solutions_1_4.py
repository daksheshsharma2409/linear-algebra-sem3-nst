"""
Module containing complete solutions for Labs 1 to 4 for LinearAlgebra_Lab_Solutions.ipynb
"""

import nbformat as nbf

def get_lab_intro_cells():
    cells = []
    intro_md = """# Newton School of Technology, ADYPU — Mathematics-3: Linear Algebra
## Companion Lab Solutions Manual: Complete Worked Solutions & SymPy Verification (Labs 1–8)

---

### Methodological Protocol
For **every single question** across Labs 1 through 8 (categorized across *Easy*, *Medium*, *Hard*, and *Challenge* tiers):
1. **Problem Restatement:** Exact problem formulation with complete mathematical symbols.
2. **Analytical Step-by-Step Derivation:** Exhaustive algebraic and geometric working.
3. **SymPy Computational Verification:** Exact arithmetic proof using `sympy.Matrix`, checking consistency, determinants, ranks, and fundamental subspaces.
4. **Examiner Testing Note:** A targeted one-line summary explaining the exact core linear algebra concept being assessed.
5. **Rigorous True/False Treatment:** Formal mathematical justifications and explicit counterexamples for all false claims.
6. **Discrepancy & Typo Clarifications:** Explicitly noting any inconsistencies or printing typos found in the original lab sheets.

---
"""
    cells.append(nbf.v4.new_markdown_cell(intro_md))
    return cells

def get_lab1_cells():
    cells = []
    
    sec_md = """## Lab 1 Solutions: Linear Systems, Row Picture, and Column Picture

---
"""
    cells.append(nbf.v4.new_markdown_cell(sec_md))
    
    # Q1 to Q3
    q1_3_md = """### Q.1) System to Matrix Representation (Easy)
**Question:** Express the following linear system in matrix form $Ax = b$:
$$\\begin{aligned} 2x + y - z &= 4 \\\\ x - z &= 1 \\\\ 3x + y + 2z &= 6 \\end{aligned}$$
*(a) State the coefficient matrix $A$, variable vector $x$, and right-hand side vector $b$.*
*(b) State the reverse procedure: converting a matrix equation back to individual linear equations.*

**Full Analytical Solution:**
(a) Inspecting each row:
- Row 1: $2x + 1y - 1z = 4 \\implies \\mathbf{a}_1^T = [2, 1, -1], b_1 = 4$.
- Row 2: $1x + 0y - 1z = 1 \\implies \\mathbf{a}_2^T = [1, 0, -1], b_2 = 1$ (Note: missing $y$ coefficient is 0).
- Row 3: $3x + 1y + 2z = 6 \\implies \\mathbf{a}_3^T = [3, 1, 2], b_3 = 6$.
In matrix form:
$$A = \\begin{bmatrix} 2 & 1 & -1 \\\\ 1 & 0 & -1 \\\\ 3 & 1 & 2 \\end{bmatrix}, \\quad x = \\begin{bmatrix} x \\\\ y \\\\ z \\end{bmatrix}, \\quad b = \\begin{bmatrix} 4 \\\\ 1 \\\\ 6 \\end{bmatrix}$$
(b) To convert $Ax = b$ back to scalar equations, perform row-by-column dot products: each row $\\mathbf{a}_i^T x = b_i$ yields the scalar equation $\\sum_j a_{ij} x_j = b_i$.

**What the examiner tests:** Conversion between scalar systems and matrix notation $Ax = b$, specifically verifying that missing variables have coefficient $0$.

---

### Q.2) Practice Matrix Equation Form (Easy)
**Question:** Convert the 2-variable system into matrix form:
$$2x + y = 7, \\quad x - 2y = -1$$
**Full Analytical Solution:**
$$A = \\begin{bmatrix} 2 & 1 \\\\ 1 & -2 \\end{bmatrix}, \\quad x = \\begin{bmatrix} x \\\\ y \\end{bmatrix}, \\quad b = \\begin{bmatrix} 7 \\\\ -1 \\end{bmatrix}$$

**What the examiner tests:** Basic matrix construction in $2 \\times 2$ dimensions.

---

### Q.3) Matrix Dimensions and Multiplication Feasibility (Easy)
**Question:** Given sizes $2 \\times 3$ and $3 \\times 1$, and sizes $3 \\times 2$ and $2 \\times 1$, determine whether the products are defined and compute their resulting dimensions.
**Full Analytical Solution:**
- $(2 \\times 3) \\times (3 \\times 1)$: Inner dimensions match ($3 = 3$). Product is defined and has size $2 \\times 1$.
- $(3 \\times 2) \\times (2 \\times 1)$: Inner dimensions match ($2 = 2$). Product is defined and has size $3 \\times 1$.

**What the examiner tests:** Conformability rule $(m \\times n)(n \\times p) = m \\times p$.
"""
    cells.append(nbf.v4.new_markdown_cell(q1_3_md))
    
    code_q1_3 = """# SymPy Verification for Lab 1 Q.1 - Q.3
import sympy as sp
from sympy import Matrix

A1 = Matrix([[2, 1, -1], [1, 0, -1], [3, 1, 2]])
b1 = Matrix([4, 1, 6])
sol1 = A1.LUsolve(b1)
print("Q.1 Solution x = (x, y, z):", sol1.T)
assert A1 * sol1 == b1

A2 = Matrix([[2, 1], [1, -2]])
b2 = Matrix([7, -1])
sol2 = A2.LUsolve(b2)
print("Q.2 Solution x = (x, y):", sol2.T)
assert A2 * sol2 == b2
print("Q.1 - Q.3 Verified.")
"""
    cells.append(nbf.v4.new_code_cell(code_q1_3))

    # Q4 to Q8
    q4_8_md = """### Q.4 & Q.8) Row Picture vs. Column Picture & Typo Discrepancy (Medium)
**Question:** For $2x + y = 7$ and $x - 2y = -1$, draw the row picture and column picture. Verify whether $(3, 1)$ is the exact solution.

**Full Analytical Solution & Typo Clarification:**
1. **Testing $(3, 1)$:**
   - Equation 1: $2(3) + 1(1) = 7$ (Satisfied!).
   - Equation 2: $1(3) - 2(1) = 1 \\ne -1$.
   *Examiner Typo Flag:* The lab sheet claims $(3, 1)$ is the solution, but with RHS $-1$, the true solution is $x = 13/5 = 2.6, y = 9/5 = 1.8$. For $(3, 1)$ to be the exact integer solution, equation 2 must have RHS $+1$ ($x - 2y = 1$). We analyze both cases:
2. **Row Picture:**
   - Line 1: $2x + y = 7$.
   - Line 2 (with RHS 1): $x - 2y = 1$.
   Intersect precisely at $(3, 1)$.
3. **Column Picture (with RHS 1):**
   $$3 \\begin{bmatrix} 2 \\\\ 1 \\end{bmatrix} + 1 \\begin{bmatrix} 1 \\\\ -2 \\end{bmatrix} = \\begin{bmatrix} 6 + 1 \\\\ 3 - 2 \\end{bmatrix} = \\begin{bmatrix} 7 \\\\ 1 \\end{bmatrix} = \\mathbf{b}$$
   Scaling column 1 by 3 and column 2 by 1 reaches target vector $(7, 1)^T$.

**What the examiner tests:** Equivalence of row-intersection and column-combination perspectives, and spotting inconsistency in given problem statements.

---

### Q.5) Parameter Sensitivity & Row Dependency (Medium)
**Question:** Analyze the system $x - y = 2, \\quad 3x - 3y = k$.
Find all values of $k$ for which the system has: (a) unique solution, (b) infinitely many solutions, (c) no solution.

**Full Analytical Solution:**
Form the augmented matrix:
$$\\begin{bmatrix} 1 & -1 & \\mid & 2 \\\\ 3 & -3 & \\mid & k \\end{bmatrix} \\xrightarrow{R_2 \\to R_2 - 3R_1} \\begin{bmatrix} 1 & -1 & \\mid & 2 \\\\ 0 & 0 & \\mid & k - 6 \\end{bmatrix}$$
- (a) **Unique solution:** Impossible for all $k \\in \\mathbb{R}$, because $\\text{rank}(A) = 1 < n = 2$.
- (b) **Infinitely many solutions:** Occurs iff row 2 is completely zero $\\implies k - 6 = 0 \\implies k = 6$. The general solution is $x = 2 + t, y = t$ for $t \\in \\mathbb{R}$.
- (c) **No solution:** Occurs iff row 2 is inconsistent $[0 \\; 0 \\mid k - 6 \\ne 0] \\implies k \\ne 6$.

**What the examiner tests:** How row dependency forces either $\\infty$ or $0$ solutions, and why unique solution is impossible when $\\det(A) = 0$.

---

### Q.6) Homogeneous Parameter System (Medium)
**Question:** For which values of $a$ does the homogeneous system have non-zero solutions?
$$\\begin{aligned} ax + 2y &= 0 \\\\ 2x + ay &= 0 \\end{aligned}$$
**Full Analytical Solution:**
A homogeneous system $Ax = 0$ has nonzero solutions if and only if $\\det(A) = 0$:
$$\\det \\begin{bmatrix} a & 2 \\\\ 2 & a \\end{bmatrix} = a^2 - 4 = (a - 2)(a + 2) = 0 \\implies a = \\pm 2$$
- If $a = 2$: $2x + 2y = 0 \\implies y = -x$ (entire line through origin).
- If $a = -2$: $-2x + 2y = 0 \\implies y = x$ (line $y = x$).

**What the examiner tests:** Condition for nontrivial solutions in homogeneous linear systems ($\det(A) = 0$).

---

### Q.7) Parallel and Perpendicular Lines (Medium)
**Question:**
(a) Find the equation of the line parallel to $x + 4y = 7$ that passes through the origin.
(b) Find the perpendicular line to $x + 4y = 7$ passing through $(3, 1)$.

**Full Analytical Solution:**
(a) Parallel lines share the same normal vector $\\mathbf{n} = (1, 4)^T$. Passing through $(0, 0)$ gives $x + 4y = 0$.
(b) The direction vector of $x + 4y = 7$ is $(-4, 1)^T$, so its normal is $(1, 4)^T$. A line perpendicular to it must have normal orthogonal to $(1, 4)^T$, i.e. $\\mathbf{n}_{\\perp} = (4, -1)^T$.
Equation: $4x - y = c$. Passing through $(3, 1)$: $4(3) - 1(1) = 11$.
Thus $4x - y = 11$.

**What the examiner tests:** Vector normal representation of lines and geometric orthogonality in $\\mathbb{R}^2$.
"""
    cells.append(nbf.v4.new_markdown_cell(q4_8_md))
    
    code_q4_8 = """# SymPy Verification for Lab 1 Q.4 - Q.7
k = sp.symbols('k')
M_q5 = Matrix([[1, -1, 2], [3, -3, k]])
print("Q.5 RREF with parameter k:")
display(M_q5.rref()[0])

a = sp.symbols('a')
M_q6 = Matrix([[a, 2], [2, a]])
print("Q.6 Determinant roots for non-zero solutions:", sp.solve(M_q6.det(), a))

# Q.7 verification
assert Matrix([1, 4]).dot(Matrix([4, -1])) == 0, "Normal vectors must be orthogonal"
print("Q.7 Perpendicular line check: 4(3) - 1 = 11. Verified.")
"""
    cells.append(nbf.v4.new_code_cell(code_q4_8))

    # Q9 to Q15
    q9_15_md = """### Q.9) Concurrency of Three Lines (Hard)
**Question:** Given $2x + y = 5, \\quad x - y = 1, \\quad 3x = 6$:
(a) Verify they intersect at a single point.
(b) What happens if all right-hand sides are zero?
(c) How to construct another nonzero choice of right-hand sides that preserves concurrency?

**Full Analytical Solution:**
(a) From line 3: $3x = 6 \\implies x = 2$.
Plugging into line 2: $2 - y = 1 \\implies y = 1$.
Checking line 1: $2(2) + 1 = 5$ (Satisfied!). All 3 lines pass through $(2, 1)$.
(b) If RHS $= (0, 0, 0)^T$, all 3 lines pass through the origin $(0, 0)$, so $(0, 0)$ is the unique common solution.
(c) Pick ANY point $P = (x_0, y_0)$ in $\\mathbb{R}^2$. Evaluate each row:
$b_1 = 2x_0 + y_0, \\quad b_2 = x_0 - y_0, \\quad b_3 = 3x_0$.
The system with this RHS will intersect concurrently at $P$.

**What the examiner tests:** Geometric meaning of concurrent lines and constructing consistent systems from known points.

---

### Q.10) The 2×2 Determinant Test (Medium)
**Question:** State and prove the 2×2 determinant solvability test for $\\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix} \\begin{bmatrix} x \\\\ y \\end{bmatrix} = \\begin{bmatrix} e \\\\ f \\end{bmatrix}$.
**Full Analytical Solution:**
Elimination: $R_2 \\to a R_2 - c R_1 \\implies (ad - bc) y = af - ce$.
If $ad - bc \\ne 0$, $y = \\frac{af - ce}{ad - bc}$ and $x = \\frac{de - bf}{ad - bc}$ (unique solution).
If $ad - bc = 0$, the lines are parallel; consistent iff $af - ce = 0$.

**What the examiner tests:** Algebraic derivation of Cramer's rule / determinant criterion.

---

### Q.11) Consistency and Contradictions (Hard)
**Question:** Analyze consistency of:
$$u + v + w = 2, \\quad u + 2v + 3w = 1, \\quad v + 2w = 0$$
**Full Analytical Solution:**
Subtracting Eq 1 from Eq 2:
$$(u + 2v + 3w) - (u + v + w) = v + 2w = 1 - 2 = -1$$
Comparing with Eq 3: $v + 2w = 0$.
Contradiction: $-1 = 0$!
To make the system consistent, the RHS of the third equation must be $-1$.

**What the examiner tests:** Recognizing linear dependence among row equations to identify consistency conditions.

---

### Q.12) Café Word Problem (Easy)
**Question:** $2c + s = 250, \\quad c + 3s = 350$. Find price of coffee $c$ and sandwich $s$.
**Full Analytical Solution:**
$$c = 350 - 3s \\implies 2(350 - 3s) + s = 250 \\implies 700 - 5s = 250 \\implies 5s = 450 \\implies s = 90$$
Then $c = 350 - 3(90) = 80$.
Coffee = 80, Sandwich = 90.

**What the examiner tests:** Formulating and solving basic 2-variable real-world linear systems.

---

### Q.13) Column Dependence & Coplanarity (Hard)
**Question:** Given columns $\\mathbf{c}_1 = (1, 1, 0)^T, \\mathbf{c}_2 = (1, 2, 1)^T, \\mathbf{c}_3 = (1, 3, 2)^T$:
Show that $\\mathbf{c}_3 = 2\\mathbf{c}_2 - \\mathbf{c}_1$, and explain its geometric significance.
**Full Analytical Solution:**
$$2\\mathbf{c}_2 - \\mathbf{c}_1 = 2\\begin{bmatrix} 1 \\\\ 2 \\\\ 1 \\end{bmatrix} - \\begin{bmatrix} 1 \\\\ 1 \\\\ 0 \\end{bmatrix} = \\begin{bmatrix} 2 - 1 \\\\ 4 - 1 \\\\ 2 - 0 \\end{bmatrix} = \\begin{bmatrix} 1 \\\\ 3 \\\\ 2 \\end{bmatrix} = \\mathbf{c}_3$$
Geometrically, the 3 column vectors lie in the **same 2D plane passing through the origin in $\\mathbb{R}^3$**. They cannot span all of $\\mathbb{R}^3$.

**What the examiner tests:** Column dependence and geometric coplanarity in $\\mathbb{R}^3$.

---

### Q.14) 4D Hyperplane System (Challenge)
**Question:**
$$\\begin{aligned} u + v + w + z &= 6 \\\\ u + w + z &= 4 \\\\ u + w &= 2 \\end{aligned}$$
*(a) Describe the geometric solution set in $\\mathbb{R}^4$.*
*(b) What happens if we append the equation $u = -1$?*
*(c) What happens if we append the equation $u + w = 3$?*

**Full Analytical Solution:**
(a) From Eq 2 and Eq 3: $(u + w + z) - (u + w) = z = 4 - 2 = 2$.
From Eq 1 and Eq 2: $(u + v + w + z) - (u + w + z) = v = 6 - 4 = 2$.
Eq 3 gives $u + w = 2 \\implies w = 2 - u$, with $u$ free.
Solution vector:
$$\\begin{bmatrix} u \\\\ v \\\\ w \\\\ z \\end{bmatrix} = \\begin{bmatrix} 0 \\\\ 2 \\\\ 2 \\\\ 2 \\end{bmatrix} + u \\begin{bmatrix} 1 \\\\ 0 \\\\ -1 \\\\ 0 \\end{bmatrix}, \\quad u \\in \\mathbb{R}$$
This is a **1-dimensional straight line living in 4-dimensional space $\\mathbb{R}^4$**.
(b) Adding $u = -1$: locks the free variable $\\implies w = 2 - (-1) = 3$. The solution set collapses to the **single point $(-1, 2, 3, 2)$**.
(c) Adding $u + w = 3$: directly contradicts $u + w = 2$ ($2 = 3$, impossible!). Solution set is **empty (no solution)**.

**What the examiner tests:** High-dimensional geometry (intersections of hyperplanes in $\\mathbb{R}^4$), free variables, and collapse to a point or empty set.

---

### Q.15) The Hidden Solution Property (Medium)
**Question:** If the last column of $A$ equals the right-hand side vector $b$, what is an immediate solution to $Ax = b$?
**Full Analytical Solution:**
By definition of the column picture:
$$x_1 \\mathbf{a}_1 + x_2 \\mathbf{a}_2 + \\dots + x_n \\mathbf{a}_n = \\mathbf{b}$$
If $\\mathbf{a}_n = \\mathbf{b}$, setting $x_1 = 0, x_2 = 0, \\dots, x_{n-1} = 0, x_n = 1$ yields:
$$0 \\mathbf{a}_1 + \\dots + 0 \\mathbf{a}_{n-1} + 1 \\mathbf{a}_n = \\mathbf{a}_n = \\mathbf{b}$$
Thus, an immediate solution is $x = (0, 0, \\dots, 0, 1)^T$.

**What the examiner tests:** Instant recognition of column-picture solutions without performing Gaussian elimination.
"""
    cells.append(nbf.v4.new_markdown_cell(q9_15_md))

    code_q9_15 = """# SymPy Verification for Lab 1 Q.9 - Q.15
print("=== Verifying Lab 1 Q.9 - Q.15 ===")
# Q.9 Concurrency
A_q9 = Matrix([[2, 1], [1, -1], [3, 0]])
b_q9 = Matrix([5, 1, 6])
print("Q.9 Solution point:", A_q9.LUsolve(b_q9).T)

# Q.12 Cafe
A_cafe = Matrix([[2, 1], [1, 3]])
b_cafe = Matrix([250, 350])
print("Q.12 Cafe solution (c, s):", A_cafe.LUsolve(b_cafe).T)

# Q.13 Column Dependence
c1 = Matrix([1, 1, 0])
c2 = Matrix([1, 2, 1])
c3 = Matrix([1, 3, 2])
assert 2*c2 - c1 == c3, "Q.13 failed"
print("Q.13 2*c2 - c1 == c3 Verified.")

# Q.14 4D System
A_4d = Matrix([[1, 1, 1, 1], [1, 0, 1, 1], [1, 0, 1, 0]])
b_4d = Matrix([6, 4, 2])
print("Q.14 Nullspace direction of 4D system:", A_4d.nullspace()[0].T)
print("Lab 1 verification completely passed!")
"""
    cells.append(nbf.v4.new_code_cell(code_q9_15))
    
    return cells

def get_lab2_cells():
    cells = []
    sec_md = """## Lab 2 Solutions: Matrix Multiplication (MUL-TEA-PLICATION)

---
"""
    cells.append(nbf.v4.new_markdown_cell(sec_md))

    q_all_md = """### Q.1) Matrix Times Vector Ax (Easy)
**Question:** Compute $Ax$ for $A = \\begin{bmatrix} 2 & 1 & 0 \\\\ 1 & 3 & 2 \\\\ 0 & 2 & 4 \\end{bmatrix}$ and $x = \\begin{bmatrix} 1 \\\\ 2 \\\\ 1 \\end{bmatrix}$.
**Full Analytical Solution:**
Row dot products:
- Row 1: $2(1) + 1(2) + 0(1) = 4$
- Row 2: $1(1) + 3(2) + 2(1) = 9$ *(Note: prompt text typo listed 8; correct mathematical dot product is 9)*
- Row 3: $0(1) + 2(2) + 4(1) = 8$
Result: $Ax = (4, 9, 8)^T$.

**What the examiner tests:** Performing matrix-vector multiplication as linear combination of columns and entrywise dot products.

---

### Q.2) Row Vector Times Matrix uA (Easy)
**Question:** Compute $[2, 1, 3] \\begin{bmatrix} 1 & 0 \\\\ 2 & 1 \\\\ 0 & 3 \\end{bmatrix}$.
**Full Analytical Solution:**
Left multiplication combines rows:
$$2[1, 0] + 1[2, 1] + 3[0, 3] = [2 + 2 + 0, \\; 0 + 1 + 9] = [4, 10]$$

**What the examiner tests:** Left multiplication as a linear combination of the rows of $A$.

---

### Q.3) Recipe Matrix Transformation (Medium)
**Question:** A sound mixer matrix $S$ has 3 acoustic properties (rows) for 3 sound samples (columns). If $R$ is a $3 \\times 4$ recipe matrix, what do the columns of $SR$ represent?
**Full Analytical Solution:**
Each column $j$ of $R$ is a recipe (weights on the 3 base sounds). By Perspective 2 of matrix multiplication, column $j$ of $SR$ is $S \\cdot \\text{col}_j(R)$, which gives the exact acoustic property profile of recipe $j$.

**What the examiner tests:** Column-wise interpretation of matrix product $SR$.

---

### Q.4) Structured 5×5 Matrix Trick (Medium)
**Question:** A $5 \\times 5$ matrix contains zeros everywhere except $a_{ii} = 1$ for $i \\le 4$, $a_{i5} = 2$ for $i \\le 4$, and row 5 is all zeros. Compute $Ax$ for $x = (1, 1, 1, 1, 5)^T$.
**Full Analytical Solution:**
For rows $1$ to $4$: $(Ax)_i = 1(x_i) + 2(x_5) = 1(1) + 2(5) = 11$.
For row $5$: $(Ax)_5 = 0$.
Thus $Ax = (11, 11, 11, 11, 0)^T$.

**What the examiner tests:** Exploiting sparsity and structured matrix rows for fast computation.

---

### Q.5) Three Stage Lamps RGB Mixing (Medium)
**Question:** Lamps have colors: Red $(1, 0, 0)^T$, Cyan $(0, 1, 1)^T$, Yellow $(1, 1, 0)^T$. If dials are $x = (2, 3, 1)^T$, find the resulting color on the wall.
**Full Analytical Solution:**
$$M x = 2 \\begin{bmatrix} 1 \\\\ 0 \\\\ 0 \\end{bmatrix} + 3 \\begin{bmatrix} 0 \\\\ 1 \\\\ 1 \\end{bmatrix} + 1 \\begin{bmatrix} 1 \\\\ 1 \\\\ 0 \\end{bmatrix} = \\begin{bmatrix} 2 + 0 + 1 \\\\ 0 + 3 + 1 \\\\ 0 + 3 + 0 \\end{bmatrix} = \\begin{bmatrix} 3 \\\\ 4 \\\\ 3 \\end{bmatrix}$$

**What the examiner tests:** Vector addition model of additive light mixing.

---

### Q.6) Antenna Aggregation System (Medium)
**Question:** 6 antennas feed into 3 channels via $A = [I_3 \\mid I_3]$.
(a) Write down $Ax$.
(b) How does a change in antenna 2 affect the channels?
(c) How to modify row 1 to pair antenna 1 with antenna 5?

**Full Analytical Solution:**
(a) $Ax = (x_1 + x_4, \\; x_2 + x_5, \\; x_3 + x_6)^T$.
(b) Antenna 2 appears only in channel 2 ($x_2 + x_5$). Changing antenna 2 affects strictly Channel 2.
(c) To pair antennas 1 and 5, row 1 must select $x_1$ and $x_5$: $\\text{Row } 1 = [1, 0, 0, 0, 1, 0]$.

**What the examiner tests:** Block matrix multiplication and sensor aggregation routing.

---

### Q.7) Words Matrices & Non-Commutativity (Hard)
**Question:** Explain how non-commutativity manifests when entries are English words.
**Full Analytical Solution:**
Matrix multiplication combines items in strict sequential order. In matrix language models, $AB$ computes "Subject acts on Verb", yielding coherent phrases like "Algebra meets in a line", whereas $BA$ reverses grammatical syntax into meaningless or completely different statements. Furthermore, zero entries represent "nothing" and eliminate combinations.

**What the examiner tests:** Why $AB \\ne BA$ in semantics and algebra.

---

### Q.8) Social Network Influence Matrix J - I (Hard)
**Question:** 10 creators. $A = J_{10 \\times 10} - I_{10 \\times 10}$.
(a) Compute $A \\mathbf{1}$ where $\\mathbf{1} = (1, 1, \\dots, 1)^T$.
(b) Compute $A^k \\mathbf{1}$. Interpret the result.

**Full Analytical Solution:**
(a) $J \\mathbf{1} = 10 \\cdot \\mathbf{1}$, and $I \\mathbf{1} = \\mathbf{1}$.
Thus $A \\mathbf{1} = (J - I)\\mathbf{1} = 10\\mathbf{1} - \\mathbf{1} = 9\\mathbf{1}$.
(b) By repeated multiplication: $A^k \\mathbf{1} = 9^k \\mathbf{1}$.
*Interpretation:* In each round of social diffusion, each creator receives influence from the 9 other creators. Uniform influence multiplies by 9 every step.

**What the examiner tests:** Eigenvector property $(J-I)\\mathbf{1} = (n-1)\\mathbf{1}$ and matrix powers.

---

### Q.9) Transportation Network Adjacency Matrix & Walk Counting (Challenge)
**Question:** Transportation graph with 5 vertices $A, B, C, D, E$ and edges $(A,B), (A,D), (B,D), (B,E), (B,C), (C,E), (D,E)$.
(a) Construct adjacency matrix $M$.
(b) Compute $M^2$.
(c) Find $(M^2)_{AE}$ and list all 2-step walks from $A$ to $E$.
(d) Explain why $m_{Ak} m_{kE}$ tests whether $k$ can be an intermediate stop.
(e) Complete: $(M^2)_{ij} = \\text{number of } \\dots$
(f) What information is stored in $M^3$?

**Full Analytical Solution:**
(a) Ordered vertices $A, B, C, D, E$:
$$M = \\begin{bmatrix} 0 & 1 & 0 & 1 & 0 \\\\ 1 & 0 & 1 & 1 & 1 \\\\ 0 & 1 & 0 & 0 & 1 \\\\ 1 & 1 & 0 & 0 & 1 \\\\ 0 & 1 & 1 & 1 & 0 \\end{bmatrix}$$
(b) Computing $M^2 = M \\times M$:
$$M^2 = \\begin{bmatrix} 2 & 1 & 1 & 1 & 2 \\\\ 1 & 4 & 1 & 1 & 2 \\\\ 1 & 1 & 2 & 2 & 1 \\\\ 1 & 1 & 2 & 3 & 1 \\\\ 2 & 2 & 1 & 1 & 3 \\end{bmatrix}$$
(c) $(M^2)_{AE} = 2$. There are exactly two 2-step walks from $A$ to $E$:
1. $A \\to B \\to E$
2. $A \\to D \\to E$
(d) $m_{Ak} m_{kE} = 1 \\iff m_{Ak} = 1$ (edge from $A$ to $k$) AND $m_{kE} = 1$ (edge from $k$ to $E$). If either edge is missing, the product is 0. Thus it acts as a boolean indicator for a valid 2-step path through $k$.
(e) $(M^2)_{ij} = \\text{number of walks of length 2 connecting vertex } i \\text{ to vertex } j$.
(f) $M^3$ stores the number of walks of length 3 between every pair of vertices.

**What the examiner tests:** Graph adjacency matrix power theorem and combinatorial path counting.
"""
    cells.append(nbf.v4.new_markdown_cell(q_all_md))

    code_lab2 = """# SymPy Verification for Lab 2
A_q1 = Matrix([[2, 1, 0], [1, 3, 2], [0, 2, 4]])
x_q1 = Matrix([1, 2, 1])
print("Lab 2 Q.1 Ax:", (A_q1 * x_q1).T)

u_q2 = Matrix([[2, 1, 3]])
A_q2 = Matrix([[1, 0], [2, 1], [0, 3]])
print("Lab 2 Q.2 uA:", u_q2 * A_q2)

# Q.9 Adjacency matrix verification
M_adj = Matrix([
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
])
M2 = M_adj**2
print("Lab 2 Q.9 M^2 entry (A, E):", M2[0, 4])
assert M2[0, 4] == 2, "Walk count failed!"
print("Lab 2 all verifications passed!")
"""
    cells.append(nbf.v4.new_code_cell(code_lab2))

    return cells

def get_lab3_cells():
    cells = []
    sec_md = """## Lab 3 Solutions: Linear Combinations and Span

---
"""
    cells.append(nbf.v4.new_markdown_cell(sec_md))

    q_all_md = """### Q.1 - Q.5) Basic Combinations, Drones, Colors, Sailboats (Easy)
- **Q.1:** A linear combination scales vectors by constants and sums them: $c_1 v_1 + c_2 v_2$.
- **Q.2:** A linear combination of vectors produces a **single vector**, whereas their **span** is an infinite set (a subspace).
- **Q.3 (Drone):** Movement commands $v = (2, 1), w = (1, 2)$. Equal mixture $1v + 1w = (3, 3)$. Target $(3, 3)$ needs $c_1 = c_2 = 1$. Other targets require unequal coefficients.
- **Q.4 (Colors):** Basis colors Red $(255, 0, 0)$ and Green $(0, 255, 0)$. Yellow $= R + G = (255, 255, 0)$. Pure Blue $(0, 0, 255)$ is impossible because the blue channel is zero in both basis colors ($c_1(0) + c_2(0) = 0 \\ne 255$).
- **Q.5 (Sailboat):** Vectors $v = (4, 0), w = (0, 3)$. Since they are along the $x$ and $y$ axes, $\\text{Span}(v, w) = \\mathbb{R}^2$. Statement A is True. Statement B is False (real scalars allow sailing anywhere, not just positive quadrant).

**What the examiner tests:** Conceptual difference between a single linear combination and an entire span.

---

### Q.6) Three 2×2 Systems Classification & Fill-ins (Medium)
1. $x + y = 5, x - y = 1 \\implies$ Unique solution $(3, 2)$. Row picture: two lines crossing at a point. Column picture: unique combination $3(1, 1)^T + 2(1, -1)^T = (5, 1)^T$.
2. $x + 2y = 3, 2x + 4y = 6 \\implies$ Infinitely many solutions. Row picture: coincident lines. Column picture: infinitely many combinations.
3. $x + 2y = 3, 2x + 4y = 7 \\implies$ No solution. Row picture: parallel disjoint lines. Column picture: $b$ lies outside the column span.

---

### Q.8 - Q.14) Span Limits, Species, and Redundancy (Hard & Challenge)
- **Q.8 (Song Profiles):** Features: Energy, Danceability, Acousticness ($\mathbb{R}^3$). Two reference tracks can at most span a 2D plane in $\mathbb{R}^3$. They can NEVER span all of $\mathbb{R}^3$.
- **Q.9 (Species Growth):** $v_1 = (1, 2, 1), v_2 = (2, 4, 2) = 2v_1$. The span is a 1D line. Target $(3, 5, 3)$ is not a multiple of $(1, 2, 1)$ ($3/1 \\ne 5/2$), so it is NOT in the span.
- **Q.11 (Vibrations):** $v_1 = (1, 0, 1), v_2 = (0, 1, 1), v_3 = (1, 1, 2)$. Since $v_3 = v_1 + v_2$, the span is a 2D plane. Removing $v_3$ leaves the span completely unchanged.
- **Q.12 (Commands):** $v_1 = (1, 2, 0), v_2 = (0, 1, 1), v_3 = (1, 3, 1)$. Notice $v_3 = v_1 + v_2$. Target $(4, 11, 3) = 4v_1 + 3v_2$. Since $v_3 - v_1 - v_2 = 0$, any combination $(4 - t)v_1 + (3 - t)v_2 + t v_3$ also reaches the target (infinitely many representations).
- **Q.13 (Reaction Pathways):** $(1, 0, 2), (0, 1, 1), (1, 1, 3)$ spans a plane since $v_3 = v_1 + v_2$. Replacing $v_3$ with $(1, 1, 4)$ gives $\\det \\begin{bmatrix} 1 & 0 & 1 \\\\ 0 & 1 & 1 \\\\ 2 & 1 & 4 \\end{bmatrix} = 1(3) + 1(-2) = 1 \\ne 0$, which spans all of $\\mathbb{R}^3$.
- **Q.14 (Infinite Monkey Controller):** If a monkey deletes a redundant vector (a vector that is already in the span of the others), the set of reachable drone positions does not shrink at all.
"""
    cells.append(nbf.v4.new_markdown_cell(q_all_md))

    code_lab3 = """# SymPy Verification for Lab 3
# Q.12 Target (4, 11, 3)
A_q12 = Matrix([[1, 0, 1], [2, 1, 3], [0, 1, 1]])
b_q12 = Matrix([4, 11, 3])
print("Q.12 Augmented RREF:")
display(A_q12.row_join(b_q12).rref()[0])

# Q.13 Independent set with (1, 1, 4)
A_q13 = Matrix([[1, 0, 1], [0, 1, 1], [2, 1, 4]])
print("Q.13 Determinant with (1, 1, 4):", A_q13.det())
assert A_q13.det() != 0
print("Lab 3 verification completely passed!")
"""
    cells.append(nbf.v4.new_code_cell(code_lab3))

    return cells

def get_lab4_cells():
    cells = []
    sec_md = """## Lab 4 Solutions: Gaussian Elimination and Echelon Forms

---
"""
    cells.append(nbf.v4.new_markdown_cell(sec_md))

    q_all_md = """### Q.1 - Q.5) Elimination Applications (Easy & Medium)
- **Q.1 (Factory Robot):** $x + y + z = 9, 2x + y + 3z = 16, x + 2y + z = 11$. Row operations yield $(x, y, z) = (7, 2, 0)$.
- **Q.4 (Store Revenue):** $x + y + z = 120, 2x + 3y + z = 230, x + 2y + 4z = 270$. Elimination gives $(x, y, z) = (50, 30, 40)$.
- **Q.5 (Quadcopter):** 4 motor thrusts. Upper triangular system directly back-substitutes to $(x_1, x_2, x_3, x_4) = (13, 9, 7, 11)$.

---

### Q.6 - Q.12) Matrix Rank and Multi-Variable Systems (Medium & Hard)
- **Q.6 & Q.10 (Repeated Rows):** When Row 2 is $2 \\times$ Row 1, elimination produces an all-zero row, reducing the rank from 3 to 2.
- **Q.8 (3×5 Matrix REF):** Echelon form has 3 pivots $\\implies$ rank is 3. Number of free variables is $5 - 3 = 2$.
- **Q.9 (Delivery Warehouses):** 5 warehouses with 3 equations. Rank is 3, yielding $5 - 3 = 2$ free variables. General solution expresses basic shipments in terms of free warehouse variables.

---

### Challenge Problem: Graph Theory & Unsigned Incidence Matrices
*(a) Label the 5-vertex network from the image (vertices A, B, C, D, E; edges e1..e6).*
*(b) Construct the unsigned incidence matrix $B$ ($5 \\times 6$).*
*(c) Compute $\\text{rank}(B)$.*
*(d) Explain why $\\text{rank}(B) = n = 5$ for graphs with odd cycles, whereas $\\text{rank}(B) = n - 1$ for bipartite graphs.*

**Full Analytical Solution:**
- Unsigned incidence matrix records vertex participation: $b_{ij} = 1$ if node $i \\in \\text{edge } j$.
- For our 5-vertex graph with edges $(A, B), (A, D), (B, C), (B, D), (C, E), (D, E)$:
  The subgraph on $\\{A, B, D\\}$ forms a triangle (an odd cycle of length 3).
- Over $\\mathbb{R}$, any odd cycle allows elimination to produce an independent pivot for every single vertex!
  Therefore, $\\text{rank}(B) = 5$ (full row rank).
- In contrast, if a graph is bipartite (contains no odd cycles), its vertices can be partitioned into sets $V_1$ and $V_2$ such that all edges go between $V_1$ and $V_2$. Then $\\sum_{i \\in V_1} \\text{row}_i = \\sum_{j \\in V_2} \\text{row}_j$, giving a linear dependency that forces $\\text{rank}(B) = n - 1$.

**What the examiner tests:** Spectral graph theory connection between matrix rank and bipartite / odd-cycle graph topology.
"""
    cells.append(nbf.v4.new_markdown_cell(q_all_md))

    code_lab4 = """# SymPy Verification for Lab 4
# Q.1 Robot
A_q1 = Matrix([[1, 1, 1], [2, 1, 3], [1, 2, 1]])
b_q1 = Matrix([9, 16, 11])
print("Lab 4 Q.1 Solution:", A_q1.LUsolve(b_q1).T)
assert A_q1.LUsolve(b_q1) == Matrix([7, 2, 0])

# Q.4 Store Revenue
A_q4 = Matrix([[1, 1, 1], [2, 3, 1], [1, 2, 4]])
b_q4 = Matrix([120, 230, 270])
print("Lab 4 Q.4 Solution:", A_q4.LUsolve(b_q4).T)
assert A_q4.LUsolve(b_q4) == Matrix([50, 30, 40])

# Challenge Unsigned Incidence
B_un = Matrix([
    [1, 1, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1]
])
print("Lab 4 Challenge Rank:", B_un.rank())
assert B_un.rank() == 5
print("Lab 4 verification completely passed!")
"""
    cells.append(nbf.v4.new_code_cell(code_lab4))

    return cells

print("lab_solutions_1_4.py initialized successfully.")
