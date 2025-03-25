# Evaluating the Theory: \( (a + b)^2 \mod (a \times b) = a^2 + b^2 \mod (a \times b) \)

## Introduction

This project explores an intriguing mathematical relationship:

\[
(a + b)^2 \equiv a^2 + b^2 \pmod{a \times b}
\]

The goal is to validate whether this equation holds true for all integer values of \( a \) and \( b \) within a specified range. In this code, I tested for the first 100,000 values (1/10 of a million).

## Code Description

The provided Python script systematically tests the theory by iterating through a range of integers and comparing the left-hand side (LHS) and right-hand side (RHS) of the equation modulo \( a \times b \). The main steps of the script are:

1. Iterate over all pairs \( (a, b) \) where \( a \neq b \), within a defined range.
2. Compute:
   - LHS: \( (a + b)^2 \mod (a \times b) \)
   - RHS: \( (a^2 + b^2) \mod (a \times b) \)
3. Compare LHS and RHS:
   - If they are equal, log a match.
   - If they differ, log a mismatch and exit.
4. Verify the total number of iterations against the expected count to ensure the process was exhaustive.

## Observations

- Initial testing suggests the theory holds true for most cases.
- Larger ranges or more complex configurations may be explored for further validation.

## Future Work

- Extend the testing range for a more comprehensive validation.
- Optimize the script for efficiency with larger values.
- Explore potential mathematical proofs or counterexamples.

---

🚀 **Contributions and discussions are welcome!** If you find any edge cases or have ideas for improvement, feel free to open an issue or submit a pull request.
