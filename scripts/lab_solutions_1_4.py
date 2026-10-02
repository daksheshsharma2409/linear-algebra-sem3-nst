"""
Script module: lab_solutions_1_4.py — detailed cell content for the lab notebook.
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


INTRO_MD = r"""# Newton School of Technology, ADYPU — Mathematics-3: Linear Algebra
## Companion Lab Solutions Manual: Complete Worked Solutions & SymPy Verification (Labs 1–8)

---

### Methodological Protocol
For **every single question** across Labs 1 through 8 (categorized across *Easy*, *Medium*, *Hard*, and *Challenge* tiers):
1. **Problem Restatement:** Exact problem formulation with complete mathematical symbols.
2. **Analytical Step-by-Step Derivation:** Exhaustive algebraic and geometric working, shown step by step.
3. **SymPy Computational Verification:** Exact arithmetic proof using `sympy.Matrix`, checking consistency, determinants, ranks, and fundamental subspaces.
4. **Examiner Testing Note:** A targeted one-line summary explaining the exact core linear algebra concept being assessed.
5. **Rigorous True/False Treatment:** Formal mathematical justifications and explicit counterexamples for all false claims.
6. **Discrepancy & Typo Clarifications:** Explicitly noting any inconsistencies or printing typos found in the original lab sheets.

### Coverage Map
| Lab | Topic | Questions solved |
| :--- | :--- | :--- |
| 1 | Linear systems, row & column picture | Q.1 – Q.16 |
| 2 | Matrix multiplication (MUL-TEA-PLICATION) | Q.1 – Q.9 |
| 3 | Linear combinations, span, vector spaces | Q.1 – Q.14 + Reflection |
| 4 | Gaussian elimination, echelon forms, rank | Q.1 – Q.12 + Incidence Challenge |
| 5 | Elementary matrices, $A = LU$ | Q.1 – Q.13 |
| 6 | Linear independence, column space | Q.1 – Q.14 + Four-Lamp Challenge |
| 7 | Null space, subspaces, complete solutions | Q.1 – Q.16 |
| 8 | Four fundamental subspaces, network duality | Q.1 – Q.18 |

### Sheet Issues Flagged In-Text
- **Lab 1 Q.8:** RHS $-1$ as printed gives $(13/5, 9/5)$; the likely intended $x - 2y = 1$ gives the clean $(3, 1)$ — both analysed.
- **Lab 4 Q.7 & Q.11:** as printed both systems are **inconsistent** (rank $[A] = 3 <$ rank $[A\mid b] = 4$); the exact consistency condition $3b_4 = 5b_1 + b_2 + 2b_3$ is derived.
- **Lab 5 Q.5:** sheet typo "whther" for "whether".
- **Lab 6:** the four-lamp Challenge is printed with the duplicate number "Q.14".
- **Lab 8 Q.11(b):** the printed "$C(A) = \mathbb{R}^4$" for a $5\times6$ matrix should read $\mathbb{R}^5$.

---
"""


def get_lab_intro_cells():
    cells = []
    md(cells, INTRO_MD)

    # Shared environment for all verification cells
    code(cells,
         "import sympy as sp\n"
         "from sympy import Matrix, Rational, simplify, zeros\n"
         "from IPython.display import display\n"
         "print('SymPy', sp.__version__, 'ready — exact arithmetic verification environment loaded')")
    return cells



LAB_TITLE = "Lab 1 Solutions: Linear Systems, Row Picture, and Column Picture"
LAB_SUB = (
    "**Core ideas tested:** $Ax = b$ as a row picture (intersecting lines/planes/hyperplanes) "
    "and a column picture (combining column vectors), the three solution possibilities "
    "(unique / infinite / none), and how dependence between equations or columns decides which one occurs."
)


def get_lab1_cells():
    cells = []
    md(cells, lab_header(LAB_TITLE, LAB_SUB))

    # ---------------- Q1 ----------------
    md(cells, r"""### Q.1) Write the System in Matrix Notation (Easy)

**Question (as printed):** Write the following system in matrix notation:
$$\begin{aligned} 2x + y - z &= 4 \\ x - z &= 1 \\ 3x + y + 2z &= 6 \end{aligned}$$

