# Playground
This repo contains some of the code files explaining few relationships or something that I feel interesting in Math and Computer Science
Evaluating the Theory: (a + b)^2 Modulo (a * b) = a^2 + b^2 Modulo (a * b)

Introduction

This project explores an intriguing mathematical relationship:



The goal is to validate whether this equation holds true for all integer values of  and  within a specified range.

Code Description

The provided Python script systematically tests the theory by iterating through a range of integers and comparing the left-hand side (LHS) and right-hand side (RHS) of the equation modulo . The main steps of the script are:

Iterate over all pairs , where , within a defined range.

Calculate:





Compare  and :

If they are equal, log a match.

If they differ, log a mismatch and exit.

Verify the total number of iterations against the expected count to ensure the process was exhaustive.

Code

end = 100000
count = 0
for i in range(1, end):
    for j in range(i, end):
        a = i
        b = j
        c = (a**2) + (b**2)
        d = (a + b) ** 2
        k = a * b
        c = c % k
        d = d % k

        if c == d:
            print("Match: " + str(a) + " " + str(b) + " Modulo: " + str(c))
        else:
            print("Unmatched: " + str(a) + " " + str(b))
            break

        count += 1
end -= 1
sample = (end / 2) * (end + 1)
print("Count: ", count)
if (sample == count):
    print("Trustworthy")
else:
    print("Broken somewhere")

How to Run

Clone the repository:

git clone <repository-url>

Navigate to the project directory:

cd <project-directory>

Execute the script:

python3 theory_test.py

Output

The script outputs:

Matches: Lists pairs  that satisfy the theory and their modulo result.

Mismatches: Identifies any pair that violates the theory (if such pairs exist).

Summary: A final statement confirming whether the relationship holds consistently for the given range.

Observations

Initial testing suggests the theory holds true for most cases.

Larger ranges or more complex configurations may be explored for further validation.

Optimization Ideas

Refactor the code to reduce the computational overhead for large ranges.

Analyze patterns in matches and mismatches to identify potential mathematical proofs.

Extend the analysis to other numerical systems, such as floating-point numbers or prime-only values.

Contributing

Contributions are welcome! To contribute:

Fork this repository.

Make changes or additions.

Submit a pull request for review.

License

This project is licensed under the MIT License. Feel free to use and modify the code as per the terms of the license.

