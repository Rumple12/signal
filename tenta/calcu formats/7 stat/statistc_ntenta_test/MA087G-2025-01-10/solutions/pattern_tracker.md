# Pattern Tracker for 2025-01

Official exam PDF:

- `2025-01 tenta.pdf`
- Status: image-only PDF, but the rendered pages were readable.

Compared against already processed exams:

- 2026-01
- 2025-08
- 2025-06
- 2024-08
- 2024-05

This file tracks patterns only. It is not a full solution guide.

## Uppgift 1

Pattern:

- Three-set inclusion-exclusion.
- Venn diagram counting.
- "At least one", "none", and "exactly one" probabilities.

What the question is really testing:

You have three activity areas `A`, `B`, and `C`. Some students belong to one area, some to two, and some to all three. The question checks whether you can count overlaps without double-counting people.

Same or similar questions:

- 2024-08, Uppgift 1: same three-event family, but with probabilities and independence instead of student counts.
- 2024-05, Uppgift 1a-c: related event-overlap and conditional-probability thinking, but with two main categories.
- 2026-01, Uppgift 1 and 2025-08, Uppgift 1: related event-table/conditional-probability patterns.

Reusable method:

1. For "at least one", use inclusion-exclusion.
2. Add the three single groups.
3. Subtract the three pairwise overlaps.
4. Add back the triple overlap once.
5. For "none", use the complement: total minus at least one.
6. For "exactly one", count only-A, only-B, and only-C, then add them.

Exam trick:

If there are three sets, the key memory line is: add singles, subtract pair overlaps, add the triple overlap back.

## Uppgift 2

Pattern:

- Normal distribution direct probability.
- Repeated independent items using powers and complements.
- One-sided z-test for a mean with known `sigma`.

What the question is really testing:

The screw length is normally distributed. First you find the chance that one screw is usable. Then that one-screw probability is reused for boxes or repeated production. Finally, the question switches to a hypothesis test about whether the machine mean has increased.

Same or similar questions:

- 2024-05, Uppgift 4a: same direct normal probability pattern.
- 2024-08, Uppgift 4a: same normal-standardization idea.
- 2025-08, Uppgift 6; 2025-06, Uppgift 6; 2024-05, Uppgift 4c-d: same known-sigma mean-test family.
- 2025-01, Uppgift 2b-c is related to 2024-05, Uppgift 1d and 2024-08, Uppgift 3c-d because all use repeated independent trials.

Reusable method:

1. For one screw, standardize the cutoff with `z=(x-mu)/sigma`.
2. Use the normal table/calculator to get the one-screw probability.
3. For "all 10 usable", raise the one-screw probability to the power 10.
4. For "at least one usable", use the complement if that is easier.
5. For the test, use `z=(bar{x}-mu_0)/(sigma/sqrt(n))`.
6. Because the suspicion is "greater than 1.8", use a right-tailed test.

Exam trick:

One observation uses `sigma`. A sample mean uses `sigma/sqrt(n)`. That switch is the whole point in part d.

## Uppgift 3

Pattern:

- Continuous density normalization.
- CDF/probability from a density.
- Transformation of a random variable.

What the question is really testing:

You are given a density with an unknown constant. After making it a valid density, you find the distribution function and a probability. The last part asks for the density of a transformed variable `Y=ln X`.

Same or similar questions:

- 2026-01, Uppgift 2; 2025-08, Uppgift 2; 2025-06, Uppgift 2; 2024-08, Uppgift 3; 2024-05, Uppgift 2a-c: same density/CDF/probability family.
- 2025-06, Uppgift 3c: same transformed-variable CDF idea.
- 2024-08, Uppgift 4c and 2025-01, Uppgift 4c: related transformation/linear-combination thinking, but not the same density transformation.

Reusable method:

1. Set the integral of the density equal to 1 to find the constant.
2. Build the CDF by integrating the density from the start of the support up to `x`.
3. For probability, use the CDF or integrate over the wanted interval.
4. For `Y=ln X`, start from `F_Y(y)=P(Y<=y)`.
5. Rewrite as `P(ln X <= y)`.
6. Solve back to `X <= e^y`, then use the old CDF.
7. Differentiate the new CDF if the question asks for a density.

Exam trick:

For transformed variables, start with the CDF. It keeps the inequality direction and support much safer.

## Uppgift 4

Pattern:

- Uniform distribution probability.
- Linear transformation expectation and variance.
- Distribution function of a linear transformation.
- Maximum of independent variables.

What the question is really testing:

`X` is uniform on `(-1,1)`, so probabilities are just interval lengths. Then the question checks whether you can handle the new variable `2X-1` and the maximum of two independent variables.

Same or similar questions:

- 2024-08, Uppgift 4c; 2024-05, Uppgift 2e; 2025-08, Uppgift 3c; 2025-06, Uppgift 3b; 2026-01, Uppgift 4b: same linear-combination expectation/variance pattern.
- 2024-08, Uppgift 4b; 2024-05, Uppgift 2d; 2025-08, Uppgift 3b; 2025-06, Uppgift 3d: same `max <= c` pattern.
- 2025-06, Uppgift 3c and 2025-01, Uppgift 3d: related transformed-variable distribution pattern.

Reusable method:

1. For a uniform variable, probability is interval length divided by total length.
2. For `E(2X-1)`, use linearity: `2E(X)-1`.
3. For `V(2X-1)`, square the coefficient: `2^2V(X)`.
4. For the CDF of `2X-1`, start with `P(2X-1 <= y)` and solve for `X`.
5. For `P(max(X,Y)<=0)`, rewrite as `P(X<=0 and Y<=0)`.
6. Use independence to multiply the two probabilities.

Exam trick:

`max <= c` means every variable must be below `c`. It is an "all of them" event.

## Uppgift 5

Pattern:

- Maximum likelihood estimation over a finite parameter set.

What the question is really testing:

The parameter `theta` can only be `2`, `3`, or `4`. Instead of doing a long derivative method, you can compute the likelihood for each allowed value and choose the largest.

Same or similar questions:

- 2026-01, Uppgift 5; 2025-08, Uppgift 4; 2025-06, Uppgift 4; 2024-08, Uppgift 5; 2024-05, Uppgift 5: same broad ML-estimation pattern.
- This 2025-01 version is a special shortcut version because the parameter has only three possible values.

Reusable method:

1. Write the likelihood as the product of the two density values.
2. Insert the observations `0.2` and `0.8`.
3. Evaluate the likelihood for `theta=2`, `theta=3`, and `theta=4`.
4. Pick the `theta` that gives the largest likelihood.

Exam trick:

If the parameter is only allowed to be a few values, do not overcomplicate ML. Just test the allowed values.

## Uppgift 6

Pattern:

- Chi-square homogeneity test for count data in a two-way table.

What the question is really testing:

There are two exam groups and three grade categories. The question asks whether the grade distribution looks the same in both groups.

Same or similar questions:

- 2024-05, Uppgift 6: related chi-square count-data test, but there it is a goodness-of-fit test for a random number generator.
- No exact later/earlier match found among the processed exams for a two-row grade-distribution homogeneity test.

Reusable method:

1. State the null hypothesis: both groups have the same grade distribution.
2. Compute row totals, column totals, and the grand total.
3. For each cell, compute expected count as `row total * column total / grand total`.
4. Compute `sum (observed - expected)^2 / expected`.
5. Use degrees of freedom `(rows-1)(columns-1)`.
6. Compare to the chi-square critical value at 5%.

Exam trick:

For table-count tests, the expected count in a cell is always row total times column total divided by grand total.

