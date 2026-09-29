"""
Module containing Mock-Exam Extras (Section 9) for LinearAlgebra_Master_Notes.ipynb
"""

import nbformat as nbf

def get_extras_cells():
    cells = []
    
    extras_md = """# Section 9: Mock Exam Preparation Suite

---

### 9.1 One-Page Linear Algebra Formula Cheat Sheet

| Category | Fundamental Formula / Principle | Key Conditions / Dimensions |
| :--- | :--- | :--- |
| **Matrix Systems** | $Ax = b \\iff \\sum_{j=1}^n x_j \\mathbf{a}_j = b$ | Consistent $\\iff \\text{rank}(A) = \\text{rank}([A \\mid b])$ |
| **Multiplication** | $(AB)_{ij} = \\text{row}_i(A) \\cdot \\text{col}_j(B) = \\sum_k \\mathbf{a}_k \\mathbf{b}_k^T$ | $(m \\times n)(n \\times p) = m \\times p$ |
| **Walk Theorem** | $(M^k)_{ij} = \\text{number of walks of length } k$ | $M$ is graph adjacency matrix |
| **Elimination & LU** | $A = LU$ (No row exchanges) | $L$ unit lower triangular ($l_{ij}$ multipliers), $U$ upper triangular |
| **Linear Independence**| $\\sum c_i \\mathbf{v}_i = \\mathbf{0} \\implies c_i = 0$ | Rank $= n \\iff$ No free variables |
| **Rank-Nullity** | $\\text{rank}(A) + \\text{nullity}(A) = n$ | $n = \\text{number of columns (input variables)}$ |
| **Complete Solution**| $\\mathbf{x} = \\mathbf{x}_p + \\mathbf{x}_n = \\mathbf{x}_p + \\sum c_i \\mathbf{s}_i$ | $\\mathbf{x}_p$: free vars $= 0$; $\\mathbf{s}_i$: special solutions |
| **Fundamental Subspaces**| $\\dim C(A) = r, \\quad \\dim C(A^T) = r$ | $C(A) \\subseteq \\mathbb{R}^m, \\quad C(A^T) \\subseteq \\mathbb{R}^n$ |
| | $\\dim N(A) = n - r, \\quad \\dim N(A^T) = m - r$ | $N(A) \\subseteq \\mathbb{R}^n, \\quad N(A^T) \\subseteq \\mathbb{R}^m$ |
| **Orthogonality** | $C(A^T) \\perp N(A) \\quad \\text{in } \\mathbb{R}^n$ | $C(A) \\perp N(A^T) \\quad \\text{in } \\mathbb{R}^m$ |
| **Fredholm Solvability**| $Ax = b \\text{ solvable } \\iff \\mathbf{y}^T \\mathbf{b} = 0 \\; \\forall \\mathbf{y} \\in N(A^T)$ | Orthogonal complement test |
| **Incidence Matrices**| Signed: $\\text{rank} = n - 1$; Unsigned: $\\text{rank} = n$ (odd cycle) or $n-1$ (bipartite) | Signed: $N(A) = \\text{span}(\\mathbf{1})$ |

---

### 9.2 Common Mistakes & Pitfalls Per Lecture

- **Lecture 1 Trap:** Confusing row picture and column picture. In 2D, row picture lines cross at the solution $(x, y)$, while column picture vectors add up to $\\mathbf{b}$. Also, forgetting $0$ coefficients when variables are missing.
- **Lecture 2 Trap:** Assuming $AB = BA$. They rarely commute! Also forgetting that $(AB)^T = B^T A^T$ (order reverses).
- **Lecture 3 Trap:** Thinking that 3 vectors in $\\mathbb{R}^3$ automatically span $\\mathbb{R}^3$. If one vector is coplanar with the other two (dependent), they only span a plane! Always check the determinant or rank.
- **Lecture 4 Trap:** Mixing up pivot columns and free columns. Free variables arise from columns *without* pivots, NOT from zero rows in $A$.
- **Lecture 5 Trap:** Placing multipliers with wrong signs into $L$. In $E$, the operation $R_2 - c R_1$ has $-c$, but in $L$ the entry $l_{21} = +c$ (because $L = E^{-1}$).
- **Lecture 6 Trap:** Taking the pivot columns of the reduced echelon matrix $U$ or $R$ as the basis for $C(A)$. You MUST extract the corresponding columns from the **ORIGINAL matrix $A$**!
- **Lecture 7 Trap:** Confusing the ambient spaces: $N(A) \\subseteq \\mathbb{R}^n$ (input dimension), NOT $\\mathbb{R}^m$.
- **Lecture 8 Trap:** Forgetting that row rank equals column rank ($r$). A rectangular matrix $100 \\times 3$ has at most rank 3, so its row space is at most 3-dimensional!

---

### 9.3 "If You See X, Do Y" Exam Decision Matrix

| If You See This in the Exam Problem... | Do This Immediate Mathematical Action... |
| :--- | :--- |
| **"Find conditions on $b$ for $Ax = b$ to be solvable"** | Compute the Left Null Space $N(A^T)$ by reducing $[A \\mid I]$. Set each zero row's combination to zero: $\\mathbf{y}^T \\mathbf{b} = 0$. |
| **"Find a basis for the column space $C(A)$"** | Reduce $A$ to REF to identify pivot columns. Return the corresponding columns of the **original matrix $A$**. |
| **"Find a basis for the row space $C(A^T)$"** | Reduce $A$ to REF. Return the **nonzero rows of the echelon matrix $U$** (or $R$). |
| **"Find a basis for the null space $N(A)$"** | Solve $Rx = 0$. Set each free variable to $1$ in turn (others $0$) to obtain the special solutions. |
| **"Determine if vectors are linearly independent"** | Place them as columns of a matrix $A$ and row-reduce. Independent $\\iff$ no free variables $\\iff \\text{rank} = n$. |
| **"Matrix equation with unknown parameters $r, s$"** | Row-reduce symbolically; track where pivots could become zero. Analyze roots of pivot expressions. |
| **"Two matrices satisfy $AB = 0$"** | Use the subspace inclusion $C(B) \\subseteq N(A)$ and $C(A^T) \\subseteq N(B^T)$. Rank inequality: $\\text{rank}(A) + \\text{rank}(B) \\le n$. |

---

### 9.4 20 Original Practice Problems with Full Worked Solutions

#### Problem 1 (System Classification)
Determine all values of $k$ such that $\\begin{bmatrix} 1 & 2 & 1 \\\\ 2 & k & 2 \\\\ 3 & 6 & 3 \\end{bmatrix} \\begin{bmatrix} x \\\\ y \\\\ z \\end{bmatrix} = \\begin{bmatrix} 1 \\\\ 2 \\\\ 3 \\end{bmatrix}$ is consistent.
*Solution:* Row 3 is $3 \\times$ Row 1. Row 2 is $2 \\times$ Row 1 if $k = 4$. If $k = 4$, rank is 1 and system is consistent for this $b$. If $k \\ne 4$, subtracting $2 R_1$ from $R_2$ gives $(k-4)y = 0$, which is also solvable ($y = 0, x + z = 1$). Thus consistent for **all** $k \\in \\mathbb{R}$!

#### Problem 2 (Outer Product Expansion)
Decompose $A = \\begin{bmatrix} 2 & 4 \\\\ 3 & 6 \\end{bmatrix}$ into an outer product $\\mathbf{u} \\mathbf{v}^T$.
*Solution:* Col 1 is $(2, 3)^T$, Col 2 is $2 \\times (2, 3)^T$. Thus $A = \\begin{bmatrix} 2 \\\\ 3 \\end{bmatrix} \\begin{bmatrix} 1 & 2 \\end{bmatrix}$.

#### Problem 3 (LU Factorization)
Compute $L$ and $U$ for $A = \\begin{bmatrix} 3 & 1 \\\\ 6 & 5 \\end{bmatrix}$.
*Solution:* $R_2 \\to R_2 - 2R_1 \\implies U = \\begin{bmatrix} 3 & 1 \\\\ 0 & 3 \\end{bmatrix}$. Multiplier $l_{21} = 2$. $L = \\begin{bmatrix} 1 & 0 \\\\ 2 & 1 \\end{bmatrix}$.

#### Problem 4 (Null Space Basis)
Find a basis for $N(A)$ for $A = \\begin{bmatrix} 1 & 2 & 0 & 3 \\\\ 0 & 0 & 1 & 4 \\end{bmatrix}$.
*Solution:* $A$ is in RREF. Pivots in col 1, 3. Free: $x_2, x_4$.
$x_1 = -2x_2 - 3x_4$, $x_3 = -4x_4$.
Setting $x_2 = 1, x_4 = 0 \\implies \\mathbf{s}_1 = (-2, 1, 0, 0)^T$.
Setting $x_2 = 0, x_4 = 1 \\implies \\mathbf{s}_2 = (-3, 0, -4, 1)^T$.
Basis: $\\{(-2, 1, 0, 0)^T, (-3, 0, -4, 1)^T\\}$.

#### Problem 5 (Subspace Test)
Is $W = \\{(x, y, z) \\in \\mathbb{R}^3 : x + 2y - 3z = 0\\}$ a subspace?
*Solution:* **Yes.** It is the null space of the $1 \\times 3$ matrix $[1 \\; 2 \\; -3]$. All null spaces are valid subspaces.

#### Problem 6 (Orthogonality Proof)
Prove that every row of $A$ is orthogonal to every vector in $N(A)$.
*Solution:* Let $\\mathbf{r}_i^T$ be row $i$ of $A$ and $\\mathbf{x} \\in N(A)$. By definition $A\\mathbf{x} = \\mathbf{0}$. The $i$-th component of $A\\mathbf{x}$ is the dot product $\\mathbf{r}_i \\cdot \\mathbf{x} = 0$. Hence $\\mathbf{r}_i \\perp \\mathbf{x}$.

#### Problem 7 (Complete Solution)
Find the complete solution to $\\begin{bmatrix} 1 & 3 \\\\ 2 & 6 \\end{bmatrix} \\begin{bmatrix} x_1 \\\\ x_2 \\end{bmatrix} = \\begin{bmatrix} 4 \\\\ 8 \\end{bmatrix}$.
*Solution:* $R_2 - 2R_1 \\implies 0 = 0$. Particular: set free var $x_2 = 0 \\implies x_1 = 4$. Null vector: $x_1 + 3x_2 = 0 \\implies (-3, 1)^T$. Complete solution: $\\mathbf{x} = \\begin{bmatrix} 4 \\\\ 0 \\end{bmatrix} + t \\begin{bmatrix} -3 \\\\ 1 \\end{bmatrix}$.

#### Problem 8 (Rank Inequality)
If $A$ is $4 \\times 6$ with rank 3, what is the dimension of the left null space $N(A^T)$?
*Solution:* $\\dim N(A^T) = m - r = 4 - 3 = 1$.

#### Problem 9 (Adjacency Powers)
A graph has vertices $1, 2, 3$ connected as a triangle. How many walks of length 3 exist from node 1 to node 1?
*Solution:* In $K_3$, adjacency matrix $M = \\begin{bmatrix} 0 & 1 & 1 \\\\ 1 & 0 & 1 \\\\ 1 & 1 & 0 \\end{bmatrix}$. $M^2 = \\begin{bmatrix} 2 & 1 & 1 \\\\ 1 & 2 & 1 \\\\ 1 & 1 & 2 \\end{bmatrix}$. $M^3 = M^2 M \\implies (M^3)_{11} = 2(0) + 1(1) + 1(1) = 2$ walks ($1 \\to 2 \\to 3 \\to 1$ and $1 \\to 3 \\to 2 \\to 1$).

#### Problem 10 (Construct a Matrix)
Construct a $2 \\times 2$ matrix whose column space is the line $y = 2x$ and whose null space is the line $y = -x$.
*Solution:* Col space is $\\text{span}(1, 2)^T$, so columns must be multiples of $(1, 2)^T$: $A = \\begin{bmatrix} c_1 & c_2 \\\\ 2c_1 & 2c_2 \\end{bmatrix}$.
Null space has $(1, -1)^T \\implies c_1(1) + c_2(-1) = 0 \\implies c_2 = c_1$.
Choosing $c_1 = 1$: $A = \\begin{bmatrix} 1 & 1 \\\\ 2 & 2 \\end{bmatrix}$.

#### Problem 11 (True/False on Rank)
True or False: If $A$ and $B$ are $n \\times n$, then $\\text{rank}(AB) = \\text{rank}(BA)$.
*Solution:* **False.** Counterexample: $A = \\begin{bmatrix} 0 & 1 \\\\ 0 & 0 \\end{bmatrix}, B = \\begin{bmatrix} 0 & 0 \\\\ 0 & 1 \\end{bmatrix}$. $AB = \\begin{bmatrix} 0 & 1 \\\\ 0 & 0 \\end{bmatrix}$ (rank 1), but $BA = \\begin{bmatrix} 0 & 0 \\\\ 0 & 0 \\end{bmatrix}$ (rank 0).

#### Problem 12 (Determinant Product)
If $A = LU$, prove that $\\det(A) = \\det(U) = u_{11} u_{22} \\cdots u_{nn}$.
*Solution:* $\\det(A) = \\det(L) \\det(U)$. Since $L$ is unit lower triangular, its diagonal entries are all $1$, so $\\det(L) = 1$. Since $U$ is triangular, its determinant is the product of its diagonal pivot entries.

#### Problem 13 (Signed Incidence Loop Property)
Why is the sum of entries of any column of a signed incidence matrix always zero?
*Solution:* Each edge leaves exactly one vertex ($-1$) and enters exactly one vertex ($+1$). All other entries in that column are $0$. Thus $-1 + 1 = 0$.

#### Problem 14 (Kirchhoff's Current Law)
In a network, what fundamental subspace does the conservation of current at all nodes belong to?
*Solution:* Left null space $N(A^T)$, where $A^T \\mathbf{y} = \\mathbf{0}$ enforces $\\sum_{\\text{edges at node } i} y_e = 0$.

#### Problem 15 (Parametric Matrix Rank)
For which values of $c$ does $A = \\begin{bmatrix} 1 & c \\\\ c & 9 \\end{bmatrix}$ have rank 1?
*Solution:* $\\det(A) = 9 - c^2 = 0 \\implies c = \\pm 3$. Since row 1 is nonzero, rank is 1 for $c = 3$ and $c = -3$.

#### Problem 16 (Dimension of Intersection)
If $V$ and $W$ are two 2-dimensional planes in $\\mathbb{R}^3$, what are the possible dimensions of $V \\cap W$?
*Solution:* $\\dim(V + W) = \\dim(V) + \\dim(W) - \\dim(V \\cap W)$. Since $V+W \\subseteq \\mathbb{R}^3$, $\\dim(V+W) \\le 3$. Thus $3 \\ge 2 + 2 - \\dim(V \\cap W) \\implies \\dim(V \\cap W) \\ge 1$. Possibilities: $\\dim(V \\cap W) = 1$ (planes intersect in a line) or $\\dim(V \\cap W) = 2$ (coincident planes).

#### Problem 17 (Matrix Powers for Idempotent Matrix)
If $P^2 = P$ (projection matrix), what are the possible eigenvalues / pivots of $P$?
*Solution:* $P(P - I) = 0$. Only $0$ and $1$.

#### Problem 18 (Word Problem: Circuit Loops)
A circuit has 4 nodes and 5 branches. How many independent loop equations are required by Kirchhoff's Voltage Law?
*Solution:* $\\text{Number of independent loops} = \\dim N(A^T) = m - n + 1 = 5 - 4 + 1 = 2$.

#### Problem 19 (Unsigned Incidence Cycle)
Construct the unsigned incidence matrix for a 3-vertex cycle (triangle). Verify that its determinant is $\\pm 2 \\ne 0$.
*Solution:* $B = \\begin{bmatrix} 1 & 0 & 1 \\\\ 1 & 1 & 0 \\\\ 0 & 1 & 1 \\end{bmatrix}$. $\\det(B) = 1(1) - 0 + 1(1) = 2$. Rank is 3!

#### Problem 20 (Four Subspaces Verification)
Given $A = \\begin{bmatrix} 1 & 2 \\\\ 2 & 4 \\end{bmatrix}$, give orthogonal bases for all four fundamental subspaces.
*Solution:*
- Row space $C(A^T)$: $\\text{span}\\{(1, 2)^T\\}$.
- Null space $N(A)$: $\\text{span}\\{(-2, 1)^T\\}$. (Note: $(1)( -2) + 2(1) = 0 \\implies \\perp$).
- Column space $C(A)$: $\\text{span}\\{(1, 2)^T\\}$.
- Left null space $N(A^T)$: $\\text{span}\\{(-2, 1)^T\\}$.

---

### 9.5 3-Day Intensive Mock Exam Study Plan

```
DAY 1: Computational Foundations & Elimination Mastery
├── Morning: Lecture 1 & 2 (Row vs Col Picture, Ax & AB 4 Perspectives)
│   └── Practice: 2D/3D intersection drawings, M^k walk counting
├── Afternoon: Lecture 3 & 4 (Span, Target Test, Gaussian Elimination)
│   └── Practice: REF reduction, identifying pivot vs free columns
└── Evening: 5 Self-Test problems from Lectures 1-4 + SymPy verification

DAY 2: Factorization & Subspace Architecture
├── Morning: Lecture 5 (Elementary matrices, A = LU without row swaps)
│   └── Practice: Forward (Lc=b) and back (Ux=c) substitution by hand
├── Afternoon: Lecture 6 & 7 (Linear Independence, C(A), N(A), Complete Solution)
│   └── Practice: Finding xp + t*xn, Subspace 3-step test
└── Evening: Stage lamp challenge & 6-beam laser quiver problem

DAY 3: The Big Picture, Network Applications & Mock Exam
├── Morning: Lecture 8 (Four Fundamental Subspaces, Orthogonality, Fredholm Alternative)
│   └── Practice: Signed vs unsigned incidence matrices, Water grid flows
├── Afternoon: Complete the 20 Practice Problems under timed conditions (90 mins)
└── Evening: Review Formula Cheat Sheet and "If You See X, Do Y" decision matrix
```
"""
    cells.append(nbf.v4.new_markdown_cell(extras_md))
    return cells

print("master_extras.py initialized successfully.")
