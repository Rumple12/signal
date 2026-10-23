# Pattern tracker: MA087G-2026-01-07

Status: No earlier processed `solutions/` folders were found, so this file seeds the cross-exam pattern memory.

## Pattern: Conditional probability table with independence check

Current question:

- 2026-01, Uppgift 1

Similar previous questions:

- None found yet.

Why this is the pattern:

- The problem gives partial probabilities about events and complements.
- You must reconstruct `P(A)`, `P(B)`, and `P(A cap B)`.
- Independence is checked by comparing `P(A cap B)` with `P(A)P(B)`.

Reusable solving recipe:

1. Translate every sentence into a probability.
2. Use complement and union formulas to find missing pieces.
3. Check independence with `P(A cap B)=P(A)P(B)`.
4. Use `P(B|A^c)=P(B cap A^c)/P(A^c)` for the conditional probability.

Exam shortcut:

Draw a 2-by-2 event table if the wording feels messy.

## Pattern: Continuous density normalization plus CDF and moments

Current question:

- 2026-01, Uppgift 2

Similar previous questions:

- None found yet.

Why this is the pattern:

- A function with unknown constant is given on a finite interval.
- You normalize it to make a density.
- You compute a CDF, a tail probability, expected value, and standard deviation.

Reusable solving recipe:

1. Set `int f(x) dx = 1` over the support.
2. Solve for the constant.
3. Build `F(x)` piecewise.
4. Use `1-F(c)` for right-tail probabilities.
5. Compute `E(X)` and `E(X^2)`.
6. Use `Var(X)=E(X^2)-[E(X)]^2`.

Exam shortcut:

Always include the CDF pieces outside the support: 0 before and 1 after.

## Pattern: Minimum of independent exponential variables

Current question:

- 2026-01, Uppgift 3

Similar previous questions:

- None found yet.

Why this is the pattern:

- Two independent exponential variables are given.
- The new variable is the minimum.
- The survival function makes the solution one line.

Reusable solving recipe:

1. Write `P(Z>z)=P(X>z,Y>z)`.
2. Use independence to multiply survival functions.
3. Combine exponentials.
4. Identify the new exponential rate.
5. Use `E(Z)=1/lambda`.

Exam shortcut:

For a minimum of independent exponentials, add the rates.

## Pattern: Discrete distribution from word proportions

Current question:

- 2026-01, Uppgift 4a

Similar previous questions:

- None found yet.

Why this is the pattern:

- The outcomes are a few fixed numerical values.
- The probabilities are described in words and ratios.
- The task asks for expectation and standard deviation.

Reusable solving recipe:

1. Let the unknown probability be `q`.
2. Use the ratio information to express the others.
3. Make the probabilities sum to 1.
4. Compute `E(X)`, `E(X^2)`, variance, and standard deviation.

Exam shortcut:

When outcomes are money amounts, remember that the standard deviation is also in money units.

## Pattern: Linear combination of normal variables

Current question:

- 2026-01, Uppgift 4b

Similar previous questions:

- None found yet.

Why this is the pattern:

- A real-world quantity is written as a linear formula in normal variables.
- The desired probability is an interval probability.
- You need the resulting mean and variance before standardizing.

Reusable solving recipe:

1. Define the total variable, e.g. `C=57+14X+9Y`.
2. Compute the mean linearly.
3. Compute variance with squared coefficients.
4. Standardize both endpoints.
5. Use the standard normal CDF/table.

Exam shortcut:

Means add directly; variances add with squared coefficients; standard deviations do not add.

## Pattern: Maximum likelihood for geometric distribution

Current question:

- 2026-01, Uppgift 5

Similar previous questions:

- None found yet.

Why this is the pattern:

- A probability function with unknown parameter `p` is given.
- A sample is observed.
- The task asks for the ML estimate.

Reusable solving recipe:

1. Multiply probabilities to form the likelihood.
2. Simplify to powers of `p` and `1-p`.
3. Take logs.
4. Differentiate.
5. Set equal to zero and solve for `p`.
6. Insert the data.

Exam shortcut:

For `p_X(k)=p^k(1-p)`, memorize `p_hat=sum x_i/(sum x_i+n)`.

## Pattern: Confidence interval for mean, sigma unknown

Current question:

- 2026-01, Uppgift 6a

Similar previous questions:

- None found yet.

Why this is the pattern:

- A sample mean, sample standard deviation, and sample size are given.
- The population is treated as normal.
- The population standard deviation is unknown.

Reusable solving recipe:

1. Identify `bar{x}`, `s`, and `n`.
2. Use degrees of freedom `n-1`.
3. Choose the correct `t` value.
4. Use `bar{x} +/- t s/sqrt(n)`.
5. Interpret in words.

Exam shortcut:

Sample standard deviation means `t`, not `z`, unless the course explicitly tells you to approximate.

## Pattern: Two-sided hypothesis test for mean

Current question:

- 2026-01, Uppgift 6b-c

Similar previous questions:

- None found yet.

Why this is the pattern:

- A claimed mean is tested against sample data.
- The question asks whether the claim is reasonable or can be rejected.
- The natural alternative is two-sided.

Reusable solving recipe:

1. State `H_0: mu=mu_0`.
2. State `H_1: mu != mu_0`.
3. Compute `T=(bar{x}-mu_0)/(s/sqrt(n))`.
4. Compare with `+-t` critical values.
5. Conclude in plain language.

Exam shortcut:

If the claimed mean lies inside the matching confidence interval, you do not reject it.