**Step 1 — Read off one row at a time.** Each equation contributes one row of the coefficient matrix $A$; a variable that is *missing* contributes a $0$:
- Row 1: $2x + 1y - 1z = 4 \;\Rightarrow\; [2,\; 1,\; -1]$, right side $4$.
- Row 2: $x - z = 1$ has **no $y$ term** $\;\Rightarrow\; [1,\; 0,\; -1]$, right side $1$. *(Forgetting this zero is the #1 exam mistake.)*
- Row 3: $3x + y + 2z = 6 \;\Rightarrow\; [3,\; 1,\; 2]$, right side $6$.

**Step 2 — Assemble $Ax = b$:**
$$\underbrace{\begin{bmatrix} 2 & 1 & -1 \\ 1 & 0 & -1 \\ 3 & 1 & 2 \end{bmatrix}}_{A}\;
\underbrace{\begin{bmatrix} x \\ y \\ z \end{bmatrix}}_{x} =
\underbrace{\begin{bmatrix} 4 \\ 1 \\ 6 \end{bmatrix}}_{b}$$

**Step 3 — What $Ax=b$ *means* (column picture).** The equation says
$$x\begin{bmatrix}2\\1\\3\end{bmatrix} + y\begin{bmatrix}1\\0\\1\end{bmatrix} + z\begin{bmatrix}-1\\-1\\2\end{bmatrix} = \begin{bmatrix}4\\1\\6\end{bmatrix},$$
i.e. "find the recipe $(x,y,z)$ that mixes the three columns of $A$ to produce $b$." Both readings — rows as equations, columns as ingredients — are the *same* statement.

**Answer:** $A = \begin{bmatrix} 2 & 1 & -1 \\ 1 & 0 & -1 \\ 3 & 1 & 2 \end{bmatrix},\ x = (x,y,z)^T,\ b = (4,1,6)^T$.

**Examiner's note:** Tests conversion between scalar systems and $Ax=b$, especially zero coefficients for absent variables.
""")
    code(cells, r"""# SymPy verification — Lab 1, Q.1
from sympy import Matrix, Rational

A1 = Matrix([[2, 1, -1], [1, 0, -1], [3, 1, 2]])
b1 = Matrix([4, 1, 6])
x1 = A1.LUsolve(b1)
print("Q.1  unique solution (x, y, z) =", x1.T)
assert A1 * x1 == b1, "solution must reproduce Ax = b"
print("Check 2x+y-z = ", 2*x1[0] + x1[1] - x1[2])""")

    # ---------------- Q2 ----------------
    md(cells, r"""### Q.2) Sketch Two Lines and Count Solutions (Easy)

**Question (as printed):** Sketch $x + y = 3$ and $x - y = 1$. State the number of solutions.

**Step 1 — Row picture.**
- Line 1: $x + y = 3$ has intercepts $(3, 0)$ and $(0, 3)$ (slope $-1$).
- Line 2: $x - y = 1$ has intercepts $(1, 0)$ and $(0, -1)$ (slope $+1$).
Different slopes $\Rightarrow$ the lines meet exactly once.

**Step 2 — Solve.** Add the equations: $2x = 4 \Rightarrow x = 2$; then $y = 3 - 2 = 1$. Intersection point $(2, 1)$.

**Step 3 — Column picture.** We need $x\binom{1}{1} + y\binom{1}{-1} = \binom{3}{1}$: scale the column $(1,1)$ by $2$ and the column $(1,-1)$ by $1$:
$$2\begin{bmatrix}1\\1\end{bmatrix} + 1\begin{bmatrix}1\\-1\end{bmatrix} = \begin{bmatrix}3\\1\end{bmatrix}. \checkmark$$

**Answer:** Exactly **one** solution, $(x, y) = (2, 1)$ — the non-parallel lines cross once; equivalently the two columns are independent so the recipe is unique.

**Examiner's note:** Tests the row-vs-column picture duality in the easiest 2×2 setting.
""")
    code(cells, r"""# SymPy verification — Lab 1, Q.2
A2 = Matrix([[1, 1], [1, -1]])
x2 = A2.LUsolve(Matrix([3, 1]))
print("Q.2  solution (x, y) =", x2.T, "| det(A) =", A2.det(), "=> one solution")
assert x2 == Matrix([2, 1])""")

    # ---------------- Q3 ----------------
    md(cells, r"""### Q.3) Convert Matrix Equations Back into Systems (Easy)

**Question (as printed):** Convert into systems of linear equations:
$$\text{(a) } \begin{bmatrix} 2 & 1 & 3 \\ 3 & 1 & 1 \end{bmatrix}\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 5 \\ 4 \end{bmatrix} \qquad
\text{(b) } \begin{bmatrix} 4 & 0 \\ -1 & 2 \\ 3 & 7 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 4 \\ 1 \\ 10 \end{bmatrix}$$

**Part (a) — each row becomes one equation:**
$$\begin{aligned} 2x + y + 3z &= 5 \\ 3x + y + z &= 4 \end{aligned}$$
Two equations, three unknowns $\Rightarrow$ the row picture is **two planes in $\mathbb{R}^3$**, which meet in a **line** (they are not parallel), so there are *infinitely many* solutions. Parametrising with $z = t$:
subtracting the equations gives $-x + 2t = 1 \Rightarrow x = 2t - 1$, and then $y = 5 - 3t - 2x = 7 - 7t$:
$$(x, y, z) = (-1 + 2t,\; 7 - 7t,\; t), \quad t \in \mathbb{R}. \quad \text{(Check } t = 1: (1, 0, 1):\ 2+0+3 = 5\ \checkmark,\ 3+0+1 = 4\ \checkmark)$$

**Part (b) — three equations, two unknowns (more rows than unknowns):**
$$\begin{aligned} 4x &= 4 \\ -x + 2y &= 1 \\ 3x + 7y &= 10 \end{aligned}$$
The first forces $x = 1$, the second gives $y = 1$, and the third is the consistency check: $3(1) + 7(1) = 10$ ✓. Here the *over-determined* system happens to be consistent — the third line passes through the intersection of the first two.

**Examiner's note:** Tests that "rows = equations" works in both directions, and that shape $(2\times3)$ vs $(3\times2)$ predicts too-few vs too-many equations.
""")
    code(cells, r"""# SymPy verification — Lab 1, Q.3
Aa = Matrix([[2, 1, 3], [3, 1, 1]]); ba = Matrix([5, 4])
Ab = Matrix([[4, 0], [-1, 2], [3, 7]]); bb = Matrix([4, 1, 10])

t_a = Matrix([1, 0, 1])                     # t = 1 representative of the solution line
assert Aa * t_a == ba
print("Q.3(a) solution line contains (1, 0, 1); rank(A) =", Aa.rank(),
      "< 3 unknowns => infinitely many solutions")

xb = Ab.LUsolve(bb)
assert Ab * xb == bb and xb == Matrix([1, 1])
print("Q.3(b) consistent over-determined system, unique solution (x, y) =", xb.T)""")

    # ---------------- Q4 ----------------
    md(cells, r"""### Q.4) Two Pictures in Two Planes for $x - 2y = 0,\ x + y = 6$ (Easy)

**Question (as printed):** Draw the two pictures (row and column) for $x - 2y = 0$, $x + y = 6$.

**Row picture (lines in the $xy$-plane):**
- $x - 2y = 0 \Rightarrow y = x/2$: a line through the **origin** with slope $1/2$.
- $x + y = 6 \Rightarrow y = 6 - x$: slope $-1$, intercepts $(6, 0)$ and $(0, 6)$.
Setting $y = x/2$ in the second: $\tfrac{3}{2}x = 6 \Rightarrow x = 4,\ y = 2$. The lines cross at $(4, 2)$.

**Column picture (vectors in the same plane):** The columns of $A$ are $\mathbf{a}_1 = (1, 1)^T$ and $\mathbf{a}_2 = (-2, 1)^T$; the target is $\mathbf{b} = (0, 6)^T$:
$$4\begin{bmatrix}1\\1\end{bmatrix} + 2\begin{bmatrix}-2\\1\end{bmatrix} = \begin{bmatrix}4-4\\4+2\end{bmatrix} = \begin{bmatrix}0\\6\end{bmatrix}. \checkmark$$
Geometrically: walk $4$ steps along $\mathbf{a}_1$, then $2$ steps along $\mathbf{a}_2$, and you land on $\mathbf{b}$.

**Answer:** Unique solution $(4, 2)$; both pictures describe the same single recipe.

**Examiner's note:** Tests drawing both pictures for one system and connecting the intersection point to the vector recipe.
""")
    code(cells, r"""# SymPy verification — Lab 1, Q.4
A4 = Matrix([[1, -2], [1, 1]])
x4 = A4.LUsolve(Matrix([0, 6]))
print("Q.4  solution (x, y) =", x4.T)
assert x4 == Matrix([4, 2])""")

    # ---------------- Q5 ----------------
    md(cells, r"""### Q.5) Fill in the Blanks: Intersections Through the Origin (Medium)

**Question (as printed):**
(a) The intersection of two planes through $(0,0,0)$ is probably a ______ but it could be a ______. It can't be the origin itself.
(b) The intersection of a plane through $(0,0,0)$ with a line through $(0,0,0)$ is probably a ______ but it could be a ______.

**Part (a).** Two planes through the origin are the solution sets of two homogeneous equations $a_1x + b_1y + c_1z = 0$ and $a_2x + b_2y + c_2z = 0$. If the two normal vectors are not parallel, elimination leaves **two independent equations in three unknowns** $\Rightarrow$ one free variable $\Rightarrow$ the solution set is a **line** through the origin. If the two planes are actually *the same plane* (equations proportional), the intersection is that whole **plane**. And because $(0,0,0)$ satisfies both homogeneous equations, the intersection always contains the origin — so it can never be "the origin itself" (a single point).

$$\boxed{\text{(a) probably a \textbf{line}, could be a \textbf{plane}.}}$$

**Part (b).** A generic line through the origin pierces a generic plane through the origin only at the origin itself, so the intersection is "probably" just the **point** $(0,0,0)$. But if the line happens to *lie inside* the plane, the intersection is the whole **line**.

$$\boxed{\text{(b) probably a \textbf{point} (the origin), could be a \textbf{line}.}}$$

**Examiner's note:** Tests dimension counting for intersections of homogeneous sets: 2 equations in 3 unknowns leave $3 - 2 = 1$ free parameter.
""")

    # ---------------- Q6 ----------------
    md(cells, r"""### Q.6) Parallel and Perpendicular Lines (Medium)

**Question (as printed):** Starting with $x + 4y = 7$, find the equation of the parallel line through $x = 0, y = 0$. Find the equation of another line perpendicular to the first at $x = 3, y = 1$.

**Step 1 — parallel through the origin.** Parallel lines share the same left-hand side (same normal vector $\mathbf{n} = (1, 4)^T$) and differ only in the right side. Passing through $(0,0)$: $1(0) + 4(0) = 0$, so
$$x + 4y = 0.$$
Both lines have slope $-1/4$; they differ by a vertical shift of $7/4$.

**Step 2 — perpendicular at $(3, 1)$.** The given line has slope $m_1 = -1/4$, so a perpendicular line has slope $m_2 = 4$ (because $m_1 m_2 = -1$). Through $(3, 1)$:
$$y - 1 = 4(x - 3) \quad\Longleftrightarrow\quad y = 4x - 11 \quad\Longleftrightarrow\quad 4x - y = 11.$$
In normal-vector language: the perpendicular line's normal $\mathbf{n}_\perp = (4, -1)^T$ must be orthogonal to the original normal $(1,4)^T$ — and indeed $(1,4)\cdot(4,-1) = 4 - 4 = 0$ ✓.

**Answer:** parallel: $x + 4y = 0$; perpendicular at $(3,1)$: $y = 4x - 11$ (i.e. $4x - y = 11$).

**Examiner's note:** Tests normals of lines, the parallel-line family $ax+by=c$, and $m_1m_2=-1$ orthogonality.
""")
    code(cells, r"""# SymPy verification — Lab 1, Q.6
from sympy import Matrix as Mx
assert Mx([1, 4]).dot(Mx([4, -1])) == 0, "normals of perpendicular lines are orthogonal"
assert 4 * 3 - 1 == 11
print("Q.6  parallel line x + 4y = 0; perpendicular line 4x - y = 11 through (3, 1). Verified.")""")

    # ---------------- Q7 ----------------
    md(cells, r"""### Q.7) Three Lines: Concurrency, Zero RHS, and New RHS (Medium)

**Question (as printed):** Sketch $2x + y = 5$, $x - y = 1$, $3x = 6$.
(a) Does the system have a common solution? (b) What if all right-hand sides become zero? (c) Is there another non-zero choice of right-hand sides that lets all three lines meet at one point?

**Part (a).** Line 3 gives $x = 2$ immediately. Line 2 then forces $2 - y = 1 \Rightarrow y = 1$. Check line 1: $2(2) + 1 = 5$ ✓. All three lines pass through $\boxed{(2, 1)}$ — the system is consistent, and because the third line pins $x$ and the second pins $y$, the common point is *unique*.

**Part (b) — homogeneous system** $2x + y = 0$, $x - y = 0$, $3x = 0$:
$3x = 0 \Rightarrow x = 0$; then $y = 0$ and line 1 is satisfied automatically. All three lines pass through the **origin** $(0, 0)$ — the unique solution. (A homogeneous square system with independent rows *always* has exactly this outcome.)

**Part (c).** Pick **any** point $P = (x_0, y_0)$ and evaluate each left-hand side there:
$$b_1 = 2x_0 + y_0, \qquad b_2 = x_0 - y_0, \qquad b_3 = 3x_0.$$
With these right sides the three lines automatically meet at $P$. Example: $P = (1, 2)$ gives $(b_1, b_2, b_3) = (4, -1, 3) \ne \mathbf{0}$.

**Examiner's note:** Tests concurrency, the trivial homogeneous solution, and the fact that the *left-hand sides* fix where lines can meet while the *right-hand sides* choose which concurrent point.
""")
    code(cells, r"""# SymPy verification — Lab 1, Q.7
A7 = Matrix([[2, 1], [1, -1], [3, 0]])
print("Q.7(a) common solution:", A7.LUsolve(Matrix([5, 1, 6])).T)
print("Q.7(b) homogeneous solution:", A7.LUsolve(Matrix([0, 0, 0])).T)
P = Matrix([1, 2])
print("Q.7(c) RHS making the lines meet at (1, 2):", (A7 * P).T)
assert (A7 * P) == Matrix([4, -1, 3])""")

    # ---------------- Q8 ----------------
    md(cells, r"""### Q.8) Row Picture vs. Column Picture, with a Sheet Typo Flag (Medium)

**Question (as printed):** For $2x + y = 7$, $x - 2y = -1$: draw the row picture and the column picture, and explain in one or two sentences how the two pictures represent the same problem from different perspectives.

> **⚠ Discrepancy flag:** the current notebook's earlier treatment suspected the intended RHS was $(7, 1)$. As *printed*, the system is perfectly consistent — it just has a non-integer solution. Both versions are analysed below.

**Step 1 — solve as printed.** From $x = 2y - 1$ substitute into $2x + y = 7$:
$2(2y-1) + y = 7 \Rightarrow 5y = 9 \Rightarrow y = 9/5$, $x = 13/5$. The lines $y = 7 - 2x$ and $y = (x+1)/2$ cross at $\left(\tfrac{13}{5}, \tfrac{9}{5}\right)$.

**Step 2 — column picture (as printed).**
$$\tfrac{13}{5}\begin{bmatrix}2\\1\end{bmatrix} + \tfrac{9}{5}\begin{bmatrix}1\\-2\end{bmatrix} = \begin{bmatrix}26/5 + 9/5\\ 13/5 - 18/5\end{bmatrix} = \begin{bmatrix}7\\-1\end{bmatrix}.\ \checkmark$$

**Step 3 — likely intended version** $x - 2y = 1$ (RHS $+1$): elimination gives the clean solution $(3, 1)$:
$$2(3) + 1 = 7\ \checkmark, \qquad 3 - 2(1) = 1\ \checkmark, \qquad 3\begin{bmatrix}2\\1\end{bmatrix} + 1\begin{bmatrix}1\\-2\end{bmatrix} = \begin{bmatrix}7\\1\end{bmatrix}.\ \checkmark$$

**Step 4 — the one-sentence explanation (the real question).** The **row picture** treats each equation as a whole line and looks for the single *point* lying on every line; the **column picture** treats each column as a vector and looks for the single *recipe* $(x, y)$ of scaled additions that builds $\mathbf{b}$. Same numbers, same solution — one picture is geometric about points, the other about combining vectors.

**Examiner's note:** Tests fluency between intersection-of-lines and combination-of-columns viewpoints.
""")
    code(cells, r"""# SymPy verification — Lab 1, Q.8 (both printed and suspected versions)
A8 = Matrix([[2, 1], [1, -2]])
print("As printed (b = (7, -1)):  solution =", A8.LUsolve(Matrix([7, -1])).T)
print("Suspected  (b = (7, 1)):   solution =", A8.LUsolve(Matrix([7, 1])).T)
assert A8.LUsolve(Matrix([7, 1])) == Matrix([3, 1])""")

    # ---------------- Q9 ----------------
    md(cells, r"""### Q.9) Classify Three Systems Without Solving (Medium)

**Question (as printed):** Without solving algebraically, decide: exactly one / infinitely many / no solution.
(a) $x + y = 3;\ 2x + 2y = 6$  (b) $x + y = 3;\ 2x + 2y = 3$  (c) $x + y = 3;\ x - y = 1$

**Reasoning by slopes (row picture):**

| System | Second line after simplifying | Geometry | Verdict |
| :--- | :--- | :--- | :--- |
| (a) | $x + y = 3$ — *same line* | coincident lines | **infinitely many** solutions |
| (b) | $x + y = 3/2$ — parallel, distinct | never meet | **no** solution |
| (c) | $x - y = 1$ — slope $+1$ vs $-1$ | cross once | **exactly one** solution $(2, 1)$ |

**Column-picture reading of (a):** the second equation is $2\times$ the first, i.e. row 2 of $A$ is $2\times$ row 1. The columns of the second matrix are also $2\times$ the first's columns — so $\binom{2}{2} = 2\binom{1}{1}$ is *dependent*: one vector carries no new direction, and every solution of equation 1 automatically satisfies equation 2, leaving a free parameter.
**(b):** the left sides are dependent but the right sides are *not* ($3 \ne 2 \times 3$), so after elimination we get $0 = -3$: impossible.
**(c):** $\det\begin{bmatrix}1&1\\1&-1\end{bmatrix} = -2 \ne 0$: independent columns $\Rightarrow$ unique recipe.

**Examiner's note:** Tests classification *before* computation — proportional rows + proportional RHS ⇒ ∞; proportional rows + mismatched RHS ⇒ 0; $\det \ne 0$ ⇒ 1.
""")
    code(cells, r"""# SymPy verification — Lab 1, Q.9
cases = [(Matrix([[1, 1], [2, 2]]), Matrix([3, 6])),
         (Matrix([[1, 1], [2, 2]]), Matrix([3, 3])),
         (Matrix([[1, 1], [1, -1]]), Matrix([3, 1]))]
for i, (Ac, bc) in enumerate(cases, 1):
    ra, raug = Ac.rank(), Ac.row_join(bc).rank()
    verdict = "unique" if (ra == raug == 2) else ("infinite" if ra == raug else "none")
    print(f"Q.9({chr(96+i)}) rank(A) = {ra}, rank([A|b]) = {raug}  =>  {verdict}")
assert [c[0].row_join(c[1]).rref()[0] for c in cases][2] == Matrix([[1, 0, 2], [0, 1, 1]])""")

    # ---------------- Q10 ----------------
    md(cells, r"""### Q.10) Café: Coffee and Sandwiches (Medium)

**Question (as printed):** Two coffees and one sandwich cost ₹250. One coffee and three sandwiches cost ₹350.
(a) Form the system. (b) Solve by substitution/elimination. (c) Write the matrix equation. (d) Explain the row picture.

**Part (a).** Let $c$ = price of a coffee, $s$ = price of a sandwich:
$$\begin{aligned} 2c + s &= 250 \\ c + 3s &= 350 \end{aligned}$$

**Part (b) — elimination.** Double the second equation and subtract the first: $(2c + 6s) - (2c + s) = 700 - 250 \Rightarrow 5s = 450 \Rightarrow s = 90$. Back-substitute: $c = 350 - 3(90) = 80$.
$$\boxed{\text{coffee} = ₹80, \quad \text{sandwich} = ₹90}$$
Check: $2(80) + 90 = 250$ ✓ and $80 + 270 = 350$ ✓.

**Part (c).**
$$\begin{bmatrix} 2 & 1 \\ 1 & 3 \end{bmatrix}\begin{bmatrix} c \\ s \end{bmatrix} = \begin{bmatrix} 250 \\ 350 \end{bmatrix}$$

**Part (d) — row picture.** In the $(c, s)$-plane each equation is a straight *line of price combinations*: the line $2c + s = 250$ collects every bundle costing ₹250, and $c + 3s = 350$ every bundle costing ₹350. Their single intersection point $(80, 90)$ is the only bundle satisfying both price conditions simultaneously.

**Examiner's note:** Tests the full modelling chain: words → equations → matrix → geometry.
""")
    code(cells, r"""# SymPy verification — Lab 1, Q.10
Acafe = Matrix([[2, 1], [1, 3]])
xcafe = Acafe.LUsolve(Matrix([250, 350]))
print("Q.10 (c, s) =", xcafe.T, "=> coffee ₹80, sandwich ₹90")
assert xcafe == Matrix([80, 90])""")

    # ---------------- Q11 ----------------
    md(cells, r"""### Q.11) For Which $k$ Does $x - y = 2,\ 3x - 3y = k$ Have One / Infinite / No Solutions? (Medium)

**Question (as printed):** Find the values of $k$ for which the system has (a) exactly one, (b) infinitely many, (c) no solution; explain geometrically.

**Step 1 — eliminate.** $R_2 \to R_2 - 3R_1$:
$$\begin{bmatrix} 1 & -1 & | & 2 \\ 3 & -3 & | & k \end{bmatrix} \longrightarrow \begin{bmatrix} 1 & -1 & | & 2 \\ 0 & 0 & | & k - 6 \end{bmatrix}$$

**Part (a) — exactly one solution: impossible for every $k$.** After elimination only **one** pivot remains (rank $= 1 < n = 2$): there is always a free variable. A unique solution would need $\det A = (1)(-3) - (-1)(3) = 0$ — never.

**Part (b) — infinitely many: $k = 6$.** The bottom row becomes $0 = 0$ (consistent), leaving $x - y = 2$ alone:
$$x = 2 + t,\; y = t \quad (t \in \mathbb{R}).$$

**Part (c) — no solution: $k \ne 6$.** The bottom row reads $0 = k - 6 \ne 0$, a contradiction.

**Geometry.** Both equations describe lines with slope $+1$. Equation 2 is always *parallel* to equation 1 (identical slope): for $k = 6$ it is the **same line** (infinitely many shared points); for $k \ne 6$ it is a **distinct parallel line** (no shared points). No value of $k$ can make parallel lines cross in exactly one point.

**Examiner's note:** Tests the trichotomy for singular systems: dependent rows force either $\infty$ or $0$, never $1$.
""")
    code(cells, r"""# SymPy verification — Lab 1, Q.11
k = sp.symbols('k')
M11 = Matrix([[1, -1, 2], [3, -3, k]])
print("Q.11 RREF with parameter k:")
display(M11.rref()[0])
assert Matrix([[1, -1], [3, -3]]).det() == 0   # symbolic rank sees k as an indeterminate; det(A) = 0 identically
print("=> unique solution never; k = 6 => infinite; k != 6 => none")""")

    # ---------------- Q12 ----------------
    md(cells, r"""### Q.12) A Whole Line of Solutions for $ax + 2y = 0,\ 2x + ay = 0$ (Hard)

**Question (as printed):** These equations certainly have the solution $x = y = 0$. Using the row or column picture, determine for which values of $a$ there is a whole **line** of solutions.

**Step 1 — when does a homogeneous $2\times2$ system have non-zero solutions?** Exactly when the two rows are proportional, i.e. when the columns fail to be independent:
$$\det \begin{bmatrix} a & 2 \\ 2 & a \end{bmatrix} = a^2 - 4 = (a - 2)(a + 2) = 0 \quad\Longrightarrow\quad a = \pm 2.$$

**Step 2 — describe the line for each case.**
- $a = 2$: both equations become $x + y = 0$. The two lines **coincide**; the solution set is the line $y = -x$ — every point $t(1, -1)$.
- $a = -2$: both equations become $-x + y = 0$, i.e. $y = x$ — the solution set is the line $y = x$, every point $t(1, 1)$.

**Column picture for $a = 2$:** the columns $\binom{2}{2}$ and $\binom{2}{2}$ are identical, so the only reachable vectors lie on the single line spanned by $(1,1)$; forcing $b = 0$ means any pair of opposite recipes works — a whole line of them.

**Answer:** $a = 2$ (line $x + y = 0$) or $a = -2$ (line $y = x$); for all other $a$ the origin is the *only* solution.

**Examiner's note:** Tests the singular-value criterion for non-trivial homogeneous solutions, plus reading the geometry off the dependent rows.
""")
    code(cells, r"""# SymPy verification — Lab 1, Q.12
a = sp.symbols('a')
A12h = Matrix([[a, 2], [2, a]])
print("Q.12 det = ", A12h.det(), " => line of solutions at a =", sp.solve(A12h.det(), a))
for aval, expect in [(2, Matrix([-1, 1])), (-2, Matrix([1, 1]))]:
    Aa = A12h.subs(a, aval)
    ns = Aa.nullspace()
    assert len(ns) == 1 and ns[0] == expect
    print(f"  a = {aval}: N(A) = span({ns[0].T})")""")

    # ---------------- Q13 ----------------
    md(cells, r"""### Q.13) Why $u + v + w = 2$, $u + 2v + 3w = 1$, $v + 2w = 0$ Has No Solution (Hard)

**Question (as printed):** Explain why the system has no solutions. What value should replace the last zero on the right side to allow a solution?

**Step 1 — find the dependency among the left-hand sides.** Subtract equation 1 from equation 2:
$$(u + 2v + 3w) - (u + v + w) = v + 2w.$$
So the combination *(equation 2) − (equation 1)* has **exactly the same left-hand side** as equation 3. The three left sides are linearly dependent: $\text{row}_2 - \text{row}_1 - \text{row}_3 = 0$.

**Step 2 — apply the same combination to the right sides.** Whatever the left side forces, the right side must obey:
$$(\text{eq }2) - (\text{eq }1) \Rightarrow \underbrace{1 - 2}_{-1} \quad\text{must equal}\quad \underbrace{0}_{\text{eq 3 RHS}} \qquad\Rightarrow\qquad -1 = 0\ \text{— impossible.}$$
In the column picture, $\mathbf{b} = (2, 1, 0)^T$ lies **outside the plane** spanned by the three dependent columns.

**Step 3 — the fix.** The right side of equation 3 must equal (RHS 2) − (RHS 1) $= -1$:
$$\boxed{v + 2w = -1}$$
With $b_3 = -1$: set $w = t$ freely, then $v = -1 - 2t$ and $u = 2 - v - w = 3 + t$ — infinitely many solutions (rank $2 < 3$ unknowns). E.g. $t = 0$: $(u, v, w) = (3, -1, 0)$; check eq 2: $3 - 2 + 0 = 1$ ✓.

**Examiner's note:** Tests spotting dependent equations and transferring the dependency to the RHS (the Fredholm solvability idea in embryo).
""")
    code(cells, r"""# SymPy verification — Lab 1, Q.13
A13 = Matrix([[1, 1, 1], [1, 2, 3], [0, 1, 2]])
print("Q.13 left-null vector y (rows combine to zero):", [v.T for v in A13.T.nullspace()])
y = Matrix([-1, 1, -1])          # -eq1 + eq2 - eq3 = 0 on the left
print("y^T b with printed b = (2,1,0):", y.dot(Matrix([2, 1, 0])), " (non-zero => inconsistent)")
print("y^T b with corrected b = (2,1,-1):", y.dot(Matrix([2, 1, -1])), " (zero => consistent)")
assert y.dot(Matrix([2, 1, 0])) != 0 and y.dot(Matrix([2, 1, -1])) == 0""")

    # ---------------- Q14 ----------------
    md(cells, r"""### Q.14) Three Columns in the Same Plane (Hard)

**Question (as printed):** Show that the three columns of
$$u\begin{bmatrix}1\\1\\0\end{bmatrix} + v\begin{bmatrix}1\\2\\1\end{bmatrix} + w\begin{bmatrix}1\\3\\2\end{bmatrix} = \begin{bmatrix}b_1\\b_2\\b_3\end{bmatrix}$$
lie in the same plane by expressing the third column as a combination of the first two.

**Step 1 — hunt for the relation.** Look for $\alpha, \beta$ with $\alpha\,\mathbf{c}_1 + \beta\,\mathbf{c}_2 = \mathbf{c}_3$ where $\mathbf{c}_1 = (1,1,0)^T$, $\mathbf{c}_2 = (1,2,1)^T$, $\mathbf{c}_3 = (1,3,2)^T$.
Matching the first component: $\alpha + \beta = 1$; second: $\alpha + 2\beta = 3 \Rightarrow \beta = 2, \alpha = -1$; **check the third**: $0\cdot\alpha + 1\cdot\beta = 2$ ✓.

$$\boxed{\mathbf{c}_3 = 2\,\mathbf{c}_2 - \mathbf{c}_1}$$

**Step 2 — geometric meaning.** Since $\mathbf{c}_3$ is built from $\mathbf{c}_1$ and $\mathbf{c}_2$, all three columns live in the **single plane through the origin** spanned by $\mathbf{c}_1, \mathbf{c}_2$ (equivalently $\det[\mathbf{c}_1\ \mathbf{c}_2\ \mathbf{c}_3] = 0$). Consequences:
- Only vectors **in that plane** can ever be produced: most $\mathbf{b} \in \mathbb{R}^3$ are unreachable.
- When $\mathbf{b}$ *is* in the plane, the recipe is **not unique**: adding $t(1, -2, 1)$ (a null-space vector, since $1\cdot\mathbf{c}_1 - 2\mathbf{c}_2 + 1\cdot\mathbf{c}_3 = 0$) to any solution gives another.

**Examiner's note:** Tests column dependence by inspection and its two consequences: restricted $C(A)$ and non-unique solutions.
""")
    code(cells, r"""# SymPy verification — Lab 1, Q.14
c1, c2, c3 = Matrix([1, 1, 0]), Matrix([1, 2, 1]), Matrix([1, 3, 2])
assert 2 * c2 - c1 == c3
print("Q.14  c3 = 2*c2 - c1 verified; det = ", Matrix.hstack(c1, c2, c3).det())
print("Null-space direction of [c1 c2 c3]:", Matrix.hstack(c1, c2, c3).nullspace()[0].T)""")

    # ---------------- Q15 ----------------
    md(cells, r"""### Q.15) The Third Column Equals the Right Side (Hard)

**Question (as printed):** In
$$\begin{aligned} 6u + 7v + 8w &= 8 \\ 4u + 5v + 9w &= 9 \\ 2u - 2v + 7w &= 7 \end{aligned}$$
the third column (multiplying $w$) is the same as the right side. The column form of the equations immediately gives the solution for $(u, v, w)$?

**Step 1 — read the system as columns.** $u\,\mathbf{c}_1 + v\,\mathbf{c}_2 + w\,\mathbf{c}_3 = \mathbf{b}$ with
$$\mathbf{c}_1 = \begin{bmatrix}6\\4\\2\end{bmatrix},\quad \mathbf{c}_2 = \begin{bmatrix}7\\5\\-2\end{bmatrix},\quad \mathbf{c}_3 = \begin{bmatrix}8\\9\\7\end{bmatrix},\quad \mathbf{b} = \begin{bmatrix}8\\9\\7\end{bmatrix}.$$

**Step 2 — spot the identity.** $\mathbf{c}_3 = \mathbf{b}$. So the recipe
$$u = 0,\quad v = 0,\quad w = 1 \qquad\Longrightarrow\qquad 0\cdot\mathbf{c}_1 + 0\cdot\mathbf{c}_2 + 1\cdot\mathbf{c}_3 = \mathbf{b}$$
solves the system **with no elimination at all**. (Every row checks instantly: row 1 reads $8 = 8$, etc.)

**Step 3 — is it unique?** $\det[\mathbf{c}_1\ \mathbf{c}_2\ \mathbf{c}_3] \ne 0$ (rows are independent after elimination), so the columns are independent and $(0, 0, 1)$ is the **only** recipe.

$$\boxed{(u, v, w) = (0,\ 0,\ 1)}$$

**Examiner's note:** Tests instant column-picture recognition: if some column equals $b$, put a $1$ there and $0$s elsewhere.
""")
    code(cells, r"""# SymPy verification — Lab 1, Q.15
A15 = Matrix([[6, 7, 8], [4, 5, 9], [2, -2, 7]])
x15 = A15.LUsolve(Matrix([8, 9, 7]))
print("Q.15 solution (u, v, w) =", x15.T, "| det(A) =", A15.det(), "(non-zero => unique)")
assert x15 == Matrix([0, 0, 1])""")

    # ---------------- Q16 ----------------
    md(cells, r"""### Q.16) Challenge: Three Hyperplanes in $\mathbb{R}^4$ (Challenge)

**Question (as printed):** Describe the intersection of the three planes
$$u + v + w + z = 6, \qquad u + w + z = 4, \qquad u + w = 2$$
in four-dimensional space. Is it a line, a point, or an empty set? What is the intersection if the fourth plane $u = -1$ is included? Find a fourth equation that leaves us with no solution.

**Step 1 — eliminate by subtraction (the equations are designed for it).**
- (eq 1) − (eq 2): $v = 2$.
- (eq 2) − (eq 3): $z = 2$.
- (eq 3): $u + w = 2$ — **one free parameter remains**, say $u = t$, $w = 2 - t$.

$$x = \begin{bmatrix} u \\ v \\ w \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 2 \\ 2 \\ 2 \end{bmatrix} + t\begin{bmatrix} 1 \\ 0 \\ -1 \\ 0 \end{bmatrix}, \qquad t \in \mathbb{R}.$$

**Answer to the trick question: it is a LINE** — neither a point nor empty. (Three equations in four unknowns with independent rows leave $4 - 3 = 1$ free variable; the general solution set is a 1-dimensional affine line in $\mathbb{R}^4$, passing through $(0,2,2,2)$ in the direction $(1,0,-1,0)$.)

**Step 2 — add the plane $u = -1$.** The free parameter is locked: $u = -1 \Rightarrow w = 3$, and the line collapses to the single **point**
$$(-1,\ 2,\ 3,\ 2). \quad \text{(Check eq 1: } -1 + 2 + 3 + 2 = 6\ \checkmark\text{)}$$

**Step 3 — a fourth equation with no solution.** Any equation contradicting one already forced is enough, e.g.
$$u + w = 3 \qquad (\text{it directly contradicts } u + w = 2),$$
or equally $v = 0$ or $z = 0$. The system becomes inconsistent: elimination produces a row $[0\ 0\ 0\ 0 \mid \ne 0]$.

**Examiner's note:** Tests free-variable counting in $\mathbb{R}^4$: three good hyperplanes leave a line; pinning the free variable gives a point; one contradictory equation empties the set.
""")
    code(cells, r"""# SymPy verification — Lab 1, Q.16
A16 = Matrix([[1, 1, 1, 1], [1, 0, 1, 1], [1, 0, 1, 0]])
ns = A16.nullspace()
print("Q.16 null-space direction(s):", [v.T for v in ns], "=> solution set is a line")
assert len(ns) == 1
assert A16 * Matrix([-1, 2, 3, 2]) == Matrix([6, 4, 2])   # the u = -1 point
print("Point with u = -1: (-1, 2, 3, 2). Contradictory 4th equation: u + w = 3 vs u + w = 2.")""")

    return cells


LAB_TITLE = "Lab 2 Solutions: Matrix Multiplication (MUL-TEA-PLICATION)"
LAB_SUB = (
    "**Core ideas tested:** $Ax$ as a combination of columns and as dot products of rows, "
    "$uA$ as a combination of rows, block structure, word matrices and non-commutativity, "
    "the influence matrix $J - I$, and the adjacency-matrix walk-counting theorem $(M^k)_{ij}$."
)


def get_lab2_cells():
    cells = []
    md(cells, lab_header(LAB_TITLE, LAB_SUB))

    # ---------------- Q1 ----------------
    md(cells, r"""### Q.1) Raw-Material Requirements: $Ax$ for a Production Plan (Easy)

**Question (as printed):** Each column of
$$A = \begin{bmatrix} 2 & 1 & 0 \\ 1 & 3 & 2 \\ 0 & 2 & 4 \end{bmatrix}$$
represents the amount of Steel, Plastic and Silicon required to produce one unit of each product (laptop, tablet, smart watch). The production plan is $x = (1, 2, 1)^T$. Compute the total amount of each raw material, $Ax$.

**Step 1 — column picture (the *right* way to see this problem).** Making 1 laptop, 2 tablets and 1 watch means taking
$$Ax = 1\cdot\underbrace{\begin{bmatrix}2\\1\\0\end{bmatrix}}_{\text{laptop}} + 2\cdot\underbrace{\begin{bmatrix}1\\3\\2\end{bmatrix}}_{\text{tablet}} + 1\cdot\underbrace{\begin{bmatrix}0\\2\\4\end{bmatrix}}_{\text{watch}} = \begin{bmatrix}2\\1\\0\end{bmatrix} + \begin{bmatrix}2\\6\\4\end{bmatrix} + \begin{bmatrix}0\\2\\4\end{bmatrix}$$

**Step 2 — add the columns.**
$$Ax = \begin{bmatrix} 2+2+0 \\ 1+6+2 \\ 0+4+4 \end{bmatrix} = \begin{bmatrix} 4 \\ 9 \\ 8 \end{bmatrix}$$

**Step 3 — row-by-row cross-check (dot products).**
- Steel: $2(1) + 1(2) + 0(1) = 4$
- Plastic: $1(1) + 3(2) + 2(1) = 9$
- Silicon: $0(1) + 2(2) + 4(1) = 8$

**Answer:** $Ax = (4, 9, 8)^T$ — 4 units of steel, 9 of plastic, 8 of silicon.

**Examiner's note:** Tests matrix–vector multiplication both as column combinations (input–output interpretation) and row dot products.
""")
    code(cells, r"""# SymPy verification — Lab 2, Q.1
A1 = Matrix([[2, 1, 0], [1, 3, 2], [0, 2, 4]])
x1 = Matrix([1, 2, 1])
print("Q.1  Ax (Steel, Plastic, Silicon) =", (A1 * x1).T)
assert A1 * x1 == Matrix([4, 9, 8])""")

    # ---------------- Q2 ----------------
    md(cells, r"""### Q.2) Recommendation Scores: Row Vector Times Matrix $uA$ (Easy)

**Question (as printed):** A music recommendation system stores user preferences as $u = [\,2\ \ 1\ \ 3\,]$ and song characteristics as
$$A = \begin{bmatrix} 1 & 0 \\ 2 & 1 \\ 0 & 3 \end{bmatrix}. \qquad \text{The row vector } s = uA \text{ gives the score of each song. Compute } s.$$

**Step 1 — left multiplication combines the ROWS of $A$.** A $1\times3$ times a $3\times2$ gives a $1\times2$:
$$s = 2[\,1\ \ 0\,] + 1[\,2\ \ 1\,] + 3[\,0\ \ 3\,]$$

**Step 2 — add the weighted rows.**
$$s = [\,2+2+0,\ \ 0+1+9\,] = [\,4\ \ 10\,]$$

**Step 3 — entrywise check (row · column).**
- Score of song 1: $2(1) + 1(2) + 3(0) = 4$
- Score of song 2: $2(0) + 1(1) + 3(3) = 10$

**Answer:** $s = (4,\ 10)$ — song 2 matches this listener better.

**Examiner's note:** Tests $uA$ as a linear combination of rows of $A$ — the mirror image of Q.1.
""")
    code(cells, r"""# SymPy verification — Lab 2, Q.2
u2 = Matrix([[2, 1, 3]])
A2 = Matrix([[1, 0], [2, 1], [0, 3]])
print("Q.2  s = uA =", u2 * A2)
assert u2 * A2 == Matrix([[4, 10]])""")

    # ---------------- Q3 ----------------
    md(cells, r"""### Q.3) Sound Recipes: Bach and MLK in a Matrix $S$ (Medium)

**Question (as printed):** Sound clips of the Bach and MLK audios are stored as the **columns** of
$$S = \begin{bmatrix} 2 & 1 \\ -1 & 1 \\ 1 & -1 \\ 0 & 2 \end{bmatrix} = \left[\;\underset{|}{\text{Bach}}\;\quad \underset{|}{\text{MLK}}\;\right].$$
(a) Which recipe produces both sounds at their original amplitudes? (b) Which recipe reduces Bach to half amplitude while keeping MLK unchanged? (c) Interpret the recipe matrix $R = \begin{bmatrix} 1 & 1 & \tfrac12 \\ 0 & 1 & 1 \end{bmatrix}$ column by column, without multiplying. (d) Compute $SR$.

**Step 1 — what is a "recipe"?** A recipe is a 2-vector $r = (r_1, r_2)^T$ of amplitudes for (Bach, MLK). Playing them together produces
$$Sr = r_1\cdot\text{Bach} + r_2\cdot\text{MLK}$$
— a linear combination of the two columns.

**Part (a).** Both sounds at *original* amplitude means $1\cdot$Bach $+\ 1\cdot$MLK:
$$\boxed{r = \begin{bmatrix} 1 \\ 1 \end{bmatrix}} \qquad (\text{not } (1,0)^T \text{ or } (0,1)^T, \text{ which play only one sound}).$$

**Part (b).** Half Bach, full MLK:
$$\boxed{r = \begin{bmatrix} \tfrac12 \\ 1 \end{bmatrix}} \qquad (\text{the alternative } (1, \tfrac12)^T \text{ would halve MLK instead — the order of entries matters!})$$

**Part (c) — read $R$ column by column without multiplying.** With $R = [\,r_1\ r_2\ r_3\,]$:
- $r_1 = (1, 0)^T$: Bach at full volume, MLK **silent** $\Rightarrow Sr_1$ is the Bach clip alone.
- $r_2 = (1, 1)^T$: both at original amplitude — the answer to (a) $\Rightarrow Sr_2$ is the full mixture.
- $r_3 = (\tfrac12, 1)^T$: Bach halved, MLK full — the answer to (b) $\Rightarrow Sr_3$ is the half-Bach mix.

By the column-operation view of multiplication, **the $j$-th column of $SR$ is exactly $Sr_j$**: $SR$ performs all three recipes in one multiplication.

**Part (d) — compute $SR$.**
$$SR = \begin{bmatrix} 2 & 1 \\ -1 & 1 \\ 1 & -1 \\ 0 & 2 \end{bmatrix}\begin{bmatrix} 1 & 1 & \tfrac12 \\ 0 & 1 & 1 \end{bmatrix} = \begin{bmatrix} 2 & 3 & 2 \\ -1 & 0 & \tfrac12 \\ 1 & 0 & -\tfrac12 \\ 0 & 2 & 2 \end{bmatrix}$$
Column-by-column check: $Sr_1 = (2,-1,1,0)^T$ ✓ (Bach alone); $Sr_2 = (3,0,0,2)^T$ ✓ (both); $Sr_3 = (2,\tfrac12,-\tfrac12,2)^T$ ✓ (half Bach).

**Examiner's note:** Tests the columns-at-a-time view: $(SR)_{\cdot j} = S(\text{col}_j R)$, and that recipe order (which entry is which sound) matters.
""")
    code(cells, r"""# SymPy verification — Lab 2, Q.3
S3 = Matrix([[2, 1], [-1, 1], [1, -1], [0, 2]])
R3 = Matrix([[1, 1, sp.Rational(1, 2)], [0, 1, 1]])
SR = S3 * R3
print("Q.3(d) SR =")
display(SR)
assert SR == Matrix([[2, 3, 2], [-1, 0, sp.Rational(1,2)], [1, 0, sp.Rational(-1,2)], [0, 2, 2]])
assert (S3 * R3[:, 1]) == S3 * Matrix([1, 1])    # part (a) recipe
assert (S3 * R3[:, 2]) == S3 * Matrix([sp.Rational(1,2), 1])  # part (b) recipe""")

    # ---------------- Q4 ----------------
    md(cells, r"""### Q.4) Compute $Ax$ for a Sparse 5×5 Without Building It (Medium)

**Question (as printed):** A $5\times5$ matrix contains zeros everywhere except $a_{ii} = 1$ and $a_{i,5} = 2$ for $i = 1, \dots, 4$. Let $x = (1, 1, 1, 1, 5)^T$. Compute $Ax$ **without constructing the full matrix**.

**Step 1 — write down only the pattern.**
$$A = \begin{bmatrix} 1 & 0 & 0 & 0 & 2 \\ 0 & 1 & 0 & 0 & 2 \\ 0 & 0 & 1 & 0 & 2 \\ 0 & 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$$
It is almost the identity with an extra "2" in the last column and a zero bottom row.

**Step 2 — reason row by row.** For $i = 1, \dots, 4$: row $i$ touches only $x_i$ (weight 1) and $x_5$ (weight 2):
$$(Ax)_i = 1\cdot x_i + 2\cdot x_5 = 1 + 2(5) = 11.$$
Row 5 is all zeros: $(Ax)_5 = 0$.

**Answer:**
$$Ax = \begin{bmatrix} 11 \\ 11 \\ 11 \\ 11 \\ 0 \end{bmatrix}$$

**Why this works (the deeper point):** $(Ax)_i = \text{row}_i \cdot x$ needs only the *non-zero* entries of row $i$ — exploiting sparsity avoids $25$ multiplications. Equivalently, in column form $Ax = x_1(\text{col}_1) + \dots + x_5(\text{col}_5) = I_4x' + 5\cdot(2,2,2,2,0)^T$.

**Examiner's note:** Tests structured/sparsity reasoning instead of brute-force multiplication.
""")
    code(cells, r"""# SymPy verification — Lab 2, Q.4 (build A only to check the shortcut)
A4 = sp.eye(4).row_join(Matrix([2, 2, 2, 2]))      # 4x5 block
A4 = A4.col_join(Matrix([[0, 0, 0, 0, 0]]))        # add zero 5th row
x4 = Matrix([1, 1, 1, 1, 5])
print("Q.4  Ax =", (A4 * x4).T)
assert A4 * x4 == Matrix([11, 11, 11, 11, 0])""")

    # ---------------- Q5 ----------------
    md(cells, r"""### Q.5) Three Stage Lamps: Full Sub-Question Treatment (Medium)

**Question (as printed):** Three lamps with colours Red $(1,0,0)^T$, Cyan $(0,1,1)^T$, Yellow $(1,1,0)^T$ are the columns of
$$L = \begin{bmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 1 & 0 \end{bmatrix}\;\begin{matrix}\leftarrow R\\ \leftarrow G\\ \leftarrow B\end{matrix}$$
A recipe is a dial column $x \in [0,1]^3$ and $Lx$ is the colour on the wall.
(a) Which recipe turns Red and Cyan on at full power with Yellow off? What colour appears, and why is it not one of the three lamp colours?
(b) Which recipe dims Red to half with Cyan full and Yellow off?
(c) For $R = \begin{bmatrix} 1 & \tfrac12 & 0 \\ 1 & \tfrac12 & \tfrac12 \\ 0 & 0 & \tfrac12 \end{bmatrix}$, say what happens for each of $Lr_1, Lr_2, Lr_3$ without multiplying. What is the relation between $r_1$ and $r_2$, and what does it force about the two colours?
(d) What does the second row $(0,1,1)$ of $L$ describe? What quantity is the second entry of $Lr_1$?
(e) Why can the wall never show pure blue $(0,0,1)$, no matter how the dials are set?

**Part (a).** Red full, Cyan full, Yellow off: $x = (1, 1, 0)^T$ (first of the three printed options).
$$Lx = \text{Red} + \text{Cyan} = \begin{bmatrix}1\\0\\0\end{bmatrix} + \begin{bmatrix}0\\1\\1\end{bmatrix} = \begin{bmatrix}1\\1\\1\end{bmatrix} = \textbf{white}.$$
White is not a lamp colour because **mixing lamps creates new colours**: the output lives in the *span* of the lamp columns, which contains vectors (like $(1,1,1)$) that no single column reaches. Additive colour mixing is literally linear combination.

**Part (b).** Red at $\tfrac12$, Cyan at $1$, Yellow at $0$: $x = (\tfrac12, 1, 0)^T$:
$$Lx = \tfrac12\text{Red} + \text{Cyan} = \begin{bmatrix} 1/2 \\ 1 \\ 1 \end{bmatrix} \; \text{(a pale cyan-blue)}.$$

**Part (c).** Read the recipe columns of $R$:
- $r_1 = (1, 1, 0)^T$ = exactly the recipe from (a) $\Rightarrow Lr_1 = (1,1,1)^T$ = **white**.
- $r_2 = (\tfrac12, \tfrac12, 0)^T = \tfrac12\, r_1$. **Linearity forces** $Lr_2 = \tfrac12\, Lr_1 = (\tfrac12, \tfrac12, \tfrac12)^T$ = **mid grey**. (Scaling the recipe scales the colour — no arithmetic needed.)
- $r_3 = (0, \tfrac12, \tfrac12)^T = \tfrac12(\text{Cyan} + \text{Yellow})$ as a combination $\Rightarrow Lr_3 = \tfrac12\,(0,1,1) + \tfrac12\,(1,1,0) = (\tfrac12, 1, \tfrac12)^T$ = **pale green**.

The relationship $r_2 = \frac12 r_1$ **forces** the two output colours to be related by the same factor: equal recipes give equal colours up to overall brightness.

**Part (d).** Row 2 of $L$ is $(0, 1, 1)$: it records **which lamps feed the green channel** (Cyan and Yellow emit green; Red does not). The second entry of $Lr_1$ is $\text{row}_2 \cdot r_1 = $ the **total amount of green light** landing on the wall — the green intensity of the mixed colour.

**Part (e).** Suppose $Lx = (0, 0, 1)$ with dials $x_1, x_2, x_3 \ge 0$. The three output rows demand:
$$\underbrace{x_1 + x_3}_{\text{red out}} = 0, \qquad \underbrace{x_2 + x_3}_{\text{green out}} = 0, \qquad \underbrace{x_2}_{\text{blue out}} = 1.$$
Red out $= 0$ with non-negative dials forces $x_1 = x_3 = 0$ (dials can only *add* light). Then green out $= x_2 = $ blue out $= 1 \ne 0$ — contradiction. In words: the only lamp that emits blue (Cyan) emits **equal green at the same time**, so any blue on the wall drags green with it; killing the green kills the blue.

**Examiner's note:** Tests $Lx$ as additive colour mixing, linearity ($L(\alpha r) = \alpha Lr$), row meanings, and a feasibility argument using non-negativity.
""")
    code(cells, r"""# SymPy verification — Lab 2, Q.5
L5 = Matrix([[1, 0, 1], [0, 1, 1], [0, 1, 0]])
H = sp.Rational(1, 2)
assert L5 * Matrix([1, 1, 0]) == Matrix([1, 1, 1])                      # (a) white
assert L5 * Matrix([H, 1, 0]) == Matrix([H, 1, 1])                  # (b)
R5 = Matrix([[1, sp.Rational(1, 2), 0], [1, sp.Rational(1, 2), sp.Rational(1, 2)], [0, 0, sp.Rational(1, 2)]])
LR = L5 * R5
print("Q.5(c) LR columns (white, mid-grey, pale green):")
display(LR)
assert LR[:, 0] == Matrix([1, 1, 1]) and LR[:, 1] == Matrix([H, H, H]) and LR[:, 2] == Matrix([H, 1, H])
# (e) solve for "pure blue" and show the recipe needs a negative dial
xb = L5.LUsolve(Matrix([0, 0, 1]))
print("Q.5(e) the only mathematical recipe for blue is x =", xb.T, "-> needs dial = -1 (impossible)")
assert xb == Matrix([1, 1, -1])""")

    # ---------------- Q6 ----------------
    md(cells, r"""### Q.6) Six Antennas into Three Channels (Medium)

**Question (as printed):** Six antenna signals $x = (2,4,6,8,10,12)^T$ are aggregated by
$$A = \begin{bmatrix} 1 & 0 & 0 & 1 & 0 & 0 \\ 0 & 1 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{bmatrix} = [\,I_3 \mid I_3\,].$$
(a) Which two antennas feed each channel? (b) If antenna 4 doubles, is it true that only one channel is affected? (c) Which channels change if antenna 2 stops? (d) With the rearranged $x' = (2,6,4,8,10,12)^T$, which channels change — without multiplying? (e) Which row of $A$ must change so channel 1 combines antennas 1 and 5?

**Part (a) — read the rows.** Channel $i$ adds exactly the two entries where row $i$ has a 1:
$$\text{ch }1: x_1 + x_4, \qquad \text{ch }2: x_2 + x_5, \qquad \text{ch }3: x_3 + x_6.$$
So channel 1 pairs antennas **1 & 4**, channel 2 pairs **2 & 5**, channel 3 pairs **3 & 6** (numerically: $10, 14, 18$).

**Part (b).** **Agree.** The number 4 appears in *exactly one row* — row 1. Doubling $x_4$ changes only $\text{ch}_1 = x_1 + x_4$ (from $10$ to $18$); channels 2 and 3 never see $x_4$. Each row of a block matrix $[\,I_3\mid I_3\,]$ touches a disjoint pair.

**Part (c).** Antenna 2 appears only in row 2: only **channel 2** changes ($x_2 + x_5$ drops from $14$ to $10$).

**Part (d).** $x'$ swaps entries 2 and 3 of $x$ (4 ↔ 6). Channel 1 uses $x_1, x_4$ — untouched. Channel 2 uses $x_2$ ($4 \to 6$) and channel 3 uses $x_3$ ($6 \to 4$): **channels 2 and 3 both change** (to $6 + 10 = 16$ and $4 + 12 = 16$), and they actually become *equal* because both channels now sum the same multiset $\{4, 6, 10, 12\}$ pairs. No multiplication required — only the row patterns matter.

**Part (e).** Row 1 must select $x_1$ and $x_5$ instead of $x_1$ and $x_4$:
$$\text{row}_1 = [\,1\ \ 0\ \ 0\ \ 0\ \ 1\ \ 0\,].$$

**Examiner's note:** Tests reading a matrix's *structure* (which row touches which input) to predict input–output behaviour without computing.
""")
    code(cells, r"""# SymPy verification — Lab 2, Q.6
A6 = Matrix([[1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1]])
x6 = Matrix([2, 4, 6, 8, 10, 12])
x6b = Matrix([2, 6, 4, 8, 10, 12])
print("Q.6   Ax  =", (A6 * x6).T, "   (channels: ch1=ant1+ant4, ch2=ant2+ant5, ch3=ant3+ant6)")
print("Q.6(d) Ax' =", (A6 * x6b).T, " (ch1 unchanged; ch2, ch3 change and coincide)")
assert A6 * x6 == Matrix([10, 14, 18]) and A6 * x6b == Matrix([10, 16, 16])
A6mod = A6.copy(); A6mod[0, :] = Matrix([[1, 0, 0, 0, 1, 0]])
print("Q.6(e) modified row 1 pairs antennas 1 & 5:", A6mod.row(0))""")

    # ---------------- Q7 ----------------
    md(cells, r"""### Q.7) Word Matrices: Why $AB \ne BA$ (Hard)

**Question (as printed):** $A$ is the matrix of subjects (each row $[\,\varnothing,\ \varnothing,\ \text{subject}\,]$, so the subjects sit in the **third column** and the "wipe-out" symbol $\varnothing$ fills the rest), $B$ is the $3\times3$ matrix of predicates
$$B = \begin{bmatrix} \text{meet in a line} & \text{can be parallel} & \text{never meet at a point} \\ \text{rocks} & \text{combines the columns} & \text{takes rows times columns} \\ \text{is fun} & \text{explains everything} & \text{never lies} \end{bmatrix},$$
$C = \left[\,\text{", and that is a fact"};\ \text{"as Strang shows"};\ \text{"believe it or not"}\,\right]$. Operations: $x\,\text{⧺}\,y$ glues words with a space; $+$ keeps both alternatives; $\varnothing$ **wipes out** whatever it touches ($\varnothing\,\text{⧺}\,y = \varnothing$ and $y\,\text{⧺}\,\varnothing = \varnothing$).
(a) Which of $AB$, $BA$ is more meaningful? (b) Compute $(AB)_{11}$ and $(BA)_{11}$ and explain why $AB \ne BA$. (c) Compute $((AB)C)_{31}$.

> **Interpretation note:** the sheet prints $A$ as a $3\times3$ whose every row is $[\,\varnothing\ \varnothing\ \text{subject}\,]$. We use that printed form throughout; the conclusions (a)–(c) are the same under the alternative "$A$ is a $3\times1$ subject column" reading.

**Step 1 — what does the $\varnothing$ column do to $AB$?** By the row-times-column rule with word-multiplication:
$$(AB)_{ij} = \underbrace{\varnothing\,\text{⧺}\,B_{1j}}_{\varnothing} + \underbrace{\varnothing\,\text{⧺}\,B_{2j}}_{\varnothing} + \underbrace{A_{i3}\,\text{⧺}\,B_{3j}}_{\text{subject}_i\ +\ \text{predicate}_j}$$
Only the **third column of $A$** and the **third row of $B$** survive. So
$$(AB)_{ij} = \text{subject}_i\ \text{⧺}\ B_{3j} \in \{\text{"is fun", "explains everything", "never lies"}\}.$$

**Part (a).** $AB$ is a $3\times3$ matrix of complete English sentences — e.g. row 3 is "Two planes is fun / Two planes explains everything / Two planes never lies". For $BA$: $(BA)_{ij} = \sum_k B_{ik}\,\text{⧺}\,A_{kj}$; columns 1 and 2 of $A$ are all $\varnothing$, so $(BA)_{i1} = (BA)_{i2} = \varnothing$ (everything wiped), and $(BA)_{i3}$ glues **predicate before subject** — "rocks Algebra", "never lies Two planes" — reversed nonsense. **$AB$ is far more meaningful.**

**Part (b).**
$$(AB)_{11} = \text{Algebra ⧺ "is fun"} = \textbf{``Algebra is fun''}, \qquad (BA)_{11} = \varnothing\ \ (\text{wiped}).$$
Different entries (a sentence vs. wiped nothing) in the same position $\Rightarrow$ $AB \ne BA$ — even the *shapes* of meaningful content differ. This is the linguistic version of the algebraic fact that $AB$ mixes rows of $A$ with columns of $B$ **in that order**, and the order is not interchangeable.

**Part (c).** $AB$ is $3\times3$, $C$ is $3\times1$, so $(AB)C$ is $3\times1$ and, by the same row-column rule with "$+$ keeps alternatives":
$$((AB)C)_{31} = (AB)_{31}\,\text{⧺}\,C_{11} \;+\; (AB)_{32}\,\text{⧺}\,C_{21} \;+\; (AB)_{33}\,\text{⧺}\,C_{31}$$
$$= \text{``Two planes is fun, and that is a fact''} \;+\; \text{``Two planes explains everything, as Strang shows''} \;+\; \text{``Two planes never lies, believe it or not''}.$$
All three alternatives survive — a beautifully silly complete sentence produced by pure matrix mechanics.

**Examiner's note:** Tests the row-times-column definition with non-numeric entries, and why commutativity fails structurally (order of combination is built into the definition).
""")
    code(cells, r"""# Symbolic simulation of the word-matrix product — Lab 2, Q.7
# (plain Python lists: sympy.Matrix would try to sympify the words)

EMPTY = "EMPTY"
subjects = ["Algebra", "Matrix multiplication", "Two planes"]
A7w = [[EMPTY, EMPTY, subjects[i]] for i in range(3)]
B7w = [["meet in a line", "can be parallel", "never meet at a point"],
       ["rocks", "combines the columns", "takes rows times columns"],
       ["is fun", "explains everything", "never lies"]]

def wmul(a, b):
    # word-multiplication: EMPTY wipes, otherwise concatenate with a space
    return EMPTY if EMPTY in (a, b) else f"{a} {b}"

def wmat(A, B):
    out = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            terms = [wmul(A[i][k], B[k][j]) for k in range(len(A[0]))]
            terms = [t for t in terms if t != EMPTY]   # "+" keeps the surviving alternatives
            row.append(" + ".join(terms) if terms else EMPTY)
        out.append(row)
    return out

AB = wmat(A7w, B7w)
BA = wmat(B7w, A7w)
print("Q.7(b) (AB)_11 =", AB[0][0])
print("Q.7(b) (BA)_11 =", BA[0][0])
print("Q.7(a) AB row 3:", AB[2])
print("Q.7(a) BA column 3 (predicate-first gibberish):", [BA[i][2] for i in range(3)])
assert AB[0][0] == "Algebra is fun" and BA[0][0] == EMPTY
C7 = [["and that is a fact"], ["as Strang shows"], ["believe it or not"]]
ABC = wmat(AB, C7)
print("Q.7(c) ((AB)C)_31 =", ABC[2][0])

# SymPy verification — Lab 2, Q.8 (on the full 10x10)
J8 = sp.ones(10, 10)
A8 = J8 - sp.eye(10)
one = sp.ones(10, 1)
v1, v2, v3 = A8 * one, A8**2 * one, A8**3 * one
print("Q.8  A*1 =", v1.T, " A^2*1 =", v2.T, " A^3*1 =", v3.T)
assert v1 == 9 * one and v2 == 81 * one and v3 == 729 * one
assert (A8**7 * one) == 9**7 * one          # the k-formula, checked at k = 7
print("Q.8(d) A^k * 1 = 9^k * 1 verified (k = 7 check passed)")""")

    # ---------------- Q9 ----------------
    md(cells, r"""### Q.9) Challenge: Can a Matrix Count Routes? (Challenge)

**Question (as printed):** Transportation network on $\{A, B, C, D, E\}$ with roads $A\!-\!B$, $A\!-\!D$, $B\!-\!C$, $B\!-\!D$, $B\!-\!E$, $C\!-\!E$, $D\!-\!E$. $m_{ij} = 1$ when a road directly connects $i$ to $j$.
(a) Build $M$ in the vertex order $A, B, C, D, E$. (b) Compute $M^2$. (c) List all walks $A \to E$ of exactly two roads via $(M^2)_{AE}$. (d) Why does $m_{Ak}m_{kE}$ test whether $k$ can be the middle stop? (e) Complete: $(M^2)_{ij} = $ number of ______. (f) What does $M^3$ store?

**Part (a).** Rows/columns in the order $A, B, C, D, E$:
$$M = \begin{bmatrix} 0 & 1 & 0 & 1 & 0 \\ 1 & 0 & 1 & 1 & 1 \\ 0 & 1 & 0 & 0 & 1 \\ 1 & 1 & 0 & 0 & 1 \\ 0 & 1 & 1 & 1 & 0 \end{bmatrix} \begin{matrix} A\\ B\\ C\\ D\\ E \end{matrix}$$
(symmetric, zero diagonal — an undirected graph).

**Part (b).**
$$M^2 = \begin{bmatrix} 2 & 1 & 1 & 1 & 2 \\ 1 & 4 & 1 & 2 & 2 \\ 1 & 1 & 2 & 2 & 1 \\ 1 & 2 & 2 & 3 & 1 \\ 2 & 2 & 1 & 1 & 3 \end{bmatrix}$$

**Part (c).** $(M^2)_{AE} = 2$. The two length-2 walks are
$$A \to B \to E \qquad\text{and}\qquad A \to D \to E.$$
(No other neighbour of $A$ — $B$ or $D$ — is adjacent to $E$ except through these, and $C$ is not adjacent to $A$ at all.)

**Part (d).** $(M^2)_{AE} = \sum_k m_{Ak}\, m_{kE}$. The term for middle stop $k$ is the **product** $m_{Ak} \cdot m_{kE}$, which equals 1 exactly when *both* roads $A\!-\!k$ and $k\!-\!E$ exist, and 0 if either is missing. Summing over $k$ counts every valid middle stop once — each term is a boolean "can $k$ be the middle stop?" indicator.

**Part (e).** $(M^2)_{ij} = $ number of **walks of length 2 from vertex $i$ to vertex $j$**.

**Part (f).** $M^3 = M^2 \cdot M$: entry $(i,j)$ sums $ (M^2)_{ik} m_{kj}$ over $k$ — every length-2 walk to $k$ extended by one final edge $k \to j$. So **$M^3$ stores the number of walks of length 3** between every pair of vertices. In general $(M^k)_{ij}$ counts length-$k$ walks (proof by induction — exactly the argument of parts (b)–(e)).

**Examiner's note:** Tests the adjacency-matrix walk theorem, its proof pattern (sum over intermediate vertices), and reading graph facts off matrix powers.
""")
    code(cells, r"""# SymPy verification — Lab 2, Q.9
Mq = Matrix([[0, 1, 0, 1, 0],
             [1, 0, 1, 1, 1],
             [0, 1, 0, 0, 1],
             [1, 1, 0, 0, 1],
             [0, 1, 1, 1, 0]])   # order: A, B, C, D, E
M2 = Mq**2
print("Q.9(b) M^2 ="); display(M2)
assert M2[0, 4] == 2                      # (M^2)_AE = 2
# brute-force count of length-2 walks A -> E to confirm the theorem
paths = [(k, ) for k in range(5) if Mq[0, k] and Mq[k, 4]]
print("Q.9(c) middle stops k for A->k->E:", ["ABCDE"[k[0]] for k in paths])
assert len(paths) == M2[0, 4]
M3 = Mq**3
print("Q.9(f) (M^3)_AE =", M3[0, 4], "(three-road routes from A to E)")
# spot-check (M^3)_AE by hand-enumeration logic: A->B->C->E, A->B->D->E, A->D->B->E, A->B->B->E? (no self loop)
assert M3[0, 4] == sum(1 for k in range(5) for m in range(5)
                       if Mq[0, k] and Mq[k, m] and Mq[m, 4])""")

    return cells


LAB_TITLE = "Lab 3 Solutions: Linear Combinations and Span"
LAB_SUB = (
    '**Core ideas tested:** "One Recipe, Infinite Menu" — a single combination produces '
    "*one* vector while the span is the set of *all* reachable vectors; dependence/redundancy; "
    "and the target test $[\\,v_1 \\dots v_k\\,]c = b$."
)


def get_lab3_cells():
    cells = []
    md(cells, lab_header(LAB_TITLE, LAB_SUB))

    # ---------------- Q1 ----------------
    md(cells, r"""### Q.1) A Combination vs. the Span (Easy)

**Question (as printed):** For $v_1 = (1, 0)^T$, $v_2 = (0, 1)^T$: (a) compute $3v_1 + 2v_2$; (b) fill in: "$3v_1 + 2v_2$ is a ______ while the set of all vectors of the form $av_1 + bv_2$ is called their ______."

**Part (a).** $3\binom{1}{0} + 2\binom{0}{1} = \binom{3}{2}$.

**Part (b).** $3v_1 + 2v_2$ is **a (single) linear combination — one vector** — while the set $\{av_1 + bv_2 : a, b \in \mathbb{R}\}$ is their **span** (here all of $\mathbb{R}^2$).

**Examiner's note:** One combination = one point on the menu; the span = the whole menu.
""")
    code(cells, r"""# SymPy verification — Lab 3, Q.1
v1, v2 = Matrix([1, 0]), Matrix([0, 1])
print("Q.1  3*v1 + 2*v2 =", (3 * v1 + 2 * v2).T)
assert 3 * v1 + 2 * v2 == Matrix([3, 2])""")

    # ---------------- Q2 ----------------
    md(cells, r"""### Q.2) Fill in the Blanks: Combination vs. Span (Easy)

**Question (as printed):** "A linear combination produces ______ vector, whereas the span describes ______ vectors that can be produced."

**Answer:** A linear combination produces **one (single)** vector, whereas the span describes **all the** vectors that can be produced. Formally:
$$\text{span}\{v_1, \dots, v_k\} = \{\, c_1v_1 + \dots + c_kv_k \;:\; c_i \in \mathbb{R} \,\}.$$
The distinction is *one choice of coefficients* vs. *every choice at once*.

**Examiner's note:** Vocabulary check that prevents the classic exam confusion between a combination and a span.
""")

    # ---------------- Q3 ----------------
    md(cells, r"""### Q.3) Drone: Equal Amounts Only (Easy)

**Question (as printed):** Movement commands $v = (2, 1)^T$, $w = (1, 2)^T$. Without solving for coefficients, decide which of $(3,3)^T$, $(3,6)^T$, $(6,3)^T$ could be reached using **equal amounts** of the two commands; then find the coefficients for the reachable target.

**Step 1 — what "equal amounts" means.** The target must be $cv + cw = c(v + w) = c\,(3, 3)^T$ — i.e. a **multiple of $v + w = (3,3)^T$**, the line $y = x$.

**Step 2 — test each target against the line $y = x$:**
- $(3, 3)^T$: on the line ✓ — reachable with $c = 1$.
- $(3, 6)^T$: $3 \ne 6$ ✗ (would need unequal weights).
- $(6, 3)^T$: $6 \ne 3$ ✗.

**Step 3 — coefficients for the reachable target.** $c(v + w) = (3,3) \Rightarrow c = 1$: **one unit of each command**: $1\cdot(2,1) + 1\cdot(1,2) = (3,3)$ ✓.

**Examiner's note:** Tests reading a constraint ("equal coefficients") as a geometric line test *before* solving any system.
""")
    code(cells, r"""# SymPy verification — Lab 3, Q.3
v3, w3 = Matrix([2, 1]), Matrix([1, 2])
print("Q.3  v + w =", (v3 + w3).T, "=> equal-amount targets are multiples of (3, 3)")
assert v3 + w3 == Matrix([3, 3]) and 1 * v3 + 1 * w3 == Matrix([3, 3])""")

    # ---------------- Q4 ----------------
    md(cells, r"""### Q.4) Digital Artist: Yellow from Red and Green? (Easy)

**Question (as printed):** Basis colours $R = (255, 0, 0)^T$, $G = (0, 255, 0)^T$.
(a) A student claims yellow can be created by adding equal amounts of $R$ and $G$. Do you agree? Write the combination and explain the coefficients. (b) Can pure blue be created using only $R$ and $G$?

**Part (a).** **Agree.** Additive colour mixing is vector addition:
$$1\cdot R + 1\cdot G = \begin{bmatrix}255\\0\\0\end{bmatrix} + \begin{bmatrix}0\\255\\0\end{bmatrix} = \begin{bmatrix}255\\255\\0\end{bmatrix} = \text{yellow}.$$
The coefficients $(1, 1)$ are the **intensities** of each basis colour (here full brightness of each channel); other yellows arise from other equal coefficients, e.g. $0.5R + 0.5G = (127.5, 127.5, 0)$ — a dimmer yellow.

**Part (b).** **No — pure blue is impossible.** Every combination has the form
$$c_1 R + c_2 G = (255c_1,\; 255c_2,\; 0):$$
the **third (blue) coordinate is always $0$** because *both* basis vectors have zero there. Blue light simply is not in the ingredients — $\text{span}\{R, G\}$ is the plane $z = 0$ of $\mathbb{R}^3$, and $(0, 0, 255)$ is not in it.

**Examiner's note:** Tests span reasoning on a concrete coordinate: a coordinate that vanishes in every basis vector stays zero in every combination.
""")
    code(cells, r"""# SymPy verification — Lab 3, Q.4
Rc, Gc = Matrix([255, 0, 0]), Matrix([0, 255, 0])
print("Q.4(a) R + G =", (Rc + Gc).T)
assert Rc + Gc == Matrix([255, 255, 0])
comb = 3 * Rc - 7 * Gc           # any coefficients at all
assert comb[2] == 0
print("Q.4(b) blue channel of c1*R + c2*G is always 0 (checked with (3, -7))")""")

    # ---------------- Q5 ----------------
    md(cells, r"""### Q.5) Sailboat: Which Student Is Right? (Easy)

**Question (as printed):** A sailboat moves according to $v = (4, 0)^T$ and $w = (0, 3)^T$. Three students claim:
**A:** "The boat can reach every point in the plane." **B:** "Only points whose $x$ is a multiple of 4 and $y$ a multiple of 3." **C:** "Only points in the first quadrant." Which claims are correct if arbitrary **real** coefficients are allowed?

**Step 1 — what does a combination look like?** $c_1v + c_2w = (4c_1, 3c_2)$.

**Step 2 — is the target map onto?** Given any destination $(a, b) \in \mathbb{R}^2$, choose $c_1 = a/4$ and $c_2 = b/3$ — real coefficients are allowed, so division by 4 and 3 is harmless. Every point is reachable:
$$\text{span}\{v, w\} = \mathbb{R}^2 \quad (\det\begin{bmatrix}4&0\\0&3\end{bmatrix} = 12 \ne 0).$$

**Verdicts.** **A: correct** (the two axis directions are independent and cover the plane). **B: incorrect** — "multiples of 4 and 3" describes *integer* coefficients; real coefficients reach $(1, 0) = \tfrac14 v$, which is not a multiple of 4. **C: incorrect** — negative coefficients head west/south: $-v = (-4, 0)$, so all four quadrants are reachable.

**Examiner's note:** Tests how the allowed coefficient set (real vs integer vs non-negative) changes the reachable set — exactly A/B/C.
""")
    code(cells, r"""# SymPy verification — Lab 3, Q.5
v5, w5 = Matrix([4, 0]), Matrix([0, 3])
A5 = Matrix.hstack(v5, w5)
print("Q.5  det =", A5.det(), "=> span is all of R^2: only A is correct")
assert A5.det() != 0
assert sp.Rational(1, 4) * v5 == Matrix([1, 0])   # refutes B
assert -1 * v5 == Matrix([-4, 0])                                                  # refutes C""")

    # ---------------- Q6 ----------------
    md(cells, r"""### Q.6) Three 2×2 Systems: Both Pictures + Fill-ins (Medium)

**Question (as printed):** For the three systems
$$\text{(i) } x+y=5,\ x-y=1 \qquad \text{(ii) } x+2y=3,\ 2x+4y=6 \qquad \text{(iii) } x+2y=3,\ 2x+4y=7$$
(a) draw both pictures; (b) decide whether the columns can be scaled and added to produce $b$; (c) fill in the blanks (i)–(v).

**Part (a)+(b) system by system.**

**System (i).** Rows: lines $y = 5 - x$ and $y = x - 1$ cross at $(3, 2)$. Columns: need $c_1\binom{1}{1} + c_2\binom{1}{-1} = \binom{5}{1}$; adding gives $2c_1 = 6 \Rightarrow c_1 = 3$, $c_2 = 2$: $3\binom{1}{1} + 2\binom{1}{-1} = \binom{5}{1}$ ✓ — **exactly one** recipe.

**System (ii).** Rows: $2x + 4y = 6$ is literally $2\times(x + 2y = 3)$ — one line drawn twice; **infinitely many** intersection points. Columns: $\binom{2}{4} = 2\binom{1}{2}$, so the reachable set is the line $y = 2x$ through the origin, and $b = (3, 6)^T = 3\binom{1}{2}$ lies **on** it — but in *infinitely many ways*, e.g. $c_1 = 3, c_2 = 0$ or $c_1 = 1, c_2 = 1$: both give $(3,6)$.

**System (iii).** Rows: $2x + 4y = 7$ is *parallel* to $x + 2y = 3$ (doubled left side, mismatched right side $6 \ne 7$): **no** intersection. Columns: the reachable line is still $y = 2x$, but $b = (3, 7)^T$ has $7 \ne 6$ — off the line, **unreachable**.

**Part (c) — fill in the blanks.**
1. If $b$ can be formed from the columns of $A$ in exactly one way, the system has **a unique** solution.
2. If $b$ can be formed in more than one way, the system has **infinitely many** solutions.
3. If $b$ cannot be formed, then $b$ lies **outside** the span of the columns of $A$, and the system has **no** solution.
4. In the row picture, a solution corresponds to a point where the two **lines intersect**.
5. In the column picture, a solution corresponds to a way of mixing the columns of $A$ to obtain **the right-hand side vector $b$**.

**Examiner's note:** Tests the full trichotomy in both pictures, plus the vocabulary linking "ways of forming $b$" to solution counts.
""")
    code(cells, r"""# SymPy verification — Lab 3, Q.6
systems = [(Matrix([[1, 1], [1, -1]]), Matrix([5, 1])),
           (Matrix([[1, 2], [2, 4]]), Matrix([3, 6])),
           (Matrix([[1, 2], [2, 4]]), Matrix([3, 7]))]
for k, (Ak, bk) in enumerate(systems, 1):
    aug = Ak.row_join(bk)
    ra, rg = Ak.rank(), aug.rank()
    print(f"Q.6 system ({'i ii iii'.split()[k-1]}): rank(A) = {ra}, rank([A|b]) = {rg}")
assert systems[2][0].row_join(systems[2][1]).rank() == 2   # inconsistent: 2 > 1
assert systems[1][0].row_join(systems[1][1]).rank() == 1   # consistent, dependent""")

    # ---------------- Q7 ----------------
    md(cells, r"""### Q.7) Rover: Line or Plane? (Medium)

**Question (as printed):** Rover commands $v_1 = (2, 1)^T$, $v_2 = (-1, 2)^T$.
(a) Is their span a line or the entire plane? (b) What evidence from the vectors supports your answer? (c) Would replacing $v_2$ by $(4, 2)^T$ change your answer? Why?

**Part (a).** **The entire plane.** Two vectors in $\mathbb{R}^2$ span either a line (if dependent) or all of $\mathbb{R}^2$ (if independent); here
$$\det\begin{bmatrix} 2 & -1 \\ 1 & 2 \end{bmatrix} = 5 \ne 0 \Rightarrow \text{independent} \Rightarrow \text{span} = \mathbb{R}^2.$$

**Part (b) — the evidence.** The vectors are **not scalar multiples** of each other: $\tfrac{2}{-1} = -2$ but $\tfrac{1}{2} = 0.5$. Geometrically they point in genuinely different directions, so scaling and adding them can sweep out every direction.

**Part (c).** With $v_2' = (4, 2)^T = 2v_1$: now the second command is just "do the first twice" — **no new direction**. The span collapses to the single line through $(2, 1)^T$: the reachable set shrinks from the whole plane to a line. Yes — the answer changes completely.

**Examiner's note:** Tests the dependence criterion (proportionality) and its geometric consequence for the span.
""")
    code(cells, r"""# SymPy verification — Lab 3, Q.7
A7r = Matrix([[2, -1], [1, 2]])
print("Q.7  det =", A7r.det(), "=> span{v1, v2} = R^2")
assert A7r.det() != 0
print("Q.7(c) (4, 2) = 2*(2, 1):", 2 * Matrix([2, 1]) == Matrix([4, 2]),
      "=> new span is just the line through (2, 1)")""")

    # ---------------- Q8 ----------------
    md(cells, r"""### Q.8) Song Profiles: Can Two Vectors Span $\mathbb{R}^3$? (Medium)

**Question (as printed):** Songs are triples (Energy, Danceability, Acousticness). Reference tracks $v_1 = (1, 2, 0)^T$, $v_2 = (2, 1, 1)^T$. An engineer claims: "By adjusting the two coefficients, we can create any possible three-feature song profile." Do you agree? Justify using the structure of the vectors, without finding coefficients.

**Answer: disagree.** A combination of two vectors has only **two free parameters**:
$$c_1v_1 + c_2v_2 = (c_1 + 2c_2,\; 2c_1 + c_2,\; c_2),$$
but a song profile lives in $\mathbb{R}^3$ and needs **three** degrees of freedom. The span of two vectors is at most a **plane** (2-dimensional) inside $\mathbb{R}^3$ — here the plane through the origin containing $v_1$ and $v_2$ (rank of the two columns is $2 < 3$).

Geometric one-liner: **two directions can never fill three-dimensional space** — however you tilt the plane spanned by $v_1, v_2$, most song profiles sit outside it. To generate *every* profile you need three independent reference tracks.

**Examiner's note:** Tests the dimension inequality $k$ vectors span at most a $k$-dimensional set: $2 < 3$ kills the claim instantly.
""")
    code(cells, r"""# SymPy verification — Lab 3, Q.8
A8s = Matrix([[1, 2], [2, 1], [0, 1]])   # columns v1, v2
print("Q.8  rank =", A8s.rank(), "< 3 => span is a plane, not all of R^3")
assert A8s.rank() == 2""")

    # ---------------- Q9 ----------------
    md(cells, r"""### Q.9) Species Growth: $v_2 = 2v_1$ (Medium)

**Question (as printed):** $v_1 = (1, 2, 1)^T$, $v_2 = (2, 4, 2)^T$.
(a) Before calculating: what do you notice, and what does it say about the span? (b) Can $(3, 5, 3)^T$ belong to the span? (c) A student says two vectors in $\mathbb{R}^3$ must span a plane. Correct?

**Part (a).** Eyeball first: $v_2 = 2v_1$ **exactly** — every component doubled. The vectors are *dependent*, pointing along one line. Their span is therefore a **line through the origin** (1-dimensional), not a plane: the second vector adds no new direction.

**Part (b).** A vector is in the span iff it is a **multiple of $v_1$**. Compare $(3, 5, 3)$: if $c\,(1,2,1) = (3,5,3)$ then $c = 3$ from the first coordinate, but then the second would be $6 \ne 5$. So $(3,5,3)^T$ is **not** in the span. (Equivalently: it is not on the line $\{(t, 2t, t)\}$.)

**Part (c).** **Incorrect.** Two vectors in $\mathbb{R}^3$ span a plane **only if they are independent**. When one is a multiple of the other (as here) the span degenerates to a line. "Two vectors ⇒ plane" silently assumes independence — always check proportionality (or rank) first.

**Examiner's note:** Tests proportionality-by-inspection and the conditional nature of "n vectors span n dimensions".
""")
    code(cells, r"""# SymPy verification — Lab 3, Q.9
v9a, v9b = Matrix([1, 2, 1]), Matrix([2, 4, 2])
print("Q.9(a) v2 = 2*v1:", v9b == 2 * v9a, "=> span is a line")
assert v9b == 2 * v9a
target = Matrix([3, 5, 3])
print("Q.9(b) is (3,5,3) a multiple of v1?", Matrix.hstack(v9a).row_join(target).rank() == 1)
assert Matrix.hstack(v9a, target).rank() == 2     # rank jump => not in the span""")

    # ---------------- Q10 ----------------
    md(cells, r"""### Q.10) Three Toy Drones: Infinitely Many Representations (Medium)

**Question (as printed):** Drones' movement vectors $v_1 = (1, 0)^T$, $v_2 = (0, 1)^T$, $v_3 = (1, 1)^T$.
(a) Can $(4, 5)^T$ be expressed as a combination in **infinitely many** ways? Explain. (b) Why did infinitely many occur? (c) What relationship among the three vectors makes this possible? (d) If the third vector were removed, would infinitely many still be possible?

**Part (a).** Yes. One representation is obvious: $4v_1 + 5v_2 + 0\cdot v_3 = (4, 5)$. But since $v_3 = v_1 + v_2$, we can shift weight between them freely:
$$(4 - t)\,v_1 + (5 - t)\,v_2 + t\,v_3 = (4 - t + t,\; 5 - t + t) = (4, 5) \quad \text{for every } t \in \mathbb{R}.$$
Examples: $t = 1$: $(3, 4, 1)$; $t = 2$: $(2, 3, 2)$ — all reach the same target. **Infinitely many representations.**

**Part (b).** Infinitely many representations occur exactly when the representing vectors are **linearly dependent**: there is a non-trivial combination of them equal to $\mathbf{0}$, and adding any multiple of it to a solution gives another solution.

**Part (c).** The enabling relationship is $v_3 = v_1 + v_2$ (equivalently $v_1 + v_2 - v_3 = 0$): the null space of $[\,v_1\ v_2\ v_3\,]$ is non-trivial — one-dimensional, spanned by $(1, 1, -1)^T$.

**Part (d).** No. With only $v_1, v_2$ (independent), the representation of any reachable target is **unique** — $(4, 5) = 4v_1 + 5v_2$ and nothing else. Redundancy was entirely carried by the third vector.

**Examiner's note:** Tests the dependence ⟺ non-unique representation equivalence, with the null-space direction made explicit.
""")
    code(cells, r"""# SymPy verification — Lab 3, Q.10
V10 = Matrix([[1, 0, 1], [0, 1, 1]])       # columns v1, v2, v3
ns10 = V10.nullspace()
print("Q.10 null-space direction:", [v.T for v in ns10], "(the 'shift' vector)")
assert ns10[0] == Matrix([-1, -1, 1]) or ns10[0] == Matrix([1, 1, -1])
for t in [0, 1, 2]:
    rep = Matrix([4 - t, 5 - t, t])
    assert V10 * rep == Matrix([4, 5])
print("Q.10(a) representations t = 0, 1, 2 all reach (4, 5)")""")

    # ---------------- Q11 ----------------
    md(cells, r"""### Q.11) Vibration Sensors: No Determinant Allowed (Hard)

**Question (as printed):** Sensor modes $v_1 = (1, 0, 1)^T$, $v_2 = (0, 1, 1)^T$, $v_3 = (1, 1, 2)^T$. An engineer claims: "We have three independent sensor modes in $\mathbb{R}^3$, so we can generate every possible vibration profile." Without determinants or solving systems, determine:
(a) whether all three give genuinely new directions; (b) whether the span is a line, plane, or all of $\mathbb{R}^3$; (c) what happens if $v_3$ is removed.

**Part (a) — compare the vectors by eye.** Add the first two:
$$v_1 + v_2 = (1 + 0,\; 0 + 1,\; 1 + 1) = (1, 1, 2) = v_3.$$
The third mode is **not new**: it is literally mode 1 plus mode 2. Only two genuinely new directions exist. (No determinant needed — the relation is visible.)

**Part (b).** Since $v_3$ is a combination of $v_1, v_2$, the span is just $\text{span}\{v_1, v_2\}$: a **plane** through the origin (2-dimensional), **not** all of $\mathbb{R}^3$. The engineer's claim is false — most vibration profiles are unreachable. (The plane is $\{x : z = x + y\}$: check $v_1: 1 = 1 + 0$ ✓, $v_2: 1 = 0 + 1$ ✓.)

**Part (c).** Removing $v_3$ changes **nothing**: it was already in the span of the remaining two, so $\text{span}\{v_1, v_2, v_3\} = \text{span}\{v_1, v_2\}$ — the same plane. (Removing $v_1$ or $v_2$ instead would *also* leave the plane unchanged, since each of the three is a combination of the other two: $v_1 = v_3 - v_2$, $v_2 = v_3 - v_1$.)

**Examiner's note:** Tests dependence detection by direct combination (no determinant), and that a redundant vector can be dropped without shrinking the span.
""")
    code(cells, r"""# SymPy verification — Lab 3, Q.11
v11a, v11b, v11c = Matrix([1, 0, 1]), Matrix([0, 1, 1]), Matrix([1, 1, 2])
assert v11c == v11a + v11b
print("Q.11(a) v3 = v1 + v2 exactly")
M11v = Matrix.hstack(v11a, v11b, v11c)
print("Q.11(b) rank =", M11v.rank(), "=> span is a plane; plane check z = x + y:")
for vv in (v11a, v11b, v11c):
    assert vv[2] == vv[0] + vv[1]
print("Q.11(c) span with and without v3:", M11v.columnspace() == Matrix.hstack(v11a, v11b).columnspace())""")

    # ---------------- Q12 ----------------
    md(cells, r"""### Q.12) Movement Commands: Non-Unique Coefficients (Hard)

**Question (as printed):** Commands $v_1 = (1, 2, 0)^T$, $v_2 = (0, 1, 1)^T$, $v_3 = (1, 3, 1)^T$.
(a) Express $(4, 11, 3)^T$ as a combination. Are the coefficients unique?
(b) Two students obtain *different* coefficient sets and both claim to be correct. Can both be right? Explain **before calculating**. What must be true about the three vectors? Then verify by finding two different sets.

**Part (a).** Notice first that $v_1 + v_2 = (1, 3, 1) = v_3$ — the third command is redundant. Try using only the first two: $c_1v_1 + c_2v_2 = (c_1,\, 2c_1 + c_2,\, c_2) = (4, 11, 3)$ gives $c_1 = 4$, $c_2 = 3$. So
$$(4, 11, 3) = 4v_1 + 3v_2 + 0\cdot v_3. \qquad \text{Not unique (see part b).}$$

**Part (b) — the pre-calculation argument.** Both students can be right **only if the vectors are linearly dependent**: if some non-trivial combination of $v_1, v_2, v_3$ equals $\mathbf{0}$, that "zero recipe" can be added to any solution without changing the target, producing a second, different solution. Here the dependency is $v_3 = v_1 + v_2$, i.e. $1\cdot v_1 + 1\cdot v_2 - 1\cdot v_3 = 0$, so the answer is **yes, both can be correct**.

**Verification — two different sets.** Add $t\,(1, 1, -1)$ to $(4, 3, 0)$:
$$t = 0:\ \ (4, 3, 0) \qquad\qquad t = 1:\ \ (3, 2, 1) \qquad\qquad t = 5:\ \ (-1, -2, 5).$$
Check $t = 1$: $3v_1 + 2v_2 + v_3 = (3, 6, 0) + (0, 2, 2) + (1, 3, 1) = (4, 11, 3)$ ✓. Check $t = 5$: $-v_1 - 2v_2 + 5v_3 = (-1, -2, 0) + (0, -2, -2) + (5, 15, 5) = (4, 11, 3)$ ✓.

$$\boxed{\text{Every set is } (4 - t,\; 3 - t,\; t),\ t \in \mathbb{R}\ -\ \text{a one-parameter family.}}$$

**Examiner's note:** Tests that uniqueness of $Ax = b$ solutions is governed by dependence of the *columns*, and constructing the family from the null-space direction.
""")
    code(cells, r"""# SymPy verification — Lab 3, Q.12
V12 = Matrix([[1, 0, 1], [2, 1, 3], [0, 1, 1]])   # columns v1, v2, v3
b12 = Matrix([4, 11, 3])
print("Q.12 augmented RREF:"); display(V12.row_join(b12).rref()[0])
for t in [0, 1, 5]:
    rep = Matrix([4 - t, 3 - t, t])
    assert V12 * rep == b12
print("Q.12(b) coefficient sets (4-t, 3-t, t) for t = 0, 1, 5 all verified")
ns12 = V12.nullspace()
assert ns12[0] == Matrix([1, 1, -1]) or ns12[0] == Matrix([-1, -1, 1])
print("Q.12 null-space direction:", [v.T for v in ns12])""")

    # ---------------- Q13 ----------------
    md(cells, r"""### Q.13) Reaction Pathways: Which Set Spans $\mathbb{R}^3$? (Hard)

**Question (as printed):** Pathways $v_1 = (1, 0, 2)^T$, $v_2 = (0, 1, 1)^T$, $v_3 = (1, 1, 3)^T$; a second chemist replaces $v_3$ by $(1, 1, 4)^T$. Without solving any system:
(a) which set spans a plane? (b) which can span all of $\mathbb{R}^3$? (c) what changed structurally?

**Part (a) — test the original set by eye.** $v_1 + v_2 = (1, 1, 3) = v_3$ exactly. Dependent $\Rightarrow$ the original set spans only the **plane** through $v_1$ and $v_2$.

**Part (b) — test the new set.** Is $(1, 1, 4)^T$ a combination of $v_1, v_2$? Any combination is $c_1(1, 0, 2) + c_2(0, 1, 1) = (c_1, c_2, 2c_1 + c_2)$; matching the first two coordinates forces $c_1 = 1, c_2 = 1$, giving third coordinate $3 \ne 4$. So the new $v_3$ is **outside** the plane of $v_1, v_2$ — the three vectors are independent and span **all of $\mathbb{R}^3$**. (Determinant confirmation: $\det\begin{bmatrix}1&0&1\\0&1&1\\2&1&4\end{bmatrix} = 1 \ne 0$.)

**Part (c) — what changed structurally.** The dependency $v_3 = v_1 + v_2$ was **broken**: the replacement vector points out of the plane (its third coordinate is one too large: $4$ instead of $3$). One broken relation converts a rank-2 (plane) set into a rank-3 (space) set — the column space jumps from a plane to everything.

**Examiner's note:** Tests detecting dependence by inspection and understanding rank as "number of genuinely new directions".
""")
    code(cells, r"""# SymPy verification — Lab 3, Q.13
V13a = Matrix([[1, 0, 1], [0, 1, 1], [2, 1, 3]])   # original columns
V13b = Matrix([[1, 0, 1], [0, 1, 1], [2, 1, 4]])   # replaced v3
print("Q.13(a) original: rank =", V13a.rank(), "(plane)   Q.13(b) replaced: rank =", V13b.rank(),
      ", det =", V13b.det(), "(all of R^3)")
assert V13a.rank() == 2 and V13b.rank() == 3 and V13b.det() == 1""")

    # ---------------- Q14 ----------------
    md(cells, r"""### Q.14) Challenge: The Infinite Monkey Drone Controller (Challenge)

**Question (as printed):** The monkey controls commands $v_1 = (1, 1, 0)^T$, $v_2 = (0, 1, 1)^T$, $v_3 = (1, 2, 1)^T$ with arbitrary real coefficients.
(a) Describe the set of all reachable locations. (b) One command is deleted and the reachable set is **unchanged** — which could it be? Justify without solving a system. (c) If instead the monkey deletes $v_1$, what would you need to know to decide whether the reachable region changed?

**Part (a).** Spot the relation: $v_1 + v_2 = (1, 2, 1) = v_3$. The third command is redundant, so the reachable set is
$$\text{span}\{v_1, v_2\} = \text{span}\{v_1, v_2, v_3\} = \text{the plane through the origin containing } v_1, v_2.$$
Its equation: a normal vector is $v_1 \times v_2 = (1\cdot1 - 0\cdot1,\; 0\cdot0 - 1\cdot1,\; 1\cdot1 - 1\cdot0) = (1, -1, 1)$, so the plane is $x - y + z = 0$ (check: $v_1: 1 - 1 + 0 = 0$ ✓, $v_2: 0 - 1 + 1 = 0$ ✓). **Answer:** exactly the plane $x - y + z = 0$ in $\mathbb{R}^3$ — a 2-dimensional menu in a 3-dimensional world.

**Part (b).** Deleting a command keeps the span unchanged **iff the deleted vector was already a combination of the other two**. Check all three:
$$v_3 = v_1 + v_2 \ \checkmark, \qquad v_1 = v_3 - v_2 \ \checkmark, \qquad v_2 = v_3 - v_1 \ \checkmark.$$
Remarkably, **any one of the three could be deleted** — each lies in the plane of the other two, so any pair still spans the same plane $x - y + z = 0$. The monkey may delete whichever it likes.

**Part (c).** Deleting $v_1$ leaves commands $v_2, v_3$. The new reachable set is $\text{span}\{v_2, v_3\}$. To decide whether it *changed*, the one piece of information needed is:
$$\text{whether } v_1 \text{ is a linear combination of } v_2 \text{ and } v_3 \quad (\text{equivalently, whether } \text{span}\{v_2, v_3\} = \text{span}\{v_1, v_2\}).$$
For *these particular* vectors the answer is already yes ($v_1 = v_3 - v_2$), so the region does **not** change — but in general that membership fact is exactly what must be checked (it is the definition of redundancy).

**Reflection (from the sheet).** The same idea of a linear combination appears everywhere: robotics (reachable positions from motor commands), graphics (colours from RGB primaries — Lab 2's lamps), music recommendation (playlists as combinations of track features), chemistry (reaction pathways mixing into products), and biology (population growth modes). Whenever outputs are built by *scaling and adding* inputs, the mathematics is span — and redundancy means some inputs can be removed for free.

**Examiner's note:** Tests span-of-dependent-set simplification and the precise criterion for safe deletion of a generator.
""")
    code(cells, r"""# SymPy verification — Lab 3, Q.14
v14a, v14b, v14c = Matrix([1, 1, 0]), Matrix([0, 1, 1]), Matrix([1, 2, 1])
assert v14c == v14a + v14b and v14a == v14c - v14b and v14b == v14c - v14a
print("Q.14(b) every vector is a combination of the other two -> any one can be deleted")
# the plane x - y + z = 0 contains all three and has rank 2
for vv in (v14a, v14b, v14c):
    assert vv[0] - vv[1] + vv[2] == 0
print("Q.14(a) reachable set = plane x - y + z = 0; rank =",
      Matrix.hstack(v14a, v14b, v14c).rank())""")

    return cells


LAB_TITLE = "Lab 4 Solutions: Gaussian Elimination, Echelon Forms, and Rank"
LAB_SUB = (
    '**Core ideas tested:** "Same Solution, Simpler System" — elimination steps, pivots, '
    "row echelon form, rank, consistency of over-determined systems, and the incidence-matrix "
    "connection to graph theory (odd cycles vs. bipartite rank)."
)


def get_lab4_cells():
    cells = []
    md(cells, lab_header(LAB_TITLE, LAB_SUB))

    # ---------------- Q1 ----------------
    md(cells, r"""### Q.1) Factory Robot: Gaussian Elimination (Easy)

**Question (as printed):** Use Gaussian elimination on
$$\begin{aligned} x + y + z &= 9 \\ 2x + y + 3z &= 16 \\ x + 2y + z &= 11 \end{aligned}$$

**Step 1 — eliminate the first column.**
- $R_2 \to R_2 - 2R_1$: $(0, -1, 1 \mid -2)$
- $R_3 \to R_3 - R_1$: $(0, 1, 0 \mid 2)$

$$\begin{bmatrix} 1 & 1 & 1 &|& 9 \\ 0 & -1 & 1 &|& -2 \\ 0 & 1 & 0 &|& 2 \end{bmatrix}$$

**Step 2 — eliminate the second column.** $R_3 \to R_3 + R_2$: $(0, 0, 1 \mid 0)$.

**Step 3 — back-substitute** on the triangular system $x + y + z = 9$, $-y + z = -2$, $z = 0$:
$z = 0 \Rightarrow y = 2 \Rightarrow x = 9 - 2 - 0 = 7$.

$$\boxed{(x, y, z) = (7,\ 2,\ 0)}$$
Check: $2(7) + 2 + 0 = 16$ ✓ and $7 + 4 + 0 = 11$ ✓.

**Examiner's note:** Tests the standard eliminate → back-substitute pipeline with a clean integer answer.
""")
    code(cells, r"""# SymPy verification — Lab 4, Q.1
A1 = Matrix([[1, 1, 1], [2, 1, 3], [1, 2, 1]])
x1 = A1.LUsolve(Matrix([9, 16, 11]))
print("Q.1  robot position (x, y, z) =", x1.T)
assert x1 == Matrix([7, 2, 0])""")

    # ---------------- Q2 ----------------
    md(cells, r"""### Q.2) Row Echelon Form and Pivot Count (Easy)

**Question (as printed):** Apply Gaussian elimination to obtain the REF of
$$A = \begin{bmatrix} 1 & 2 & 1 \\ 2 & 5 & 3 \\ 1 & 3 & 2 \end{bmatrix}. \quad \text{How many pivots?}$$

**Step 1.** $R_2 \to R_2 - 2R_1$: $(0, 1, 1)$.  $R_3 \to R_3 - R_1$: $(0, 1, 1)$.
**Step 2.** $R_3 \to R_3 - R_2$: $(0, 0, 0)$.

$$U = \begin{bmatrix} \boxed{1} & 2 & 1 \\ 0 & \boxed{1} & 1 \\ 0 & 0 & 0 \end{bmatrix}$$

**Answer:** the row echelon form has **two pivots** (boxed, in columns 1 and 2), so $\text{rank}(A) = 2$. The zero third row reflects a hidden dependency: $R_3 = R_2 - R_1$ (check: $(2,5,3)-(1,2,1) = (1,3,2)$ ✓). Consequences: columns are dependent, $A$ is singular, and $Ax = 0$ has $3 - 2 = 1$ free variable.

**Examiner's note:** Tests clean production of a REF and reading pivot count = rank off the staircase.
""")
    code(cells, r"""# SymPy verification — Lab 4, Q.2
A2 = Matrix([[1, 2, 1], [2, 5, 3], [1, 3, 2]])
U2 = A2.echelon_form()
print("Q.2  REF:"); display(U2)
assert U2 == Matrix([[1, 2, 1], [0, 1, 1], [0, 0, 0]]) and A2.rank() == 2
assert A2.row(2) == A2.row(1) - A2.row(0)      # the hidden dependency
print("Q.2  row 3 = row 2 - row 1 confirmed")""")

    # ---------------- Q3 ----------------
    md(cells, r"""### Q.3) Drone Sensor Matrix: REF and Rank (Easy)

**Question (as printed):** Reduce to row echelon form and determine the rank:
$$B = \begin{bmatrix} 1 & 2 & 1 & 0 \\ 2 & 4 & 2 & 1 \\ 1 & 2 & 1 & 1 \end{bmatrix}$$

**Step 1.** $R_2 \to R_2 - 2R_1$: $(0, 0, 0, 1)$.  $R_3 \to R_3 - R_1$: $(0, 0, 0, 1)$.
**Step 2.** $R_3 \to R_3 - R_2$: $(0, 0, 0, 0)$.

$$U = \begin{bmatrix} \boxed{1} & 2 & 1 & 0 \\ 0 & 0 & 0 & \boxed{1} \\ 0 & 0 & 0 & 0 \end{bmatrix}$$

**Answer:** pivots sit in columns **1 and 4** — note the staircase *skips* columns 2 and 3 (a row of zeros in the middle of the working is fine; the pivot of row 2 simply moves right). $\text{rank}(B) = 2$; the null space of $B$ has $4 - 2 = 2$ dimensions (free variables $x_2, x_3$).

**Examiner's note:** Tests REF when the staircase jumps columns — pivots need not be adjacent.
""")
    code(cells, r"""# SymPy verification — Lab 4, Q.3
B3 = Matrix([[1, 2, 1, 0], [2, 4, 2, 1], [1, 2, 1, 1]])
U3 = B3.echelon_form()
print("Q.3  REF:"); display(U3)
assert U3 == Matrix([[1, 2, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]]) and B3.rank() == 2""")

    # ---------------- Q4 ----------------
    md(cells, r"""### Q.4) Online Store Revenue (Medium)

**Question (as printed):** Use Gaussian elimination on
$$\begin{aligned} x + y + z &= 120 \\ 2x + 3y + z &= 230 \\ x + 2y + 4z &= 270 \end{aligned}$$

**Step 1.** $R_2 \to R_2 - 2R_1$: $(0, 1, -1 \mid -10)$.  $R_3 \to R_3 - R_1$: $(0, 1, 3 \mid 150)$.
**Step 2.** $R_3 \to R_3 - R_2$: $(0, 0, 4 \mid 160)$.
**Step 3 — back-substitute.** $4z = 160 \Rightarrow z = 40$; $y = -10 + z = 30$; $x = 120 - 30 - 40 = 50$.

$$\boxed{(x, y, z) = (50,\ 30,\ 40)}$$
Check in equation 2: $2(50) + 3(30) + 40 = 100 + 90 + 40 = 230$ ✓.

**Examiner's note:** Same pipeline as Q1 with slightly less friendly multipliers — tests careful fraction-free elimination.
""")
    code(cells, r"""# SymPy verification — Lab 4, Q.4
A4 = Matrix([[1, 1, 1], [2, 3, 1], [1, 2, 4]])
x4 = A4.LUsolve(Matrix([120, 230, 270]))
print("Q.4  units sold (x, y, z) =", x4.T)
assert x4 == Matrix([50, 30, 40])""")

    # ---------------- Q5 ----------------
    md(cells, r"""### Q.5) Quadcopter Motor Thrusts (Medium)

**Question (as printed):** Four motors with thrusts $x_1, \dots, x_4$ satisfy
$$\begin{aligned} x_1 + x_2 + x_3 + x_4 &= 40 \\ x_1 - x_2 + x_3 - x_4 &= 0 \\ x_1 + x_2 - x_3 - x_4 &= 4 \\ x_1 - x_2 - x_3 + x_4 &= 8 \end{aligned}$$

**Step 1 — eliminate below the first pivot.** With the augmented matrix
$$\left[\begin{array}{cccc|c} 1 & 1 & 1 & 1 & 40 \\ 1 & -1 & 1 & -1 & 0 \\ 1 & 1 & -1 & -1 & 4 \\ 1 & -1 & -1 & 1 & 8 \end{array}\right]$$
- $R_2 \to R_2 - R_1$: $(0, -2, 0, -2 \mid -40) \;\Rightarrow\; x_2 + x_4 = 20$
- $R_3 \to R_3 - R_1$: $(0, 0, -2, -2 \mid -36) \;\Rightarrow\; x_3 + x_4 = 18$
- $R_4 \to R_4 - R_1$: $(0, -2, -2, 0 \mid -32) \;\Rightarrow\; x_2 + x_3 = 16$

**Step 2 — eliminate below the second pivot** (column 2, pivot row $R_2'$).
- $R_4' \to R_4' - R_2'$: $(0, 0, -2, 2 \mid 8)$
- Then $R_4'' \to R_4'' + R_3'$: $(0, 0, -4, 0 \mid -28) \;\Rightarrow\; x_3 = 7$

**Step 3 — back-substitute.** $x_4 = 18 - 7 = 11$; $x_2 = 20 - 11 = 9$; $x_1 = 40 - 9 - 7 - 11 = 13$.

$$\boxed{(x_1, x_2, x_3, x_4) = (13,\ 9,\ 7,\ 11)}$$
Check (2): $13 - 9 + 7 - 11 = 0$ ✓. Check (3): $13 + 9 - 7 - 11 = 4$ ✓. Check (4): $13 - 9 - 7 + 11 = 8$ ✓.

**Examiner's note:** Tests a $4\times4$ elimination with sign patterns — and rewards verifying every equation at the end.
""")
    code(cells, r"""# SymPy verification — Lab 4, Q.5
A5 = Matrix([[1, 1, 1, 1], [1, -1, 1, -1], [1, 1, -1, -1], [1, -1, -1, 1]])
x5 = A5.LUsolve(Matrix([40, 0, 4, 8]))
print("Q.5  motor thrusts =", x5.T)
assert x5 == Matrix([13, 9, 7, 11])
assert A5 * x5 == Matrix([40, 0, 4, 8])""")

    # ---------------- Q6 ----------------
    md(cells, r"""### Q.6) Rank of a 4×5 Rectangular Matrix (Medium)

**Question (as printed):** Find the rank of
$$A = \begin{bmatrix} 1 & 2 & 3 & 4 & 5 \\ 2 & 4 & 6 & 8 & 10 \\ 1 & 1 & 2 & 3 & 4 \\ 3 & 5 & 8 & 11 & 14 \end{bmatrix}$$

**Step 1 — elimination.**
- $R_2 \to R_2 - 2R_1$: $(0, 0, 0, 0, 0)$ — row 2 is exactly $2\times$ row 1.
- $R_3 \to R_3 - R_1$: $(0, -1, -1, -1, -1)$.
- $R_4 \to R_4 - 3R_1$: $(0, -1, -1, -1, -1)$; then $R_4 \to R_4 - R_3$: zero.

$$U = \begin{bmatrix} \boxed{1} & 2 & 3 & 4 & 5 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & \boxed{-1} & -1 & -1 & -1 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix} \;\xrightarrow{\text{reorder}}\; \begin{bmatrix} \boxed{1} & 2 & 3 & 4 & 5 \\ 0 & \boxed{-1} & -1 & -1 & -1 \\ 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$$

**Answer:** $\text{rank}(A) = 2$ — only two pivots. Both dependencies are structural and can be named in the original rows: row 2 is $2\times$ row 1, and $R_4 - R_3 = (2,4,6,8,10) = R_2$, i.e. $R_4 = R_3 + R_2$. Two independent rows out of four.

**Examiner's note:** Tests spotting proportional rows early and counting pivots for a wide matrix (rank ≤ 4 here, and in fact = 2).
""")
    code(cells, r"""# SymPy verification — Lab 4, Q.6
A6 = Matrix([[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [1, 1, 2, 3, 4], [3, 5, 8, 11, 14]])
print("Q.6  rank(A) =", A6.rank())
assert A6.rank() == 2
assert A6.row(1) == 2 * A6.row(0) and A6.row(3) == A6.row(2) + A6.row(1)
print("Q.6  dependencies: row2 = 2*row1 and row4 = row3 + row2")""")

    # ---------------- Q7 ----------------
    md(cells, r"""### Q.7) Chemistry Concentrations — Inconsistent as Printed (Medium)

**Question (as printed):** Use Gaussian elimination to solve for all concentrations:
$$\begin{aligned} x + y + z + w &= 18 \\ 2x + 3y + z + 2w &= 30 \\ x + 2y + 3z + w &= 25 \\ 3x + 4y + 4z + 3w &= 48 \end{aligned}$$

> **⚠ Discrepancy flag:** as printed, this system has **no solution**. The elimination below is shown honestly, followed by the exact consistency condition and a corrected version.

**Step 1 — eliminate.**
- $R_2 - 2R_1$: $(0, 1, -1, 0 \mid -6)$
- $R_3 - R_1$: $(0, 1, 2, 0 \mid 7)$
- $R_4 - 3R_1$: $(0, 1, 1, 0 \mid -6)$

**Step 2 — eliminate the second column.**
- $R_3' - R_2'$: $(0, 0, 3, 0 \mid 13) \Rightarrow z = 13/3$
- $R_4' - R_2'$: $(0, 0, 2, 0 \mid 0) \Rightarrow z = 0$

**Step 3 — the contradiction.** The same variable $z$ is forced to equal both $13/3$ and $0$. Equivalently: rows 1, 2, 3 are independent (rank $A = 3$) but the augmented matrix has rank $4$: the left-null combination $-5\,\text{eq}_1 - \text{eq}_2 - 2\,\text{eq}_3 + 3\,\text{eq}_4$ produces $0 = -\tfrac{26}{3}$ on the printed right sides.

**The consistency condition.** For the coefficient matrix at hand, $Ax = b$ is solvable **iff**
$$3b_4 = 5b_1 + b_2 + 2b_3.$$
The printed values give $3(48) = 144$ vs $5(18) + 30 + 2(25) = 170$ — the sheet's $b_4$ (or another entry) contains a typo. *If* the intended third right side were $b_3 = 12$ (so that $5(18) + 30 + 24 = 144$), the system would be consistent, with rank $3 < 4$ unknowns and general solution $x = \tfrac{46}{3} - w$, $y = -\tfrac53$, $z = \tfrac{13}{3}$, $w$ free.

**Answer:** **no solution as printed**; the exam skill being tested is exactly detecting this: rank $[A] = 3 <$ rank $[A \mid b] = 4$.

**Examiner's note:** Tests using elimination to *detect* inconsistency via a zero row with non-zero right side — the answer "no solution" is a legitimate, and here the correct, outcome.
""")
    code(cells, r"""# SymPy verification — Lab 4, Q.7
A7c = Matrix([[1, 1, 1, 1], [2, 3, 1, 2], [1, 2, 3, 1], [3, 4, 4, 3]])
b7c = Matrix([18, 30, 25, 48])
print("Q.7  rank(A) =", A7c.rank(), " rank([A|b]) =", A7c.row_join(b7c).rank())
assert A7c.rank() < A7c.row_join(b7c).rank()          # inconsistent
y7 = A7c.T.nullspace()[0]                              # left-null vector
print("Q.7  left-null y =", y7.T, " y^T b =", y7.dot(b7c), "(non-zero => no solution)")
print("Q.7  consistency condition 3*b4 = 5*b1 + b2 + 2*b3  <=>  y = (-5,-1,-2,3)")
assert 3 * y7 == Matrix([-5, -1, -2, 3])""")

    # ---------------- Q8 ----------------
    md(cells, r"""### Q.8) 3×5 Matrix: REF, Rank, Pivot Columns (Medium)

**Question (as printed):** Reduce to REF, determine the rank, identify the pivot columns:
$$A = \begin{bmatrix} 1 & 1 & 2 & 1 & 0 \\ 2 & 3 & 5 & 3 & 1 \\ 1 & 2 & 3 & 2 & 1 \end{bmatrix}$$

**Step 1.** $R_2 - 2R_1$: $(0, 1, 1, 1, 1)$.  $R_3 - R_1$: $(0, 1, 1, 1, 1)$.
**Step 2.** $R_3 - R_2$: $(0, 0, 0, 0, 0)$.

$$U = \begin{bmatrix} \boxed{1} & 1 & 2 & 1 & 0 \\ 0 & \boxed{1} & 1 & 1 & 1 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$$

**Answer:** pivots in columns **1 and 2**; $\text{rank}(A) = 2$; free columns are 3, 4, 5, so $Ax = 0$ has a $5 - 2 = 3$-dimensional null space. Also note row 3 of $A$ equals row 2 minus... directly: $R_3 - R_1 = R_2 - 2R_1$, i.e. $R_3 = R_2 - R_1$ ✓ (check: $(2,3,5,3,1) - (1,1,2,1,0) = (1,2,3,2,1)$ ✓).

**Examiner's note:** Tests identifying pivot vs. free columns — the distinction that later drives bases of $C(A)$ and $N(A)$.
""")
    code(cells, r"""# SymPy verification — Lab 4, Q.8
A8l = Matrix([[1, 1, 2, 1, 0], [2, 3, 5, 3, 1], [1, 2, 3, 2, 1]])
U8l = A8l.echelon_form()
print("Q.8  REF:"); display(U8l)
assert U8l == Matrix([[1, 1, 2, 1, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0]]) and A8l.rank() == 2
assert A8l.row(2) == A8l.row(1) - A8l.row(0)
print("Q.8  pivot columns: 1, 2;  free columns: 3, 4, 5")""")

    # ---------------- Q9 ----------------
    md(cells, r"""### Q.9) Five Warehouses: A Full-Rank 5×5 System (Hard)

**Question (as printed):** Solve by Gaussian elimination:
$$\begin{aligned} x_1 + x_2 + x_3 + x_4 + x_5 &= 30 \\ 2x_1 + x_2 + 3x_3 + x_4 + x_5 &= 50 \\ x_1 + 2x_2 + x_3 + 2x_4 + x_5 &= 40 \\ 3x_1 + 2x_2 + 4x_3 + 3x_4 + 2x_5 &= 70 \\ x_1 + x_2 + 2x_3 + x_4 + 3x_5 &= 45 \end{aligned}$$

**Step 1 — eliminate below the first pivot.**
- $R_2 - 2R_1$: $(0, -1, 1, -1, -1 \mid -10)$
- $R_3 - R_1$: $(0, 1, 0, 1, 0 \mid 10)$
- $R_4 - 3R_1$: $(0, -1, 1, 0, -1 \mid -20)$
- $R_5 - R_1$: $(0, 0, 1, 0, 2 \mid 15)$

**Step 2 — eliminate below the second pivot** (in column 2, using $R_2'$).
- $R_3' + R_2'$: $(0, 0, 1, 0, -1 \mid 0)$
- $R_4' - R_2'$: $(0, 0, 0, 1, 0 \mid -10)$
- ($R_5$ has a 0 in column 2 — nothing to do.)

**Step 3 — eliminate below the third pivot** (column 3).
- $R_5 - R_3''$: $(0, 0, 0, 0, 3 \mid 15) \Rightarrow x_5 = 5$

**Step 4 — back-substitute.** From $R_4''$: $x_4 = -10$. From $R_3''$: $x_3 = 0 + x_5 = 5$. From $R_2'$: $x_2 = 10 + x_3 - x_4 - x_5 = 10 + 5 + 10 - 5 = 20$. From $R_1$: $x_1 = 30 - 20 - 5 + 10 - 5 = 10$.

$$\boxed{(x_1, x_2, x_3, x_4, x_5) = (10,\ 20,\ 5,\ -10,\ 5)}$$
Check eq 2: $20 + 20 + 15 - 10 + 5 = 50$ ✓; eq 4: $30 + 40 + 20 - 30 + 10 = 70$ ✓.

**Interpretation note:** the mathematics gives $x_4 = -10$ — a *negative* shipment, which would be impossible physically. As a pure linear-algebra exercise the system is consistent and has the **unique** solution above ($\det \ne 0$, rank 5).

**Examiner's note:** Tests a full-size elimination where the answer happens to contain a negative entry — distinguishing "mathematically solvable" from "physically sensible".
""")
    code(cells, r"""# SymPy verification — Lab 4, Q.9
A9w = Matrix([[1, 1, 1, 1, 1], [2, 1, 3, 1, 1], [1, 2, 1, 2, 1],
              [3, 2, 4, 3, 2], [1, 1, 2, 1, 3]])
x9 = A9w.LUsolve(Matrix([30, 50, 40, 70, 45]))
print("Q.9  shipments =", x9.T, "| rank =", A9w.rank(), "(full rank => unique)")
assert x9 == Matrix([10, 20, 5, -10, 5])
assert A9w * x9 == Matrix([30, 50, 40, 70, 45])""")

    # ---------------- Q10 ----------------
    md(cells, r"""### Q.10) ML Dataset Matrix: Find the Rank (Hard)

**Question (as printed):** Find the rank of
$$A = \begin{bmatrix} 1 & 2 & 3 & 4 & 5 & 6 \\ 2 & 4 & 6 & 8 & 10 & 12 \\ 1 & 1 & 2 & 3 & 4 & 5 \\ 3 & 5 & 8 & 11 & 14 & 17 \end{bmatrix}$$

**Step 1.** $R_2 - 2R_1$: zero row (observation 2 is exactly twice observation 1 — a duplicated measurement pattern).
**Step 2.** $R_3 - R_1$: $(0, -1, -1, -1, -1, -1)$.  $R_4 - 3R_1$: $(0, -1, -1, -1, -1, -1)$; then $R_4 - R_3$: zero.

$$\text{rank}(A) = 2$$

**Dependencies in the original data:** $R_2 = 2R_1$ and $R_4 = R_3 + R_2$ (check: $(1,1,2,3,4,5) + (2,4,6,8,10,12) = (3,5,8,11,14,17)$ ✓). Only observations 1 and 3 carry independent information — the dataset has effectively **2 distinct features' worth of row variation**.

**Examiner's note:** Tests rank-finding on a wide "data" matrix and expressing the answer as explicit row dependencies.
""")
    code(cells, r"""# SymPy verification — Lab 4, Q.10
A10 = Matrix([[1, 2, 3, 4, 5, 6], [2, 4, 6, 8, 10, 12],
              [1, 1, 2, 3, 4, 5], [3, 5, 8, 11, 14, 17]])
print("Q.10 rank(A) =", A10.rank())
assert A10.rank() == 2
assert A10.row(1) == 2 * A10.row(0) and A10.row(3) == A10.row(2) + A10.row(1)""")

    # ---------------- Q11 ----------------
    md(cells, r"""### Q.11) Robotic Arm — Inconsistent as Printed (Hard)

**Question (as printed):** Solve by Gaussian elimination and verify by substitution:
$$\begin{aligned} x + y + z + w &= 12 \\ 2x + 3y + z + 2w &= 22 \\ x + 2y + 3z + w &= 20 \\ 3x + 4y + 4z + 3w &= 34 \end{aligned}$$

> **⚠ Discrepancy flag:** this system has the **same coefficient matrix** as Q.7 and, as printed, is likewise **inconsistent**.

**Step 1 — eliminate (identical left sides to Q.7).**
- $R_2 - 2R_1$: $(0, 1, -1, 0 \mid -2)$
- $R_3 - R_1$: $(0, 1, 2, 0 \mid 8)$
- $R_4 - 3R_1$: $(0, 1, 1, 0 \mid -2)$

**Step 2.**
- $R_3' - R_2'$: $(0, 0, 3, 0 \mid 10) \Rightarrow z = 10/3$
- $R_4' - R_2'$: $(0, 0, 2, 0 \mid 0) \Rightarrow z = 0$

**Step 3 — contradiction.** $z$ cannot be both $10/3$ and $0$; the augmented rank is $4 > \text{rank}(A) = 3$. The consistency condition $3b_4 = 5b_1 + b_2 + 2b_3$ reads $3(34) = 102$ vs $5(12) + 22 + 2(20) = 122$ — mismatch again. **No solution as printed.** (E.g. changing $b_3$ from $20$ to $10$ would satisfy the condition and yield a consistent rank-3 system.)

**Examiner's note:** Tests detecting inconsistency and connecting it to the left-null test $y^Tb \ne 0$ — the "verification by substitution" the sheet asks for is impossible when no solution exists.
""")
    code(cells, r"""# SymPy verification — Lab 4, Q.11
A11l = Matrix([[1, 1, 1, 1], [2, 3, 1, 2], [1, 2, 3, 1], [3, 4, 4, 3]])
b11l = Matrix([12, 22, 20, 34])
print("Q.11 rank(A) =", A11l.rank(), " rank([A|b]) =", A11l.row_join(b11l).rank())
assert A11l.rank() < A11l.row_join(b11l).rank()
y11 = A11l.T.nullspace()[0]
print("Q.11 y^T b =", y11.dot(b11l), "(non-zero => no solution as printed)")
print("Q.11 note: condition 3*b4 = 5*b1 + b2 + 2*b3 fails: 102 vs 122")""")

    # ---------------- Q12 ----------------
    md(cells, r"""### Q.12) 4×4 Matrix: REF and Rank (Hard)

**Question (as printed):** For
$$A = \begin{bmatrix} 1 & 2 & 1 & 3 \\ 2 & 4 & 2 & 6 \\ 1 & 3 & 2 & 4 \\ 3 & 7 & 4 & 10 \end{bmatrix}$$
(a) find the REF; (b) determine the rank.

**Step 1.** $R_2 - 2R_1$: $(0, 0, 0, 0)$ — row 2 is exactly $2\times$ row 1.
$R_3 - R_1$: $(0, 1, 1, 1)$.  $R_4 - 3R_1$: $(0, 1, 1, 1)$.
**Step 2.** $R_4 - R_3$: zero row.

$$U = \begin{bmatrix} \boxed{1} & 2 & 1 & 3 \\ 0 & 0 & 0 & 0 \\ 0 & \boxed{1} & 1 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix} \;\xrightarrow{\text{reorder}}\; \begin{bmatrix} \boxed{1} & 2 & 1 & 3 \\ 0 & \boxed{1} & 1 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$

**Answer:** (a) REF as shown, pivots in columns 1 and 2; (b) $\text{rank}(A) = 2$. Dependencies: $R_2 = 2R_1$ and $R_4 - R_3 = (2,4,2,6) = R_2$, i.e. $R_4 = R_3 + R_2$ (check: $(1,3,2,4)+(2,4,2,6) = (3,7,4,10)$ ✓).

**Examiner's note:** Tests REF production with a zero row appearing *above* a later pivot row (row ordering is cosmetic in REF).
""")
    code(cells, r"""# SymPy verification — Lab 4, Q.12
A12l = Matrix([[1, 2, 1, 3], [2, 4, 2, 6], [1, 3, 2, 4], [3, 7, 4, 10]])
print("Q.12 rank(A) =", A12l.rank(), "| REF:"); display(A12l.echelon_form())
assert A12l.rank() == 2 and A12l.row(1) == 2 * A12l.row(0)
assert A12l.row(3) == A12l.row(2) + A12l.row(1)""")

    # ---------------- Challenge ----------------
    md(cells, r"""### Challenge: Incidence Matrices — Worked Example and Part C

**Question (as printed):** The sheet first works the 4-node example graph ($A, B, C, D$ with edges $e_1\!: A\!-\!B$, $e_2\!: A\!-\!D$, $e_3\!: B\!-\!C$, $e_4\!: B\!-\!D$, $e_5\!: C\!-\!D$), giving the **unsigned** incidence matrix ($b_{ij} = 1$ if vertex $i$ lies on edge $j$). **Part C** then asks, for the 5-node transportation network ($A, B, C, D, E$ with edges $A\!-\!B$, $B\!-\!C$, $C\!-\!E$, $A\!-\!D$, $B\!-\!D$, $D\!-\!E$):
1. label the edges and construct the incidence matrix; 2. determine its rank; 3. what does the rank say about the network's structure?

**The worked example (verification).**
$$B_{\text{ex}} = \begin{bmatrix} 1 & 1 & 0 & 0 & 0 \\ 1 & 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 0 & 1 \\ 0 & 1 & 0 & 1 & 1 \end{bmatrix} \quad\text{(rows } A, B, C, D;\ \text{cols } e_1 \dots e_5\text{)}$$
The graph contains the **triangle** $B\!-\!C\!-\!D$ (edges $e_3, e_4, e_5$) — an odd cycle. Over $\mathbb{R}$, each column of a triangle contributes an independent direction, so elimination finds a pivot for **every** vertex: $\text{rank}(B_{\text{ex}}) = 4 = n$ (full row rank), despite the visible dependency pattern $\text{row}_B + \text{row}_C - \text{row}_D \ne 0$ that a bipartite graph would force.

**Part C — step 1: label and construct.** Edges (any labelling works; we use):
$$e_1\!: A\!-\!B,\quad e_2\!: B\!-\!C,\quad e_3\!: C\!-\!E,\quad e_4\!: A\!-\!D,\quad e_5\!: B\!-\!D,\quad e_6\!: D\!-\!E$$
$$B = \begin{bmatrix} 1 & 0 & 0 & 1 & 0 & 0 \\ 1 & 1 & 0 & 0 & 1 & 0 \\ 0 & 1 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 1 & 1 \\ 0 & 0 & 1 & 0 & 0 & 1 \end{bmatrix}\;\begin{matrix}A\\B\\C\\D\\E\end{matrix}$$
Every column has exactly two 1's (each edge joins two vertices); rows = vertices, columns = edges.

**Part C — step 2: rank.** The sub-graph on $\{A, B, D\}$ is a **triangle** (edges $e_1, e_4, e_5$) — an odd cycle. Eliminating the $5\times3$ triangle block alone already yields pivots for $A, B, D$; edges $e_2, e_3, e_6$ then attach $C$ and $E$ with two more independent rows:
$$\text{rank}(B) = 5 = n \quad \text{(full row rank — verified numerically below)}.$$

**Part C — step 3: what the rank says.** For an unsigned incidence matrix over $\mathbb{R}$:
$$\text{rank}(B) = \begin{cases} n & \text{if the graph contains an odd cycle (is not bipartite),} \\ n - 1 & \text{if the graph is bipartite (all cycles even).} \end{cases}$$
*Why:* if the graph is bipartite with vertex parts $V_1 \cup V_2$, every edge has one endpoint in each part, so $\sum_{i \in V_1}\text{row}_i = \sum_{j \in V_2}\text{row}_j$ — one dependency, rank $n - 1$. An odd cycle destroys every such splitting, so no dependency survives and the rank is full. Here: the triangle makes the network **non-bipartite**, and the rank $5$ certifies exactly that. Structurally, full row rank also means the *only* vector $y$ with $y^TA = 0$ is $y = 0$: there is no way to assign weights to vertices that cancels on every edge.

**Examiner's note:** Tests constructing an incidence matrix and the odd-cycle/bipartite rank dichotomy — the graph-theoretic payoff of rank.
""")
    code(cells, r"""# SymPy verification — Lab 4, Challenge
Bex = Matrix([[1, 1, 0, 0, 0],
              [1, 0, 1, 1, 0],
              [0, 0, 1, 0, 1],
              [0, 1, 0, 1, 1]])
print("Challenge example: rank =", Bex.rank(), "(4 nodes, triangle B-C-D => full rank)")
assert Bex.rank() == 4

BpC = Matrix([[1, 0, 0, 1, 0, 0],       # A
              [1, 1, 0, 0, 1, 0],       # B
              [0, 1, 1, 0, 0, 0],       # C
              [0, 0, 0, 1, 1, 1],       # D
              [0, 0, 1, 0, 0, 1]])      # E
print("Part C: rank =", BpC.rank(), "(5 nodes, triangle A-B-D => full row rank, non-bipartite)")
assert BpC.rank() == 5
assert all(sum(BpC[i, j] for i in range(5)) == 2 for j in range(6))
print("Part C: every column of B has exactly two 1s (each edge joins two vertices)")""")

    return cells
