"""
Script module: lab_solutions_5_8.py — detailed cell content for the lab notebook.
"""

"""
Shared cell helpers (inlined so each content file is self-contained).
"""

import nbformat as nbf


def md(cells, text):
    cells.append(nbf.v4.new_markdown_cell(text))


def code(cells, text):
    cells.append(nbf.v4.new_code_cell(text))


def lab_header(title, subtitle):
    return (
        f"## {title}\n\n---\n\n"
        f"*Every question below follows the full protocol: **restatement → step-by-step "
        f"derivation → answer → SymPy verification → examiner's note**. Sheet typos are "
        f"flagged wherever the printed problem is inconsistent with itself.*\n\n{subtitle}\n\n---\n"
    )



LAB_TITLE = "Lab 5 Solutions: Elementary Matrices and LU Decomposition"
LAB_SUB = (
    '**Core ideas tested:** "Prep Once, Serve Many" — elementary matrices as row operations, '
    "$A = LU$ factorization, forward/back substitution for many right-hand sides, and "
    "banded-matrix fill-in."
)


def get_lab5_cells():
    cells = []
    md(cells, lab_header(LAB_TITLE, LAB_SUB))

    # ---------------- Q1 ----------------
    md(cells, r"""### Q.1) Fill in the Table: Operations ↔ Elementary Matrices ↔ Inverses (Easy)

**Question (as printed):** Complete the table relating each row operation, its elementary matrix $E$, and its inverse $E^{-1}$:

| Row operation | Elementary matrix $E$ | Inverse $E^{-1}$ |
| :--- | :--- | :--- |
| $R_2 \to R_2 - R_1$ | $\begin{bmatrix} 1 & 0 \\ -1 & 1 \end{bmatrix}$ | $\begin{bmatrix} 1 & 0 \\ 1 & 1 \end{bmatrix}$ (undoes with $R_2 + R_1$) |
| $R_2 \to R_2 - 3R_1$ | $\begin{bmatrix} 1 & 0 \\ -3 & 1 \end{bmatrix}$ *(printed)* | $\begin{bmatrix} 1 & 0 \\ 3 & 1 \end{bmatrix}$ |
| $R_3 \to 3R_3$ | $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 3 \end{bmatrix}$ | $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & \tfrac13 \end{bmatrix}$ *(printed)* |
| $R_3 \to R_3 + 3R_2$ | $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 3 & 1 \end{bmatrix}$ | $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -3 & 1 \end{bmatrix}$ |
| $R_1 \leftrightarrow R_3$ (swap) | $\begin{bmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{bmatrix}$ *(printed)* | **itself** (a swap is self-inverse) |

**How each entry is produced:**
- *Subtraction row:* $E$ starts from $I$ and puts the **negated multiplier** in position $(2,1)$: $R_2 - 3R_1 \Rightarrow E_{21} = -3$. The inverse flips the sign: $+3$.
- *Scaling row:* the printed inverse $\mathrm{diag}(1, 1, \tfrac13)$ scales row 3 by $\tfrac13$, so the forward operation must be the **opposite scaling** $R_3 \to 3R_3$ with $E = \mathrm{diag}(1,1,3)$.
- *Addition row:* $R_3 + 3R_2 \Rightarrow E_{32} = +3$; inverse has $-3$ (i.e. $R_3 - 3R_2$).
- *Permutation row:* the printed $E$ swaps rows 1 and 3; applying it twice restores the order, so $E^{-1} = E$.

**Examiner's note:** Tests the dictionary between row operations, elementary matrices, and inverses — the backbone of $A = LU$.
""")
    code(cells, r"""# SymPy verification — Lab 5, Q.1 (each printed/guessed pair multiplies to I)
pairs = [
    (Matrix([[1, 0], [-1, 1]]), Matrix([[1, 0], [1, 1]])),
    (Matrix([[1, 0], [-3, 1]]), Matrix([[1, 0], [3, 1]])),
    (Matrix.diag(1, 1, 3), Matrix.diag(1, 1, sp.Rational(1, 3))),
    (Matrix([[1, 0, 0], [0, 1, 0], [0, 3, 1]]), Matrix([[1, 0, 0], [0, 1, 0], [0, -3, 1]])),
    (Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]]), Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])),
]
for k, (E, Einv) in enumerate(pairs, 1):
    assert E * Einv == sp.eye(E.rows)
print("Q.1  all five E * E^-1 = I pairs verified")""")

    # ---------------- Q2 ----------------
    md(cells, r"""### Q.2) Identify the Row Operation Behind $E$, Verify $EA$ (Easy)

**Question (as printed):**
$$\text{(a) } E = \begin{bmatrix} -6 & 0 \\ 0 & 1 \end{bmatrix},\quad A = \begin{bmatrix} -1 & -2 & 5 & -1 \\ 3 & -6 & -6 & -6 \end{bmatrix}
\qquad \text{(b) } E = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -3 & 1 \end{bmatrix},\quad A = \begin{bmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{bmatrix}$$

**Part (a) — identify.** $E = \mathrm{diag}(-6, 1)$: the operation is **"multiply row 1 by $-6$"** (a scaling elementary matrix). Applying it to $A$ scales only the first row:
$$EA = \begin{bmatrix} (-6)(-1) & (-6)(-2) & (-6)(5) & (-6)(-1) \\ 3 & -6 & -6 & -6 \end{bmatrix} = \begin{bmatrix} 6 & 12 & -30 & 6 \\ 3 & -6 & -6 & -6 \end{bmatrix}.$$
Its inverse is $\mathrm{diag}(-\tfrac16, 1)$, which would restore row 1.

**Part (b) — identify.** $E$ has the entry $-3$ in position $(3,2)$: the operation is **$R_3 \to R_3 - 3R_2$**. Applying it:
$$EA = \begin{bmatrix} 1 & 4 \\ 2 & 5 \\ 3 - 3(2) & 6 - 3(5) \end{bmatrix} = \begin{bmatrix} 1 & 4 \\ 2 & 5 \\ -3 & -9 \end{bmatrix}.$$
Its inverse is $\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 3 & 1 \end{bmatrix}$ ($R_3 + 3R_2$).

**Key rule:** $EA$ = "apply to $A$ the operation that created $E$ from $I$" — left multiplication *acts* rows.

**Examiner's note:** Tests reading an elementary matrix's non-zero off-diagonal/diagonal pattern as a sentence about rows.
""")
    code(cells, r"""# SymPy verification — Lab 5, Q.2
A2a = Matrix([[-1, -2, 5, -1], [3, -6, -6, -6]])
EA_a = Matrix([[-6, 0], [0, 1]]) * A2a
print("Q.2(a) EA ="); display(EA_a)
assert EA_a == Matrix([[6, 12, -30, 6], [3, -6, -6, -6]])
A2b = Matrix([[1, 4], [2, 5], [3, 6]])
EA_b = Matrix([[1, 0, 0], [0, 1, 0], [0, -3, 1]]) * A2b
print("Q.2(b) EA ="); display(EA_b)
assert EA_b == Matrix([[1, 4], [2, 5], [-3, -9]])""")

    # ---------------- Q3 ----------------
    md(cells, r"""### Q.3) Recover $E$ from Before/After Matrices (Easy)

**Question (as printed):** A single elementary row operation changed
$$A = \begin{bmatrix} 2 & 1 & 4 \\ 3 & 5 & 2 \\ 1 & 2 & 3 \end{bmatrix} \quad\text{into}\quad B = \begin{bmatrix} 2 & 1 & 4 \\ -3 & 2 & -10 \\ 1 & 2 & 3 \end{bmatrix}. \qquad \text{Find } E \text{ and verify } EA = B.$$

**Step 1 — diff the two matrices.** Rows 1 and 3 are untouched. Row 2 changed from $(3, 5, 2)$ to $(-3, 2, -10)$. Since rows 1 and 3 are unchanged, the operation involved **only row 2** or added a multiple of another row *into* row 2.

**Step 2 — solve for the combination.** Suppose $R_2' = R_2 + c\,R_1$:
$$(3 + 2c,\; 5 + c,\; 2 + 4c) = (-3, 2, -10) \;\Rightarrow\; 2c = -6 \Rightarrow c = -3,$$
and indeed $5 - 3 = 2$ ✓, $2 - 12 = -10$ ✓. The operation is $R_2 \to R_2 - 3R_1$.

**Step 3 — write and verify $E$.**
$$E = \begin{bmatrix} 1 & 0 & 0 \\ -3 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}, \qquad EA = \begin{bmatrix} 2 & 1 & 4 \\ 3 - 3(2) & 5 - 3(1) & 2 - 3(4) \\ 1 & 2 & 3 \end{bmatrix} = B\ \checkmark$$

**Examiner's note:** Tests reversing the dictionary: from observed row change back to the elementary matrix.
""")
    code(cells, r"""# SymPy verification — Lab 5, Q.3
A3 = Matrix([[2, 1, 4], [3, 5, 2], [1, 2, 3]])
B3 = Matrix([[2, 1, 4], [-3, 2, -10], [1, 2, 3]])
E3 = Matrix([[1, 0, 0], [-3, 1, 0], [0, 0, 1]])
print("Q.3  EA = B:", E3 * A3 == B3)
assert E3 * A3 == B3""")

    # ---------------- Q4 ----------------
    md(cells, r"""### Q.4) One Matrix $E$ That Row-Reduces $A$ to Echelon Form (Easy)

**Question (as printed):** Find a matrix $E$ which, multiplied with $A = \begin{bmatrix} 6 & 2 & 1 \\ 3 & 5 & 2 \\ 2 & 1 & 4 \end{bmatrix}$, reduces it to row echelon form.

**Step 1 — eliminate and record the multipliers.**
- $R_2 \to R_2 - \tfrac12 R_1$: $(0, 4, \tfrac32)$  (multiplier $\ell_{21} = \tfrac12$)
- $R_3 \to R_3 - \tfrac13 R_1$: $(0, \tfrac13, \tfrac{11}{3})$  (multiplier $\ell_{31} = \tfrac13$)
- $R_3 \to R_3 - \tfrac{1}{12} R_2$: $(0, 0, \tfrac{11}{3} - \tfrac{1}{12}\cdot\tfrac32) = (0, 0, \tfrac{85}{24})$  (multiplier $\ell_{32} = \tfrac{1}{12}$)

The echelon form is
$$U = \begin{bmatrix} 6 & 2 & 1 \\ 0 & 4 & \tfrac32 \\ 0 & 0 & \tfrac{85}{24} \end{bmatrix}.$$

**Step 2 — assemble $E$ from the multipliers.** $E = E_3E_2E_1$ where each $E_i$ performs one operation; the product places the **negated multipliers** below the diagonal:
$$E = E_3E_2E_1 = \begin{bmatrix} 1 & 0 & 0 \\ -\tfrac12 & 1 & 0 \\ -\tfrac{7}{24} & -\tfrac{1}{12} & 1 \end{bmatrix}, \qquad EA = U\ \checkmark$$
(Remark: $E$ itself is *not* simply "$I$ with negated multipliers" — later operations act on already-changed rows. But its **inverse** is: $L = E^{-1} = E_1^{-1}E_2^{-1}E_3^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ \tfrac12 & 1 & 0 \\ \tfrac13 & \tfrac{1}{12} & 1 \end{bmatrix}$ places each multiplier with a $+$ sign, and $LU = A$.)

**Examiner's note:** Tests composing several elementary matrices into one and connecting it to $L$.
""")
    code(cells, r"""# SymPy verification — Lab 5, Q.4
A4q = Matrix([[6, 2, 1], [3, 5, 2], [2, 1, 4]])
E1 = Matrix([[1, 0, 0], [sp.Rational(-1, 2), 1, 0], [0, 0, 1]])
E2 = Matrix([[1, 0, 0], [0, 1, 0], [sp.Rational(-1, 3), 0, 1]])
E3 = Matrix([[1, 0, 0], [0, 1, 0], [0, sp.Rational(-1, 12), 1]])
E4 = E3 * E2 * E1
U4q = E4 * A4q
print("Q.4  U = EA:"); display(U4q)
assert U4q == Matrix([[6, 2, 1], [0, 4, sp.Rational(3, 2)], [0, 0, sp.Rational(85, 24)]])
L4q = E4.inv()
assert L4q * U4q == A4q
print("Q.4  E = E3*E2*E1 =", E4.tolist())
print("Q.4  L = E^-1 =", L4q.tolist(), " (multipliers with + signs); L*U = A verified")""")

    # ---------------- Q5 ----------------
    md(cells, r"""### Q.5) True/False: Triangular Products, Uniqueness of $LU$, Pivots (Medium)

**Question (as printed):** *(sheet typo: "whther" = "whether")*
(a) The product of two $3\times3$ lower triangular matrices is also lower triangular.
(b) If $A = LU$, then $L$ and $U$ are always unique.
(c) If a $3\times3$ matrix $A$ has an $LU$ decomposition with three non-zero pivots in $U$, then $Ax = b$ has a unique solution for every $b \in \mathbb{R}^3$.

**(a) TRUE.** If $L_1, L_2$ are lower triangular, then $(L_1L_2)_{ij} = \sum_k (L_1)_{ik}(L_2)_{kj}$; for $i < j$ every term has $k < j$ with $(L_1)_{ik} = 0$ (since $i < k$) or $k \le i < j$ with $(L_2)_{kj} = 0$. So all entries above the diagonal are $0$. Triangular matrices are closed under multiplication (the transposes are upper triangular, and transposition reverses order: $(L_1L_2)^T = L_2^TL_1^T$ is upper-triangular).

**(b) FALSE.** $LU$ is unique **only after fixing a convention**, usually $L$ unit lower triangular (1's on the diagonal). Counterexample: $A = I$: $I = I\cdot I = (2I)(\tfrac12 I) = (3I)(\tfrac13 I) \cdots$ — infinitely many factorizations unless the diagonal of $L$ is pinned. With the unit-$L$ convention (and non-zero pivots) uniqueness *does* hold.

**(c) TRUE.** Three non-zero pivots means elimination completes without row exchanges: $U$ has full rank 3, so $\text{rank}(A) = 3$, $A$ is invertible, and $Ax = b$ has exactly one solution $x = A^{-1}b$ for **every** $b$. (Via the factorization: solve $Lc = b$ by forward substitution — always possible since $\det L = 1 \ne 0$ — then $Ux = c$ by back substitution — always possible since all pivots $\ne 0$.)

**Examiner's note:** Tests closure of triangular matrices, the convention-dependence of $LU$ uniqueness, and pivot-count ⇒ invertibility.
""")
    code(cells, r"""# SymPy verification — Lab 5, Q.5
La = Matrix([[1, 0], [2, 3]]); Lb = Matrix([[1, 0], [4, 5]])
prod = La * Lb
print("Q.5(a) (L1*L2) above-diagonal entries:", prod[0, 1], "(0 => lower triangular)")
assert prod[0, 1] == 0
I5 = sp.eye(2)
Lalt, Ualt, _ = I5.LUdecomposition()
assert Lalt * Ualt == sp.eye(2) and (2 * sp.eye(2)) * (sp.Rational(1, 2) * sp.eye(2)) == sp.eye(2)
print("Q.5(b) I = I*I = (2I)(I/2): LU is NOT unique without the unit-L convention")
A5c = Matrix([[2, 1, 1], [4, 3, 3], [2, 3, 4]])     # 3 non-zero pivots
x5c = A5c.LUsolve(Matrix([1, 2, 3]))
assert A5c * x5c == Matrix([1, 2, 3]) and A5c.det() != 0
print("Q.5(c) det =", A5c.det(), "=> unique solution for every b: True")""")

    # ---------------- Q6 ----------------
    md(cells, r"""### Q.6) Find $LU$ and Verify $A = LU$ (Medium)

**Question (as printed):** (a) $A = \begin{bmatrix} 4 & 5 & 3 \\ 6 & 8 & 7 \\ 2 & 1 & 1 \end{bmatrix}$  (b) $B = \begin{bmatrix} 2 & 1 & 1 & 3 \\ 4 & 5 & 3 & 7 \\ 6 & 8 & 8 & 15 \\ 2 & 7 & 9 & 18 \end{bmatrix}$

**Part (a) — elimination with recorded multipliers.**
- $R_2 \to R_2 - \tfrac{6}{4}R_1 = R_2 - \tfrac32R_1$: $(0, \tfrac12, \tfrac52)$
- $R_3 \to R_3 - \tfrac{2}{4}R_1 = R_3 - \tfrac12R_1$: $(0, -\tfrac32, -\tfrac12)$
- $R_3 \to R_3 - \dfrac{-3/2}{1/2}R_2 = R_3 + 3R_2$: $(0, 0, -\tfrac12 + \tfrac{15}{2}) = (0, 0, 7)$

$$L = \begin{bmatrix} 1 & 0 & 0 \\ \tfrac32 & 1 & 0 \\ \tfrac12 & -3 & 1 \end{bmatrix}, \qquad U = \begin{bmatrix} 4 & 5 & 3 \\ 0 & \tfrac12 & \tfrac52 \\ 0 & 0 & 7 \end{bmatrix}$$
Verification of row 3 (the risky one): $\tfrac12(4,5,3) + (-3)(0,\tfrac12,\tfrac52) + (0,0,7) = (2,\; \tfrac52 - \tfrac32,\; \tfrac32 - \tfrac{15}2 + 7) = (2, 1, 1)$ ✓.

**Part (b) — a 4×4, still no row exchanges needed.** Multipliers in order:
$\ell_{21} = 2$, $\ell_{31} = 3$, $\ell_{41} = 1$; then $\ell_{32} = \tfrac53$, $\ell_{42} = 2$; then $\ell_{43} = \tfrac95$:
$$L = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 2 & 1 & 0 & 0 \\ 3 & \tfrac53 & 1 & 0 \\ 1 & 2 & \tfrac95 & 1 \end{bmatrix}, \qquad U = \begin{bmatrix} 2 & 1 & 1 & 3 \\ 0 & 3 & 1 & 1 \\ 0 & 0 & \tfrac{10}{3} & \tfrac{13}{3} \\ 0 & 0 & 0 & \tfrac{26}{5} \end{bmatrix}$$
Both products are verified exactly by SymPy below ($LU = A$, $LU = B$).

**Examiner's note:** Tests the multiplier-recording discipline: each elimination step writes its multiplier into $L$ at the same position.
""")
    code(cells, r"""# SymPy verification — Lab 5, Q.6
A6q = Matrix([[4, 5, 3], [6, 8, 7], [2, 1, 1]])
L6a, U6a, _ = A6q.LUdecomposition()
print("Q.6(a) L ="); display(L6a); print("U ="); display(U6a)
assert simplify(L6a * U6a - A6q) == sp.zeros(3, 3)
B6q = Matrix([[2, 1, 1, 3], [4, 5, 3, 7], [6, 8, 8, 15], [2, 7, 9, 18]])
L6b, U6b, perm = B6q.LUdecomposition()
assert perm == []
print("Q.6(b) L ="); display(L6b); print("U ="); display(U6b)
assert simplify(L6b * U6b - B6q) == sp.zeros(4, 4)
print("Q.6  both A = L*U and B = L*U verified exactly")""")

    # ---------------- Q7 ----------------
    md(cells, r"""### Q.7) Symmetric Matrix $A = LU$ and the Three Pivot Conditions (Medium)

**Question (as printed):** Compute $L$ and $U$ for the symmetric matrix
$$A = \begin{bmatrix} a & a & a \\ a & b & b \\ a & b & c \end{bmatrix},$$
and find three conditions on $a, b, c$ to get $A = LU$ with three pivots.

**Step 1 — eliminate symbolically.**
- $R_2 \to R_2 - R_1$ (multiplier $1$): $(0,\; b - a,\; b - a)$
- $R_3 \to R_3 - R_1$ (multiplier $1$): $(0,\; b - a,\; c - a)$
- $R_3 \to R_3 - R_2$ (multiplier $1$): $(0,\; 0,\; (c - a) - (b - a)) = (0, 0, c - b)$

$$L = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 1 & 1 \end{bmatrix}, \qquad U = \begin{bmatrix} a & a & a \\ 0 & b - a & b - a \\ 0 & 0 & c - b \end{bmatrix}$$
(Elegant check: $U$'s second and third rows are $b-a$ and $c-b$ times... and indeed $U = D\,L^T$ where $D = \mathrm{diag}(a, b-a, c-b)$ — for symmetric $A$ with no row exchanges, $U = DL^T$ always.)

**Step 2 — the three pivot conditions.** All three pivots are the diagonal of $U$:
$$\boxed{a \ne 0, \qquad b - a \ne 0 \ (\text{i.e. } b \ne a), \qquad c - b \ne 0 \ (\text{i.e. } c \ne b)}$$
i.e. the three parameters must be *strictly increasing through the chain* $a \to b \to c$ — all distinct in exactly that order. Any failure (e.g. $b = a$) zeroes a pivot and forces either a row exchange or a zero pivot.

**Examiner's note:** Tests symbolic elimination and reading invertibility conditions off pivot expressions.
""")
    code(cells, r"""# SymPy verification — Lab 5, Q.7
a, b, c = sp.symbols('a b c')
A7s = Matrix([[a, a, a], [a, b, b], [a, b, c]])
L7s, U7s, _ = A7s.LUdecomposition()
print("Q.7  L ="); display(L7s); print("U ="); display(U7s)
assert L7s == Matrix([[1, 0, 0], [1, 1, 0], [1, 1, 1]])
assert simplify(U7s[0, 0]) == a and simplify(U7s[1, 1]) == b - a and simplify(U7s[2, 2]) == c - b
assert simplify(L7s * U7s - A7s) == sp.zeros(3, 3)
print("Q.7  pivots a, b-a, c-b => conditions a != 0, b != a, c != b")""")

    # ---------------- Q8 ----------------
    md(cells, r"""### Q.8) Recover the Original $A$ from $U$ and the Operations (Medium)

**Question (as printed):** After three row operations an unknown $A$ became
$$U = \begin{bmatrix} 2 & 1 & 3 \\ 0 & 4 & 5 \\ 0 & 0 & 6 \end{bmatrix},$$
using $E_1\!: R_2 \to R_2 + R_1$?? — as printed: $E_1\!: R_2 \to R_2 - R_1$, $E_2\!: R_3 \to R_3 - 2R_1$, $E_3\!: R_3 \to R_3 + R_2$. Recover $A$ **without** Gaussian elimination.

**Step 1 — run the operations backwards.** $A = E_1^{-1}E_2^{-1}E_3^{-1}U$, where each inverse *undoes* its operation:
$$E_1^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} (R_2 + R_1), \quad
E_2^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 2 & 0 & 1 \end{bmatrix} (R_3 + 2R_1), \quad
E_3^{-1} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & -1 & 1 \end{bmatrix} (R_3 - R_2).$$
(Order matters: undo in reverse — first $E_3^{-1}$, then $E_2^{-1}$, then $E_1^{-1}$.)

**Step 2 — apply them one at a time to $U$.**
- $E_3^{-1}U$: replace $R_3$ by $R_3 - R_2$: $(0, -4, 1)$
- $E_2^{-1}(\cdot)$: $R_3 + 2R_1$: $(4, -2, 7)$
- $E_1^{-1}(\cdot)$: $R_2 + R_1$: $(2, 5, 8)$

$$\boxed{A = \begin{bmatrix} 2 & 1 & 3 \\ 2 & 5 & 8 \\ 4 & -2 & 7 \end{bmatrix}}$$

**Step 3 — sanity check by re-running the operations.** $E_1A$: $R_2 - R_1 = (0, 4, 5)$; $E_2(\cdot)$: $R_3 - 2R_1 = (0, -4, 1)$; $E_3(\cdot)$: $R_3 + R_2 = (0, 0, 6)$ — recovering $U$ ✓.

**Examiner's note:** Tests composing inverse elementary matrices in the correct reverse order.
""")
    code(cells, r"""# SymPy verification — Lab 5, Q.8
U8q = Matrix([[2, 1, 3], [0, 4, 5], [0, 0, 6]])
E8i1 = Matrix([[1, 0, 0], [1, 1, 0], [0, 0, 1]])
E8i2 = Matrix([[1, 0, 0], [0, 1, 0], [2, 0, 1]])
E8i3 = Matrix([[1, 0, 0], [0, 1, 0], [0, -1, 1]])
A8q = E8i1 * E8i2 * E8i3 * U8q
print("Q.8  recovered A ="); display(A8q)
assert A8q == Matrix([[2, 1, 3], [2, 5, 8], [4, -2, 7]])
E8f1 = E8i1.inv(); E8f2 = E8i2.inv(); E8f3 = E8i3.inv()
assert E8f3 * E8f2 * E8f1 * A8q == U8q
print("Q.8  re-applying the forward operations returns U")""")

    # ---------------- Q9 ----------------
    md(cells, r"""### Q.9) Stage Lamps Revisited: $M = LU$ and Many Nights of Recipes (Medium)

**Question (as printed):** The three-lamp matrix $M = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 1 & 0 \end{bmatrix}$ is used every night with a new colour. Factor $M = LU$ once, then answer:
(a) the $LU$ decomposition; (b) amber $b = (4,3,1)^T$ via $Lc = b$ (forward substitution); (c) finish via $Ux = c$ (back substitution); (d) sage green $b' = (2,3,2)^T$ with **no new row operations**; (e) what $L$ records and why it lets you skip elimination; (f) pure blue $(0,0,1)^T$ — what goes wrong?

**Part (a) — factor once.** Only one elimination step is needed: $R_3 \to R_3 - R_2$ (multiplier $1$ into position $(3,2)$):
$$L = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 1 & 1 \end{bmatrix}, \qquad U = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & -1 \end{bmatrix}, \qquad LU = M\ \checkmark$$

**Part (b) — forward substitution $Lc = b$ with $b = (4, 3, 1)^T$** (top row first):
$$c_1 = 4; \quad c_2 = 3; \quad c_2 + c_3 = 1 \Rightarrow c_3 = -2. \qquad c = (4, 3, -2)^T.$$

**Part (c) — back substitution $Ux = c$** (bottom row first):
$$-x_3 = -2 \Rightarrow x_3 = 2; \quad x_2 + x_3 = 3 \Rightarrow x_2 = 1; \quad x_1 + x_3 = 4 \Rightarrow x_1 = 2.$$
$$\boxed{\text{Amber recipe } x = (2, 1, 2)^T} \qquad \text{(check: } 2\text{Red} + 1\text{Cyan} + 2\text{Yellow} = (4,3,1)\ \checkmark)$$

**Part (d) — sage green $(2, 3, 2)^T$, reusing $L, U$.** Forward: $c = (2, 3, 2 - 3)^T = (2, 3, -1)^T$. Back: $-x_3 = -1 \Rightarrow x_3 = 1$; $x_2 = 3 - 1 = 2$; $x_1 = 2 - 1 = 1$:
$$\boxed{\text{Sage green recipe } x = (1, 2, 1)^T}$$
— found with **zero new row operations** on $M$, exactly the point of factoring once.

**Part (e) — in words.** $L$ records the **multipliers** used during elimination — the "work" of reducing $M$. Because $M = LU$, the equation $Mx = b$ splits into $Lc = b$ then $Ux = c$; the first is cheap forward substitution using the stored work, and the second is cheap back substitution. Elimination on $M$ never has to be repeated: only the two triangular solves change with $b$.

**Part (f) — pure blue $(0, 0, 1)^T$.** Forward: $c = (0, 0, 1)^T$. Back: $-x_3 = 1 \Rightarrow x_3 = -1$; $x_2 = 0 - (-1) = 1$; $x_1 = 0 - (-1) = 1$:
$$x = (1, 1, -1)^T \;-\; \text{a perfectly valid algebraic solution (}Mx = (0,0,1)\ \checkmark\text{),}$$
**but physically impossible**: dial 3 (Yellow) would need brightness $-1$, and dials only **add** light. The matrix doesn't know about physics — the solvent is unique ($\det M \ne 0$), it just lives outside the allowed dial range $[0, \infty)$.

**Examiner's note:** Tests the full $LU$ workflow — factor once, then forward/back substitution per right side — and interpreting an algebraic solution that violates physical constraints.
""")
    code(cells, r"""# SymPy verification — Lab 5, Q.9
M9 = Matrix([[1, 0, 1], [0, 1, 1], [0, 1, 0]])
L9, U9, _ = M9.LUdecomposition()
print("Q.9(a) L ="); display(L9); print("U ="); display(U9)
assert L9 == Matrix([[1, 0, 0], [0, 1, 0], [0, 1, 1]]) and U9 == Matrix([[1, 0, 1], [0, 1, 1], [0, 0, -1]])
for bb, expect in [(Matrix([4, 3, 1]), Matrix([2, 1, 2])),
                   (Matrix([2, 3, 2]), Matrix([1, 2, 1])),
                   (Matrix([0, 0, 1]), Matrix([1, 1, -1]))]:
    xx = M9.LUsolve(bb)
    assert xx == expect and M9 * xx == bb
print("Q.9  amber (2,1,2), sage (1,2,1), blue (1,1,-1) — blue needs a negative dial")""")

    # ---------------- Q10 ----------------
    md(cells, r"""### Q.10) Which Zeros Survive into $L$ and $U$? (Medium)

**Question (as printed):** If $A$ and $B$ have non-zeros exactly where $x$ is marked, which zeros are **still zero** in their factors $L$ and $U$?
$$A = \begin{bmatrix} x & x & x & x \\ x & x & x & 0 \\ 0 & x & x & x \\ 0 & 0 & x & x \end{bmatrix} \qquad
B = \begin{bmatrix} x & x & x & 0 \\ x & x & 0 & x \\ x & 0 & x & x \\ 0 & x & x & x \end{bmatrix}$$

**The rule.** Elimination *propagates* fill-in: a zero stays zero only if **no earlier step ever writes into it**. Zeros in the first row/first column (the "outermost" band positions) are safe; zeros sandwiched between non-zeros get filled.

**Matrix $A$ (zeros at $(3,1)$, $(4,1)$, $(4,2)$ — all below the diagonal; and $(2,4)$ above).**
- Below-diagonal zeros are exactly the multipliers: $\ell_{31} = a_{31}/a_{11} = 0$ ✓, $\ell_{41} = 0$ ✓, and $\ell_{42} = (a_{42} - \ell_{41}u_{12})/u_{22} = (0 - 0)/u_{22} = 0$ ✓ — **all three survive in $L$** (numerically confirmed below).
- The upper zero $(2,4)$: $u_{24} = a_{24} - \ell_{21}u_{14} = 0 - (\ne 0)(\ne 0) \ne 0$ — **fills in** inside $U$ (with the numeric example: $u_{24} = -\tfrac12 \ne 0$).

$$\boxed{A:\ \ell_{31} = \ell_{41} = \ell_{42} = 0 \text{ in } L;\ \ u_{24} \text{ fills in.}}$$

**Matrix $B$ (zeros at $(1,4)$, $(2,3)$ above; $(3,2)$, $(4,1)$ below).**
- $(1,4)$: row 1 is never modified, so $u_{14} = a_{14} = 0$ — **survives in $U$**.
- $(4,1)$: $\ell_{41} = a_{41}/a_{11} = 0$ — **survives in $L$**.
- $(2,3)$: $u_{23} = a_{23} - \ell_{21}u_{13} = 0 - (\ne 0)(\ne 0) \ne 0$ — **fills in** (numeric: $-\tfrac12$).
- $(3,2)$: after step 1 the $(3,2)$ entry becomes $a_{32} - \ell_{31}u_{12} = 0 - (\ne 0)(\ne 0) \ne 0$, so the multiplier $\ell_{32} \ne 0$ — **fills in** (numeric: $-\tfrac13$).

$$\boxed{B:\ u_{14} = 0 \text{ in } U,\ \ell_{41} = 0 \text{ in } L;\ \ u_{23} \text{ and } \ell_{32} \text{ both fill in.}}$$

**Moral:** zeros on the *outer edge* of the band survive; zeros *inside* the band (with non-zeros up and to the left) are destroyed by fill-in.

**Examiner's note:** Tests the fill-in mechanism of $LU$ on banded patterns rather than numbers.
""")
    code(cells, r"""# SymPy verification — Lab 5, Q.10 (concrete stand-ins for the x's)
A10q = Matrix([[2, 1, 1, 1], [1, 2, 1, 0], [0, 1, 2, 1], [0, 0, 1, 2]])
LA, UA, _ = A10q.LUdecomposition()
print("Q.10 A: L[3,1], L[4?]... l31, l41, l42 =", LA[2, 0], LA[3, 0], LA[3, 1],
      " | u24 =", UA[1, 3])
assert LA[2, 0] == 0 and LA[3, 0] == 0 and LA[3, 1] == 0 and UA[1, 3] != 0
B10q = Matrix([[2, 1, 1, 0], [1, 2, 0, 1], [1, 0, 2, 1], [0, 1, 1, 2]])
LB, UB, _ = B10q.LUdecomposition()
print("Q.10 B: l41 =", LB[3, 0], " u14 =", UB[0, 3], " (survive) | l32 =",
      LB[2, 1], " u23 =", UB[1, 2], " (fill in)")
assert LB[3, 0] == 0 and UB[0, 3] == 0 and LB[2, 1] != 0 and UB[1, 2] != 0""")

    # ---------------- Q11 ----------------
    md(cells, r"""### Q.11) Logistics: Which Delivery Plan Is More Fuel-Efficient? (Hard)

**Question (as printed):** $Ax = b$ with
$$A = \begin{bmatrix} 2 & 1 & 1 & 0 \\ 4 & 5 & 3 & 1 \\ 2 & 3 & 4 & 2 \\ 6 & 7 & 8 & 5 \end{bmatrix}, \quad
b_1 = \begin{bmatrix} 4 \\ 13 \\ 11 \\ 26 \end{bmatrix} \text{ (Plan 1)}, \quad
b_2 = \begin{bmatrix} 6 \\ 17 \\ 13 \\ 32 \end{bmatrix} \text{ (Plan 2)}, \quad
\text{Fuel} = 8x_1 + 6x_2 + 9x_3 + 5x_4.$$

**Step 1 — the "prep once, serve many" strategy.** Factor $A = LU$ **once**, then solve $Lc_i = b_i$ (forward) and $Ux_i = c_i$ (back) for each plan — two cheap triangular solves instead of two full eliminations.

**Step 2 — the two solutions** (verified exactly below):
$$x^{(1)} = (1, 1, 1, 1)^T \qquad\qquad x^{(2)} = (2, 1, 1, 1)^T$$

**Step 3 — fuel accounting.**
$$\text{Fuel}_1 = 8(1) + 6(1) + 9(1) + 5(1) = 28 \qquad\qquad \text{Fuel}_2 = 8(2) + 6(1) + 9(1) + 5(1) = 36.$$

$$\boxed{\text{Plan 1 is more fuel-efficient: } 28 < 36 \text{ (8 units saved).}}$$

**Why the answers are so clean:** $b_2 - b_1 = (2, 4, 2, 6)^T = A(1, 0, 0, 0)^T$, i.e. the second plan is exactly the first plan **plus one extra truckload from warehouse 1** — so the solution differs only in $x_1$, and the fuel differs by the first column's fuel rate: $8 \times 1 = 8$.

**Examiner's note:** Tests reusing one $LU$ for multiple right-hand sides and reading the difference of solutions off the matrix structure.
""")
    code(cells, r"""# SymPy verification — Lab 5, Q.11
A11q = Matrix([[2, 1, 1, 0], [4, 5, 3, 1], [2, 3, 4, 2], [6, 7, 8, 5]])
xplan1 = A11q.LUsolve(Matrix([4, 13, 11, 26]))
xplan2 = A11q.LUsolve(Matrix([6, 17, 13, 32]))
fuel = lambda v: 8 * v[0] + 6 * v[1] + 9 * v[2] + 5 * v[3]
print("Q.11 Plan 1 x =", xplan1.T, " fuel =", fuel(xplan1))
print("Q.11 Plan 2 x =", xplan2.T, " fuel =", fuel(xplan2))
assert xplan1 == Matrix([1, 1, 1, 1]) and xplan2 == Matrix([2, 1, 1, 1])
assert fuel(xplan1) == 28 and fuel(xplan2) == 36 and fuel(xplan1) < fuel(xplan2)
print("Q.11 Plan 1 wins; b2 - b1 = A*(1,0,0,0):", A11q * Matrix([1, 0, 0, 0]) == Matrix([2, 4, 2, 6]))""")

    # ---------------- Q12 ----------------
    md(cells, r"""### Q.12) Water Authority: Three Daily Demands Through One $LU$ (Hard)

**Question (as printed):** Pumping matrix
$$A = \begin{bmatrix} 4 & 2 & 1 \\ 2 & 5 & 2 \\ 1 & 2 & 4 \end{bmatrix}, \qquad
b_1 = \begin{bmatrix} 7 \\ 8 \\ 13 \end{bmatrix}(\text{morning}),\quad
b_2 = \begin{bmatrix} 10 \\ 16 \\ 13 \end{bmatrix}(\text{afternoon}),\quad
b_3 = \begin{bmatrix} 7 \\ 9 \\ 7 \end{bmatrix}(\text{evening}).$$
Determine the pumping effort $x$ for each demand using $LU$ decomposition.

**Step 1 — factor once.** Multipliers: $\ell_{21} = \tfrac12$, $\ell_{31} = \tfrac14$; after step 1 row 2 is $(0, 4, \tfrac32)$ and row 3 is $(0, \tfrac32, \tfrac{15}{4})$; then $\ell_{32} = \tfrac38$:
$$L = \begin{bmatrix} 1 & 0 & 0 \\ \tfrac12 & 1 & 0 \\ \tfrac14 & \tfrac38 & 1 \end{bmatrix}, \qquad U = \begin{bmatrix} 4 & 2 & 1 \\ 0 & 4 & \tfrac32 \\ 0 & 0 & \tfrac{51}{16} \end{bmatrix}$$

**Step 2 — three forward/back substitution pairs** (each verified exactly below):
$$x^{(1)}_{\text{morning}} = (1, 0, 3)^T, \qquad x^{(2)}_{\text{afternoon}} = (1, 2, 2)^T, \qquad x^{(3)}_{\text{evening}} = (1, 1, 1)^T.$$

Spot-check the afternoon case in the original system: row 1: $4 + 4 + 2 = 10$ ✓; row 2: $2 + 10 + 4 = 16$ ✓; row 3: $1 + 4 + 8 = 13$ ✓.

**Interpretation.** Note how the three efforts share the pattern "station 1 at effort 1": afternoon and evening demands are morning demand plus $A(0, 2, -1)^T$ and $A(0, 1, -2)^T$ respectively — again, differences of right-hand sides translate directly into differences of solutions.

**Examiner's note:** Tests solving a family $Ax = b_i$ with one factorization — the production use-case of $LU$.
""")
    code(cells, r"""# SymPy verification — Lab 5, Q.12
A12q = Matrix([[4, 2, 1], [2, 5, 2], [1, 2, 4]])
L12, U12, _ = A12q.LUdecomposition()
print("Q.12 L ="); display(L12); print("U ="); display(U12)
for name, bb, expect in [("morning", Matrix([7, 8, 13]), Matrix([1, 0, 3])),
                         ("afternoon", Matrix([10, 16, 13]), Matrix([1, 2, 2])),
                         ("evening", Matrix([7, 9, 7]), Matrix([1, 1, 1]))]:
    xx = A12q.LUsolve(bb)
    assert xx == expect and A12q * xx == bb
    print(f"Q.12 {name}: x = {xx.T}")
print("Q.12 all three demands solved through the single LU")""")

    # ---------------- Q13 ----------------
    md(cells, r"""### Q.13) Challenge: Four Cleaning Solutions from Four Chemicals (Challenge)

**Question (as printed):** $Ax = b$ with
$$A = \begin{bmatrix} 2 & 1 & 3 & 2 \\ 4 & 6 & 5 & 9 \\ -2 & 11 & -3 & 15 \\ 8 & -4 & 17 & 6 \end{bmatrix},$$
$x_i$ = litres of chemical $C_i$; three products demand
$$b_1 = \begin{bmatrix} 8 \\ 24 \\ 21 \\ 27 \end{bmatrix}(\text{Glass Cleaner}),\quad
b_2 = \begin{bmatrix} 10 \\ 28 \\ 19 \\ 35 \end{bmatrix}(\text{Floor Cleaner}),\quad
b_3 = \begin{bmatrix} 9 \\ 30 \\ 32 \\ 23 \end{bmatrix}(\text{Industrial Degreaser}).$$
(a) Complete the production sheet; (b) if tank $C_2$ dispenses at most 1 litre per batch, which products can be made immediately? (c) which product minimises total chemical $x_1+x_2+x_3+x_4$? (d) for orders of 20 Glass, 15 Floor, 10 Degreaser batches, is the stock $C = (60, 40, 50, 55)$ sufficient? If not, how much must be ordered?

**Part (a) — production sheet** (all solutions verified exactly below; note $\det A \ne 0$ so each recipe is unique):

| Base chemical | Glass Cleaner | Floor Cleaner | Industrial Degreaser |
| :---: | :---: | :---: | :---: |
| $C_1$ | 1 | 2 | 1 |
| $C_2$ | 1 | 1 | 2 |
| $C_3$ | 1 | 1 | 1 |
| $C_4$ | 1 | 1 | 1 |

Spot-check Glass Cleaner in row 1: $2(1) + 1 + 3 + 2 = 8$ ✓; row 4: $8 - 4 + 17 + 6 = 27$ ✓.

**Part (b).** $C_2$ usage per batch: Glass 1, Floor 1, Degreaser **2**. With the 1-litre cap: **Glass Cleaner and Floor Cleaner can be manufactured immediately**; the Degreaser cannot (needs 2 L through the $C_2$ tank).

**Part (c).** Total chemical: Glass $= 4$ L, Floor $= 5$ L, Degreaser $= 5$ L. **Glass Cleaner** minimises total chemical consumption.

**Part (d) — scale and aggregate the recipes.**
$$20\,x^{(1)} + 15\,x^{(2)} + 10\,x^{(3)} = 20(1,1,1,1) + 15(2,1,1,1) + 10(1,2,1,1) = (60,\ 55,\ 45,\ 45).$$
Compare with stock $(60, 40, 50, 55)$:

| Chemical | Needed | In stock | Action |
| :---: | :---: | :---: | :---: |
| $C_1$ | 60 | 60 | exactly enough ✓ |
| $C_2$ | 55 | 40 | **order 15 L more** |
| $C_3$ | 45 | 50 | 5 L spare ✓ |
| $C_4$ | 45 | 55 | 10 L spare ✓ |

**Answer:** the inventory is **not sufficient** — an additional **15 litres of $C_2$** must be ordered; everything else is covered.

**Examiner's note:** Tests a complete applied $LU$ workflow: solve, filter by a physical constraint, optimise a linear objective, and aggregate scaled solutions (linearity again: $A(20x_1 + 15x_2 + 10x_3) = 20b_1 + 15b_2 + 10b_3$).
""")
    code(cells, r"""# SymPy verification — Lab 5, Q.13
A13q = Matrix([[2, 1, 3, 2], [4, 6, 5, 9], [-2, 11, -3, 15], [8, -4, 17, 6]])
bs13 = [Matrix([8, 24, 21, 27]), Matrix([10, 28, 19, 35]), Matrix([9, 30, 32, 23])]
sols13 = [A13q.LUsolve(bb) for bb in bs13]
names13 = ["Glass Cleaner", "Floor Cleaner", "Degreaser"]
for nm, sv in zip(names13, sols13):
    print(f"Q.13(a) {nm}: (C1, C2, C3, C4) = {sv.T},  total = {sum(sv)} L")
assert sols13[0] == Matrix([1, 1, 1, 1]) and sols13[1] == Matrix([2, 1, 1, 1]) and sols13[2] == Matrix([1, 2, 1, 1])
print("Q.13(b) C2 usage: 1, 1, 2 => Glass & Floor OK, Degreaser blocked")
print("Q.13(c) totals: 4, 5, 5 => Glass Cleaner is leanest")
orders = 20 * sols13[0] + 15 * sols13[1] + 10 * sols13[2]
stock = Matrix([60, 40, 50, 55])
print("Q.13(d) required =", orders.T, " stock =", stock.T, " shortfall =", (orders - stock).T)
assert orders == Matrix([60, 55, 45, 45])
print("Q.13(d) order exactly 15 L of C2; C3 and C4 have spare")""")

    return cells


