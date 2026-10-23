# Student attempts summary: MA087G-2025-06-07

Student attempts available:

| File | Grade from filename | Notes |
|---|---:|---|
| `VZUYRS3Q0000_Grade-C.pdf` | C | Most complete and useful; still contains mistakes |
| `BTJ0EYZQ0000_Grade-C.pdf` | C | Partial and contains several incorrect starts |
| `0LNL2U910000_Grade-D.pdf` | D | Useful for common mistakes and later question structure |

The attempts were used as evidence of approaches and mistakes, not as an official answer key.

## Uppgift 1

Useful pattern:

- The best attempts treated drawing without replacement as a combinations problem.
- Correct method is hypergeometric/combinations, not ordinary binomial.

Common mistakes:

- Some students used changing probabilities by hand and made arithmetic slips.
- Some treated `A union B` as if there were overlap, but `A` and `B` are disjoint.
- Several struggled with `P(A|B^c)`.

Correct key results:

- `P(A)=21/1292`.
- `P(B)=625/646`.
- `P(A union B)=1271/1292`.
- `P(A|B^c)=1/2`.

## Uppgift 2

Useful pattern:

- Students generally recognized the density normalization step.
- The CDF is `sqrt(x)/2` on `0<x<=4`.

Common mistakes:

- Confusing `P(X<=1)` with expected value.
- Missing the piecewise CDF outside the support.
- Arithmetic mistakes in `E(X)` and variance.

Correct key results:

- `a=1/4`.
- `P(X<=1)=1/2`.
- `E(X)=4/3`.
- `D(X)=sqrt(64/45)`.

## Uppgift 3

Useful pattern:

- Students recognized exponential survival and CDF formulas.
- Several used independence correctly for `P(max{X,Y}<=1)`.

Common mistakes:

- Some attempts used values from formula sheets without clearly identifying rate vs mean.
- Some variance calculations for `3X+Y` missed the squared coefficient.
- Part c was often messy because transforming a random variable into a CDF is easy to confuse.

Correct key results:

- `P(1<=X<3)=e^{-2}-e^{-6}`.
- `E(3X+Y)=11/6`.
- `V(3X+Y)=85/36`.
- `F_{4X+1}(w)=0` for `w<1`, and `1-e^{-(w-1)/2}` for `w>=1`.
- `P(max{X,Y}<=1)=(1-e^{-2})(1-e^{-3})`.

## Uppgift 4

Useful pattern:

- The stronger attempts wrote the likelihood and log-likelihood.
- Correct ML estimate is based on differentiating with respect to `a`.

Common mistakes:

- Forgetting that `a` appears inside the exponential denominator.
- Losing signs when differentiating `-sum x_i^2/(2a)`.
- Not finishing the solve step.

Correct key result:

- `a_hat_ML = (1/(2n)) sum x_i^2`.

## Uppgift 5

Useful pattern:

- Students recognized part a uses known sigma and part b uses unknown sigma.
- Good attempts used `z=1.96` for part a and `t_{0.975,7}=2.365` for part b.

Common mistakes:

- Mixing up known-sigma and unknown-sigma formulas.
- Incorrect sample variance arithmetic.

Correct key results:

- `xbar=14.2625`.
- Known sigma interval: `(13.916, 14.609)`.
- Unknown sigma interval: `(13.805, 14.720)`.

## Uppgift 6

Useful pattern:

- Students recognized the hypotheses should be about `mu<70`.
- Known sigma means a z-test.

Common mistakes:

- Rejecting just because `xbar<70`, without checking the critical value.
- Confusing left-tailed and right-tailed rejection.
- Part b is especially easy to answer incorrectly because `69<70`, but it is not low enough to reject.

Correct key results:

- Hypotheses: `H_0: mu=70`, `H_1: mu<70`.
- Part a: `z=-2`, reject.
- Part b: `z≈-1.414`, do not reject.
