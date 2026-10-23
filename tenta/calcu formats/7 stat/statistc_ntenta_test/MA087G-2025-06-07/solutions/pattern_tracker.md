# Pattern tracker: MA087G-2025-06-07

Seed source:

- `MA087G-2025-08-23/solutions/pattern_tracker.md`
- `MA087G-2026-01-07/solutions/pattern_tracker.md`

This file updates the cross-exam memory for the June 2025 exam.

## Pattern: Hypergeometric/combinations without replacement

Current question:

- 2025-06, Uppgift 1

Similar previous questions:

- None found yet.

Why this is the pattern:

- The problem draws balls without replacement.
- Order does not matter.
- The solution counts favorable combinations over all combinations.

Reusable solving recipe:

1. Count total outcomes with `binom(total, drawn)`.
2. Count favorable outcomes with combinations.
3. Use complements for "at least one of each" questions.
4. For conditional probability, restrict to the given event.

Exam shortcut:

Without replacement usually means combinations/hypergeometric, not binomial.

## Pattern: Continuous density normalization plus CDF and moments

Current question:

- 2025-06, Uppgift 2

Similar previous questions:

- 2026-01, Uppgift 2
- 2025-08, Uppgift 2

Why they are the same pattern:

- All give a density with an unknown constant.
- All ask for a distribution function.
- All ask for a probability and moments.

Reusable solving recipe:

1. Set the integral of the density over its support equal to 1.
2. Solve for the constant.
3. Build a piecewise CDF.
4. Use the CDF for probability questions.
5. Compute `E(X)` and `E(X^2)`.
6. Use `V(X)=E(X^2)-[E(X)]^2`.

Exam shortcut:

The CDF must include 0 before the support and 1 after the support.

## Pattern: Exponential probabilities

Current question:

- 2025-06, Uppgift 3a

Similar previous questions:

- 2026-01, Uppgift 3, related exponential survival pattern

Why this is the pattern:

- The notation `Exp(lambda)` appears.
- The solution uses `P(X>t)=e^{-lambda t}` and `F(t)=1-e^{-lambda t}`.

Reusable solving recipe:

1. Identify the rate `lambda`.
2. Use survival for right tails.
3. For intervals, subtract two CDF/survival values.

Exam shortcut:

For `P(a<=X<b)`, use `P(X>=a)-P(X>=b)` for exponential variables.

## Pattern: Linear combination expectation and variance

Current question:

- 2025-06, Uppgift 3b

Similar previous questions:

- 2025-08, Uppgift 3c
- 2026-01, Uppgift 4b

Why they are related:

- All ask for expectation and/or variance of a linear expression.
- Coefficients are squared in variance calculations.

Reusable solving recipe:

1. Use linearity of expectation.
2. Use known variances of the variables.
3. If independent, add variances with squared coefficients.

Exam shortcut:

For variance, `3X` becomes `3^2 V(X)`.

## Pattern: Distribution function of transformed variable

Current question:

- 2025-06, Uppgift 3c

Similar previous questions:

- None found yet.

Why this is the pattern:

- A new variable is defined as a transformation, `4X+1`.
- The task asks for its distribution function.

Reusable solving recipe:

1. Name the new variable, e.g. `W=4X+1`.
2. Start with `F_W(w)=P(W<=w)`.
3. Substitute and solve the inequality for `X`.
4. Insert into the CDF of `X`.
5. Remember the new support.

Exam shortcut:

Always solve the inequality before inserting into the old CDF.

## Pattern: Maximum of independent variables

Current question:

- 2025-06, Uppgift 3d

Similar previous questions:

- 2025-08, Uppgift 3b

Why they are the same pattern:

- Both ask for `P(max(...)<=c)`.
- Both require all variables to be below the boundary.
- Independence lets us multiply probabilities.

Reusable solving recipe:

1. Rewrite `max(X,Y)<=c` as `X<=c and Y<=c`.
2. Use independence to multiply.
3. Insert each variable's CDF at `c`.

Exam shortcut:

`max <= c` means every variable is `<= c`.

## Pattern: Maximum likelihood estimation

Current question:

- 2025-06, Uppgift 4

Similar previous questions:

- 2026-01, Uppgift 5
- 2025-08, Uppgift 4

Why they are the same pattern:

- All ask for an ML estimate.
- All use likelihood, log-likelihood, derivative, and solving.

Reusable solving recipe:

1. Write the likelihood as a product.
2. Take logs.
3. Differentiate with respect to the unknown parameter.
4. Set derivative equal to zero.
5. Solve for the parameter.

Exam shortcut:

Do not stop at the likelihood. The estimator comes after differentiation.

## Pattern: Confidence interval for mean, sigma known

Current question:

- 2025-06, Uppgift 5a

Similar previous questions:

- 2025-08, Uppgift 6 uses known sigma in a test rather than interval

Why this is the pattern:

- The question asks for a CI for `mu`.
- The population standard deviation is given.
- The method uses a z critical value.

Reusable solving recipe:

1. Compute `xbar`.
2. Use `z_{alpha/2}`.
3. Use `xbar +/- z sigma/sqrt(n)`.

Exam shortcut:

Known sigma means z-method.

## Pattern: Confidence interval for mean, sigma unknown

Current question:

- 2025-06, Uppgift 5b

Similar previous questions:

- 2026-01, Uppgift 6a

Why they are the same pattern:

- Both ask for an interval for a mean.
- Population sigma is unknown.
- The method uses sample standard deviation and a t critical value.

Reusable solving recipe:

1. Compute `xbar`.
2. Compute sample standard deviation `s`.
3. Use degrees of freedom `n-1`.
4. Use `xbar +/- t s/sqrt(n)`.

Exam shortcut:

Unknown sigma means t-method.

## Pattern: One-sided z-test for mean, sigma known

Current question:

- 2025-06, Uppgift 6

Similar previous questions:

- 2025-08, Uppgift 6

Why they are the same pattern:

- Both test a mean with known sigma.
- Both use a z statistic.
- 2025-06 is left-tailed, while 2025-08 is right-tailed.

Reusable solving recipe:

1. State `H_0` and `H_1`.
2. Compute `z=(xbar-mu_0)/(sigma/sqrt(n))`.
3. Choose the correct one-sided critical value.
4. Compare and conclude in words.

Exam shortcut:

Do not reject just because the sample mean is on the expected side. It must pass the critical value.
