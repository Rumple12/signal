# Mistake bank: MA087G-2025-08-23

## Uppgift 1: Conditional probability with complements

Common mistakes:

- Treating conditional probability as multiplication.
- Forgetting that `A^c` means "not A".
- Losing track of the overlap `P(A^c cap B^c)`.

What causes lost points:

- Not using the conditional probability formula.
- Not using the union formula for `A^c union B^c`.
- Giving decimal guesses without showing the algebra.

What to memorize:

- `P(A|B)=P(A cap B)/P(B)`.
- `P(A union B)=P(A)+P(B)-P(A cap B)`.
- Complements: `P(A)=1-P(A^c)`.

## Uppgift 2: Density, CDF, expected value, standard deviation

Common mistakes:

- Forgetting the density must integrate to 1.
- Writing only the middle part of the CDF and forgetting the 0 and 1 parts.
- Using `E(X^2)` as the variance directly.

What causes lost points:

- Missing `a=1/9`.
- Missing the piecewise CDF.
- Not showing `V(X)=E(X^2)-[E(X)]^2`.

What to memorize:

- Density: total area equals 1.
- CDF: integrate density up to `x`.
- Right-tail probability: `P(X>c)=1-F(c)`.
- Standard deviation is the square root of variance.

## Uppgift 3: Poisson and max of independent variables

Common mistakes:

- Forgetting the factorial in the Poisson formula.
- Treating `max(X_1,X_2)<=2` as only one variable being at most 2.
- Getting a negative variance in part c.

What causes lost points:

- Not using independence in part b.
- Not squaring the coefficient in the variance formula.
- Misreading the interval `1 <= X < 4`.

What to memorize:

- For Poisson: `P(X=k)=mu^k e^{-mu}/k!`.
- For Poisson: `E(X)=mu`, `V(X)=mu`.
- `max(X_1,X_2)<=c` means both variables are `<=c`.
- Variance coefficients are squared.

## Uppgift 4: Maximum likelihood

Common mistakes:

- Stopping after writing the likelihood.
- Losing the `(theta-1)` when taking logs.
- Forgetting that `ln(x_i)` is negative for `0<x_i<1`.

What causes lost points:

- No log-likelihood.
- No derivative.
- No final solved estimator.

What to memorize:

- ML workflow: likelihood, log, derivative, set to zero, solve.
- For this density, `theta_hat = -n / sum ln(x_i)`.

## Uppgift 5: Confidence interval for sigma

Common mistakes:

- Calculating a confidence interval for the mean instead of `sigma`.
- Using a `t` interval or normal interval for `sigma`.
- Forgetting to take square roots at the end.

What causes lost points:

- Not calculating `s^2`.
- Not using chi-square critical values.
- Reporting an interval for `sigma^2` when the question asks for `sigma`.

What to memorize:

- Intervals for normal variance/standard deviation use chi-square.
- First get the interval for `sigma^2`, then square-root endpoints for `sigma`.

## Uppgift 6: One-sided z-test and power

Common mistakes:

- Using a two-sided test even though the question says "has increased".
- Using a `t` test even though `sigma=10` is known.
- In the power part, plugging in the old observed sample mean again.
- Rounding sample size down.

What causes lost points:

- Missing hypotheses.
- Missing test statistic.
- Missing the rejection rule.
- Not solving the power inequality carefully.

What to memorize:

- Known sigma means `z = (xbar - mu_0)/(sigma/sqrt(n))`.
- "Increased" means right-tailed test.
- For 5% right-tailed test, use `z_0.95 approx 1.645`.
- For sample size, always round up.