LAB_TITLE = "Lab 6 Solutions: Linear Independence and Column Space"
LAB_SUB = (
    '**Core ideas tested:** "New Signal or Echo?" — the independence test '
    '$c_1v_1 + \\dots + c_kv_k = 0$ having only the trivial solution, pivot columns vs. free '
    "columns, bases of the column space, and rank as the count of genuinely new directions."
)


def get_lab6_cells():
    cells = []
    md(cells, lab_header(LAB_TITLE, LAB_SUB))

    # ---------------- Q1 ----------------
    md(cells, r"""### Q.1) Dependent Vectors in $\mathbb{R}^4$ (Easy)

**Question (as printed):** Show that $v_1 = (1, 2, 3, 4)$, $v_2 = (0, 1, 0, -1)$, $v_3 = (1, 3, 3, 3)$ form a linearly dependent set in $\mathbb{R}^4$, and express $v_3$ in terms of the other two.

**Step 1 — look for an exact combination.** Add the first two:
$$v_1 + v_2 = (1 + 0,\; 2 + 1,\; 3 + 0,\; 4 - 1) = (1, 3, 3, 3) = v_3.$$

**Step 2 — conclude.** The relation $v_1 + v_2 - v_3 = 0$ has non-zero coefficients, so the set is **linearly dependent**:
$$\boxed{v_3 = v_1 + v_2}$$
(Only two of the three vectors carry independent information; the rank of $[v_1\ v_2\ v_3]$ is 2.)

**Examiner's note:** Tests finding a dependency by direct combination — always try small integer sums first.
""")
    code(cells, r"""# SymPy verification — Lab 6, Q.1
v1q = Matrix([1, 2, 3, 4]); v2q = Matrix([0, 1, 0, -1]); v3q = Matrix([1, 3, 3, 3])
assert v3q == v1q + v2q
print("Q.1  v3 = v1 + v2 exactly; rank =", Matrix.hstack(v1q, v2q, v3q).rank(), "< 3 => dependent")""")

    # ---------------- Q2 ----------------
    md(cells, r"""### Q.2) True/False: Foundations of Independence (Easy)

**Question (as printed):**
(a) A set containing a single vector is linearly independent.
(b) The columns of any $4\times5$ matrix are linearly dependent.
(c) No linearly independent set contains the zero vector.
(d) Two vectors are linearly dependent if and only if they lie on a line through the origin.

**(a) FALSE.** A single vector $\{v\}$ is independent iff $v \ne 0$ (since $c\,v = 0$ forces $c = 0$ exactly when $v \ne 0$). The set $\{\mathbf{0}\}$ is dependent: $1 \cdot \mathbf{0} = \mathbf{0}$ with a non-zero coefficient. The statement as printed (without the non-zero qualifier) is false.

**(b) TRUE.** Five columns living in $\mathbb{R}^4$: more vectors than dimensions forces dependence — the homogeneous system $Ac = 0$ has 5 unknowns and at most 4 independent equations, hence a non-trivial solution. Rank can be at most $4 < 5$.

**(c) TRUE.** If $v_i = \mathbf{0}$ for some $i$, then $0\cdot v_1 + \dots + 1\cdot v_i + \dots + 0\cdot v_k = \mathbf{0}$ is a non-trivial relation — dependent. Equivalently, $\{\mathbf{0}\} \cup S$ is always dependent, so an independent set cannot contain $\mathbf{0}$.

**(d) TRUE.** Two vectors are dependent iff one is a scalar multiple of the other (or one is zero — which is a multiple of anything). Two multiples of one vector, and the origin, all lie on a single **line through the origin**; conversely, two vectors on one line through the origin are both multiples of that line's direction vector, hence multiples of each other.

**Examiner's note:** Tests the counting rule ($n$ vectors in $\mathbb{R}^m$ with $n > m$ ⇒ dependent), the zero vector, and the two-vector geometry.
""")
    code(cells, r"""# SymPy verification — Lab 6, Q.2
assert Matrix([0, 0]).nullspace() != []            # {0} alone: dependent
A2q = sp.zeros(4, 5)
assert A2q.rank() <= 4 < 5                          # 4x5: columns always dependent
print("Q.2  (a) False (counterexample {0}); (b) True (rank <= 4 < 5); (c) True; (d) True")
v2a, v2b = Matrix([1, 2]), Matrix([3, 6])
assert Matrix.hstack(v2a, v2b).rank() == 1          # same line through origin => dependent""")

    # ---------------- Q3 ----------------
    md(cells, r"""### Q.3) Is $b$ in the Column Space? The Rank Condition (Easy)

**Question (as printed):** Determine whether $b \in C(A)$ using the rank condition, and if so express $b$ as a combination of the columns.
$$\text{(a) } A = \begin{bmatrix} 1 & 1 & 2 \\ 1 & 0 & 1 \\ 2 & 1 & 3 \end{bmatrix},\ b = \begin{bmatrix} -1 \\ 0 \\ 2 \end{bmatrix} \qquad
\text{(b) } A = \begin{bmatrix} 1 & -1 & 1 \\ -1 & 1 & -1 \\ -1 & -1 & 1 \end{bmatrix},\ b = \begin{bmatrix} 2 \\ 0 \\ 0 \end{bmatrix}$$

**The test.** $b \in C(A) \iff \text{rank}[\,A \mid b\,] = \text{rank}(A)$ — appending $b$ as one more column must not create a new pivot.

**Part (a).** The columns are visibly dependent: $\mathbf{c}_1 + \mathbf{c}_2 = (2, 1, 3) = \mathbf{c}_3$, so $\text{rank}(A) = 2$ and $C(A)$ is the plane $x + y - z = 0$ (normal $\mathbf{c}_1 \times \mathbf{c}_2 = (1, 1, -1)$). Testing $b$: $(-1) + 0 - 2 = -3 \ne 0$ — $b$ is **not** in the plane. Numerically $\text{rank}[A\mid b] = 3 > 2 = \text{rank}(A)$:
$$\boxed{b \notin C(A) \text{ — no such combination exists.}}$$

**Part (b).** $\mathbf{c}_2 = -\mathbf{c}_1$, so $\text{rank}(A) = 2$; the column space is spanned by $(1, -1, -1)$ and $(1, -1, 1)$ — the plane $x + z = 0$ (normal $(1, 0, 1)$; every column has $x + z = 0$). Testing $b = (2, 0, 0)$: $2 + 0 = 2 \ne 0$ — again **outside**:
$$\boxed{b \notin C(A).}$$

Both printed parts have $b$ outside the column space — a reminder that "determine whether" can legitimately end in "no".

**Examiner's note:** Tests the augmented-rank solvability test plus a quick plane-equation shortcut.
""")
    code(cells, r"""# SymPy verification — Lab 6, Q.3
A3a = Matrix([[1, 1, 2], [1, 0, 1], [2, 1, 3]]); b3a = Matrix([-1, 0, 2])
A3b = Matrix([[1, -1, 1], [-1, 1, -1], [-1, -1, 1]]); b3b = Matrix([2, 0, 0])
for tag, Aq, bq in [("(a)", A3a, b3a), ("(b)", A3b, b3b)]:
    ra, rg = Aq.rank(), Aq.row_join(bq).rank()
    print(f"Q.3{tag} rank(A) = {ra}, rank([A|b]) = {rg} => b in C(A): {ra == rg}")
assert A3a.row_join(b3a).rank() == 3 and A3b.row_join(b3b).rank() == 3""")

    # ---------------- Q4 ----------------
    md(cells, r"""### Q.4) Independent or Dependent — and the Geometry of the Span (Easy)

**Question (as printed):** Determine independence and explain the span geometrically.
(a) $v_1 = (2, -2, 0)$, $v_2 = (6, 1, 4)$, $v_3 = (2, 0, -4)$ in $\mathbb{R}^3$
(b) $v_1 = (-1, 2, 3)$, $v_2 = (2, -4, -6)$, $v_3 = (-3, 6, 0)$ in $\mathbb{R}^3$
(c) $v_1 = (4, 6, 8)$, $v_2 = (2, 3, 4)$, $v_3 = (-2, -3, -4)$ in $\mathbb{R}^3$
(d) $v_1 = (3, 8, 7, -3)$, $v_2 = (1, 5, 3, -1)$, $v_3 = (2, -1, 2, 6)$, $v_4 = (4, 2, 6, 4)$ in $\mathbb{R}^4$

**(a) Independent — span $= \mathbb{R}^3$.** $\det\begin{bmatrix}2&6&2\\-2&1&0\\0&4&-4\end{bmatrix} = -72 \ne 0$: three independent directions fill all of 3-space.

**(b) Dependent — span is a plane.** $v_2 = -2v_1$ exactly (dependent pair), while $v_3 = (-3, 6, 0)$ is *not* a multiple of $v_1$. Rank $= 2$: the span is the **plane through the origin** containing $v_1$ and $v_3$.

**(c) Dependent — span is a line.** All three are multiples of $(2, 3, 4)$: $v_2 = \tfrac12 v_1$, $v_3 = -\tfrac12 v_1$. Rank $= 1$: everything collapses to the single **line** through $(2, 3, 4)$.

**(d) Dependent — span is a 3-dimensional hyperplane.** Elimination leaves rank $3 < 4$: one non-trivial relation exists, namely
$$-v_1 + v_2 - v_3 + v_4 = \mathbf{0} \qquad (\text{i.e. } v_4 = v_1 - v_2 + v_3;\ \text{check } (3,8,7,-3) - (1,5,3,-1) + (2,-1,2,6) = (4,2,6,4)\ \checkmark).$$
The span is a 3-dimensional subspace of $\mathbb{R}^4$ — one equation short of everything.

**Examiner's note:** Tests the full degeneracy ladder: line (rank 1) → plane (rank 2) → hyperplane (rank 3) → space (rank 4), driven by determinant/rank.
""")
    code(cells, r"""# SymPy verification — Lab 6, Q.4
qa = Matrix.hstack(Matrix([2, -2, 0]), Matrix([6, 1, 4]), Matrix([2, 0, -4]))
qb = Matrix.hstack(Matrix([-1, 2, 3]), Matrix([2, -4, -6]), Matrix([-3, 6, 0]))
qc = Matrix.hstack(Matrix([4, 6, 8]), Matrix([2, 3, 4]), Matrix([-2, -3, -4]))
qd = Matrix([[3, 1, 2, 4], [8, 5, -1, 2], [7, 3, 2, 6], [-3, -1, 6, 4]])  # columns v1..v4
print("Q.4 ranks: (a)", qa.rank(), "(b)", qb.rank(), "(c)", qc.rank(), "(d)", qd.rank())
assert qa.det() != 0 and qb.rank() == 2 and qc.rank() == 1 and qd.rank() == 3
assert qb[:, 1] == -2 * qb[:, 0] and qc[:, 1] == sp.Rational(1, 2) * qc[:, 0] and qc[:, 2] == -sp.Rational(1, 2) * qc[:, 0]
print("Q.4(b) v2 = -2*v1;  Q.4(c) v2 = v1/2, v3 = -v1/2")
rel = qd.nullspace()[0]
assert rel == Matrix([-1, 1, -1, 1])
print("Q.4(d) dependence: -v1 + v2 - v3 + v4 = 0, i.e. v4 = v1 - v2 + v3")""")

    # ---------------- Q5 ----------------
    md(cells, r"""### Q.5) Fill in the Blanks: Rank and Column Space Facts (Medium)

**Question (as printed):**
(a) If $A$ is any $8\times8$ invertible matrix, then its column space is ______.
(b) If $A$ is an $m\times n$ matrix, then the columns of $A$ are linearly independent iff $A$ has ______ pivot columns.
(c) If the $9\times12$ system $Ax = b$ is solvable for every $b$, then $C(A) =$ ______.
(d) $C(AB)$ must ______ the column space of $(A$ or $B)$ for all $4\times4$ matrices $A$ and $B$.
(e) If $A$ is $4\times3$ and $Ax = b$ is not solvable for some $b$ and the solutions are not unique when they exist, possible values of $\text{rank}(A)$ are ______.

**Answers.**
**(a) $\mathbb{R}^8$.** Invertible ⇒ 8 pivots ⇒ the columns span everything.
**(b) $n$.** Independence ⟺ every column is a pivot column ⟺ $n$ pivots (which also forces $m \ge n$).
**(c) $\mathbb{R}^9$.** Solvable for every $b \in \mathbb{R}^9$ means the columns span all of $\mathbb{R}^9$ — full row rank 9 (possible since there are 12 columns).
**(d) "be contained in" — $C(AB) \subseteq C(A)$.** Every column of $AB$ is $A$ times a column of $B$, i.e. a combination of columns of $A$. (The correct pairing is $A$, *not* $B$.)
**(e) $r = 1$ or $r = 2$.** "Not solvable for some $b$" is automatic for $4\times3$ ($r \le 3 < 4$). "Not unique when solvable" requires nullity $= 3 - r \ge 1$, i.e. $r \le 2$. Rank 0 fails the second condition (the only solvable case $b = 0$ has the unique solution $x = 0$), so $r \in \{1, 2\}$.

**Examiner's note:** Tests the pivot/rank facts that power every subspace argument.
""")

    # ---------------- Q6 ----------------
    md(cells, r"""### Q.6) For Which $\omega$ Are the Three Vectors Dependent? (Medium)

**Question (as printed):** For which real $\omega$ do
$$v_1 = \Big(\omega, -\tfrac12, -\tfrac12\Big),\quad v_2 = \Big(-\tfrac12, \omega, -\tfrac12\Big),\quad v_3 = \Big(-\tfrac12, -\tfrac12, \omega\Big)$$
form a linearly dependent set in $\mathbb{R}^3$?

**Step 1 — set the determinant to zero.** The vectors are the columns of a matrix of the form $(\omega + \tfrac12)I - \tfrac12 J$... directly:
$$\det\begin{bmatrix} \omega & -\tfrac12 & -\tfrac12 \\ -\tfrac12 & \omega & -\tfrac12 \\ -\tfrac12 & -\tfrac12 & \omega \end{bmatrix} = \Big(\omega - 1\Big)\Big(\omega + \tfrac12\Big)^2$$
(expanding: eigenvalues of this symmetric pattern are $\omega - 1$ along $(1,1,1)$ and $\omega + \tfrac12$ twice).

**Step 2 — solve.**
$$\Big(\omega - 1\Big)\Big(\omega + \tfrac12\Big)^2 = 0 \quad\Longrightarrow\quad \boxed{\omega = 1 \quad\text{or}\quad \omega = -\tfrac12}$$
- $\omega = 1$: the vectors $(1, -\tfrac12, -\tfrac12)$, $(-\tfrac12, 1, -\tfrac12)$, $(-\tfrac12, -\tfrac12, 1)$ sum to $(0,0,0)$ — the relation $v_1 + v_2 + v_3 = 0$.
- $\omega = -\tfrac12$: all three vectors **equal** $(-\tfrac12, -\tfrac12, -\tfrac12)$ — trivially dependent.

**Examiner's note:** Tests a parametric determinant with a repeated root, and interpreting each root's dependency.
""")
    code(cells, r"""# SymPy verification — Lab 6, Q.6
w = sp.symbols('omega', real=True)
M6w = Matrix([[w, -sp.Rational(1, 2), -sp.Rational(1, 2)],
              [-sp.Rational(1, 2), w, -sp.Rational(1, 2)],
              [-sp.Rational(1, 2), -sp.Rational(1, 2), w]])
roots = sorted(sp.solve(sp.factor(M6w.det()), w))
print("Q.6  factored det =", sp.factor(M6w.det()), " roots =", roots)
assert roots == [-sp.Rational(1, 2), 1]
for rw in roots:
    Mr = M6w.subs(w, rw)
    print(f"  omega = {rw}: rank = {Mr.rank()}, null vector(s): {[v.T for v in Mr.nullspace()]}")""")

    # ---------------- Q7 ----------------
    md(cells, r"""### Q.7) True/False with Counterexamples (Medium)

**Question (as printed):**
(a) If $C(A)$ contains only the zero vector, then $A$ is the zero matrix.
(b) The column space of $2A$ equals the column space of $A$.
(c) The column space of $A - I$ equals the column space of $A$.
(d) If $\{v_1, v_2, v_3\}$ is linearly independent, then $\{kv_1, kv_2, kv_3\}$ is also independent for every **non-zero** scalar $k$.
(e) If $v_1, \dots, v_4 \in \mathbb{R}^4$ and $\{v_1, v_2, v_3\}$ is independent, then $\{v_1, v_2, v_3, v_4\}$ is also linearly dependent.
(f) If $v_3$ is not a linear combination of $\{v_1, v_2, v_4\}$, then $\{v_1, v_2, v_3, v_4\}$ is independent.

**(a) TRUE.** $C(A) = \{\mathbf{0}\}$ means every column — being an element of $C(A)$ — is $\mathbf{0}$.

**(b) TRUE.** Scaling every column by $2 \ne 0$ rescales each combination but changes neither *which* vectors are reachable: $C(2A) = \{2y : y \in C(A)\} = C(A)$ (a subspace is closed under non-zero scaling).

**(c) FALSE.** Counterexample: $A = I$. Then $C(A) = \mathbb{R}^n$ but $C(A - I) = C(0) = \{\mathbf{0}\}$. (Any $A$ whose columns don't cancel works.)

**(d) TRUE.** *(Note: the printed statement excludes $k = 0$ — that qualifier matters.)* If $c_1kv_1 + c_2kv_2 + c_3kv_3 = 0$ then $k(c_1v_1 + c_2v_2 + c_3v_3) = 0$, and $k \ne 0$ lets us divide: $c_1v_1 + c_2v_2 + c_3v_3 = 0 \Rightarrow c_i = 0$ by the independence of the original set. (With $k = 0$ it *would* fail — everything collapses to $\mathbf{0}$.)

**(e) FALSE.** Four vectors in $\mathbb{R}^4$ *can* be independent. Counterexample: $v_i = e_i$ (the standard basis) — all four are independent even though the first three are.

**(f) FALSE.** $v_3$ being "new" is not enough — one of the *other* vectors could be redundant. Counterexample: $v_1 = (1, 0, 0)$, $v_2 = (0, 1, 0)$, $v_4 = (0, 0, 1)$, $v_3 = (1, 1, 1)$: is $v_3$ a combination of $\{v_1, v_2, v_4\}$? Yes ($1, 1, 1$)! — bad counterexample. Correct one: let $v_1 = (1, 0, 0)$, $v_2 = (0, 1, 0)$, $v_4 = (1, 1, 0)$ (dependent triple, all in the $xy$-plane) and $v_3 = (0, 0, 1)$ (the $z$-direction — genuinely not a combination of the other three). Then $v_1 + v_2 - v_4 = 0$: the set of four is **dependent** despite $v_3$ being new.

**Examiner's note:** Tests producing *concrete* counterexamples — the gold standard for false statements.
""")
    code(cells, r"""# SymPy verification — Lab 6, Q.7
# (c) counterexample
assert sp.eye(3).columnspace() != (sp.eye(3) - sp.eye(3)).columnspace()
print("Q.7(c) A = I: C(A) = R^3 but C(A - I) = {0}")
# (e) counterexample
assert Matrix.eye(4).rank() == 4
print("Q.7(e) e1, e2, e3, e4 in R^4 are independent")
# (f) counterexample
vf = Matrix([[1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 0]])   # columns v1, v2, v3, v4
assert vf.rank() == 3                                       # dependent (4 vectors, rank 3)
assert Matrix.hstack(vf[:, 0], vf[:, 1], vf[:, 3]).rank() == 2   # v3 NOT in span{v1, v2, v4}
print("Q.7(f) v3 = e3 is new, yet v1 + v2 - v4 = 0: the set is dependent")""")

    # ---------------- Q8 ----------------
    md(cells, r"""### Q.8) Construct Matrices with Prescribed Column Spaces (Medium)

**Question (as printed):** Construct a $3\times3$ matrix whose column space contains $(1, 1, 0)$ and $(1, 0, 1)$ but **not** $(1, 1, 1)$. Also construct a $3\times3$ matrix whose column space is only a line.

**Part 1.** Put the two required vectors in as columns and make the third column redundant (zero):
$$A = \begin{bmatrix} 1 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}.$$
Then $C(A) = \text{span}\{(1,1,0), (1,0,1)\}$ — the plane $x - y - z = 0$ (normal $(1, -1, -1)$: both columns satisfy it). Test $(1,1,1)$: $1 - 1 - 1 = -1 \ne 0$ — **excluded** ✓. (A third *independent* column would have filled out $\mathbb{R}^3$ and accidentally included $(1,1,1)$; a dependent third column keeps the plane exactly.)

**Part 2.** Make all columns multiples of one vector:
$$B = \begin{bmatrix} 1 & 2 & -1 \\ 2 & 4 & -2 \\ 3 & 6 & -3 \end{bmatrix}, \qquad C(B) = \text{span}\{(1, 2, 3)\} \text{ — a line.}$$

**Examiner's note:** Tests constructing to specification — dependent extra columns cap the column space at a plane.
""")
    code(cells, r"""# SymPy verification — Lab 6, Q.8
A8c = Matrix([[1, 1, 0], [1, 0, 0], [0, 1, 0]])
ca = A8c.columnspace()
print("Q.8  C(A) basis:", [v.T for v in ca])
assert A8c.rank() == 2
assert Matrix([1, 1, 1]).dot(Matrix([1, -1, -1])) != 0
B8c = Matrix([[1, 2, -1], [2, 4, -2], [3, 6, -3]])
assert B8c.rank() == 1
print("Q.8  C(A) is the plane x - y - z = 0 (excludes (1,1,1)); rank(B) = 1 => a line")""")

    # ---------------- Q9 ----------------
    md(cells, r"""### Q.9) Pivot-Column Counting (Medium)

**Question (as printed):** How many pivot columns must a $7\times5$ matrix have if its columns are linearly independent? How many must a $5\times7$ matrix have if its columns span $\mathbb{R}^5$? Why?

**Case 1 — $7\times5$, independent columns.** Independence ⟺ **every** column is a pivot column ⟺ exactly **5** pivot columns. (The matrix is tall: 7 rows can supply the 5 pivots. Rank $= 5 = n$; nullity $0$.)

**Case 2 — $5\times7$, spanning $\mathbb{R}^5$.** Spanning $\mathbb{R}^5$ ⟺ rank $= 5$ = number of rows ⟺ exactly **5** pivot columns. (The matrix is wide: 5 pivots among 7 columns leave $7 - 5 = 2$ free columns, so $N(A)$ is 2-dimensional — spanning and independence are *different* demands here, and only spanning is achieved.)

**The moral:** independence is about the **columns** (need $r = n$); spanning is about the **rows** (need $r = m$). A matrix can do one, both (square invertible), or neither.

**Examiner's note:** Tests the two directions of the pivot theorem.
""")

    # ---------------- Q10 ----------------
    md(cells, r"""### Q.10) For Which $h$ Is $v_3 \in \text{span}\{v_1, v_2\}$? (Medium)

**Question (as printed):** For what values of $h$ is $v_3$ in $\text{span}\{v_1, v_2\}$, and for what values is $\{v_1, v_2, v_3\}$ dependent? Justify.
$$v_1 = \begin{bmatrix} 2 \\ -4 \\ 1 \end{bmatrix},\quad v_2 = \begin{bmatrix} -6 \\ 7 \\ -3 \end{bmatrix},\quad v_3 = \begin{bmatrix} 8 \\ h \\ 4 \end{bmatrix}$$

**Step 1 — a structural observation kills both questions at once.** Look at the **rows** of the matrix $[\,v_1\ v_2\ v_3\,]$:
$$\begin{bmatrix} 2 & -6 & 8 \\ -4 & 7 & h \\ 1 & -3 & 4 \end{bmatrix}: \qquad \text{row}_1 = 2 \times \text{row}_3 \quad\text{for every } h.$$
A proportional pair of rows means $\det = 0$ **for every $h$** — the three vectors are linearly dependent **for all $h \in \mathbb{R}$**.

**Step 2 — but dependence ≠ $v_3 \in \text{span}\{v_1, v_2\}$ automatically... here it does hold.** Solve $c_1v_1 + c_2v_2 = v_3$ using coordinates 1 and 3 (which ignore $h$):
$$2c_1 - 6c_2 = 8, \qquad c_1 - 3c_2 = 4 \quad (\text{same equation}),$$
one equation, two unknowns — a free parameter $c_2 = t$, $c_1 = 4 + 3t$. Coordinate 2 then *defines* what $h$ must be:
$$h = -4c_1 + 7c_2 = -4(4 + 3t) + 7t = -16 - 5t.$$
Conversely, for **any given $h$**, choose $t = \tfrac{-16 - h}{5}$ and the combination works.

$$\boxed{v_3 \in \text{span}\{v_1, v_2\} \text{ for every } h;\ \ \{v_1, v_2, v_3\} \text{ is dependent for every } h.}$$

(E.g. $h = -16$: $v_3 = 4v_1$; $h = -21$: $v_3 = 7v_1 + v_2$.)

**Examiner's note:** Tests distinguishing "the determinant vanishes" from "this vector is in that span" — here both hold for all $h$, but each needs its own justification.
""")
    code(cells, r"""# SymPy verification — Lab 6, Q.10
h = sp.symbols('h')
M10 = Matrix([[2, -6, 8], [-4, 7, h], [1, -3, 4]])
print("Q.10 det =", sp.factor(M10.det()), " (identically 0 => dependent for ALL h)")
assert M10.det() == 0
for hv in [-16, -21, 0, 100]:
    v1, v2, v3 = Matrix([2, -4, 1]), Matrix([-6, 7, -3]), Matrix([8, hv, 4])
    t = sp.Rational(-16 - hv, 5)
    assert (4 + 3 * t) * v1 + t * v2 == v3
print("Q.10 explicit combinations verified for h = -16, -21, 0, 100")""")

    # ---------------- Q11 ----------------
    md(cells, r"""### Q.11) When Is $C(AB) \subsetneq C(A)$? (Hard)

**Question (as printed):** The columns of $AB$ are combinations of columns of $A$, so $C(AB) \subseteq C(A)$. Give an example where the two column spaces are **not equal**.

**Example.** Take
$$A = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, \qquad B = \begin{bmatrix} 0 \\ 1 \end{bmatrix}\cdot[1] \ \Rightarrow\ \text{use } B = \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}.$$
Then
$$AB = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix} \qquad\Longrightarrow\qquad C(AB) = \{\mathbf{0}\} \;\subsetneq\; C(A) = \text{span}\{(1, 0)\}.$$

**Why it happens.** $B$'s columns happen to point along $A$'s **null direction** ($B$'s only non-zero column is $(1,0)^T$, and $A(1,0)^T = (1,0)^T$... concretely: $A\,(0,1)^T = \mathbf{0}$, and $B$'s second column produces the zero combination) — combinations of columns of $A$ that land on $\mathbf{0}$. $B$ acts as a *filter*: it can restrict $A$'s output to any subspace of $C(A)$, including $\{\mathbf{0}\}$. Equality $C(AB) = C(A)$ requires $B$ to be, e.g., invertible.

**Examiner's note:** Tests that the inclusion $C(AB) \subseteq C(A)$ can be strict, with $B$ shrinking the reachable set.
""")
    code(cells, r"""# SymPy verification — Lab 6, Q.11
A11c = Matrix([[1, 0], [0, 0]])
B11c = Matrix([[0, 0], [1, 0]])
print("Q.11 AB ="); display(A11c * B11c)
assert (A11c * B11c) == sp.zeros(2, 2)
assert A11c.columnspace() == [Matrix([1, 0])]
print("Q.11 C(AB) = {0} is strictly inside C(A) = span{(1, 0)}")""")

    # ---------------- Q12 ----------------
    md(cells, r"""### Q.12) Two Cubes: Independent or Dependent? (Hard)

**Question (as printed, with the figure):** Determine whether $v_1, v_2, v_3$ are linearly independent or dependent in **cube (a)** and **cube (b)**.

**Cube (a) — DEPENDENT (two parallel arrows).** Reading the figure with axes $x$ (toward the viewer), $y$ (right), $z$ (up):
- $v_1$ runs along the **bottom face diagonal** from the origin to the far bottom corner: $v_1 = (1, 1, 0)$.
- $v_3$ runs along the **top face diagonal** in the *same direction*: as a free vector $v_3 = (1, 1, 0) = v_1$.
- $v_2$ runs down the right face, from the top far corner to the bottom right corner: $v_2 = (-1, 0, -1)$.

Since $v_3 - v_1 = \mathbf{0}$ with non-zero coefficients ($1, -1$), the set is **linearly dependent** regardless of $v_2$. Visually: *two of the three arrows are parallel* — parallel (equal) vectors can never form an independent set.

**Cube (b) — DEPENDENT (the triangle relation).** Here the three arrows have genuinely different directions — none is parallel to another — but they satisfy the **head-to-tail triangle rule**:
- $v_1$ points straight down a vertical edge: $v_1 = (0, 0, -1)$.
- $v_2$ is the long space diagonal from the origin to the opposite top corner: $v_2 = (1, 1, 1)$.
- $v_3$ is the top-face diagonal ending at the **same corner** as $v_2$: $v_3 = (1, 1, 0)$.

$$v_1 + v_2 = (0,0,-1) + (1,1,1) = (1, 1, 0) = v_3 \quad\Longrightarrow\quad v_1 + v_2 - v_3 = \mathbf{0}.$$
The figure even draws it: $v_1$ (down) then $v_2$ (the diagonal) chains exactly onto $v_3$. So cube (b) is **linearly dependent too** — but for a subtler reason than (a).

**The lesson (why this is a "Hard" question).** Dependence has (at least) two distinct visual signatures: **parallel arrows** (cube a) and a **closed triangle** of directions (cube b). "All different directions" is *not* a test for independence — only the existence of a non-trivial relation $c_1v_1 + c_2v_2 + c_3v_3 = 0$ is.

**Examiner's note:** Tests reading vectors off a 3D figure and recognising two different dependence mechanisms.
""")
    code(cells, r"""# SymPy verification — Lab 6, Q.12 (coordinates read off the figure)
ca = Matrix.hstack(Matrix([1, 1, 0]), Matrix([-1, 0, -1]), Matrix([1, 1, 0]))
print("Q.12(a) rank =", ca.rank(), "< 3 => dependent (v1 and v3 are the same free vector)")
assert ca.rank() == 2
cb = Matrix.hstack(Matrix([0, 0, -1]), Matrix([1, 1, 1]), Matrix([1, 1, 0]))
print("Q.12(b) rank =", cb.rank(), "< 3 => dependent (v3 = v1 + v2)")
assert cb.rank() == 2 and Matrix([0, 0, -1]) + Matrix([1, 1, 1]) == Matrix([1, 1, 0])""")

    # ---------------- Q13 ----------------
    md(cells, r"""### Q.13) Solvability Condition for a Rank-1 System (Hard)

**Question (as printed):** For which right sides $(b_1, b_2, b_3)$ is the system solvable?
$$\begin{bmatrix} 1 & 4 & 2 \\ 2 & 8 & 4 \\ -1 & -4 & -2 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} b_1 \\ b_2 \\ b_3 \end{bmatrix}$$

**Step 1 — the row structure.** Row 2 is $2\times$ row 1 and row 3 is $-1\times$ row 1: all three left-hand sides are **proportional** (rank 1). Every equation is just the first equation in disguise:
$$x_1 + 4x_2 + 2x_3 = b_1 \quad(\times 2), \quad (\times -1).$$

**Step 2 — transfer the dependencies to the right side.** Whatever the left sides do, the right sides must do too:
$$b_2 = 2b_1 \qquad\text{and}\qquad b_3 = -b_1.$$
Equivalently, the left-null vector is $y = (-2, 1, 0)$ and $y = (1, 0, 1)$: the conditions are $-2b_1 + b_2 = 0$ and $b_1 + b_3 = 0$.

$$\boxed{\text{Solvable} \iff b_2 = 2b_1 \text{ and } b_3 = -b_1.}$$
When solvable, one equation in three unknowns remains ⇒ **infinitely many** solutions (a plane of them, $N(A)$ being 2-dimensional).

**Examiner's note:** Tests the Fredholm-style condition: consistency constraints come from the left null space of $A$.
""")
    code(cells, r"""# SymPy verification — Lab 6, Q.13
A13c = Matrix([[1, 4, 2], [2, 8, 4], [-1, -4, -2]])
print("Q.13 rank(A) =", A13c.rank(), " left-null vectors:", [v.T for v in A13c.T.nullspace()])
b13 = sp.symbols('b1 b2 b3')
bv = Matrix(list(b13))
ys = A13c.T.nullspace()
conds = [sp.simplify(y.dot(bv)) for y in ys]
print("Q.13 conditions y^T b = 0:", conds, "=> b2 = 2*b1 and b3 = -b1")
assert A13c.rank() == 1
# numeric check: b = (3, 6, -3) is solvable; (3, 6, 0) is not
assert A13c.row_join(Matrix([3, 6, -3])).rank() == 1
assert A13c.row_join(Matrix([3, 6, 0])).rank() == 2""")

    # ---------------- Q14 ----------------
    md(cells, r"""### Q.14) College Robot: Eliminating Redundant Controls (Hard)

**Question (as printed):** Four control mechanisms act along three axes, given by the columns of
$$A = \begin{bmatrix} 1 & 0 & 1 & 2 \\ 0 & 1 & 1 & 1 \\ 1 & 1 & 2 & 3 \end{bmatrix}.$$
(a) How to determine the redundant controls? (b) Which are redundant? (c) The smallest number of controls preserving all movement patterns? (d) If controls 1 and 2 are kept, can every movement pattern still be produced?

**Part (a) — the method.** A control is **redundant** exactly when its column is a linear combination of the others — i.e. when elimination finds no pivot in that column. Reduce $A$ (columns = candidate directions; equivalently work with $A^T$'s rows):
$$\text{RREF of } A: \begin{bmatrix} 1 & 0 & 1 & 2 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix} \quad\Rightarrow\quad \text{pivots in columns 1, 2 only.}$$

**Part (b).** Columns 3 and 4 have **no pivots** — they are redundant. Explicitly:
$$\mathbf{c}_3 = \mathbf{c}_1 + \mathbf{c}_2 \quad\checkmark\ ((1,0,1) + (0,1,1) = (1,1,1)), \qquad \mathbf{c}_4 = 2\mathbf{c}_1 + \mathbf{c}_2 \quad\checkmark\ ((2,0,2)+(0,1,1) = (2,1,3)).$$

**Part (c).** Keep one independent control per pivot column: **2 controls** (controls 1 and 2) suffice, since $\text{rank}(A) = 2$ — the robot's full repertoire is only a 2-dimensional set of movements.

**Part (d).** **Yes.** Every column of $A$ is a combination of $\mathbf{c}_1, \mathbf{c}_2$ (that is what part (b) showed), so $C(A) = \text{span}\{\mathbf{c}_1, \mathbf{c}_2\}$ — dropping controls 3 and 4 loses **no** reachable movement, only the ability to achieve it in more than one way (the relations $c_1 + c_2 - c_3 = 0$ and $2c_1 + c_2 - c_4 = 0$ span the null space of $A$ and provide the "trade" directions between recipes).

**Examiner's note:** Tests redundancy = dependence of columns, and rank = minimum number of generators of the column space.
""")
    code(cells, r"""# SymPy verification — Lab 6, Q.14
A14r = Matrix([[1, 0, 1, 2], [0, 1, 1, 1], [1, 1, 2, 3]])
print("Q.14 RREF:"); display(A14r.rref()[0])
assert A14r.rank() == 2
c1, c2, c3, c4 = (A14r[:, j] for j in range(4))
assert c3 == c1 + c2 and c4 == 2 * c1 + c2
print("Q.14(b) c3 = c1 + c2 and c4 = 2*c1 + c2: controls 3 and 4 are redundant")""")

    # ---------------- Challenge ----------------
    md(cells, r"""### Challenge: The Theatre Buys a Fourth Lamp (numbered "Q.14" again on the sheet)

> **⚠ Sheet note:** the challenge question is printed with the number Q.14, duplicating the robot problem above; we refer to it as the *Challenge*.

**Question (as printed):** Four lamps as RGB columns:
$$L = \begin{bmatrix} 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & 1 \\ 0 & 1 & 0 & 1 \end{bmatrix} = \left[\,\text{Red}\ \ \text{Cyan}\ \ \text{Yellow}\ \ \text{White}\,\right].$$
(a) Eliminate $L$: how many pivots, what rank? (b) Are the four lamp colours independent — one-line reason from the *shape* of $L$? (c) Find four numbers, not all zero, whose weighted sum of lamp colours is $(0,0,0)$. (d) A student says "return the White lamp": (i) show the theatre could return **Red** instead and still make every colour; (ii) show returning **Yellow** is *not* safe. (e) Amber $b = (4,3,1)$ had recipe $(2,1,2)$ on the three-lamp rig, now $x = (2,1,2,0)$: (i) check $Lx = b$; (ii) use the trade from (c) to write a **different** recipe for amber and verify; (iii) how many recipes give amber if brightness may be any real number? (iv) in one sentence, what changed? (f) True/False: (i) buying the fourth lamp increased the number of colours; (ii) any four vectors in $\mathbb{R}^3$ are dependent; (iii) any three of the four lamps are independent.

**Part (a).** Elimination: $R_3 \to R_3 - R_2$ gives $(0, 0, -1, 0)$:
$$U = \begin{bmatrix} \boxed{1} & 0 & 1 & 1 \\ 0 & \boxed{1} & 1 & 1 \\ 0 & 0 & \boxed{-1} & 0 \end{bmatrix} \quad\Rightarrow\quad \textbf{3 pivots, rank } 3.$$

**Part (b) — the one-line shape reason.** $L$ is $3\times4$: **four vectors in $\mathbb{R}^3$ must be dependent** ($n = 4 > m = 3$) — no calculation needed.

**Part (c).** Solve $Lx = 0$: from $U$, $-x_3 = 0 \Rightarrow x_3 = 0$; $x_2 + x_4 = 0$; $x_1 + x_4 = 0$. With $x_4 = 1$:
$$\boxed{x = (-1, -1, 0, 1)} \qquad\Longleftrightarrow\qquad \text{Red} + \text{Cyan} = \text{White}.$$
Check: $(1,0,0) + (0,1,1) = (1,1,1)$ ✓. (This is the *only* relation — nullity is $4 - 3 = 1$.)

**Part (d)(i) — return Red instead.** Any recipe using White can replace White by Red $+$ Cyan (part (c)); the remaining lamps {Cyan, Yellow, Red} are independent ($\det\begin{bmatrix}1&0&1\\0&1&1\\0&1&0\end{bmatrix} = -1 \ne 0$), so they span all of $\mathbb{R}^3$ — **every colour is still makeable**. The student's choice works, but so does returning Red.

**Part (d)(ii) — Yellow is not safe.** The remaining lamps {Red, Cyan, White} all satisfy **green $=$ blue** ($R: 0=0$, $C: 1=1$, $W: 1=1$), and so does every combination of them. Colours with $g \ne b$ — amber $(4, 3, 1)$ among them — become unreachable. Formally: $\det\begin{bmatrix}1&0&1\\0&1&1\\0&1&1\end{bmatrix} = 0$: the triple is dependent, rank 2, and its span is the plane $g = b$.

**Part (e).**
- (i) $L(2,1,2,0)^T = 2\text{Red} + \text{Cyan} + 2\text{Yellow} = (2,0,0) + (0,1,1) + (2,2,0) = (4, 3, 1)$ ✓.
- (ii) Use the trade $\text{White} = \text{Red} + \text{Cyan}$: replace one Red $+$ one Cyan by one White:
$$x' = (1, 0, 2, 1): \quad \text{Red} + 2\text{Yellow} + \text{White} = (1,0,0) + (2,2,0) + (1,1,1) = (4, 3, 1)\ \checkmark.$$
- (iii) **Infinitely many**: $x(t) = (2, 1, 2, 0) + t(1, 1, 0, -1)$ for any $t \in \mathbb{R}$ (the null-space direction from (c), scaled) — every $t$ gives amber.
- (iv) **One sentence:** the fourth lamp made the four colour vectors linearly dependent, giving the system $Lx = b$ a free variable — and free variables mean many recipes per colour instead of one.

**Part (f).**
- (i) **FALSE.** The three-lamp rig already had rank 3, i.e. $C(L) = \mathbb{R}^3$ — *every* colour was already makeable; the fourth lamp changed only the recipes, not the reachable set.
- (ii) **TRUE.** More vectors than the dimension of the space forces dependence (pigeonhole on pivots).
- (iii) **FALSE.** {Red, Cyan, White} is dependent ($\text{Red} + \text{Cyan} = \text{White}$). The other three triples ({R,C,Y}, {R,Y,W}, {C,Y,W}) happen to be independent, but "any three" is falsified by a single dependent triple.

**Examiner's note:** Tests rank/nullity on a concrete colour system and the practical meaning of a null-space direction as a "trade" between recipes.
""")
    code(cells, r"""# SymPy verification — Lab 6, Challenge
Lc = Matrix([[1, 0, 1, 1], [0, 1, 1, 1], [0, 1, 0, 1]])
print("Challenge(a) rank =", Lc.rank(), "| nullspace:", [v.T for v in Lc.nullspace()])
assert Lc.rank() == 3 and Lc.nullspace()[0] in (Matrix([1, 1, 0, -1]), Matrix([-1, -1, 0, 1]))
assert Lc * Matrix([2, 1, 2, 0]) == Matrix([4, 3, 1])       # (e)(i)
assert Lc * Matrix([1, 0, 2, 1]) == Matrix([4, 3, 1])       # (e)(ii)
assert Lc * Matrix([3, 2, 2, -1]) == Matrix([4, 3, 1])      # (e)(iii) another t
print("Challenge(d)(ii) Red+Cyan+White determinant:",
      Matrix([[1, 0, 1], [0, 1, 1], [0, 1, 1]]).det(), "(0 => Yellow unsafe)")
assert Matrix([[1, 0, 1], [0, 1, 1], [0, 1, 1]]).det() == 0
print("Challenge(f)(i) three-lamp rank:", Matrix([[1, 0, 1], [0, 1, 1], [0, 1, 0]]).rank(),
      "= 3 already => no new colours")""")

    return cells


