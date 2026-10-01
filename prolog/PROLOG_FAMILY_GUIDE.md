* [ ] 

# Comprehensive Guide: Prolog Family Tree Knowledge Base

This guide provides a comprehensive overview of [`family.pl`](file:///Users/ba/TEKVORA_SOFTWARES/AI_CLASS/prolog/family.pl), the foundational concepts of **Symbolic AI**, declarative programming, and how to query the inference engine in SWI-Prolog.

---

## 1. Conceptual Background: Why Prolog in AI?

In standard procedural/imperative languages (Python, Java, C++), you must write algorithms explaining **HOW** to solve a problem step-by-step:

> *Iterate over an array, check if person equals father, append to a list, return list.*

In **Prolog** (*Programming in Logic*), you program **declaratively**. You tell the computer **WHAT** is true about the world (Knowledge Representation), and the Prolog inference engine automatically deduces answers through logical inference:

> *John is parent of Mary. A father is a male parent. Therefore, is John the father of Mary? Prolog figures out the answer.*

### Core AI Principles Demonstrated:

1. **Knowledge Base (KB)**: A repository of known domain truths.
2. **First-Order Predicate Logic**: Expressing relationships (`parent/2`, `male/1`).
3. **Horn Clauses**: Rules of the form `Head :- Body` (*"Head is true IF Body is true"*).
4. **Resolution Refutation & Unification**: The automated theorem proving mechanism used by Prolog.

---

## 2. Visual Family Tree

Based on the facts defined in [`family.pl`](file:///Users/ba/TEKVORA_SOFTWARES/AI_CLASS/prolog/family.pl):

```
       [John] (m)   +   [Susan] (f)
                    |
       +------------+------------+
       |                         |
   [Mary] (f)                 [Tom] (m)
       |                         |
   [Alice] (f)                [Bob] (m)
```

- **Grandparents**: `john` and `susan`
- **Children**: `mary` and `tom` (siblings)
- **Grandchildren**: `alice` (child of Mary) and `bob` (child of Tom)
- **Cousins**: `alice` and `bob`

---

## 3. Deep Dive into the Code (`family.pl`)

### A. The Facts (Ground Truths)

Facts represent unconditional assertions stored in the knowledge base. Every fact ends with a period (`.`):

```prolog
% parent(Parent, Child)
parent(john, mary).
parent(john, tom).
parent(susan, mary).
parent(susan, tom).
parent(mary, alice).
parent(tom, bob).

% Gender facts
male(john).
male(tom).
male(bob).

female(susan).
female(mary).
female(alice).
```

> **Syntax Rule: Atoms vs. Variables**
>
> - **Atoms (Constants)**: Must start with a **lowercase** letter (`john`, `mary`, `alice`).
> - **Variables**: Must start with an **Uppercase** letter (`X`, `Y`, `Person`, `Who`).

---

### B. The Rules (Deductive Knowledge)

Rules define conditional truths. The symbol `:-` means **"IF"**, and the comma `,` means **"AND"**.

#### 1. Father Rule

```prolog
father(X, Y) :- parent(X, Y), male(X).
```

- **Read as**: "$X$ is the father of $Y$ **IF** $X$ is a parent of $Y$ **AND** $X$ is male."

#### 2. Mother Rule

```prolog
mother(X, Y) :- parent(X, Y), female(X).
```

- **Read as**: "$X$ is the mother of $Y$ **IF** $X$ is a parent of $Y$ **AND** $X$ is female."

#### 3. Grandparent Rule

```prolog
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
```

- **Read as**: "$X$ is a grandparent of $Z$ **IF** there exists some $Y$ such that $X$ is parent of $Y$ **AND** $Y$ is parent of $Z$."
- *Note:* $Y$ acts as an intermediate link (the child of $X$ and parent of $Z$).

#### 4. Sibling Rule

```prolog
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
```

- **Read as**: "$X$ and $Y$ are siblings **IF** they share a common parent $P$ **AND** $X$ is not identical to $Y$ (`X \= Y`)."
- *Why `X \= Y` matters:* Without this check, everyone would be considered their own sibling, because `parent(P, john)` and `parent(P, john)` would both succeed!

#### 5. Cousin Rule

```prolog
cousin(X, Y) :- parent(P1, X), parent(P2, Y), sibling(P1, P2).
```

- **Read as**: "$X$ and $Y$ are cousins **IF** $P1$ is the parent of $X$, $P2$ is the parent of $Y$, and $P1$ and $P2$ are siblings."

---

## 4. How Prolog Executes Queries (Unification & Backtracking)

When you ask Prolog:

```prolog
?- cousin(alice, bob).
```

Here is the step-by-step trace of how the inference engine resolves it:

1. **Rule Lookup**: Prolog matches `cousin(alice, bob)` with `cousin(X, Y)`.
   - Binds `X = alice`, `Y = bob`.
2. **Sub-Goal 1**: `parent(P1, alice)`
   - Scans facts $\to$ finds `parent(mary, alice)`.
   - Binds `P1 = mary`.
3. **Sub-Goal 2**: `parent(P2, bob)`
   - Scans facts $\to$ finds `parent(tom, bob)`.
   - Binds `P2 = tom`.
4. **Sub-Goal 3**: `sibling(mary, tom)`
   - Evaluates `sibling(mary, tom) :- parent(P, mary), parent(P, tom), mary \= tom.`
   - Evaluates `parent(P, mary)` $\to$ binds `P = john`.
   - Evaluates `parent(john, tom)` $\to$ succeeds!
   - Evaluates `mary \= tom` $\to$ succeeds!
5. **Conclusion**: All sub-goals succeeded, Prolog prints **`true.`**

If any branch fails, Prolog automatically **backtracks** to the last decision point and tries the next matching fact or rule.

---

## 5. Quick Start: Running & Interacting with Prolog

### Step 1: Start SWI-Prolog with the file

In your Mac terminal:

```bash
cd /Users/ba/TEKVORA_SOFTWARES/AI_CLASS
swipl prolog/family.pl
```

### Step 2: Interactive Controls at the `?-` Prompt

| Key / Command           | Action                                                                      |
| :---------------------- | :-------------------------------------------------------------------------- |
| `;` or `Space`      | Ask Prolog for the**next alternative solution**                       |
| `Enter`               | Accept the current solution and stop searching                              |
| `make.`               | Recompile/reload the`.pl` file after editing without restarting `swipl` |
| `halt.`               | Cleanly**exit** Prolog and return to the terminal                     |
| `Ctrl + C` then `a` | Abort a stuck/running query                                                 |

---

## 6. Query Cookbook (Try These in Class)

### A. Verification Queries (Yes / No)

```prolog
% Is John the father of Tom?
?- father(john, tom).
% Output: true.

% Is Susan the father of Mary?
?- father(susan, mary).
% Output: false.

% Are Alice and Bob cousins?
?- cousin(alice, bob).
% Output: true.
```

### B. Finding Single & Multiple Values with Variables

```prolog
% Who is Mary's mother?
?- mother(M, mary).
% Output: M = susan.

% Who are all of John's children?
?- parent(john, Child).
% Output:
% Child = mary ;
% Child = tom.

% Who are all grandchildren of Susan?
?- grandparent(susan, GrandChild).
% Output:
% GrandChild = alice ;
% GrandChild = bob.

% Find all cousins of Alice:
?- cousin(alice, Cousin).
% Output:
% Cousin = bob ;
% Cousin = bob.
% (Note: Appears twice because Mary and Tom share two parents: John and Susan!)
```

### C. Finding All Pairs

```prolog
% Find all pairs of siblings:
?- sibling(A, B).
% Output:
% A = mary, B = tom ;
% A = tom, B = mary.
```

---

## 7. Classroom Gotchas & Best Practices

1. **The Trailing Period (`.`)**:
   Every query and fact **must** end with a period `.`. If you press Enter and nothing happens, type `.` and press Enter again.
2. **Variable Capitalization**:
   `father(john, mary)` checks specific people.
   `father(john, Mary)` treats `Mary` as an unbound variable (`Who`), matching anyone John is father to!
3. **Duplicate Answers**:
   When querying `cousin(alice, bob)`, you might get multiple `true` or answers because there are two independent paths through the shared parents (`john` and `susan`). This is normal in First-Order Logic unless duplicate pruning (`setof/3` or cut `!`) is used.
4. **Clean Exit**:
   Do not force close your terminal. Simply enter `halt.` to exit.

---

## 8. Challenge Exercises to Try in Class

If your instructor asks you to add new rules to [`family.pl`](file:///Users/ba/TEKVORA_SOFTWARES/AI_CLASS/prolog/family.pl), try implementing these:

1. **Aunt and Uncle Rules**:
   ```prolog
   uncle(U, N) :- parent(P, N), sibling(P, U), male(U).
   aunt(A, N)  :- parent(P, N), sibling(P, A), female(A).
   ```
2. **Ancestor (Recursive Logic)**:
   ```prolog
   ancestor(A, D) :- parent(A, D).
   ancestor(A, D) :- parent(A, P), ancestor(P, D).
   ```
   *Query:* `?- ancestor(john, bob).` $\to$ `true.`
