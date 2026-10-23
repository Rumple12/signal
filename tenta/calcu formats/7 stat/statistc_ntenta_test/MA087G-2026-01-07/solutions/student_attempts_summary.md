# Student attempts summary: MA087G-2026-01-07

Only one student attempt was available:

| File | Grade from filename | Notes |
|---|---:|---|
| `5ILRSBDM0000_Grade-D.pdf` | D | Image-only PDF, readable after rendering |

This attempt was used only as evidence of student approaches and common mistakes, not as an answer key.

## Uppgift 1

The student set up the event probabilities and used the independence check `P(A cap B)=P(A)P(B)`. The main method was good: find `P(B)=0.3`, find `P(A)=0.3`, then compare `0.2` with `0.09`.

Useful pattern:

- Build a small probability table from the three given facts.
- For independence, compare product versus intersection.

Common weakness:

- Conditional probability notation was messy, but the final idea `0.1/0.7 = 1/7` was visible.

## Uppgift 2

The student solved using the displayed density `a x^2(2-x)` and found `a=3/4`, which matches the main printed formula. They also computed `P(X>1)`, `E(X)`, and the standard deviation essentially correctly.

Useful pattern:

- Normalize with `int_0^2 f(x) dx = 1`.
- Use `1-F(1)` for `P(X>1)`.
- Use `E(X^2)-E(X)^2` for variance.

Common weakness:

- The CDF explanation was not clean. A CDF must be piecewise: `0` before the support, the integral inside the support, and `1` after the support.

Source caveat:

- The official paper's fallback comment gives a different density, so the guide includes both versions.

## Uppgift 3

The student tried to use survival probabilities but did not correctly use the minimum-of-exponentials shortcut. They also gave an impossible/incorrect expectation for `Z`.

Correct pattern:

- For `Z=min(X,Y)`, use `P(Z>z)=P(X>z,Y>z)`.
- With independent exponentials, add the rates: `0.04+0.05=0.09`.

Common mistake:

- Confusing `P(Z>z)` and `P(Z<=z)`.
- Adding expected values instead of using the new exponential rate.

## Uppgift 4

For part a, the student identified the probabilities partly:

- `P(0)=0.46`
- `P(50)=0.36`
- `P(100)=0.18`

They did not complete the expected value and standard deviation cleanly.

For part b, the student wrote the taxi cost inequality but did not complete the normal linear combination correctly.

Correct pattern:

- Cost is `C=57+14X+9Y`.
- Means combine linearly.
- Variances combine with squared coefficients, assuming independence.

Common mistake:

- Treating the expression `14X+9Y` without calculating its variance.
- Forgetting that standard deviations do not add directly.

## Uppgift 5

The student wrote the likelihood idea but did not finish the derivative and solve for the MLE.

Correct pattern:

- `L(p)=p^{sum x_i}(1-p)^n`.
- `ell(p)=S ln p+n ln(1-p)`.
- Solve `S/p - n/(1-p)=0`.
- Final estimator: `S/(S+n)`.

Common mistake:

- Stopping after writing the likelihood. In an ML question, the points are usually in the log, derivative, and final estimator.

## Uppgift 6

The student solved the confidence interval/test mostly by interval logic and concluded that 1280 is not rejected. The final conclusion was right.

Useful pattern:

- A confidence interval can be reused to test whether a hypothesized mean is plausible.
- If the hypothesized value lies inside the interval, do not reject at the matching significance level.

Common weakness:

- The student used a normal critical value rather than the safer `t` critical value with sample standard deviation.
- The interval was close, but a pass-focused solution should clearly state `n=30`, `s=150`, `df=29`, and the critical value.