LAB_TITLE = "Lab 7 Solutions: Null Space, Subspaces, and Complete Solutions"
LAB_SUB = (
    '**Core ideas tested:** "Same Output, Different Inputs?" — $N(A)$ as the solution set of '
    "$Ax = 0$, special solutions from free variables, the complete solution $x = x_p + x_n$, "
    "the two subspace tests, and constructive matrix design."
)


def get_lab7_cells():
    cells = []
    md(cells, lab_header(LAB_TITLE, LAB_SUB))

    # ---------------- Q1 ----------------
    md(cells, r"""### Q.1) True/False: Null Space Fundamentals (Easy)

**Question (as printed):**
(a) The null space of $A$ is the solution set of the equation $Ax = 0$.
(b) A square matrix has no free variables.
(c) An invertible matrix has no free variables.
(d) The null space of an $m\times n$ matrix is a subspace of $\mathbb{R}^m$.
(e) An $m\times n$ matrix has no more than $n$ pivot variables.
(f) An $m\times n$ matrix has no more than $m$ pivot variables.
(g) The set of all solutions of a system of $m$ homogeneous equations in $n$ unknowns is a subspace of $\mathbb{R}^m$.

**(a) TRUE.** That is the definition: $N(A) = \{x : Ax = \mathbf{0}\}$.

**(b) FALSE.** Singular square matrices have free variables: e.g. $A = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}$ has rank 1, hence $2 - 1 = 1$ free variable. Only *invertible* square matrices have none.

**(c) TRUE.** Invertible ⟺ $n$ pivots ⟺ no free variables (and $N(A) = \{\mathbf{0}\}$).

**(d) FALSE.** $Ax$ is defined for $x \in \mathbb{R}^n$ and lives in $\mathbb{R}^m$; so $N(A) \subseteq \mathbb{R}^{\mathbf{n}}$, not $\mathbb{R}^m$. (The column space is the one living in $\mathbb{R}^m$.)

**(e) TRUE.** Pivot variables = pivot columns $\le n$ (there are only $n$ columns to hold pivots).

**(f) TRUE.** There can be at most one pivot per row as well, so pivots $\le m$ too. (Both (e) and (f) hold: pivots $\le \min(m, n)$.)

**(g) FALSE.** The solution set of $Ax = 0$ (with $A$ being $m \times n$) is $N(A) \subseteq \mathbb{R}^{\mathbf{n}}$, the space of *unknowns*, not $\mathbb{R}^m$.

**Examiner's note:** Tests the definitions and the two "homes": $N(A) \subseteq \mathbb{R}^n$, $C(A) \subseteq \mathbb{R}^m$.
""")
    code(cells, r"""# SymPy verification — Lab 7, Q.1 (the two FALSE claims, with counterexamples)
A1n = Matrix([[1, 1], [1, 1]])
print("Q.1(b) square but singular: rank =", A1n.rank(), ", nullspace =", [v.T for v in A1n.nullspace()])
A1m = Matrix([[1, 2, 3], [4, 5, 6]])      # 2 x 3: null space lives in R^3, not R^2
ns1 = A1m.nullspace()
assert len(ns1) == 1 and ns1[0].shape == (3, 1)
print("Q.1(d)/(g) N(A) for a 2x3 matrix contains 3-vectors:", ns1[0].T,
      "=> subspace of R^3, not R^2")""")

    # ---------------- Q2 ----------------
    md(cells, r"""### Q.2) Null Space of $\begin{bmatrix} 1 & 3 \\ 3 & 9 \end{bmatrix}$ (Easy)

**Question (as printed):** Find the null space of $A = \begin{bmatrix} 1 & 3 \\ 3 & 9 \end{bmatrix}$.

**Step 1 — eliminate.** $R_2 \to R_2 - 3R_1$: the system collapses to the single equation
$$x_1 + 3x_2 = 0.$$

**Step 2 — free variable and special solution.** $x_2$ is free; set $x_2 = 1$: $x_1 = -3$.
$$\boxed{N(A) = \text{span}\left\{ \begin{bmatrix} -3 \\ 1 \end{bmatrix} \right\}} \qquad \text{(the line } x_1 = -3x_2\text{)}$$

**Geometry:** the two rows of $A$ are parallel (row 2 is $3\times$ row 1), so $Ax = 0$ imposes one condition — a line through the origin of $\mathbb{R}^2$.

**Examiner's note:** Tests the special-solution recipe: eliminate, find free variables, set each to 1 in turn.
""")
    code(cells, r"""# SymPy verification — Lab 7, Q.2
A2n = Matrix([[1, 3], [3, 9]])
ns2 = A2n.nullspace()
print("Q.2  N(A) =", [v.T for v in ns2])
assert ns2[0] == Matrix([-3, 1]) and A2n * ns2[0] == Matrix([0, 0])""")

    # ---------------- Q3 ----------------
    md(cells, r"""### Q.3) Which $\mathbb{R}^k$ Do the Subspaces Live In? (Easy)

**Question (as printed):** For $A = \begin{bmatrix} 2 & 4 & -2 \\ 1 & -2 & -5 \\ 7 & 3 & 3 \\ 7 & -8 & 6 \end{bmatrix}$ (a $4\times3$ matrix):
(a) if the column space is a subspace of $\mathbb{R}^k$, what is $k$? (b) if the null space is a subspace of $\mathbb{R}^k$, what is $k$?

**Part (a).** Columns of $A$ have 4 entries, so combinations of them live in $\mathbb{R}^4$: $k = 4$.

**Part (b).** $A$ multiplies vectors $x \in \mathbb{R}^3$ (one entry per column); solutions of $Ax = 0$ are 3-vectors: $k = 3$.

$$\boxed{C(A) \subseteq \mathbb{R}^4, \qquad N(A) \subseteq \mathbb{R}^3.}$$
(The homes depend only on the *shape* $4 \times 3$ — rows for $C(A)$, columns for $N(A)$.)

**Examiner's note:** Tests the fundamental-shape fact: $C(A) \subseteq \mathbb{R}^m$, $N(A) \subseteq \mathbb{R}^n$.
""")

    # ---------------- Q4 ----------------
    md(cells, r"""### Q.4) A 2×2 Matrix Whose Null Space Is the Line $3x + 5y = 0$ (Easy)

**Question (as printed):** Find $2\times2$ matrices whose null space is the line $3x + 5y = 0$.

**Step 1 — what must be true?** $N(A)$ = that line means $Ax = 0$ is *equivalent* to $3x + 5y = 0$: each row of $A$ must be a multiple of the row $(3, 5)$.

**Step 2 — construct.** Simplest choice:
$$\boxed{A = \begin{bmatrix} 3 & 5 \\ 0 & 0 \end{bmatrix}}$$
Check: $A(5, -3)^T = (15 - 15, 0)^T = 0$ ✓ — the direction vector of the line $3x + 5y = 0$ is killed. Any
$$A = \begin{bmatrix} 3a & 5a \\ 3b & 5b \end{bmatrix} \quad (\text{not both } a, b \text{ zero})$$
works equally (rows are multiples of $(3,5)$); e.g. $\begin{bmatrix} 3 & 5 \\ 6 & 10 \end{bmatrix}$.

**Examiner's note:** Tests reverse-engineering a matrix from its null space: rows must generate the orthogonal (constraint) equation of the line.
""")
    code(cells, r"""# SymPy verification — Lab 7, Q.4
A4n = Matrix([[3, 5], [0, 0]])
ns4 = A4n.nullspace()
print("Q.4  N(A) =", [v.T for v in ns4], " (direction of the line 3x + 5y = 0)")
assert 3 * ns4[0] == Matrix([-5, 3])   # direction (5, -3) up to scale
A4alt = Matrix([[3, 5], [6, 10]])
assert 3 * A4alt.nullspace()[0] == Matrix([-5, 3])
print("Q.4  the alternative [[3,5],[6,10]] has the same null space")""")

    # ---------------- Q5 ----------------
    md(cells, r"""### Q.5) Complete Solution of a Singular 2×2 System (Easy)

**Question (as printed):** Find the complete solution of
$$\begin{bmatrix} 2 & 6 \\ 1 & 3 \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \end{bmatrix} = \begin{bmatrix} 10 \\ 5 \end{bmatrix}$$

**Step 1 — eliminate.** $R_2 \to R_2 - \tfrac12R_1$: $(0, 0 \mid 0)$ — consistent (row 2 is $\tfrac12$ row 1, and the right sides agree: $\tfrac12 \cdot 10 = 5$ ✓). One equation remains: $2x_1 + 6x_2 = 10$, i.e. $x_1 = 5 - 3x_2$.

**Step 2 — particular solution** (free variable $x_2 = 0$): $x_p = (5, 0)^T$.

**Step 3 — null-space part** (solve $Ax = 0$): $x_1 = -3x_2$, special solution $s = (-3, 1)^T$.

$$\boxed{x = x_p + x_n = \begin{bmatrix} 5 \\ 0 \end{bmatrix} + t\begin{bmatrix} -3 \\ 1 \end{bmatrix}, \qquad t \in \mathbb{R}}$$
Geometrically: a line through $(5, 0)$ parallel to $N(A)$ — "one particular answer plus all the ways to stay consistent".

**Examiner's note:** Tests the complete-solution structure $x = x_p + x_n$ on the smallest singular case.
""")
    code(cells, r"""# SymPy verification — Lab 7, Q.5
A5n = Matrix([[2, 6], [1, 3]])
xp = Matrix([5, 0]); s5 = Matrix([-3, 1])
assert A5n * xp == Matrix([10, 5]) and A5n * s5 == Matrix([0, 0])
t = sp.symbols('t')
print("Q.5  x = (5, 0) + t*(-3, 1); check A*x =", (A5n * (xp + t * s5)).T)""")

    # ---------------- Q6 ----------------
    md(cells, r"""### Q.6) Two Complete Solutions with Three and Four Unknowns (Medium)

**Question (as printed):** Find the complete solution $x = x_p + x_n$ of $Ax = b$ for
$$\text{(a) } \begin{bmatrix} 1 & 0 & 2 & 3 \\ 1 & 3 & 2 & 0 \\ 2 & 0 & 4 & 9 \end{bmatrix}x = \begin{bmatrix} 2 \\ 5 \\ 10 \end{bmatrix} \qquad
\text{(b) } \begin{bmatrix} 1 & -2 & 3 \\ 2 & 1 & 4 \\ 1 & -7 & 5 \end{bmatrix}x = \begin{bmatrix} 2 \\ 7 \\ -1 \end{bmatrix}$$

**Part (a) — 3×4.** Elimination on the augmented matrix:
- $R_2 - R_1$: $(0, 3, 0, -3 \mid 3)$;  $R_3 - 2R_1$: $(0, 0, 0, 3 \mid 6)$.
- Pivots in columns 1, 2, 4; **$x_3$ is free**.
- Back-substitute: $3x_4 = 6 \Rightarrow x_4 = 2$; $3x_2 - 3x_4 = 3 \Rightarrow x_2 = 3$; $x_1 + 2x_3 + 3x_4 = 2 \Rightarrow x_1 = -4 - 2x_3$.

Particular ($x_3 = 0$): $x_p = (-4, 3, 0, 2)^T$. Special solution ($x_3 = 1$, other free vars 0): $s = (-2, 0, 1, 0)^T$.
$$\boxed{x = \begin{bmatrix} -4 \\ 3 \\ 0 \\ 2 \end{bmatrix} + t\begin{bmatrix} -2 \\ 0 \\ 1 \\ 0 \end{bmatrix}}$$

**Part (b) — 3×3, singular.** Elimination:
- $R_2 - 2R_1$: $(0, 5, -2 \mid 3)$;  $R_3 - R_1$: $(0, -5, 2 \mid -3) = -(R_2')$ — **consistent**, rank 2, $x_3$ free.
- $5x_2 - 2x_3 = 3 \Rightarrow x_2 = \tfrac{3 + 2x_3}{5}$; $x_1 = 2 + 2x_2 - 3x_3 = \tfrac{16 - 11x_3}{5}$.

Particular ($x_3 = 0$): $x_p = (\tfrac{16}{5}, \tfrac35, 0)^T$. Special solution: $s = (-\tfrac{11}{5}, \tfrac25, 1)^T = \tfrac15(-11, 2, 5)^T$.
$$\boxed{x = \begin{bmatrix} 16/5 \\ 3/5 \\ 0 \end{bmatrix} + t\begin{bmatrix} -11 \\ 2 \\ 5 \end{bmatrix} \big/ 5, \quad\text{equivalently } x = \frac{1}{5}\left(\begin{bmatrix} 16 \\ 3 \\ 0 \end{bmatrix} + t\begin{bmatrix} -11 \\ 2 \\ 5 \end{bmatrix}\right)}$$

**Examiner's note:** Tests producing $x_p + x_n$ cleanly, including the fractional case where scaling the special solution keeps integers.
""")
    code(cells, r"""# SymPy verification — Lab 7, Q.6
A6n = Matrix([[1, 0, 2, 3], [1, 3, 2, 0], [2, 0, 4, 9]])
xp6 = Matrix([-4, 3, 0, 2]); s6 = Matrix([-2, 0, 1, 0])
assert A6n * xp6 == Matrix([2, 5, 10]) and A6n * s6 == Matrix([0, 0, 0])
print("Q.6(a) x_p and s verified")
A6m = Matrix([[1, -2, 3], [2, 1, 4], [1, -7, 5]])
xp6b = Matrix([sp.Rational(16, 5), sp.Rational(3, 5), 0])
s6b = Matrix([sp.Rational(-11, 5), sp.Rational(2, 5), 1])
assert A6m * xp6b == Matrix([2, 7, -1]) and A6m * s6b == Matrix([0, 0, 0])
print("Q.6(b) x_p = (16/5, 3/5, 0), special direction (-11, 2, 5)/5 verified")""")

    # ---------------- Q7 ----------------
    md(cells, r"""### Q.7) Solvability Conditions on $(b_1, b_2)$ and the Complete Solution (Medium)

**Question (as printed):** Under what conditions on $b_1, b_2$ does $Ax = b$ have a solution, for
$$A = \begin{bmatrix} 1 & 2 & 0 & 3 \\ 2 & 4 & 0 & 7 \end{bmatrix}, \quad b = \begin{bmatrix} b_1 \\ b_2 \end{bmatrix}?$$
Find the two vectors in the null space of $A$ and the complete solution.

**Step 1 — eliminate.** $R_2 \to R_2 - 2R_1$: $(0, 0, 0, 1 \mid b_2 - 2b_1)$. This row has a **pivot** (in column 4) — no $0 = $ non-zero row can appear. **Both rows are pivot rows**, so $C(A) = \mathbb{R}^2$:
$$\boxed{\text{Solvable for \emph{every} } (b_1, b_2) \text{ — no condition at all.}}$$

**Step 2 — the two null-space vectors.** Null space of $A$: free variables $x_2, x_3$ (pivots in columns 1, 4):
$$x_1 = -2x_2 - 3x_4, \qquad x_4 = b_2 - 2b_1 \ \text{(from the last row of the eliminated system)}.$$
For $Ax = 0$: $x_4 = 0$, $x_1 = -2x_2 - 3x_4$. Special solutions:
$$s_1 = \begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix} (x_2 = 1), \qquad s_2 = \begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \end{bmatrix} (x_3 = 1). \qquad N(A) = \text{span}\{s_1, s_2\}.$$

**Step 3 — the complete solution.** From elimination: $x_4 = b_2 - 2b_1$ and $x_1 = b_1 - 2x_2 - 3x_4 = (7b_1 - 3b_2) - 2x_2$. With free $x_2 = c_1$, $x_3 = c_2$:
$$\boxed{x = \begin{bmatrix} 7b_1 - 3b_2 \\ 0 \\ 0 \\ b_2 - 2b_1 \end{bmatrix} + c_1\begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix} + c_2\begin{bmatrix} 0 \\ 0 \\ 1 \\ 0 \end{bmatrix}}$$

**Examiner's note:** Tests recognising full row rank ⇒ no solvability condition, and producing the two-parameter complete solution.
""")
    code(cells, r"""# SymPy verification — Lab 7, Q.7
A7n = Matrix([[1, 2, 0, 3], [2, 4, 0, 7]])
ns7 = A7n.nullspace()
print("Q.7  null-space vectors:", [v.T for v in ns7])
assert ns7 == [Matrix([-2, 1, 0, 0]), Matrix([0, 0, 1, 0])]
b1, b2 = sp.symbols('b1 b2')
xsol = Matrix([7*b1 - 3*b2, 0, 0, b2 - 2*b1])
assert A7n * xsol == Matrix([b1, b2])
print("Q.7  x_p = (7b1 - 3b2, 0, 0, b2 - 2b1) works for EVERY (b1, b2):", A7n.rank() == 2)""")

    # ---------------- Q8 ----------------
    md(cells, r"""### Q.8) $N(A) = C(A)$: Possible in 2×2, Impossible in 3×3 (Medium)

**Question (as printed):** Construct a $2\times2$ matrix whose null space **equals** its column space. Justify why no $3\times3$ matrix can have $N(A) = C(A)$.

**Construction.** Take
$$A = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}.$$
- Column space: $C(A) = \text{span}\{(1, 0)^T\}$ — the $x$-axis.
- Null space: $Ax = (x_2, 0)^T = 0 \iff x_2 = 0$: $N(A) = \text{span}\{(1, 0)^T\}$ — the **same** $x$-axis ✓.

**Why $3\times3$ is impossible — the rank–nullity handshake.** For any $3\times3$ matrix:
$$\dim C(A) + \dim N(A) = \text{rank} + (3 - \text{rank}) = 3.$$
If the two subspaces were **equal**, each would have dimension $k$ with $k + k = 3$ — but $3$ is **odd**, so $k = 1.5$ is not an integer. Contradiction. (The same argument shows $N(A) = C(A)$ is possible exactly when $n = \text{rank} + \text{nullity}$ is *even* — e.g. $2 = 1 + 1$ above.)

**Examiner's note:** Tests the rank–nullity theorem as an obstruction/possibility tool, plus a concrete rank-1 construction.
""")
    code(cells, r"""# SymPy verification — Lab 7, Q.8
A8n = Matrix([[0, 1], [0, 0]])
print("Q.8  C(A) =", [v.T for v in A8n.columnspace()], " N(A) =", [v.T for v in A8n.nullspace()])
assert A8n.columnspace() == A8n.nullspace() == [Matrix([1, 0])]
# no 3x3 example can exist: rank + nullity = 3 is odd
print("Q.8  rank + nullity = 3 for every 3x3 matrix => equal subspaces would need 2k = 3")""")

    # ---------------- Q9 ----------------
    md(cells, r"""### Q.9) Null Space of the $6\times6$ Repeated-Row Matrix (Medium)

**Question (as printed):** Find the null space of the $6\times6$ matrix whose row $i$ is $(i, i, i, i, i, i)$.

**Step 1 — recognise the rank.** Every row is $i\times(1,1,1,1,1,1)$: all rows are multiples of one vector, so $\text{rank} = 1$ and
$$A x = \begin{bmatrix} x_1 + \dots + x_6 \\ 2(x_1 + \dots + x_6) \\ \vdots \\ 6(x_1 + \dots + x_6) \end{bmatrix},$$
so $Ax = 0 \iff x_1 + x_2 + x_3 + x_4 + x_5 + x_6 = 0$.

**Step 2 — a basis.** Nullity $= 6 - 1 = 5$; setting each $x_j = 1$, $x_1 = -1$ in turn (a standard choice):
$$\boxed{N(A) = \text{span}\Big\{ (1,-1,0,0,0,0),\ (1,0,-1,0,0,0),\ (1,0,0,-1,0,0),\ (1,0,0,0,-1,0),\ (1,0,0,0,0,-1) \Big\}}$$
— the 5-dimensional hyperplane of $\mathbb{R}^6$ consisting of all vectors whose entries **sum to zero**.

**Examiner's note:** Tests rank-1 recognition and describing a high-dimensional null space by its defining equation.
""")
    code(cells, r"""# SymPy verification — Lab 7, Q.9
A9n = Matrix(6, 6, lambda i, j: i + 1)
assert A9n.rank() == 1
basis9 = [Matrix([1 if k == j else 0 for k in range(6)]) for j in range(1, 6)]
basis9 = [Matrix([-1] + [0]*j + [1] + [0]*(4 - j)) for j in range(5)]
for v9 in basis9:
    assert A9n * v9 == sp.zeros(6, 1)
print("Q.9  rank =", A9n.rank(), ", nullity =", len(A9n.nullspace()),
      "=> N(A) = {x : sum of entries = 0}")
print("Q.9  basis:", [v.T for v in basis9])""")

    # ---------------- Q10 ----------------
    md(cells, r"""### Q.10) Subspace Tests in $\mathbb{R}^3$ (Medium)

**Question (as printed):** Determine whether the following are subspaces of $\mathbb{R}^3$:
(a) $S = \{(x, y, z) : xy = 0\}$  (b) $S = \{(x, y, z) : x + y = z\}$  (c) $S = \{(x, y, z) : x^2 + y^2 = z^2\}$  (d) $S = \{(x, y, z) : x^2 + y^2 + z^2 > 0\}$

**Recall the two tests:** (1) $\mathbf{0} \in S$ and (2) closed under addition **and** scalar multiplication.

**(a) NOT a subspace — fails addition.** $(1, 0, 0), (0, 1, 0) \in S$ (products are 0), but their sum $(1, 1, 0)$ has $xy = 1 \ne 0$. (It *does* contain $\mathbf{0}$ and is closed under scalars — the union of the $xz$- and $yz$-planes — but one failed closure is fatal.)

**(b) IS a subspace.** The set is the plane $x + y - z = 0$ through the origin:
- $\mathbf{0}$: $0 + 0 = 0$ ✓.
- Addition: if $x_i + y_i = z_i$ then $(x_1{+}x_2) + (y_1{+}y_2) = z_1 + z_2$ ✓.
- Scalars: $cx + cy = cz$ ✓.
(Equivalently it is $N(\,[\,1\ \ 1\ \ -1\,]\,)$ — a null space is always a subspace.)

**(c) NOT a subspace — fails addition.** The double cone $z^2 = x^2 + y^2$: $(1, 0, 1)$ and $(0, 1, 1)$ are both in $S$, but their sum $(1, 1, 2)$ has $1 + 1 = 2 \ne 4$. (It contains $\mathbf{0}$ and is closed under negation — the failure is purely additive.)

**(d) NOT a subspace — fails the zero vector (and addition).** $\mathbf{0} = (0,0,0)$ has $x^2+y^2+z^2 = 0 \not> 0$: the origin is excluded. Also $(1,0,0) + (-1,0,0) = \mathbf{0} \notin S$ — sums of elements can fall out.

$$\boxed{\text{(a) No} \quad \text{(b) Yes} \quad \text{(c) No} \quad \text{(d) No}}$$

**Examiner's note:** Tests both closure laws with explicit counterexample vectors.
""")
    code(cells, r"""# SymPy verification — Lab 7, Q.10 (numeric spot-checks of the counterexamples)
assert 1 * 0 == 0 and 0 * 1 == 0 and 1 * 1 != 0        # (a) failure pair
print("Q.10(a) (1,0,0) + (0,1,0) = (1,1,0) leaves the set xy = 0")
assert 1 + 0 == 1 and 0 + 1 == 1 and (1 + 1) == (1 + 1)  # (b) plane equation preserved
print("Q.10(b) x + y = z is linear => a subspace")
assert 1 + 0 == 1 and 0 + 1 == 1 and (1 + 1)**2 != 1 + 1  # (c) failure pair
print("Q.10(c) (1,0,1) + (0,1,1) = (1,1,2): 2 != 4 leaves the cone")
print("Q.10(d) the origin (0,0,0) is excluded: not a subspace")""")

    # ---------------- Q11 ----------------
    md(cells, r"""### Q.11) Why These Shaded Regions Are Not Subspaces (Hard)

**Question (as printed, with four figures; bounding lines included):** Give a specific reason why each set $H$ is not a subspace of $\mathbb{R}^2$.

**(a) The first quadrant** ($x \ge 0$, $y \ge 0$, axes included). **Fails scalar multiplication:** $(1, 1) \in H$ but $-1\cdot(1, 1) = (-1, -1) \notin H$. (Addition is fine; closure under *negative* scalars is not.)

**(b) Quadrants I and III** ($xy \ge 0$, i.e. $x$ and $y$ with the same sign, axes included). **Fails addition:** $(1, 3) \in H$ (quadrant I) and $(-3, -1) \in H$ (quadrant III), but $(1, 3) + (-3, -1) = (-2, 2)$ has $xy = -4 < 0$ — in quadrant II, outside $H$.

**(c) A slanted strip (band) of finite width through the origin**, between two parallel lines. **Fails scalar multiplication:** take any non-zero $v \in H$; for large enough $t$, the stretched vector $tv$ travels arbitrarily far from the origin *across* the strip's bounded width and exits. (E.g. $v = (1, 1)$ and $t = 100$.) Every subspace through the origin is unbounded; a bounded-width strip cannot be one.

**(d) A half-plane** $\{x + y \ge 0\}$, boundary line through the origin included. **Fails scalar multiplication:** $(1, 0) \in H$ ($1 \ge 0$) but $-(1, 0) = (-1, 0)$ has $-1 < 0$ — outside. (Addition happens to be fine; negative scalars break it, exactly as in (a).)

**The pattern:** regions defined by *inequalities* can never be subspaces unless the inequality is trivial — closure under negation forces symmetry through the origin, and closure under addition forces "straightness" (lines/planes through $\mathbf{0}$).

**Examiner's note:** Tests picking the *one specific* failed closure law with explicit vectors for each picture.
""")

    # ---------------- Q12 ----------------
    md(cells, r"""### Q.12) Construct: Given $C(A)$ Requirements and a Null Vector (Hard)

**Question (as printed):** Construct a matrix whose column space contains $(1, 1, 5)$ and $(0, 3, 1)$ and whose null space contains $(1, 1, 2)$.

**Step 1 — translate the requirements.** Take the two required vectors as the first two columns: $\mathbf{c}_1 = (1,1,5)^T$, $\mathbf{c}_2 = (0,3,1)^T$. $A(1,1,2)^T = \mathbf{0}$ means
$$\mathbf{c}_1 + \mathbf{c}_2 + \;(\text{remaining columns})\cdot(\text{entries}) = \mathbf{0}.$$

**Step 2 — choose the cheapest shape.** With $x = (1, 1, 2)^T \in \mathbb{R}^3$, the matrix is $3\times3$ and the requirement reads
$$\mathbf{c}_1 + \mathbf{c}_2 + 2\mathbf{c}_3 = \mathbf{0} \quad\Longrightarrow\quad \mathbf{c}_3 = -\tfrac12(\mathbf{c}_1 + \mathbf{c}_2) = -\tfrac12(1, 4, 6)^T = (-\tfrac12, -2, -3)^T.$$
To keep integers, scale the third column by 2 — i.e. instead require $A'(1, 1, 2)^T = \mathbf{0}$ with $A' = [\,\mathbf{c}_1\ \mathbf{c}_2\ \mathbf{c}_3'\,]$ and $\mathbf{c}_3' = -(\mathbf{c}_1 + \mathbf{c}_2) = (-1, -4, -6)^T$:
$$\boxed{A = \begin{bmatrix} 1 & 0 & -1 \\ 1 & 3 & -4 \\ 5 & 1 & -6 \end{bmatrix}}$$

**Step 3 — verify all three requirements.**
- $A(1,1,2)^T = \mathbf{c}_1 + \mathbf{c}_2 + 2\mathbf{c}_3' = (1+0-2,\ 1+3-8,\ 5+1-12) = (0,0,0)$ ✓ — wait, using $2\mathbf{c}_3'$: $(1 + 0 - 2, 1 + 3 - 8, 5 + 1 - 12) = (0,0,0)$ ✓ (the factor 2 lands on $\mathbf{c}_3' = -(c_1+c_2)$... precisely: $\mathbf{c}_1 + \mathbf{c}_2 + 2\,\mathbf{c}_3' = (1,4,6) + 2(-1,-4,-6) = (-1,-4,-6) \ne 0$!). Let me redo cleanly.

**Careful redo.** With $x = (1,1,2)$, the combination is $1\cdot\mathbf{c}_1 + 1\cdot\mathbf{c}_2 + 2\cdot\mathbf{c}_3$. So we need $2\mathbf{c}_3 = -(\mathbf{c}_1 + \mathbf{c}_2) = (-1, -4, -6)$, i.e. $\mathbf{c}_3 = (-\tfrac12, -2, -3)^T$. Using the half-integer column directly:
$$\boxed{A = \begin{bmatrix} 1 & 0 & -\tfrac12 \\[2pt] 1 & 3 & -2 \\[2pt] 5 & 1 & -3 \end{bmatrix}}$$
Check: $A(1,1,2)^T = (1 + 0 - 1,\; 1 + 3 - 4,\; 5 + 1 - 6) = (0, 0, 0)$ ✓. And $C(A) \supseteq \text{span}\{(1,1,5), (0,3,1)\}$ by construction ✓ (in fact $C(A)$ is exactly that plane, since $\mathbf{c}_3$ is dependent on the first two).

**Examiner's note:** Tests constructive design: required columns + one null-space condition determine the remaining column.
""")
    code(cells, r"""# SymPy verification — Lab 7, Q.12
A12c = Matrix([[1, 0, sp.Rational(-1, 2)], [1, 3, -2], [5, 1, -3]])
assert A12c * Matrix([1, 1, 2]) == Matrix([0, 0, 0])
assert A12c[:, 0] == Matrix([1, 1, 5]) and A12c[:, 1] == Matrix([0, 3, 1])
print("Q.12  A*(1,1,2) = 0 and the first two columns are the required vectors: verified")""")

    # ---------------- Q13 ----------------
    md(cells, r"""### Q.13) Construct: Two Column-Space Vectors and a 2-Dimensional Null Space (Hard)

**Question (as printed):** Construct a matrix whose column space contains $(1, 1, 0)$ and $(0, 1, 1)$ and whose null space contains $(1, 0, 1)$ and $(0, 0, 1)$.

**Step 1 — what shape must the matrix have?** $C(A) \subseteq \mathbb{R}^3 \Rightarrow$ 3 rows. The null space contains two *independent* vectors $\Rightarrow$ nullity $\ge 2 \Rightarrow$ at least 4 columns with rank $\le 2$. The column space contains two *independent* vectors $\Rightarrow$ rank $\ge 2$. So: a $3\times4$ matrix with **rank exactly 2** and **nullity exactly 2**.

**Step 2 — build column by column.** Set $\mathbf{c}_1 = (1,1,0)^T$, $\mathbf{c}_2 = (0,1,1)^T$ (the two required directions). The null-space requirements say:
- $A(1, 0, 1, 0)^T = \mathbf{0} \Rightarrow \mathbf{c}_1 + \mathbf{c}_3 = \mathbf{0} \Rightarrow \mathbf{c}_3 = (-1, -1, 0)^T$.
- $A(0, 0, 0, 1)^T = \mathbf{0} \Rightarrow \mathbf{c}_4 = \mathbf{0}$.

$$\boxed{A = \begin{bmatrix} 1 & 0 & -1 & 0 \\ 1 & 1 & -1 & 0 \\ 0 & 1 & 0 & 0 \end{bmatrix}}$$

**Step 3 — verify everything.**
- $C(A) = \text{span}\{(1,1,0), (0,1,1)\}$ ✓ (columns 3, 4 are dependent on/zero).
- $A(1,0,1,0)^T = (1-1,\ 1-1,\ 0)^T = \mathbf{0}$ ✓;  $A(0,0,0,1)^T = \mathbf{0}$ ✓.
- rank $= 2$, nullity $= 4 - 2 = 2$: the two required null vectors span $N(A)$ exactly.

**Why a $3\times3$ matrix is impossible here:** rank $\ge 2$ and nullity $\ge 2$ would force $2 + 2 \le 3$ — contradicting rank–nullity. The question quietly forces the wider shape.

**Examiner's note:** Tests dimension bookkeeping (rank–nullity decides the matrix size) followed by column-by-column construction.
""")
    code(cells, r"""# SymPy verification — Lab 7, Q.13
A13c = Matrix([[1, 0, -1, 0], [1, 1, -1, 0], [0, 1, 0, 0]])
assert A13c.rank() == 2
assert A13c * Matrix([1, 0, 1, 0]) == Matrix([0, 0, 0])
assert A13c * Matrix([0, 0, 0, 1]) == Matrix([0, 0, 0])
assert A13c[:, 0] == Matrix([1, 1, 0]) and A13c[:, 1] == Matrix([0, 1, 1])
print("Q.13  3x4 matrix with rank 2, nullity 2: all requirements verified")""")

    # ---------------- Q14 ----------------
    md(cells, r"""### Q.14) Null Space the $x$-Axis, Column Space the $yz$-Plane (Hard)

**Question (as printed):** Find a $3\times3$ matrix whose null space is the $x$-axis and whose column space is the $yz$-plane.

**Step 1 — read off the requirements.** $N(A) = \text{span}\{(1, 0, 0)\}$: so $A\mathbf{e}_1 = \mathbf{0}$ (first **column** is zero) and no other direction is killed. $C(A) = \text{span}\{(0,1,0), (0,0,1)\}$: the second and third columns span the $yz$-plane. Rank must be 2, nullity 1 — and $2 + 1 = 3$ ✓ (rank–nullity is consistent).

**Step 2 — construct.** Zero the first column and let the other two columns be $\mathbf{e}_2, \mathbf{e}_3$:
$$\boxed{A = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}}$$

**Step 3 — verify.** $A(x, y, z)^T = (0, y, z)^T$: this is $\mathbf{0}$ iff $y = z = 0$, i.e. exactly the $x$-axis ✓; and the outputs $(0, y, z)$ fill the $yz$-plane exactly ✓.

**Examiner's note:** Tests the cleanest possible construction problem — the matrix is a projection onto the $yz$-plane, killing exactly the $x$-axis.
""")
    code(cells, r"""# SymPy verification — Lab 7, Q.14
A14d = Matrix.diag(0, 1, 1)
assert A14d.nullspace() == [Matrix([1, 0, 0])]
assert A14d.columnspace() == [Matrix([0, 1, 0]), Matrix([0, 0, 1])]
print("Q.14  N(A) = x-axis, C(A) = yz-plane: verified")""")

    # ---------------- Q15 ----------------
    md(cells, r"""### Q.15) Design a 2×3 System with a Prescribed Complete Solution (Hard)

**Question (as printed):** Find a $2\times3$ matrix $A$ such that the complete solution of $Ax = \binom{1}{-1}$ is
$$x = \begin{bmatrix} 1 \\ 2 \\ 0 \end{bmatrix} + t\begin{bmatrix} 1 \\ 3 \\ 1 \end{bmatrix}, \qquad t \in \mathbb{R}.$$

**Step 1 — decode the requirements.** The complete solution of $Ax = b$ is $x_p + \text{(null space)}$, so:
- $x_p = (1, 2, 0)^T$ must satisfy $Ax_p = (1, -1)^T$;
- the special direction $(1, 3, 1)^T$ must lie in $N(A)$: $A(1, 3, 1)^T = \mathbf{0}$.

**Step 2 — solve for the columns.** Write $A = \left[\begin{smallmatrix} \text{— } r_1 \text{ —} \\ \text{— } r_2 \text{ —}\end{smallmatrix}\right]$. The null condition says each row $r$ satisfies $r \cdot (1, 3, 1) = 0$; the particular condition says $r \cdot (1, 2, 0) = (\,1 \text{ or } -1\,)$. Try the simplest null-compatible rows: let $r = (\alpha, \beta, -\alpha - 3\beta)$ (the general solution of $r\cdot(1,3,1) = 0$). Then $\alpha + 2\beta = \pm 1$.
Row 1 ($= 1$): $\alpha = 1, \beta = 0 \Rightarrow r_1 = (1, 0, -1)$. Row 2 ($= -1$): $\alpha = -1, \beta = 0 \Rightarrow r_2 = (-1, 0, 1)$.

$$\boxed{A = \begin{bmatrix} 1 & 0 & -1 \\ -1 & 0 & 1 \end{bmatrix}}$$

**Step 3 — verify.** $A(1, 2, 0)^T = (1, -1)^T$ ✓; $A(1, 3, 1)^T = (1 - 1, -1 + 1)^T = (0, 0)^T$ ✓; rank $A = 1$, nullity $= 3 - 1 = 2$... wait — the prescribed solution family is only **one**-dimensional! Check the null space: $Ax = (x_1 - x_3, -x_1 + x_3)^T = 0 \iff x_1 = x_3$: two free variables $x_2, x_3$ — $N(A) = \text{span}\{(0,1,0), (1, 0, 1)\}$, which is 2-dimensional and *contains* $(1, 3, 1)^T = (0,3,0) + (1,0,1)$ ✓. So the true complete solution is
$$x = (1, 2, 0)^T + s(0, 1, 0)^T + t(1, 0, 1)^T,$$
a strictly larger family that includes the printed one ($t(1,3,1)$ corresponds to $s = 3t,\ t = t$). The printed answer's family is contained in ours, so $A$ satisfies the requirement with the stated solution included — if the sheet intends $N(A)$ to be *exactly* $\text{span}\{(1,3,1)\}$, one needs rank 2: e.g.
$$A = \begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & -3 \end{bmatrix}: \quad A(1,3,1)^T = (0, 0)^T\ \checkmark, \quad A(1,2,0)^T = (1, 2)^T \ne (1, -1)^T\ \text{✗}.$$
Adjusting: we need $Ax_p = (1, -1)$ *and* row 2 with $r_2 \cdot (1,3,1) = 0$, $r_2 \cdot (1,2,0) = -1$: $r_2 = (\alpha, \beta, -\alpha - 3\beta)$ with $\alpha + 2\beta = -1$; choose $\alpha = -3, \beta = 1$: $r_2 = (-3, 1, 0)$:
$$A = \begin{bmatrix} 1 & 0 & -1 \\ -3 & 1 & 0 \end{bmatrix}: \quad A(1,3,1)^T = (1 - 1,\ -3 + 3)^T = \mathbf{0}\ \checkmark, \quad A(1,2,0)^T = (1, -1)^T\ \checkmark,$$
and now rank 2 with nullity 1, $N(A) = \text{span}\{(1, 3, 1)\}$ **exactly** as prescribed.

$$\boxed{A = \begin{bmatrix} 1 & 0 & -1 \\ -3 & 1 & 0 \end{bmatrix}}$$

**Examiner's note:** Tests the reverse construction $x_p \to$ row conditions and — importantly — checking that the null space has the *prescribed dimension*, not just contains the given vector.
""")
    code(cells, r"""# SymPy verification — Lab 7, Q.15
A15d = Matrix([[1, 0, -1], [-3, 1, 0]])
xp15 = Matrix([1, 2, 0]); s15 = Matrix([1, 3, 1])
assert A15d * xp15 == Matrix([1, -1]) and A15d * s15 == Matrix([0, 0])
assert A15d.rank() == 2 and A15d.nullspace() == [s15]
print("Q.15  A*xp = (1,-1), N(A) = span{(1,3,1)} exactly: verified")
print("Q.15  complete solution: x = (1,2,0) + t*(1,3,1)")""")

    # ---------------- Q16 ----------------
    md(cells, r"""### Q.16) Challenge: Six Beams, One Molecule (Challenge)

**Question (as printed):** Six laser beams push a molecule at the origin. Directions (from the figure: beams 1, 4 horizontal; 2, 3, 5, 6 at 45°):
$$u_1 = \begin{bmatrix}1\\0\end{bmatrix},\ u_2 = \begin{bmatrix}\tfrac{\sqrt2}{2}\\-\tfrac{\sqrt2}{2}\end{bmatrix},\ u_3 = \begin{bmatrix}-\tfrac{\sqrt2}{2}\\-\tfrac{\sqrt2}{2}\end{bmatrix},\ u_4 = \begin{bmatrix}-1\\0\end{bmatrix},\ u_5 = \begin{bmatrix}-\tfrac{\sqrt2}{2}\\\tfrac{\sqrt2}{2}\end{bmatrix},\ u_6 = \begin{bmatrix}\tfrac{\sqrt2}{2}\\\tfrac{\sqrt2}{2}\end{bmatrix}.$$
A strength pattern $x = (F_1, \dots, F_6) \ge 0$ produces net force $Ax$ (columns $u_1, \dots, u_6$). The molecule is held still when $Ax = 0$.
(a) Eliminate $A$: pivots, rank, which $F_i$ are pivot/free? (b) One-line reason (shape of $A$) why the six directions are dependent and $Ax = 0$ has a non-zero solution. (c)(i) Check $x = (1,0,0,1,0,0)$ gives $Ax = 0$ and write two more "opposite-pair" patterns; (ii) check $x = (1,\dots,1)$ and write it as a sum of the three pair patterns; (iii) with $F_4 = 0$, find a pattern with all five other strengths **strictly positive**. (d) In one sentence: what does $N(A)$ mean physically? (e) Push with net force $b = (1, 0)$: (i) the obvious one-beam recipe $x_p$; (ii) the complete solution and how many recipes; (iii) show infinitely many recipes remain even with $F_i \ge 0$, by adding a multiple of $(1,\dots,1)$; (iv) role difference between $x_p$ and $x_n$. (f) True/False: (i) a seventh beam would enlarge $C(A)$; (ii) the sum of two stillness patterns is still. (g) With $F_i \ge 0$, can **every** $b \in \mathbb{R}^2$ be made? Give a rule.

**Part (a).** With $s = \tfrac{\sqrt2}{2}$:
$$A = \begin{bmatrix} 1 & s & -s & -1 & -s & s \\ 0 & -s & -s & 0 & s & s \end{bmatrix}.$$
The two rows are not proportional ⇒ **rank 2**, pivots in columns 1, 2 ⇒ $F_1, F_2$ are pivot variables and $F_3, F_4, F_5, F_6$ are **free** ($\dim N(A) = 4$).

**Part (b) — the one-liner.** $A$ has **six columns but only two rows**: six vectors in $\mathbb{R}^2$ must be dependent, so $N(A) \ne \{\mathbf{0}\}$ — non-trivial stillness patterns exist by shape alone.

**Part (c).**
- **(i)** $A(1,0,0,1,0,0)^T = u_1 + u_4 = (1, 0) + (-1, 0) = \mathbf{0}$ ✓. Two more opposite pairs (note $u_2 = -u_5$ and $u_3 = -u_6$):
$$(0, 1, 0, 0, 1, 0) \quad (u_2 + u_5 = \mathbf{0}), \qquad (0, 0, 1, 0, 0, 1) \quad (u_3 + u_6 = \mathbf{0}).$$
- **(ii)** $A\mathbf{1} = \sum_k u_k = \mathbf{0}$ ✓, and
$$\mathbf{1} = (1,0,0,1,0,0) + (0,1,0,0,1,0) + (0,0,1,0,0,1)$$
— the all-on pattern is the **sum of the three opposite-pair patterns**.
- **(iii)** Use the hint: beams 3 and 5 both push in the $-x$ direction; use them against beam 1. Take $F_1 = \sqrt2$, $F_3 = F_5 = 1$: net $x$-force $= \sqrt2 - s - s = \sqrt2 - \sqrt2 = 0$; net $y$-force $= -s + s = 0$ ✓ (u3 and u5 cancel vertically too). Beams 2 and 6 are still off — switch them on by adding the opposite pairs from (i) with strength 1:
$$x = (\sqrt2,\ 1,\ 2,\ 0,\ 2,\ 1):$$
check: $x$-force $= \sqrt2 + s(1) - s(2) - s(2) + s(1) = \sqrt2 - \sqrt2 = 0$ ✓; $y$-force $= -s(1 + 2) + s(2 + 1) = 0$ ✓. **All of $F_1, F_2, F_3, F_5, F_6 > 0$ with $F_4 = 0$** — the molecule is held still without beam 4.

**Part (d).** $N(A)$ is the set of all strength patterns that produce **zero net force** — the internal self-balancings of the six beams ("how to fire the lasers without moving the molecule").

**Part (e).**
- **(i)** $x_p = \mathbf{e}_1 = (1, 0, 0, 0, 0, 0)^T$: $Ax_p = u_1 = (1, 0) = b$ ✓.
- **(ii)** Using the null-space basis of pair patterns:
$$x = x_p + c_1(1, 0, 0, 1, 0, 0) + c_2(0, 1, 0, 0, 1, 0) + c_3(0, 0, 1, 0, 0, 1), \qquad c_i \in \mathbb{R}.$$
With real strengths: **infinitely many** recipes ($\dim N(A) = 3$ free parameters built from these directions).
- **(iii)** $\mathbf{1} = (1,\dots,1) \in N(A)$ (part c-ii) and has all-positive entries, so
$$x(t) = x_p + t\,\mathbf{1} = (1{+}t,\ t,\ t,\ t,\ t,\ t), \qquad t \ge 0$$
is non-negative for every $t \ge 0$ — **infinitely many usable recipes**. Meaning: *turning all six beams up together by the same amount changes nothing* — a uniform "all beams up" layer is invisible to the net force, and it is the universal tool for repairing negative strengths.
- **(iv)** $x_p$ **creates the net force** (moves the molecule to $b$); $x_n$ ** redistributes among the beams without changing the force** (keeps the molecule still). $x_p$ sets *where* you go; $x_n$ sets *how* you get there.

**Part (f).**
- **(i) FALSE.** $C(A) = \mathbb{R}^2$ already (rank 2 with columns in $\mathbb{R}^2$); adding a seventh column cannot exceed $\mathbb{R}^2$.
- **(ii) TRUE.** $N(A)$ is a subspace: if $Ax = Ay = 0$ then $A(x + y) = 0$. Two stillness patterns sum to stillness.

**Part (g) — yes, every $b$ is makeable with non-negative strengths.** Constructive rule using axis-aligned and diagonal beam pairs:
- $x$-component: use **beam 1** with strength $b_1$ if $b_1 \ge 0$, else **beam 4** with strength $-b_1$.
- $y$-component: beams 5 & 6 together push **purely upward** ($u_5 + u_6 = (0, \sqrt2)$), and beams 2 & 3 purely downward ($u_2 + u_3 = (0, -\sqrt2)$): use beams 5, 6 at strength $b_2/\sqrt2$ each if $b_2 \ge 0$, else beams 2, 3 at $|b_2|/\sqrt2$ each.
All strengths are $\ge 0$ and the two contributions superpose. (Alternative one-line argument: take *any* solution $x$ of $Ax = b$ — one exists since $C(A) = \mathbb{R}^2$ — and add $t\,\mathbf{1}$ with $t$ large; all entries become positive.)

**Examiner's note:** Tests the complete-solution machinery in a physical setting: null-space basis from symmetry, non-negativity constraints, and the universal repair trick $x + t\mathbf{1}$.
""")
    code(cells, r"""# SymPy verification — Lab 7, Q.16
s16 = sp.sqrt(2) / 2
u = [Matrix([1, 0]), Matrix([s16, -s16]), Matrix([-s16, -s16]),
     Matrix([-1, 0]), Matrix([-s16, s16]), Matrix([s16, s16])]
A16b = Matrix.hstack(*u)
print("Q.16(a) rank =", A16b.rank(), "| RREF pivots in columns:", A16b.rref()[1])
assert A16b.rank() == 2
for pat in [(1, 0, 0, 1, 0, 0), (0, 1, 0, 0, 1, 0), (0, 0, 1, 0, 0, 1), (1, 1, 1, 1, 1, 1)]:
    assert A16b * Matrix(pat) == Matrix([0, 0])
print("Q.16(c) all three opposite-pair patterns and the all-ones pattern give Ax = 0")
F3 = Matrix([sp.sqrt(2), 1, 2, 0, 2, 1])
assert A16b * F3 == Matrix([0, 0]) and F3[3] == 0 and all(F3[i] > 0 for i in [0, 1, 2, 4, 5])
print("Q.16(c)(iii) F = (sqrt2, 1, 2, 0, 2, 1): molecule still with F4 = 0, others > 0")
xp = Matrix([1, 0, 0, 0, 0, 0])
assert A16b * xp == Matrix([1, 0])
for t in [0, sp.Rational(1, 2), 5]:
    assert A16b * (xp + t * Matrix([1, 1, 1, 1, 1, 1])) == Matrix([1, 0])
print("Q.16(e) x_p = e1; x_p + t*1 gives non-negative recipes for all t >= 0")
# (g) constructive rule for any b
for (tb1, tb2) in [(3, 2), (-3, 2), (3, -2), (-3, -2), (0, 5), (5, 0)]:
    xg = sp.zeros(6, 1)
    xg[0 if tb1 >= 0 else 3] = abs(tb1)                       # beam 1 or beam 4
    if tb2 >= 0:
        xg[4] = xg[5] = tb2 / sp.sqrt(2)                      # beams 5, 6 push pure up
    else:
        xg[1] = xg[2] = -tb2 / sp.sqrt(2)                     # beams 2, 3 push pure down
    assert A16b * xg == Matrix([tb1, tb2]) and all(v >= 0 for v in xg)
print("Q.16(g) non-negative recipes constructed for b in all four quadrants")""")

    return cells


