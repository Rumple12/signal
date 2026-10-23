# Pattern tracker: MA087G-2025-08-23

Seed source:

- `MA087G-2026-01-07/solutions/pattern_tracker.md`

This file updates the cross-exam memory using the current exam.

## Pattern: Conditional probability table with complements

Current question:

- 2025-08, Uppgift 1

Similar previous questions:

- 2026-01, Uppgift 1

Why they are the same pattern:

- Both questions use events and complements.
- Both require translating probability statements into algebra.
- Both need conditional probability formulas.

Reusable solving recipe:

1. Name the shared overlap, for example `x=P(A^c cap B^c)`.
2. Rewrite conditional probabilities as fractions.
3. Use the union formula if an "or" probability is given.
4. Solve for complement probabilities.
5. Convert back using `P(A)=1-P(A^c)`.

Exam shortcut:

If the question is full of `A^c`, `B^c`, `|`, and `union`, slow down and build the algebra from the overlap.

## Pattern: Continuous density normalization plus CDF and moments

Current question:

- 2025-08, Uppgift 2

Similar previous questions:

- 2026-01, Uppgift 2

Why they are the same pattern:

- Both give a density with an unknown constant.
- Both ask for the CDF.
- Both ask for a probability, expected value, and standard deviation.

Reusable solving recipe:

1. Set the integral of the density over its support equal to 1.
2. Solve for the constant.
3. Build a piecewise CDF.
4. Use `1-F(c)` for right-tail probabilities.
5. Compute `E(X)` and `E(X^2)`.
6. Use `V(X)=E(X^2)-[E(X)]^2`.

Exam shortcut:

For a CDF, always write 0 before the support and 1 after the support.

## Pattern: Poisson probabilities

Current question:

- 2025-08, Uppgift 3a

Similar previous questions:

- None found yet.

Why this is the pattern:

- The notation `Po(mu)` appears.
- The question asks for exact and interval probabilities.
- The formula uses `mu^k e^{-mu}/k!`.

Reusable solving recipe:

1. Identify `mu`.
2. For exact probability, insert `k` into the Poisson formula.
3. For interval probability, list the integer values included.
4. Add the individual probabilities.

Exam shortcut:

For a count variable, `1 <= X < 4` means `X=1,2,3`.

## Pattern: Maximum of independent identical variables

Current question:

- 2025-08, Uppgift 3b

Similar previous questions:

- None found yet.

Why this is the pattern:

- The question asks about `max(X_1,X_2)`.
- The variables are independent.
- `max <= c` means both variables must be `<= c`.

Reusable solving recipe:

1. Rewrite `max(X_1,X_2)<=c` as `X_1<=c and X_2<=c`.
2. Use independence to multiply.
3. If identically distributed, square the one-variable probability.

Exam shortcut:

`max <= c` means all values are below the boundary.

## Pattern: Linear combination expectation and variance

Current question:

- 2025-08, Uppgift 3c

Similar previous questions:

- 2026-01, Uppgift 4b

Why they are related:

- Both use linear combinations of random variables.
- Both require separate handling of expectation and variance.
- Coefficients must be squared in variance calculations.

Reusable solving recipe:

1. Use `E(aX+bY)=aE(X)+bE(Y)`.
2. If independent, use `V(aX+bY)=a^2V(X)+b^2V(Y)`.
3. Never let variance become negative.

Exam shortcut:

For variance, square the coefficient, including any minus sign.

## Pattern: Maximum likelihood estimation

Current question:

- 2025-08, Uppgift 4

Similar previous questions:

- 2026-01, Uppgift 5

Why they are the same pattern:

- Both ask for an ML estimate.
- Both require likelihood, log-likelihood, derivative, and solving.
- Only the distribution changes.

Reusable solving recipe:

1. Write the likelihood as a product.
2. Take the logarithm.
3. Use log rules to simplify.
4. Differentiate.
5. Set derivative equal to zero.
6. Solve for the parameter.

Exam shortcut:

If the question says `ML-skattning`, the checklist is always likelihood, log, derivative, solve.

## Pattern: Point estimate and chi-square confidence interval for normal sigma

Current question:

- 2025-08, Uppgift 5

Similar previous questions:

- None found yet.

Why this is the pattern:

- The sample is assumed normal.
- The question asks for `sigma^2` and `sigma`.
- The interval is for spread, not for the mean.

Reusable solving recipe:

1. Compute `xbar`.
2. Compute `s^2=(sum x_i^2-n xbar^2)/(n-1)`.
3. Use chi-square critical values with `n-1` degrees of freedom.
4. Build interval for `sigma^2`.
5. Square-root endpoints to get interval for `sigma`.

Exam shortcut:

Mean intervals use `z` or `t`; sigma intervals use chi-square.

## Pattern: One-sided z-test for mean, sigma known

Current question:

- 2025-08, Uppgift 6a-b

Similar previous questions:

- 2026-01, Uppgift 6b-c, as a related mean-test pattern

Why they are related:

- Both test a claim about a mean.
- 2025-08 uses known sigma and a one-sided alternative.
- 2026-01 uses sample standard deviation and a two-sided alternative.

Reusable solving recipe:

1. State `H_0` and `H_1`.
2. Use `z=(xbar-mu_0)/(sigma/sqrt(n))` when sigma is known.
3. Use right-tail critical value for "increased".
4. Reject if the test statistic is larger than the critical value.

Exam shortcut:

Known sigma means z-test. Unknown sigma means t-test.

## Pattern: Power/sample size for one-sided mean test

Current question:

- 2025-08, Uppgift 6c

Similar previous questions:

- None found yet.

Why this is the pattern:

- The question asks how large `n` must be.
- It gives a desired detection probability.
- It asks about rejecting `H_0` under a specific true mean.

Reusable solving recipe:

1. Write the rejection boundary from the hypothesis test.
2. Assume the new true mean.
3. Standardize the rejection probability under that true mean.
4. Use the given normal-table clue.
5. Solve the inequality for `n`.
6. Round up.

Exam shortcut:

Power questions are about the probability of rejecting under the alternative, not about the observed sample mean from part b.
