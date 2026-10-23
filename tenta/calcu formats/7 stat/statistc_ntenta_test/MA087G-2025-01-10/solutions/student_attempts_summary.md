# Student attempts summary: MA087G-2025-01-10

Student attempts available:

| File | Grade from filename | Notes |
|---|---:|---|
| `ONJDQRMV0000_Grade-C.pdf` | C | Mostly complete; useful for structure on Q1, Q2, Q6 |
| `8BZ4HS680000_Grade-D.pdf` | D | Shows several common beginner mistakes but also useful setups |

The attempts were used as evidence of approaches and mistakes, not as an official answer key.

## Uppgift 1

Useful pattern:

- The Grade-C attempt used inclusion-exclusion and a Venn-style setup.
- Correct method is to count at least one, none, and exactly one separately.

Common issues:

- Pair-overlaps and triple-overlap are easy to double-count.
- Exactly one is not the same as at least one.

Correct key results:

- At least one: `7/15`.
- None: `8/15`.
- Exactly one: `1/12`.

## Uppgift 2

Useful pattern:

- Attempts recognized normal standardization.
- The hypothesis test is a right-tailed known-sigma z-test.

Common issues:

- Part c is easiest with complement: at least one usable is `1 - none usable`.
- One attempt treated the test conclusion too loosely; `z=1.58` is not enough to reject at 5%.

Correct key results:

- `P(X<2)=Phi(0.5)≈0.6915`.
- All 10 usable: about `0.0250`.
- Minimum `n=4`.
- Do not reject in the one-sided 5% test.

## Uppgift 3

Useful pattern:

- Students generally recognized density normalization.
- The transformation `Y=ln X` is best handled through the CDF.

Common issues:

- Forgetting that `X` is only between 0 and 1.
- Missing that `Y=ln X` is always negative.

Correct key results:

- `a=4`.
- `F_X(x)=x^4` for `0<x<1`.
- `P(|X|<1/2)=1/16`.
- `f_Y(y)=4e^(4y)` for `y<0`.

## Uppgift 4

Useful pattern:

- The Grade-D attempt correctly used interval length for uniform probability.
- The max part requires both variables to be at most 0.

Common issues:

- Variance of `2X-1` must be `4V(X)`, not `2V(X)`.
- For the transformed CDF, solve `2X-1<=w` before using the old CDF.

Correct key results:

- `P(-0.1<X<0.2)=0.15`.
- `E(2X-1)=-1`.
- `V(2X-1)=4/3`.
- `P(max(X,Y)<=0)=1/4`.

## Uppgift 5

Useful pattern:

- Because `theta` is only allowed to be `2,3,4`, evaluate the likelihood at those values.

Common issues:

- One attempt differentiated as if theta could be any value, then got a value outside/near the allowed set.
- The final answer must be one of `2,3,4`.

Correct key result:

- `theta_hat_ML=3`.

## Uppgift 6

Useful pattern:

- The Grade-C attempt used the chi-square homogeneity test structure.
- Expected counts are row total times column total divided by grand total.

Common issues:

- Degrees of freedom must be `(2-1)(3-1)=2`.
- Do not reject because the observed table looks different by eye; compare the statistic to the critical value.

Correct key result:

- `chi^2≈1.307`, do not reject at 5%.