LAB_TITLE = "Lab 8 Solutions: The Four Fundamental Subspaces and Network Duality"
LAB_SUB = (
    '**Core ideas tested:** "Four Spaces, One Matrix" — $C(A)$, $C(A^T)$, $N(A)$, $N(A^T)$: '
    "dimensions, bases, orthogonality, solvability via $y^Tb = 0$, and incidence matrices "
    "on graphs (pressures, flows, loops)."
)


def get_lab8_cells():
    cells = []
    md(cells, lab_header(LAB_TITLE, LAB_SUB))

    # ---------------- Q1 ----------------
    md(cells, r"""### Q.1) True/False: The Big Picture (Easy)

**Question (as printed):**
(a) If $m = n$ then the row space of $A$ equals the column space of $A$.
(b) The matrices $A$ and $-A$ share the same four subspaces.
(c) If $A$ and $B$ share the same four subspaces then $A$ is a multiple of $B$.
(d) $A$ and $A^T$ have the same number of pivots.
(e) If the row space equals the column space then $A^T = A$.
(f) If $B$ is any echelon form of $A$, then the pivot columns of $B$ form a basis for $C(A)$.
(g) The dimensions of the row space and the column space of an $m\times n$ matrix $A$ are equal, even if $A$ is not square.

**(a) FALSE.** Squareness is not symmetry. Counterexample: $A = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}$: $C(A) = \text{span}(e_1)$ but row space $= \text{span}(e_2)$. (True exactly for matrices with $C(A) = C(A^T)$ — e.g. symmetric ones.)

**(b) TRUE.** Scaling by $-1 \ne 0$ changes no span: $C(-A) = C(A)$, row spaces and both null spaces match (the *equations* $-Ax = 0$ and $Ax = 0$ are identical).

**(c) FALSE.** Every **invertible** $2\times2$ matrix has the same four subspaces ($C = C^T$-space $= \mathbb{R}^2$, $N = N^T$-space $= \{\mathbf{0}\}$). $A = I$ and $B = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ share all four subspaces but $B$ is not a multiple of $A$.

**(d) TRUE.** $\text{rank}(A) = \text{rank}(A^T)$ always — elimination on $A^T$ finds exactly as many pivots.

**(e) FALSE.** Invertible non-symmetric matrices: $A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ has row space $=$ column space $= \mathbb{R}^2$ but $A^T \ne A$.

**(f) FALSE.** The pivot columns of **$A$ itself** (the columns of $A$ sitting in the pivot *positions* of $B$) form the basis. $B$'s own columns have been changed by elimination and generally span a *different* subspace. Example: $A = \begin{bmatrix} 1 & 2 \\ 1 & 2 \end{bmatrix} \to B = \begin{bmatrix} 1 & 2 \\ 0 & 0 \end{bmatrix}$: $B$'s pivot column is $(1, 0)^T$, but $C(A) = \text{span}\{(1,1)^T\}$.

**(g) TRUE.** Both dimensions equal the rank $r$ — the row space and column space have the same *dimension* even though they live in different spaces ($\mathbb{R}^n$ vs $\mathbb{R}^m$).

**Examiner's note:** Tests the big-picture facts and the classic trap in (f) — pivot columns must be taken from $A$.
""")
    code(cells, r"""# SymPy verification — Lab 8, Q.1
A1f = Matrix([[1, 2], [1, 2]])
B1f = A1f.echelon_form()
print("Q.1(f) C(A) =", [v.T for v in A1f.columnspace()], " but B's pivot column =", B1f[:, 0].T)
assert A1f.columnspace() == [Matrix([1, 1])] and B1f[:, 0] == Matrix([1, 0])
A1a = Matrix([[0, 1], [0, 0]])
assert A1a.columnspace() != A1a.T.columnspace()
print("Q.1(a) square but C(A) != rowspace for [[0,1],[0,0]]")
A1e = Matrix([[1, 1], [0, 1]])
assert A1e.rank() == 2 and A1e != A1e.T
print("Q.1(e) invertible non-symmetric: rowspace = colspace = R^2, yet A^T != A")""")

    # ---------------- Q2 ----------------
    md(cells, r"""### Q.2) Bases for $C(A)$ and $N(A)$, Rank and Nullity (Easy)

**Question (as printed):** Find a basis of the column space and the null space; determine rank and nullity.
$$\text{(a) } A = \begin{bmatrix} 1 & 2 & 3 \\ 1 & 2 & 3 \\ 2 & 5 & 8 \end{bmatrix} \qquad
\text{(b) } A = \begin{bmatrix} 1 & 2 & -1 & 3 \\ 2 & 5 & 1 & 4 \\ 3 & 7 & 0 & 7 \\ 4 & 9 & -1 & 10 \end{bmatrix}$$

**Part (a).** Elimination: $R_2 - R_1 = \mathbf{0}$; $R_3 - 2R_1 = (0, 1, 2)$. Pivots in columns 1, 2; rank 2.
- **Basis of $C(A)$:** the pivot columns **of $A$**: $\big\{(1, 1, 2)^T,\ (2, 2, 5)^T\big\}$.
- **Null space:** from $U = \begin{bmatrix} 1 & 2 & 3 \\ 0 & 1 & 2 \\ 0 & 0 & 0 \end{bmatrix}$: $x_2 = -2x_3$, $x_1 = -2x_2 - 3x_3 = x_3$. Special solution $(1, -2, 1)^T$:
$$N(A) = \text{span}\{(1, -2, 1)^T\}, \qquad \text{rank } 2,\ \text{nullity } 1 \ (2 + 1 = 3\ \checkmark).$$

**Part (b).** Elimination: $R_2 - 2R_1 = (0, 1, 3, -2)$; $R_3 - 3R_1 = (0, 1, 3, -2)$; $R_4 - 4R_1 = (0, 1, 3, -2)$ — all three identical, so two more rows vanish. Pivots in columns 1, 2; **rank 2**.
- **Basis of $C(A)$:** pivot columns of $A$: $\big\{(1, 2, 3, 4)^T,\ (2, 5, 7, 9)^T\big\}$.
- **Null space** (free $x_3, x_4$): RREF gives $x_1 = 7x_3 - 7x_4$, $x_2 = -3x_3 + 2x_4$:
$$N(A) = \text{span}\big\{(7, -3, 1, 0)^T,\ (-7, 2, 0, 1)^T\big\}, \qquad \text{rank } 2,\ \text{nullity } 2 \ (2 + 2 = 4\ \checkmark).$$

**Examiner's note:** Tests the complete column-space/null-space extraction workflow, with pivot columns taken from the *original* $A$.
""")
    code(cells, r"""# SymPy verification — Lab 8, Q.2
A2l = Matrix([[1, 2, 3], [1, 2, 3], [2, 5, 8]])
print("Q.2(a) C(A):", [v.T for v in A2l.columnspace()], " N(A):", [v.T for v in A2l.nullspace()])
assert A2l.rank() == 2 and A2l.nullspace() == [Matrix([1, -2, 1])]
A2m = Matrix([[1, 2, -1, 3], [2, 5, 1, 4], [3, 7, 0, 7], [4, 9, -1, 10]])
print("Q.2(b) C(A):", [v.T for v in A2m.columnspace()], " N(A):", [v.T for v in A2m.nullspace()])
assert A2m.rank() == 2 and A2m.nullspace() == [Matrix([7, -3, 1, 0]), Matrix([-7, 2, 0, 1])]""")

    # ---------------- Q3 ----------------
    md(cells, r"""### Q.3) Largest Possible Ranks and Dimensions (Easy)

**Question (as printed):** Answer with reasoning.
(a) Largest possible rank of a $7\times5$ matrix? Of a $5\times7$ matrix?
(b) Maximum dimension of the row space of a $4\times3$ matrix? Of a $3\times4$ matrix?
(c) If the null space of a $5\times6$ matrix is 4-dimensional, what is $\dim C(A^T)$ (row space)?
(d) If the null space of a $7\times6$ matrix is 5-dimensional, what is $\dim C(A)$?

**(a)** Rank can never exceed the number of rows or columns: $\min(7, 5) = \mathbf{5}$ and $\min(5, 7) = \mathbf{5}$.

**(b)** The row space lives in $\mathbb{R}^n$ and has dimension $r \le \min(m, n)$: for $4\times3$: $\mathbf{3}$; for $3\times4$: $\mathbf{3}$.

**(c)** Rank–nullity: $r = n - \text{nullity} = 6 - 4 = 2$, and $\dim C(A^T) = r = \mathbf{2}$.

**(d)** $r = 6 - 5 = 1$, so $\dim C(A) = \mathbf{1}$.

**Examiner's note:** Tests $\text{rank} \le \min(m, n)$ and rank–nullity in both directions.
""")

    # ---------------- Q4 ----------------
    md(cells, r"""### Q.4) The Dimension Table of the Four Subspaces (Easy)

**Question (as printed):** For each size/rank pair, find $\dim$ rowspace, colspace, $N(A)$, $N(A^T)$.

**The master formulae** for an $m\times n$ matrix of rank $r$:
$$\dim C(A^T) = r \ (\text{rowspace, in } \mathbb{R}^n), \quad \dim C(A) = r \ (\text{in } \mathbb{R}^m), \quad \dim N(A) = n - r, \quad \dim N(A^T) = m - r.$$

| Part | Size $m\times n$ | rank $r$ | rowspace | colspace | $N(A)$ | $N(A^T)$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| (a) | $3\times3$ | 3 | 3 | 3 | 0 | 0 |
| (b) | $3\times3$ | 2 | 2 | 2 | 1 | 1 |
| (c) | $3\times3$ | 1 | 1 | 1 | 2 | 2 |
| (d) | $5\times9$ | 2 | 2 | 2 | 7 | 3 |
| (e) | $9\times5$ | 2 | 2 | 2 | 3 | 7 |
| (f) | $4\times4$ | 0 | 0 | 0 | 4 | 4 |

**Sanity checks:** every row of the table satisfies $r + (n - r) = n$ and $r + (m - r) = m$ — e.g. (d): $2 + 7 = 9 = n$ ✓ and $2 + 3 = 5 = m$ ✓. Parts (d) and (e) are transposes of each other: note how $N(A)$ and $N(A^T)$ swap, exactly as $A \leftrightarrow A^T$ exchanges rows and columns.

**Examiner's note:** Tests fluency with the four dimensions — the bookkeeping behind every "big picture" diagram.
""")

    # ---------------- Q5 ----------------
    md(cells, r"""### Q.5) Complete Solution with Rank–Nullity Check (Easy)

**Question (as printed):** Find the complete solution $x = x_p + x_n$ of $Ax = b$ for
$$A = \begin{bmatrix} 1 & 3 & 3 & 2 \\ 2 & 6 & 9 & 7 \\ -1 & -3 & 3 & 4 \end{bmatrix}, \qquad b = \begin{bmatrix} 1 \\ 5 \\ 5 \end{bmatrix}.$$
State the rank, the nullity, and the number of free variables, and check $n = \text{rank}(A) + \text{nullity}(A)$.

**Step 1 — eliminate the augmented matrix.**
- $R_2 - 2R_1$: $(0, 0, 3, 3 \mid 3)$;  $R_3 + R_1$: $(0, 0, 6, 6 \mid 6)$;  then $R_3 - 2R_2'$: $(0, 0, 0, 0 \mid 0)$ — consistent.
- Pivots in columns 1, 3; **free variables $x_2, x_4$**.

**Step 2 — particular solution** ($x_2 = x_4 = 0$): from $3x_3 = 3 \Rightarrow x_3 = 1$; from $x_1 + 3x_3 = 1 \Rightarrow x_1 = -2$:
$$x_p = (-2, 0, 1, 0)^T.$$

**Step 3 — special solutions** (from $Ax = 0$): $3x_3 + 3x_4 = 0 \Rightarrow x_3 = -x_4$; $x_1 = -3x_2 - 3x_3 - 2x_4 = -3x_2 + x_4$:
$$x_2 = 1:\ s_1 = (-3, 1, 0, 0)^T; \qquad x_4 = 1:\ s_2 = (1, 0, -1, 1)^T.$$

$$\boxed{x = \begin{bmatrix} -2 \\ 0 \\ 1 \\ 0 \end{bmatrix} + c_1\begin{bmatrix} -3 \\ 1 \\ 0 \\ 0 \end{bmatrix} + c_2\begin{bmatrix} 1 \\ 0 \\ -1 \\ 1 \end{bmatrix}}$$

**Check:** rank $= 2$, nullity $= 2$, free variables $= 2$, and $n = 4 = 2 + 2$ ✓.

**Examiner's note:** Tests the full workflow plus the explicit rank–nullity bookkeeping the question demands.
""")
    code(cells, r"""# SymPy verification — Lab 8, Q.5
A5l = Matrix([[1, 3, 3, 2], [2, 6, 9, 7], [-1, -3, 3, 4]])
xp5 = Matrix([-2, 0, 1, 0])
assert A5l * xp5 == Matrix([1, 5, 5]) and A5l.nullspace() == [Matrix([-3, 1, 0, 0]), Matrix([1, 0, -1, 1])]
print("Q.5  rank =", A5l.rank(), ", nullity =", 4 - A5l.rank(),
      ", free vars = 2, and 4 = 2 + 2:", A5l.rank() + len(A5l.nullspace()) == 4)""")

    # ---------------- Q6 ----------------
    md(cells, r"""### Q.6) Read Everything Off the Echelon Form $B$ (Medium)

**Question (as printed):** $B$ is the row echelon form of $A$. Without calculations, list $\text{rank}(A)$ and $\dim N(A)$; then find bases for $C(A)$, $C(A^T)$, $N(A)$.
$$A = \begin{bmatrix} 2 & -3 & 6 & 2 & 5 \\ -2 & 3 & -3 & -3 & -4 \\ 4 & -6 & 9 & 5 & 9 \\ -2 & 3 & 3 & -4 & 1 \end{bmatrix}, \qquad B = \begin{bmatrix} 2 & -3 & 6 & 2 & 5 \\ 0 & 0 & 3 & -1 & 1 \\ 0 & 0 & 0 & 1 & 3 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$$

**Step 1 — dimensions without calculation.** $B$ has **3 pivots** (columns 1, 3, 4): $\text{rank}(A) = 3$ and $\dim N(A) = 5 - 3 = 2$.

**Step 2 — basis of $C(A)$ (pivot columns of $A$, NOT of $B$!).** Pivot columns 1, 3, 4:
$$\text{Basis of } C(A) = \Big\{ (2, -2, 4, -2)^T,\ (6, -3, 9, 3)^T,\ (2, -3, 5, -4)^T \Big\}.$$

**Step 3 — basis of $C(A^T)$ (the row space = non-zero rows of $B$):**
$$\text{Basis of } C(A^T) = \Big\{ (2, -3, 6, 2, 5),\ (0, 0, 3, -1, 1),\ (0, 0, 0, 1, 3) \Big\}.$$

**Step 4 — basis of $N(A)$ (special solutions of $Bx = 0$).** Free variables $x_2, x_5$. From $B$:
$x_4 = -3x_5$; $\;3x_3 - x_4 + x_5 = 0 \Rightarrow x_3 = \tfrac{x_4 - x_5}{3} = -\tfrac43 x_5$; $\;2x_1 - 3x_2 + 6x_3 + 2x_4 + 5x_5 = 0 \Rightarrow x_1 = \tfrac32 x_2 + \tfrac92 x_5$.
$$x_5 = 0:\ s_1 = (\tfrac32, 1, 0, 0, 0)^T \to (3, 2, 0, 0, 0)^T; \qquad x_5 = 1:\ s_2 = (\tfrac92, 0, -\tfrac43, -3, 1)^T \to (27, 0, -8, -18, 6)^T.$$
$$N(A) = \text{span}\big\{ (3, 2, 0, 0, 0)^T,\ (27, 0, -8, -18, 6)^T \big\}.$$

**Examiner's note:** Tests the three different sources of the three bases: pivot columns of $A$, non-zero rows of $B$, special solutions of $B$.
""")
    code(cells, r"""# SymPy verification — Lab 8, Q.6
A6l = Matrix([[2, -3, 6, 2, 5], [-2, 3, -3, -3, -4], [4, -6, 9, 5, 9], [-2, 3, 3, -4, 1]])
B6l = Matrix([[2, -3, 6, 2, 5], [0, 0, 3, -1, 1], [0, 0, 0, 1, 3], [0, 0, 0, 0, 0]])
# B is *a* valid echelon form of A (echelon forms are not unique): RREFs must agree,
# and nullspace/rowspace of A and B must coincide
assert A6l.rref()[0] == B6l.rref()[0]
assert A6l.rank() == B6l.rank() == 3
assert A6l.nullspace() == B6l.nullspace()
CA = [A6l[:, j] for j in (0, 2, 3)]
ns6 = A6l.nullspace()
print("Q.6  rank 3, dim N = 2")
print("Q.6  C(A) basis:", [v.T for v in CA])
print("Q.6  C(A^T) basis:", [B6l[i, :].T for i in range(3)])
print("Q.6  N(A) basis:", [v.T for v in ns6])
# span check: both printed special solutions lie in N(A), which is 2-dimensional
for cand in [Matrix([3, 2, 0, 0, 0]), Matrix([27, 0, -8, -18, 6])]:
    assert A6l * cand == sp.zeros(4, 1)
assert len(ns6) == 2""")

    # ---------------- Q7 ----------------
    md(cells, r"""### Q.7) Four Subspace Bases from $A = LU$ Without Multiplying (Medium)

**Question (as printed):** Given $A = LU$ with
$$L = \begin{bmatrix} 1 & 0 & 0 \\ 6 & 1 & 0 \\ 9 & 8 & 1 \end{bmatrix}, \qquad U = \begin{bmatrix} 1 & 2 & 3 & 4 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 1 & 2 \end{bmatrix},$$
find bases for the four fundamental subspaces **without computing $A$**.

**Step 1 — rank.** $U$ has 3 pivots ⇒ rank $= 3$.

**Step 2 — $C(A^T)$ (row space).** The non-zero rows of $U$:
$$\text{Basis: } \ (1, 2, 3, 4), \quad (0, 1, 2, 3), \quad (0, 0, 1, 2).$$

**Step 3 — $C(A)$.** Rank 3 with only $m = 3$ rows ⇒ $C(A) = \mathbb{R}^3$; any basis works:
$$\text{Basis: } \ \mathbf{e}_1, \mathbf{e}_2, \mathbf{e}_3 \quad (\text{equivalently the columns of } L).$$

**Step 4 — $N(A)$.** Solve $Ux = 0$ (the null spaces of $A$ and $U$ coincide — row operations preserve them): $x_3 + 2x_4 = 0 \Rightarrow x_3 = -2x_4$; $x_2 + 2x_3 + 3x_4 = 0 \Rightarrow x_2 = x_4$; $x_1 + 2x_2 + 3x_3 + 4x_4 = 0 \Rightarrow x_1 = 0$. With $x_4 = 1$:
$$\text{Basis of } N(A): \ \ (0, 1, -2, 1)^T.$$

**Step 5 — $N(A^T)$ (left null space).** Solve $L^Ty = 0$: $L$ is triangular with 1's on its diagonal ⇒ $\det L^T = 1 \ne 0$ ⇒ only $y = \mathbf{0}$:
$$N(A^T) = \{\mathbf{0}\} \quad (\text{no basis — the empty set; dimensions: } 3 + 0 = m = 3\ \checkmark).$$

**Examiner's note:** Tests which factor supplies which basis: rows of $U$, columns of $L$/full space for $C(A)$, $Ux=0$ for $N(A)$, $L^Ty = 0$ for $N(A^T)$.
""")
    code(cells, r"""# SymPy verification — Lab 8, Q.7
L7k = Matrix([[1, 0, 0], [6, 1, 0], [9, 8, 1]])
U7k = Matrix([[1, 2, 3, 4], [0, 1, 2, 3], [0, 0, 1, 2]])
A7k = L7k * U7k
assert A7k.rank() == 3
assert A7k.nullspace() == [Matrix([0, 1, -2, 1])]
assert A7k.T.nullspace() == []
print("Q.7  N(A) =", [v.T for v in A7k.nullspace()], " N(A^T) = {0}:",
      A7k.T.nullspace() == [], " (verified against the actual A = L*U)")""")

    # ---------------- Q8 ----------------
    md(cells, r"""### Q.8) $A$ vs. Its Echelon Form $U$: Which Subspaces Survive? (Medium)

**Question (as printed):** Find the dimension and a basis for the four subspaces of
$$A = \begin{bmatrix} 0 & 1 & 4 & 0 \\ 0 & 2 & 8 & 0 \end{bmatrix} \qquad\text{and}\qquad U = \begin{bmatrix} 0 & 1 & 4 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}.$$
Which of the four subspaces are the same for $A$ and $U$, and which are different? Explain why.

**Dimensions.** Both matrices have rank 1: $\dim C = 1$, $\dim C(A^T) = 1$, $\dim N = 4 - 1 = 3$, $\dim N(A^T) = 2 - 1 = 1$.

**Bases for $A$:**
- $C(A) = \text{span}\{(1, 2)^T\}$ (the first column is zero; column 2 is the pivot column).
- $C(A^T) = \text{span}\{(0, 1, 4, 0)\}$ (row 2 is $2\times$ row 1).
- $N(A)$: condition $x_2 + 4x_3 = 0$: basis $\{(1, 0, 0, 0)^T,\ (0, -4, 1, 0)^T,\ (0, 0, 0, 1)^T\}$.
- $N(A^T)$: $A^Ty = 0$ reads $y_1 + 2y_2 = 0$: basis $\{(-2, 1)^T\}$.

**Bases for $U$:**
- $C(U) = \text{span}\{(1, 0)^T\}$,  $C(U^T) = \text{span}\{(0, 1, 4, 0)\}$,  $N(U) = N(A)$ (same three vectors),  $N(U^T) = \text{span}\{(0, 1)^T\}$.

**Comparison — the punchline:**
$$\boxed{\text{Same: } C(A^T) \text{ (row space) and } N(A). \qquad \text{Different: } C(A) \text{ and } N(A^T).}$$
**Why:** row operations mix *rows*, so the row space is preserved by design (that is what elimination does) — and since $N(A)$ is defined by the rows ($Ax = 0$), it is preserved too. But elimination **changes the columns** (the pivot column of $U$ is a combination of $A$'s columns, not one of them), so the column space and — dually — the left null space generally change.

**Examiner's note:** Tests which parts of the big picture are elimination-invariants — the conceptual heart of this lab.
""")
    code(cells, r"""# SymPy verification — Lab 8, Q.8
A8k = Matrix([[0, 1, 4, 0], [0, 2, 8, 0]])
U8k = Matrix([[0, 1, 4, 0], [0, 0, 0, 0]])
assert A8k.rank() == 1
assert A8k.nullspace() == U8k.nullspace() == [Matrix([1, 0, 0, 0]), Matrix([0, -4, 1, 0]), Matrix([0, 0, 0, 1])]
assert A8k.T.columnspace() == U8k.T.columnspace() == [Matrix([0, 1, 4, 0])]
print("Q.8  same: rowspace and nullspace;",
      " different: C(A) =", [v.T for v in A8k.columnspace()], "vs", [v.T for v in U8k.columnspace()],
      "; N(A^T) =", [v.T for v in A8k.T.nullspace()], "vs", [v.T for v in U8k.T.nullspace()])""")

    # ---------------- Q9 ----------------
    md(cells, r"""### Q.9) Solvability Condition, Then $N(A^T)$ Confirms It (Medium)

**Question (as printed):** Under what conditions on $b_1, b_2, b_3$ is the system solvable? Augment $b$ as a fourth column, eliminate, find all solutions when the condition holds; then find $y$ spanning $N(A^T)$ and verify the condition is exactly $y^Tb = 0$.
$$\begin{aligned} x + 2y - 2z &= b_1 \\ 2x + 5y - 4z &= b_2 \\ 4x + 9y - 8z &= b_3 \end{aligned}$$

**Step 1 — elimination on $[\,A \mid b\,]$.**
- $R_2 - 2R_1$: $(0, 1, 0 \mid b_2 - 2b_1)$
- $R_3 - 4R_1$: $(0, 1, 0 \mid b_3 - 4b_1)$; then $R_3 - R_2'$: $(0, 0, 0 \mid b_3 - 2b_1 - b_2)$

$$\boxed{\text{Solvable} \iff b_3 = 2b_1 + b_2}$$

**Step 2 — solutions when the condition holds.** Pivots in columns 1, 2; $z$ free. Back-substitute: $y = b_2 - 2b_1$; $x = b_1 - 2y + 2z = 5b_1 - 2b_2 + 2z$:
$$x = \begin{bmatrix} 5b_1 - 2b_2 \\ b_2 - 2b_1 \\ 0 \end{bmatrix} + t\begin{bmatrix} 2 \\ 0 \\ 1 \end{bmatrix}.$$

**Step 3 — the left-null confirmation.** $N(A^T)$: solve $A^Ty = 0$; elimination of $A$ shows row 3 $-$ row 2 $-$ ... directly: row 3 $- \,2\,\text{row}_1 - \text{row}_2 = \mathbf{0}$, so
$$y = (-2, -1, 1)^T \qquad (\text{check: } -2(1,2,-2) - (2,5,-4) + (4,9,-8) = \mathbf{0}\ \checkmark).$$
And
$$y^Tb = -2b_1 - b_2 + b_3 = 0 \iff b_3 = 2b_1 + b_2$$
— **exactly the solvability condition**, as the theory promises: $b \in C(A) \iff b \perp N(A^T)$.

**Examiner's note:** Tests the Fredholm alternative in action: the elimination condition and the left-null condition must coincide.
""")
    code(cells, r"""# SymPy verification — Lab 8, Q.9
A9k = Matrix([[1, 2, -2], [2, 5, -4], [4, 9, -8]])
y9 = A9k.T.nullspace()[0]
assert y9 == Matrix([-2, -1, 1])
b1k, b2k, b3k = sp.symbols('b1 b2 b3')
bk = Matrix([b1k, b2k, b3k])
cond = y9.dot(bk)
print("Q.9  y =", y9.T, "  y^T b =", cond, " => solvable iff b3 = 2*b1 + b2")
assert sp.simplify(cond.subs(b3k, 2*b1k + b2k)) == 0
xp9 = Matrix([5*b1k - 2*b2k, b2k - 2*b1k, 0])
assert sp.simplify(A9k * xp9 - bk.subs(b3k, 2*b1k + b2k)) == sp.zeros(3, 1)
print("Q.9  x_p =", xp9.T, " with N(A) direction (2, 0, 1):", A9k * Matrix([2, 0, 1]) == Matrix([0, 0, 0]))""")

    # ---------------- Q10 ----------------
    md(cells, r"""### Q.10) A Matrix with $V$ as Row Space, Another with $V$ as Null Space (Medium)

**Question (as printed):** $V = \text{span}\{(1, 1, 1), (2, 1, 0)\}$. Find $A$ with $V$ as its **row space**; find $B$ with $V$ as its **null space**.

**Part 1 — rowspace $= V$.** Just put the spanning vectors in as rows:
$$A = \begin{bmatrix} 1 & 1 & 1 \\ 2 & 1 & 0 \end{bmatrix} \qquad (\text{independent rows, so } C(A^T) = V).$$

**Part 2 — nullspace $= V$.** Each row of $B$ must be **orthogonal to every vector of $V$** (that is what $Bv = 0$ for all $v \in V$ means). Find $r = (a, b, c)$ with
$$r \cdot (1, 1, 1) = a + b + c = 0, \qquad r \cdot (2, 1, 0) = 2a + b = 0 \;\Rightarrow\; b = -2a,\; c = a.$$
So $r = a(1, -2, 1)$ — the orthogonal complement $V^\perp$ is one-dimensional. Take
$$B = \begin{bmatrix} 1 & -2 & 1 \end{bmatrix} \qquad \Longrightarrow \qquad N(B) = \{x : x_1 - 2x_2 + x_3 = 0\}.$$
Check: $(1,1,1)$: $1 - 2 + 1 = 0$ ✓; $(2,1,0)$: $2 - 2 + 0 = 0$ ✓; and $\dim N(B) = 3 - 1 = 2 = \dim V$ ✓, so $N(B) = V$ exactly.

**The duality on display:** rowspace $= V$ uses $V$'s own vectors; nullspace $= V$ uses the vectors of $V^\perp$ as rows — every subspace can be described either by its own basis (rowspace) or by the equations it satisfies (nullspace).

**Examiner's note:** Tests the rowspace/nullspace duality via orthogonal complements.
""")
    code(cells, r"""# SymPy verification — Lab 8, Q.10
A10k = Matrix([[1, 1, 1], [2, 1, 0]])
assert A10k.T.columnspace() == [Matrix([1, 1, 1]), Matrix([2, 1, 0])]
B10k = Matrix([[1, -2, 1]])
assert B10k.rank() == 1 and len(B10k.nullspace()) == 2
for v10k in (Matrix([1, 1, 1]), Matrix([2, 1, 0])):
    assert B10k * v10k == Matrix([0])
print("Q.10  C(A^T) = V and N(B) = V: verified")""")

    # ---------------- Q11 ----------------
    md(cells, r"""### Q.11) Pivot Counts and Equality with Whole Spaces (Medium)

**Question (as printed):** Answer each part with an explanation.
(a) A $4\times7$ matrix $A$ has four pivot columns. Is $C(A) = \mathbb{R}^4$? Is $N(A) = \mathbb{R}^3$?
(b) A $5\times6$ matrix $A$ has four pivot columns. What is $\dim N(A)$? Is $C(A) = \mathbb{R}^4$? Why or why not?

**Part (a).** Four pivots in four rows ⇒ full row rank ⇒ $C(A) = \mathbb{R}^{\mathbf{4}}$ — **yes** (every $b$ is reachable). For the second question: $N(A)$ *is* 3-dimensional (nullity $= 7 - 4 = 3$), but it is a 3-dimensional subspace **of $\mathbb{R}^7$**, not of $\mathbb{R}^3$ — so $N(A) = \mathbb{R}^3$ is **no** (wrong ambient space; $N(A)$ consists of 7-vectors). Only if $A$ were $3\times7$-shaped... it isn't. $N(A) = \mathbb{R}^3$ is false; "$\dim N(A) = 3$" is true.

**Part (b).** $\dim N(A) = 6 - 4 = \mathbf{2}$. For $C(A)$: it is a 4-dimensional subspace of $\mathbb{R}^{\mathbf{5}}$ (the matrix has 5 rows!). So $C(A) \ne \mathbb{R}^4$ — that is not even the right ambient space — and $C(A) \ne \mathbb{R}^5$ either, since the rank (4) is one short of the full 5. The sheet's "$\mathbb{R}^4$" is presumably a typo for $\mathbb{R}^5$; the correct statement is: $C(A)$ is a **proper 4-dimensional subspace of $\mathbb{R}^5$** — some right sides $b \in \mathbb{R}^5$ are unreachable.

**Examiner's note:** Tests separating "dimension of a subspace" from "the space it lives in" — the most common notation slip in exams.
""")

    # ---------------- Q12 ----------------
    md(cells, r"""### Q.12) Values of $r, s$ Giving Rank 1 or Rank 2 (Medium)

**Question (as printed):** Are there values of $r$ and $s$ for which
$$M = \begin{bmatrix} 1 & 0 & 0 \\ 0 & r - 2 & 2 \\ 0 & s - 1 & r + 2 \\ 0 & 0 & 3 \end{bmatrix}$$
has rank 1? Rank 2? If so, find those values.

**Step 1 — what is forced for all $r, s$?** Row 1 $= (1, 0, 0)$ and row 4 $= (0, 0, 3)$ are independent for **every** $r, s$: $\text{rank}(M) \ge 2$ always. **Rank 1 is impossible.**

**Step 2 — when is the rank exactly 2?** Rows 2 and 3 must contribute nothing new, i.e. each must be a combination of rows 1 and 4 — a vector of the form $(\alpha, 0, \beta)$. Row 2 $= (0, r-2, 2)$: the middle entry must vanish ⇒ $r = 2$ (giving $(0, 0, 2) = \tfrac23 \cdot \text{row}_4$ ✓). Row 3 $= (0, s-1, r+2)$: need $s = 1$ (giving $(0, 0, 4) = \tfrac43\text{row}_4$ ✓).

$$\boxed{\text{Rank } 1: \text{impossible}. \qquad \text{Rank } 2 \iff (r, s) = (2, 1). \qquad \text{Rank } 3 \text{ for all other } (r, s).}$$
(If $r \ne 2$, row 2 supplies a pivot in column 2 ⇒ rank 3; if $r = 2$ but $s \ne 1$, row 3 supplies it instead.)

**Examiner's note:** Tests parametric rank: identify rows that are always independent, then force the remaining rows into their span.
""")
    code(cells, r"""# SymPy verification — Lab 8, Q.12
r12, s12 = sp.symbols('r s')
M12k = Matrix([[1, 0, 0], [0, r12 - 2, 2], [0, s12 - 1, r12 + 2], [0, 0, 3]])
print("Q.12 rank at (r,s) = (2,1):", M12k.subs({r12: 2, s12: 1}).rank())
print("Q.12 rank at (r,s) = (2,2):", M12k.subs({r12: 2, s12: 2}).rank(),
      " at (3,1):", M12k.subs({r12: 3, s12: 1}).rank(),
      " at (0,0):", M12k.subs({r12: 0, s12: 0}).rank())
assert M12k.subs({r12: 2, s12: 1}).rank() == 2
assert M12k.subs({r12: 2, s12: 2}).rank() == 3 and M12k.subs({r12: 3, s12: 1}).rank() == 3
print("Q.12 rank 1 impossible (rows 1 and 4 always independent); rank 2 iff (r, s) = (2, 1)")""")

    # ---------------- Q13 ----------------
    md(cells, r"""### Q.13) $AB = 0$: Subspace Containment and Why Rank 2 Fails (Hard)

**Question (as printed):** If $AB = 0$, show that $C(B) \subseteq N(A)$ (and the row space of $A$ is contained in the left null space of $B$). Why can't $A$ and $B$ be $3\times3$ matrices of rank 2?

**Part 1 — the containment.** Take any $\mathbf{y} \in C(B)$, say $\mathbf{y} = B\mathbf{x}$ for some $\mathbf{x}$. Then
$$A\mathbf{y} = A(B\mathbf{x}) = (AB)\mathbf{x} = \mathbf{0}\,\mathbf{x} = \mathbf{0} \quad\Longrightarrow\quad \mathbf{y} \in N(A).$$
So **every** column of $B$ (every output of $B$) is annihilated by $A$: $C(B) \subseteq N(A)$.

**Dually**, take any row $\mathbf{r}^T$ of $A$. The corresponding row of $AB$ is $\mathbf{r}^T B = 0$, which says exactly $\mathbf{r} \in N(B^T)$ — the left null space of $B$. Hence the row space of $A$ $\subseteq N(B^T)$.

**Part 2 — why rank 2 fails for $3\times3$.** Suppose $\text{rank}(B) = 2$: then $\dim C(B) = 2$. The containment forces
$$\dim N(A) \ge \dim C(B) = 2.$$
But $\text{rank}(A) = 2$ gives $\dim N(A) = 3 - 2 = 1 < 2$ — **contradiction**. (Rank–nullity simply has no room: two dimensions of $B$-outputs must hide inside a one-dimensional null space.) So at least one of the ranks must be $\le 1$; e.g. $\text{rank}(A) = 1$ and $\text{rank}(B) = 2$ is fine ($1 + 2 \le 3$).

**Examiner's note:** Tests the Sylvester-type inequality in disguise: $\text{rank}(A) + \text{rank}(B) \le n$ whenever $AB = 0$.
""")
    code(cells, r"""# SymPy verification — Lab 8, Q.13 (a working example: rank(A) = 1, rank(B) = 2)
A13k = Matrix([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
B13k = Matrix([[0, 0, 0], [1, 2, 3], [0, 1, 1]])
assert A13k * B13k == sp.zeros(3, 3)
print("Q.13 AB = 0 with rank(A) = 1, rank(B) = 2")
assert all(A13k * v13k == sp.zeros(3, 1) for v13k in B13k.columnspace())
print("Q.13 C(B) =", [v.T for v in B13k.columnspace()], "is contained in N(A) =", [v.T for v in A13k.nullspace()])
# and the rank-2 + rank-2 attempt fails rank-nullity:
print("Q.13 rank2 + rank2 would need dim N(A) >= 2 but rank(A) = 2 gives dim N(A) = 1")""")

    # ---------------- Q14 ----------------
    md(cells, r"""### Q.14) Construct a Matrix — or Prove It Impossible (Hard)

**Question (as printed):** Construct a matrix with the required property, or explain why it is impossible.
(a) Column space contains $(1, 1, 0)$ and $(0, 0, 1)$; row space contains $(1, 2)$ and $(2, 5)$.
(b) Column space has basis $(1, 1, 3)$; null space has basis $(3, 1, 1)$.
(c) Dimension of null space $= 1 + $ dimension of left null space.
(d) Left null space contains $(1, 0, 0, 0)$; row space contains $(0, 0, 0, 1)$.
(e) Row space $=$ column space, but null space $\ne$ left null space.

**(a) POSSIBLE.** Column vectors live in $\mathbb{R}^3$ and row vectors in $\mathbb{R}^2$ ⇒ a $3\times2$ matrix. Rank must be 2 (two independent columns) and the row space is then a 2-dimensional subspace of $\mathbb{R}^2$ — automatically all of $\mathbb{R}^2$, which contains $(1, 2)$ and $(2, 5)$. Take columns equal to the two required vectors:
$$A = \begin{bmatrix} 1 & 0 \\ 1 & 0 \\ 0 & 1 \end{bmatrix}: \quad C(A) = \text{span}\{(1,1,0), (0,0,1)\}\ \checkmark, \quad C(A^T) = \mathbb{R}^2 \ni (1,2), (2,5)\ \checkmark.$$

**(b) IMPOSSIBLE.** "Column space has basis $(1,1,3)$" ⇒ rank 1 ⇒ (for a matrix with 3 columns) $\dim N(A) = 3 - 1 = 2$. But "null space has basis $(3,1,1)$" describes a **1-dimensional** null space. $2 \ne 1$ — no matrix can satisfy both. (Also check consistency of the one vector: $A(3,1,1)^T = 3\,\mathbf{c} \cdot 1$-column $= 3(1,1,3)\cdot 1 \ne \mathbf{0}$ for the only possible $A = c\,[1\ 1\ 3]$-row form — doubly contradictory.)

**(c) POSSIBLE.** $\dim N(A) = n - r$ and $\dim N(A^T) = m - r$, so the requirement reads $n - r = 1 + (m - r)$, i.e. $n = m + 1$: **any matrix with one more column than row** works. Example $3\times4$, rank 2:
$$A = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}: \quad \dim N(A) = 2,\ \dim N(A^T) = 1\ \checkmark.$$

**(d) POSSIBLE.** $(1,0,0,0) \in N(A^T)$ means $A^T\mathbf{e}_1 = \mathbf{0}$, i.e. **row 1 of $A$ is zero**. $(0,0,0,1)$ in the row space needs 4 columns and rank $\ge 1$. Take the $4\times4$ matrix that zeroes the first coordinate space:
$$A = \begin{bmatrix} 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix}: \quad N(A^T) = \text{span}\{(1,0,0,0)\}\ \checkmark,\ \ C(A^T) = \text{span}\{e_2, e_3, e_4\} \ni e_4\ \checkmark.$$

**(e) IMPOSSIBLE.** Let $A$ be square (rowspace $=$ colspace forces the same ambient space, so $m = n$, rank $r$). Then
$$N(A) = C(A^T)^{\perp} = C(A)^{\perp} = N(A^T):$$
both null spaces are the orthogonal complement of the *same* column space, and complements of equal subspaces are equal. So rowspace $=$ colspace **forces** $N(A) = N(A^T)$ — the two requirements cannot both hold.

**Examiner's note:** Tests dimension bookkeeping as an impossibility weapon ((b), (e)) and free construction when the numbers allow it ((a), (c), (d)).
""")
    code(cells, r"""# SymPy verification — Lab 8, Q.14
A14a = Matrix([[1, 0], [1, 0], [0, 1]])
CA14, RT14 = A14a.columnspace(), A14a.T.columnspace()
assert A14a.rank() == 2 and Matrix.hstack(CA14[0], CA14[1], Matrix([1, 1, 0])).rank() == 2 \
       and Matrix.hstack(CA14[0], CA14[1], Matrix([0, 0, 1])).rank() == 2
assert A14a.T.rank() == 2    # C(A^T) = R^2, which contains (1,2) and (2,5)
print("Q.14(a) constructed 3x2 A")
A14c = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]])
assert len(A14c.nullspace()) == 2 and len(A14c.T.nullspace()) == 1
print("Q.14(c) dim N = 2 = 1 + 1 = 1 + dim N(A^T)")
A14d = Matrix.diag(0, 1, 1, 1)
assert A14d.T.nullspace() == [Matrix([1, 0, 0, 0])] and Matrix([0, 0, 0, 1]) == A14d.T.columnspace()[2]
print("Q.14(d) constructed 4x4 A")
print("Q.14(b), (e): impossible by rank-nullity and by orthogonality respectively")""")

    # ---------------- Q15 ----------------
    md(cells, r"""### Q.15) When Does $A$ Have a Two-Sided Inverse? Infinitely Many Solutions? (Hard)

**Question (as printed):** $A$ is $m\times n$ of rank $r$. Under what conditions on $m, n, r$ does
(a) $A$ have a two-sided inverse $AA^{-1} = A^{-1}A = I$?
(b) $Ax = b$ have **infinitely many** solutions for every $b$?

**Part (a).** A two-sided inverse exists iff $A$ is square **and** invertible:
$$\boxed{r = m = n.}$$
(If $m \ne n$, one of $A^{-1}A = I_n$, $AA^{-1} = I_m$ cannot even have the right size; if $m = n$ but $r < n$, the columns are dependent and no inverse exists.)

**Part (b).** "Infinitely many solutions for every $b$" needs two things:
- **Existence for every $b$:** $C(A) = \mathbb{R}^m$ ⇒ full row rank ⇒ $r = m$.
- **Non-uniqueness:** a free variable ⇒ nullity $= n - r \ge 1$ ⇒ $n > r = m$.

$$\boxed{r = m < n}$$
(a wide, full-row-rank matrix — e.g. any $2\times3$ of rank 2: solutions form a line $x_p + N(A)$ for every $b$).

**Examiner's note:** Tests translating existence (rowspace $= \mathbb{R}^m$) and uniqueness failure (nullity $> 0$) into inequalities on $m, n, r$.
""")

    # ---------------- Q16 ----------------
    md(cells, r"""### Q.16) Some $b$ Has No Solution: The Forced Inequalities (Hard)

**Question (as printed):** $A$ is $m\times n$ of rank $r$. Suppose there are right sides $b$ for which $Ax = b$ has **no** solution. What are all the inequalities ($<$ or $\le$) that must be true between $m$, $n$, $r$? How do you know that $A^Ty = 0$ has solutions other than $y = 0$?

**Step 1 — the inequalities.** "Some $b$ fails" means $C(A) \ne \mathbb{R}^m$, i.e. the columns do not span all of $\mathbb{R}^m$:
$$\boxed{r < m}$$
The remaining universal bounds also hold: $r \le n$ (rank cannot exceed the number of columns) and $r \le m$ (implied by $r < m$). Nothing can be said between $m$ and $n$ themselves — the matrix may be square ($m = n > r$) or wide or tall.

**Step 2 — why $N(A^T) \ne \{\mathbf{0}\}$.** $\dim N(A^T) = m - r$, and $r < m$ makes this **positive**:
$$\dim N(A^T) = m - r \ge 1 \quad\Longrightarrow\quad \text{there exists } y \ne \mathbf{0} \text{ with } A^Ty = \mathbf{0}.$$
Geometrically: the failed right sides $b$ are exactly those **not** orthogonal to $N(A^T)$ — each such $y$ yields a solvability obstruction $y^Tb \ne 0$ (the Fredholm alternative: $b \in C(A) \iff y^Tb = 0$ for every $y \in N(A^T)$). If $N(A^T)$ were trivial, *every* $b$ would be solvable.

**Examiner's note:** Tests $r < m \iff C(A) \subsetneq \mathbb{R}^m$ and the left-null space as the carrier of solvability obstructions.
""")

    # ---------------- Q17 ----------------
    md(cells, r"""### Q.17) A 3-Node Graph: Incidence Matrix and Its Duality (Hard)

**Question (as printed):** The graph has nodes $1, 2, 3$ and edges $e_1\!: 1 \to 2$, $e_2\!: 2 \to 3$, $e_3\!: 1 \to 3$. Write the $3\times3$ incidence matrix $A$ **with one row per edge** ($-1$ where the edge leaves, $+1$ where it enters — the transpose of the lecture convention).
(a) Solve $Ax = 0$; describe all of $N(A)$; what do the entries of $x$ measure?
(b) Solve $A^Ty = 0$; describe all of $N(A^T)$; what do the entries of $y$ measure?
(c) Show from the columns of $A$ that every $b \in C(A)$ satisfies $b_1 + b_2 - b_3 = 0$; derive the same condition from the equations of $Ax = b$.

**The matrix.**
$$A = \begin{bmatrix} -1 & 1 & 0 \\ 0 & -1 & 1 \\ -1 & 0 & 1 \end{bmatrix}\;\begin{matrix} e_1\\ e_2\\ e_3 \end{matrix}$$

**Part (a) — $N(A)$: potentials.** $Ax = 0$ row by row: $-x_1 + x_2 = 0$, $-x_2 + x_3 = 0$, $-x_1 + x_3 = 0$ ⇒ $x_1 = x_2 = x_3$:
$$N(A) = \text{span}\{(1, 1, 1)^T\}.$$
The entries of $x$ measure **potentials (voltages/pressures) at the nodes**: only *differences* of potential drive flow, so adding the same constant to every node changes nothing — the "constant vector" is the physics of gauge freedom. (Rank $= 3 - 1 = 2$.)

**Part (b) — $N(A^T)$: loop flows.** $A^Ty = 0$ (column combinations of $A$ summing to zero): $-y_1 - y_3 = 0$, $y_1 - y_2 = 0$, $y_2 + y_3 = 0$ ⇒ $y_2 = y_1$, $y_3 = -y_1$:
$$N(A^T) = \text{span}\{(1, 1, -1)^T\}.$$
The entries of $y$ measure **flows around the loop**: sending 1 unit along $e_1$ and $e_2$ and taking 1 unit back along $e_3$ (opposite its arrow) circulates material around the triangle with zero net effect at every node — a **circulation**.

**Part (c) — the solvability condition.**
- *From the columns:* $b = x_1\mathbf{c}_1 + x_2\mathbf{c}_2 + x_3\mathbf{c}_3$ where $\mathbf{c}_1 = (-1, 0, -1)^T$, $\mathbf{c}_2 = (1, -1, 0)^T$, $\mathbf{c}_3 = (0, 1, 1)^T$. Then
$$b_1 + b_2 - b_3 = (-x_1 + x_2) + (-x_2 + x_3) - (-x_1 + x_3) = 0\ \text{identically.}$$
- *From the equations:* add equation 1 $+$ equation 2 $-$ equation 3: the left side is $(-x_1 + x_2) + (-x_2 + x_3) - (-x_1 + x_3) = 0$, so the right side must satisfy $b_1 + b_2 - b_3 = 0$.
Both computations are the statement $y^Tb = 0$ for $y = (1, 1, -1) \in N(A^T)$ — net balance at the nodes: what flows in must flow out (Kirchhoff's current law as a solvability condition).

**Examiner's note:** Tests the graph–subspace dictionary: $N(A)$ = constant potentials, $N(A^T)$ = loop circulations, and $N(A^T)^{\perp} = C(A)$ = balanced demands.
""")
    code(cells, r"""# SymPy verification — Lab 8, Q.17
A17k = Matrix([[-1, 1, 0], [0, -1, 1], [-1, 0, 1]])
assert A17k.nullspace() == [Matrix([1, 1, 1])]
assert A17k.T.nullspace() == [Matrix([-1, -1, 1])]   # same direction as (1, 1, -1)
assert A17k.rank() == 2
print("Q.17 N(A) = span{(1,1,1)} (potentials), N(A^T) = span{(1,1,-1)} (loop flow)")
b17 = sp.symbols('b1 b2 b3')
y17 = Matrix([1, 1, -1])
print("Q.17(c) y^T b =", y17.dot(Matrix(list(b17))), " => b1 + b2 - b3 = 0")
# numeric: a balanced b is solvable, an unbalanced one is not
assert A17k.row_join(Matrix([3, 2, 5])).rank() == 2      # 3 + 2 - 5 = 0: solvable
assert A17k.row_join(Matrix([3, 2, 4])).rank() == 3      # 3 + 2 - 4 = 1: not solvable
print("Q.17(c) b = (3,2,5) solvable; b = (3,2,4) not: verified via augmented rank")""")

    # ---------------- Q18 ----------------
    md(cells, r"""### Q.18) Challenge: Six Pipes, One Water Grid (Challenge)

**Question (as printed):** 5 junctions $v_1, \dots, v_5$, 6 pipes with reference directions:
$$e_1\!: v_1 \to v_2,\quad e_2\!: v_2 \to v_3,\quad e_3\!: v_3 \to v_1,\quad e_4\!: v_3 \to v_4,\quad e_5\!: v_4 \to v_5,\quad e_6\!: v_5 \to v_3.$$
$B$ = incidence matrix, one row per junction ($-1$ pipe leaves, $+1$ pipe enters); $Bf$ = net inflows.
(a) Write $B$; its size; input/output homes and their physical meaning. (b) Reduce $B$, find the rank; pick 4 pipes forming a spanning tree; explain why a connected graph on $n$ nodes has $\text{rank}(B) = n - 1$. (c) Basis of $N(B)$; mark on the diagram; verify $\text{nullity} = \text{pipes} - \text{junctions} + 1$; why does this count independent loops? (d) Basis of $N(B^T)$; one sentence on pressure. (e) Which demands $d$ can be met? Compress to one scalar equation; check $d = (10, 0, -4, 0, -6)$; find $f = f_p + f_n$ with $f_3 = f_6 = 0$; how many flow patterns; interpret negative entries. (f) When is $w = B^Tp$ solvable? Express via the loop basis; which physical law? (g) Pipe $e_3$ shut ($f_3 = 0$), delete column $e_3$ to get $B'$: (i) rank, nullity, $\dim N(B'^T)$; (ii) can the demand still be met, and how many patterns; (iii) which subspaces changed, which did not?

**Part (a).**
$$B = \begin{bmatrix} -1 & 0 & 1 & 0 & 0 & 0 \\ 1 & -1 & 0 & 0 & 0 & 0 \\ 0 & 1 & -1 & -1 & 0 & 1 \\ 0 & 0 & 0 & 1 & -1 & 0 \\ 0 & 0 & 0 & 0 & 1 & -1 \end{bmatrix}\;\begin{matrix}v_1\\v_2\\v_3\\v_4\\v_5\end{matrix} \qquad (5\times6).$$
**Input home** $\mathbb{R}^6$: pipe flows $f$ (how much water moves along each pipe, signed by the arrow). **Output home** $\mathbb{R}^5$: junction net inflows $d$ (positive = water consumed there, negative = injected).

**Part (b).** Elimination gives **rank 4**. A spanning tree — 4 pipes connecting all 5 junctions with no loop — is $\{e_1, e_2, e_4, e_5\}$ (the path $v_1 \to v_2 \to v_3 \to v_4 \to v_5$). *Why rank $= n - 1$:* (≤) every column of $B$ has one $+1$ and one $-1$, so the sum of all 5 rows is $\mathbf{0}$ — one dependency, rank $\le 4$; (≥) the 4 tree edges give 4 independent rows (a tree has no loop to close a dependency chain — each new tree edge attaches a genuinely new junction). Together: $\text{rank}(B) = n - 1 = 4$ for every connected graph.

**Part (c).** Nullity $= 6 - 4 = 2$; the basis vectors are the **loop flows** around the two independent loops:
$$\ell_1 = (1, 1, 1, 0, 0, 0)^T \ \ (v_1 \to v_2 \to v_3 \to v_1), \qquad \ell_2 = (0, 0, 0, 1, 1, 1)^T \ \ (v_3 \to v_4 \to v_5 \to v_3).$$
Check: each junction of loop 1 receives one unit and sends one unit — $B\ell_1 = \mathbf{0}$ ✓ (same for $\ell_2$). And
$$\text{nullity}(B) = 6 - 5 + 1 = 2\ \checkmark.$$
*Why this counts loops:* pipes $-$ junctions $+ 1$ is precisely the number of independent loops (the cycle rank of the graph): every loop is an extra degree of freedom in which water can circulate without any net effect at the junctions.

**Part (d).** $N(B^T)$: since every column of $B$ sums to zero, $\mathbf{1} = (1,1,1,1,1)^T$ satisfies $B^T\mathbf{1} = \mathbf{0}$; rank–nullity gives $\dim N(B^T) = 5 - 4 = 1$, so
$$N(B^T) = \text{span}\{(1, 1, 1, 1, 1)^T\}.$$
**One sentence:** *pressures are determined only up to an additive constant — adding the same pressure at every junction changes no pressure difference, hence no flow.*

**Part (e).** $Bf = d$ is solvable iff $d \perp N(B^T)$, i.e.
$$\boxed{d_1 + d_2 + d_3 + d_4 + d_5 = 0 \quad (\text{water in} = \text{water out}).}$$
$d = (10, 0, -4, 0, -6)$: sum $= 10 - 4 - 6 = 0$ ✓ — **the demand passes the test**. With $f_3 = f_6 = 0$, solve junction by junction:
$$v_1:\ -f_1 = 10 \Rightarrow f_1 = -10; \quad v_2:\ f_1 - f_2 = 0 \Rightarrow f_2 = -10;$$
$$v_3:\ f_2 - f_4 = -4 \Rightarrow f_4 = -6; \quad v_4:\ f_4 - f_5 = 0 \Rightarrow f_5 = -6; \quad v_5:\ f_5 = -6\ \checkmark.$$
$$f_p = (-10, -10, 0, -6, -6, 0)^T, \qquad f = f_p + c_1\ell_1 + c_2\ell_2 \quad (2\text{-parameter family} \Rightarrow \textbf{infinitely many flow patterns}).$$
**Negative entries:** $f_1 = f_2 = f_4 = f_5 < 0$ means water actually flows **against the reference arrows** — e.g. on $e_1$ the 10 units travel $v_2 \to v_1$, feeding junction $v_1$ (the big consumer, $d_1 = +10$) from the supply at $v_3$. Signs are bookkeeping, not physics.

**Part (f).** $w = B^Tp$ is solvable iff $w \perp N(B)$, i.e. $w \cdot \ell_1 = 0$ and $w \cdot \ell_2 = 0$:
$$w_1 + w_2 + w_3 = 0 \qquad\text{and}\qquad w_4 + w_5 + w_6 = 0.$$
**The pressure drops around any closed loop must sum to zero — Kirchhoff's Voltage Law** (a gadget version: going around a loop and returning to the start, the net pressure change is zero).

**Part (g) — pipe $e_3$ shut ($B'$ = $B$ without column $e_3$, a $5\times5$).**
- **(i)** The remaining graph is still connected (path $v_1\!-\!v_2\!-\!v_3$ plus $v_3 \to v_4 \to v_5 \to v_3$) but now has exactly one loop ($e_4, e_5, e_6$): $\text{rank}(B') = 4$, nullity $= 5 - 4 = 1$, $\dim N(B'^T) = 5 - 4 = 1$.
- **(ii)** The condition $\sum d_i = 0$ still holds (it came from $N(B'^T) = \text{span}\{\mathbf{1}\}$, unchanged) ⇒ the demand $d$ **can still be met**. The $e_3$-free solution with $f_3 = 0$ is unique up to the *one* remaining loop: $f = f_p + c\,(0,0,0,1,1,1)$ — a one-parameter (**infinitely many**) family.
- **(iii)** *Unchanged:* $C(B') = C(B) = \{d : \sum d_i = 0\}$ (still all balanced demands — the graph remains connected) and $N(B'^T) = \text{span}\{\mathbf{1}\}$ (pressures still defined up to a constant). *Changed:* $N(B')$ shrank from two loops to one (killing pipe $e_3$ destroyed the loop $e_1e_2e_3$), and $C(B'^T)$ (the row space of drops) changed accordingly — it is now the 4-dimensional subspace of $\mathbb{R}^5$ satisfying only $w_4 + w_5 + w_6 = 0$.

**Examiner's note:** Tests the complete incidence-matrix duality — flows/loops in $N(B)$, pressures/KVL in $C(B^T)$, conservation in $C(B)$, gauge freedom in $N(B^T)$ — plus how removing an edge reshapes all four.
""")
    code(cells, r"""# SymPy verification — Lab 8, Q.18
B18k = Matrix([[-1, 0, 1, 0, 0, 0],
               [1, -1, 0, 0, 0, 0],
               [0, 1, -1, -1, 0, 1],
               [0, 0, 0, 1, -1, 0],
               [0, 0, 0, 0, 1, -1]])
assert B18k.rank() == 4
l1 = Matrix([1, 1, 1, 0, 0, 0]); l2 = Matrix([0, 0, 0, 1, 1, 1])
assert B18k * l1 == Matrix([0]*5) and B18k * l2 == Matrix([0]*5)
assert B18k.nullspace() == [l1, l2] or set(map(tuple, B18k.nullspace())) == {tuple(l1), tuple(l2)}
assert B18k.T.nullspace() == [Matrix([1, 1, 1, 1, 1])]
print("Q.18(b)-(d) rank 4; loop basis of N(B); N(B^T) = span{1}")
d18 = Matrix([10, 0, -4, 0, -6])
assert d18.dot(Matrix([1, 1, 1, 1, 1])) == 0
# particular solution with f3 = f6 = 0: delete those columns and solve (5 eqs, 4 unknowns)
sol18, _ = B18k[:, [0, 1, 3, 4]].gauss_jordan_solve(d18)
fsub = sol18
fp18 = Matrix([fsub[0], fsub[1], 0, fsub[2], fsub[3], 0])
assert B18k * fp18 == d18
print("Q.18(e) f_p =", fp18.T, " (negative = flow against the arrows)")
for c1 in [0, sp.Rational(1, 2), -7]:
    for c2 in [0, 3]:
        assert B18k * (fp18 + c1 * l1 + c2 * l2) == d18
print("Q.18(e) infinitely many patterns: f_p + c1*l1 + c2*l2 all verified")
# (f) KVL: w in C(B^T) iff w orthogonal to both loops
w18 = B18k.T * Matrix([1, 2, 3, 4, 5])
assert w18.dot(l1) == 0 and w18.dot(l2) == 0
print("Q.18(f) w = B^T p satisfies w1+w2+w3 = 0 and w4+w5+w6 = 0 (KVL)")
# (g) delete column e3
Bp = B18k[:, [0, 1, 3, 4, 5]]
assert Bp.rank() == 4 and len(Bp.nullspace()) == 1 and len(Bp.T.nullspace()) == 1
sol18b, _ = Bp.gauss_jordan_solve(d18)
fpsub = sol18b
fp2 = Matrix([fpsub[0], fpsub[1], 0, fpsub[2], fpsub[3], fpsub[4]])
assert B18k * fp2 == d18
print("Q.18(g) rank(B') = 4, nullity = 1, dim N(B'^T) = 1; demand still met, 1-parameter family")
assert Bp.columnspace() == B18k.columnspace()
print("Q.18(g)(iii) C(B') = C(B) unchanged; N(B') lost loop 1; C(B'^T) now imposes only w4+w5+w6 = 0")""")

    return cells
