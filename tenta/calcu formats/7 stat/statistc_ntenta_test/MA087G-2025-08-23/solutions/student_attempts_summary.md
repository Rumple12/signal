# Student attempts summary: MA087G-2025-08-23

Student attempts available:

| File | Grade from filename | Notes |
|---|---:|---|
| `JMXGPJAG0000_Grade-C.pdf` | C | Most complete and generally most reliable, but still has mistakes |
| `9BW8JD9L0000_Grade-D.pdf` | D | Covers several questions, with some algebra/probability mistakes |
| `MCS7UC8W0000_Grade-D.pdf` | D | Useful for seeing common mistakes; solves some later questions |
| `E2EBCMR20000_Grade-E.pdf` | E | Fainter handwriting and more incomplete/incorrect reasoning |

The attempts were used only as inspiration and error evidence, not as an official key.

## Uppgift 1

Useful patterns seen:

- The Grade-C and Grade-D attempts introduced algebraic unknowns for the complement/intersection probabilities.
- The correct final values are `P(A)=7/19` and `P(B)=11/19`.

Common issues:

- The notation became messy quickly.
- Some attempts tried to manipulate conditional probabilities without first naming the shared overlap.

Passing solution must include:

- A definition like `x=P(A^c cap B^c)`.
- Rewriting both conditional probabilities as fractions.
- Using `P(A^c union B^c)=P(A^c)+P(B^c)-P(A^c cap B^c)`.

## Uppgift 2

Useful patterns seen:

- Several students correctly used `int_0^3 a x^2 dx = 1`, giving `a=1/9`.
- The Grade-C attempt gave a clean CDF `F(x)=x^3/27` inside the support.

Common issues:

- Some students forgot or blurred the piecewise CDF outside the interval.
- One attempt made arithmetic mistakes in the expected value/variance.

Passing solution must include:

- `a=1/9`.
- Piecewise CDF with 0, `x^3/27`, and 1.
- `P(X>1)=26/27`.
- `E(X)=9/4` and `D(X)=sqrt(27/80)`.

## Uppgift 3

Useful patterns seen:

- Students recognized the Poisson formula.
- Multiple students treated part c as involving two different variables, consistent with the likely intended reading `Y=X_2-2X_1`.

Common issues:

- One student computed a negative variance, which is impossible.
- Some attempts mixed up interval probabilities and single-point probabilities.
- For `max(X_1,X_2)<=2`, a passing solution must square `P(X<=2)` because both variables must be at most 2.

Passing solution must include:

- Poisson formula `P(X=k)=mu^k e^{-mu}/k!`.
- Independence multiplication for the max part.
- Variance calculation with squared coefficients.

## Uppgift 4

Useful patterns seen:

- The Grade-C attempt wrote the likelihood, log-likelihood, derivative, and final estimator correctly.
- The final estimator is `theta_hat = -n / sum ln(x_i)`.

Common issues:

- Some attempts had unclear log rules.
- It is easy to stop at the likelihood and miss the actual maximization.

Passing solution must include:

- `L(theta)=theta^n prod x_i^(theta-1)`.
- `ln L(theta)=n ln theta + (theta-1) sum ln x_i`.
- Derivative `n/theta + sum ln x_i`.
- Final estimator.

## Uppgift 5

Useful patterns seen:

- Students generally used the `n-1` sample variance formula.
- Some students correctly used chi-square for the interval for `sigma`.

Common issues:

- The Grade-C attempt appears to calculate a confidence interval for the mean instead of for `sigma`.
- This is a major pattern trap: the question asks for spread, not center.

Passing solution must include:

- `xbar=14.2625`.
- `s^2 approx 0.2998`.
- `s approx 0.5476`.
- Chi-square interval for `sigma`, approximately `(0.386, 0.984)`.

## Uppgift 6

Useful patterns seen:

- Students recognized this as a hypothesis test for a mean.
- Some attempts used a critical-value idea.

Common issues:

- Some students used confidence interval language when a one-sided test statistic was cleaner.
- The sample-size/power part caused large mistakes, including plugging in the observed `xbar=83` again or solving for too small `n`.

Passing solution must include:

- `H_0: mu=80`, `H_1: mu>80`.
- Known sigma `10`, so use a `z` test.
- Test statistic `z=3`, reject at 5%.
- Power/sample-size calculation giving `n=155` using `z_0.95 approx 1.645` and `Phi(0.84) approx 0.8`.
