# Mistake bank: MA087G-2026-01-07

## Common mistakes seen or likely on this exam

### Uppgift 1: Independence and conditional probability

- Mistake: Comparing `P(A cap B)` with `P(A)+P(B)`.
- Correct: Independence means `P(A cap B)=P(A)P(B)`.
- Must include: Values for `P(A)`, `P(B)`, and `P(A cap B)`.
- Memorize: `P(B|A^c)=P(B cap A^c)/P(A^c)`.

### Uppgift 2: Continuous density

- Mistake: Forgetting the CDF is piecewise.
- Correct: `F(x)=0` before the interval, integral inside, `F(x)=1` after.
- Must include: Normalization integral, CDF, probability, `E(X)`, `E(X^2)`, variance, standard deviation.
- Memorize: `Var(X)=E(X^2)-[E(X)]^2`.
- Source warning: The exam paper has a mismatch between the displayed density and the fallback comment.

### Uppgift 3: Minimum of exponentials

- Mistake: Treating `min(X,Y)` like `X+Y`.
- Correct: `P(min(X,Y)>z)=P(X>z)P(Y>z)`.
- Must include: The rate of the minimum is the sum of the rates.
- Memorize: If independent, `min(Exp(lambda_1), Exp(lambda_2)) ~ Exp(lambda_1+lambda_2)`.

### Uppgift 4a: Discrete expected value and standard deviation

- Mistake: Finding probabilities but stopping there.
- Correct: After the probability table, compute both `E(X)` and `E(X^2)`.
- Must include: Distribution table, expected value, variance, standard deviation.
- Memorize: Standard deviation is the square root of variance, not the variance itself.

### Uppgift 4b: Linear combination of normals

- Mistake: Adding standard deviations directly.
- Correct: Add variances with squared coefficients:
  `Var(a+bX+cY)=b^2 Var(X)+c^2 Var(Y)` if independent.
- Must include: Cost variable `C=57+14X+9Y`, mean, variance, standardization.
- Memorize: Always standardize with `(value - mean)/standard deviation`.

### Uppgift 5: Maximum likelihood

- Mistake: Writing the likelihood but not maximizing it.
- Correct: Take log, differentiate, set equal to zero, solve for `p`.
- Must include: Likelihood, log-likelihood, derivative, final estimator, numerical estimate.
- Memorize: For `p_X(k)=p^k(1-p)`, the MLE is `sum x_i/(sum x_i+n)`.

### Uppgift 6: Confidence interval and hypothesis test

- Mistake: Using a normal critical value without thinking about unknown sigma.
- Correct: With sample standard deviation `s`, use the `t` distribution with `n-1` degrees of freedom.
- Must include: `H_0`, `H_1`, test statistic, critical value or interval comparison, conclusion in words.
- Memorize: If the hypothesized mean is inside the matching confidence interval, do not reject it.

## What a passing solution must show

- Clear probability translation from text into formulas.
- Correct distribution identification before calculating.
- Correct use of variance formulas.
- For ML: log-likelihood plus derivative.
- For confidence intervals/tests: critical value, standard error, and final interpretation.

## What to memorize for similar questions

- `P(A union B)=P(A)+P(B)-P(A cap B)`.
- Independence: `P(A cap B)=P(A)P(B)`.
- Conditional probability: `P(A|B)=P(A cap B)/P(B)`.
- Continuous density: integrate to 1.
- CDF: integrate density up to `x`.
- Exponential survival: `P(X>t)=e^{-lambda t}`.
- Minimum of independent exponentials: rates add.
- Discrete variance: `E(X^2)-E(X)^2`.
- Linear normal combination: means add, variances add with squared coefficients.
- MLE workflow: likelihood, log, derivative, solve.
- Mean CI with unknown sigma: `bar{x} +/- t s/sqrt(n)`.
