# Pattern Tracker for 2024-05

Official exam PDF:

- `2024-05 tenta.pdf`
- Status: image-only PDF, but the rendered pages were readable.

Compared against already processed exams:

- 2026-01
- 2025-08
- 2025-06
- 2025-01

This file tracks patterns only. It is not a full solution guide.

## Uppgift 1

Pattern:

- Two-event probability table, conditional probability, union, and independence.
- Exact binomial count probability for repeated yes/no trials.

What the question is really testing:

It first checks whether you can organize probabilities about two categories at once: candidate choice and vegetarian status. Then it turns the "not vegetarian" probability into a repeated-trials counting question.

Same or similar questions:

- 2026-01, Uppgift 1: same two-event probability table and independence-check idea.
- 2025-08, Uppgift 1: same conditional-probability/complement idea, but with messier notation.
- 2025-01, Uppgift 2b-c: related repeated-independent-trials idea, but it uses complements instead of a full binomial count.

Reusable method:

1. Draw a 2-by-2 table with the two categories.
2. Put the given overlaps and totals into the table.
3. Use `P(A|B)=P(A cap B)/P(B)` for conditional probability.
4. Use `P(A cup B)=P(A)+P(B)-P(A cap B)` for "or".
5. Check independence with `P(A cap B)=P(A)P(B)`.
6. For the repeated 10-person question, use the binomial formula with `n=10`.

Exam trick:

When the question switches from one person to ten people, the pattern changes from table probability to binomial probability.

## Uppgift 2

Pattern:

- Continuous density verification, probability, expectation, and variance.
- Maximum of independent variables.
- Variance of a sum of independent variables.

What the question is really testing:

It checks whether you understand that a density is about area, not single-point probability. Then it adds two common mini-patterns: a maximum probability and a variance-sum rule.

Same or similar questions:

- 2026-01, Uppgift 2: same density/probability/moments pattern.
- 2025-08, Uppgift 2: same density/CDF/moments pattern.
- 2025-06, Uppgift 2: same density/CDF/moments pattern.
- 2025-01, Uppgift 3a-c: same density and probability pattern.
- 2025-08, Uppgift 3b; 2025-06, Uppgift 3d; 2025-01, Uppgift 4d: same `max <= c` pattern.
- 2025-08, Uppgift 3c; 2025-06, Uppgift 3b; 2026-01, Uppgift 4b: same expectation/variance combination idea.

Reusable method:

1. For a density, check two things: it is never negative, and the total area is 1.
2. For `P(X <= 0.5)`, integrate the density up to `0.5`.
3. For `E(X)`, integrate `x f(x)`.
4. For `V(X)`, use `E(X^2)-[E(X)]^2`.
5. For `P(max(X,Y) <= 0)`, rewrite it as `P(X <= 0 and Y <= 0)` and multiply because of independence.
6. For `V(X+Y)`, add `V(X)+V(Y)` because the variables are independent.

Exam trick:

`max <= c` means every variable must be `<= c`. That one sentence saves a lot of confusion.

## Uppgift 3

Pattern:

- Discrete distribution from counting dice outcomes.
- Expected value.
- Expected profit/loss in a game.

What the question is really testing:

You must build the probability distribution yourself. The dice outcomes are equally likely, but the values of `X=|i-j|` are not equally likely.

Same or similar questions:

- 2026-01, Uppgift 4a: related discrete distribution with expectation and variance.
- No exact earlier match found among the already processed exams. This is a stronger dice-counting/game-profit version.

Reusable method:

1. Remember that two dice throws give 36 ordered outcomes.
2. Count how many outcomes give each value of `|i-j|`.
3. Divide each count by 36 to get the probability function.
4. Use `E(X)=sum xP(X=x)` for the expected value.
5. For the game, compute expected winnings: each possible win/loss times its probability.
6. If expected winnings are positive, the game is profitable in the long run. If negative, it is not.

Exam trick:

For two dice, `(2,6)` and `(6,2)` count separately. Do not accidentally count unordered pairs.

## Uppgift 4

Pattern:

- Normal distribution direct probability.
- Confidence interval for mean with known `sigma`.
- Hypothesis test for mean with known `sigma`, both two-sided and one-sided.

What the question is really testing:

The whole question is about a normally distributed measurement with known spread. First you calculate a probability for one measurement. Then you use the sample mean to estimate or test the true mean.

Same or similar questions:

- 2025-01, Uppgift 2a-c: same direct normal probability idea.
- 2025-06, Uppgift 5a: same confidence interval for mean with known `sigma`.
- 2025-08, Uppgift 6; 2025-06, Uppgift 6; 2025-01, Uppgift 2d: same one-sided known-sigma mean-test pattern.
- 2026-01, Uppgift 6b-c: related mean-test pattern, but there `sigma` is unknown and the t-method is used.

Reusable method:

1. For one measurement, standardize with `z=(x-mu)/sigma`.
2. For a sample mean, use the smaller spread `sigma/sqrt(n)`.
3. For a confidence interval with known `sigma`, use `bar{x} +/- z sigma/sqrt(n)`.
4. For a hypothesis test, compute `z=(bar{x}-mu_0)/(sigma/sqrt(n))`.
5. Use a two-sided test when the question asks whether the mean is different from a value.
6. Use a one-sided test when the question asks whether the mean is larger or smaller than a value.

Exam trick:

One observation uses `sigma`. A sample mean uses `sigma/sqrt(n)`.

## Uppgift 5

Pattern:

- Maximum likelihood estimation for a continuous density with unknown parameter.

What the question is really testing:

You are given a density with an unknown `theta`. The task is to find the `theta` value that makes the observed sample most likely.

Same or similar questions:

- 2026-01, Uppgift 5: same ML checklist, but a geometric distribution.
- 2025-08, Uppgift 4: same ML checklist.
- 2025-06, Uppgift 4: same ML checklist with a continuous density.
- 2025-01, Uppgift 5: related ML pattern, but the parameter only has a few possible values.

Reusable method:

1. Write the likelihood as `L(theta)=prod f(x_i;theta)`.
2. Since the sample has independent observations, multiply all the densities.
3. Take `ln L(theta)` because products and powers become easier.
4. Differentiate with respect to `theta`.
5. Set the derivative equal to zero.
6. Solve for `theta`.

Exam trick:

If the question says "ML-skattning", the automatic checklist is: likelihood, log-likelihood, derivative, set to zero, solve.

## Uppgift 6

Pattern:

- Chi-square goodness-of-fit test for count data.

What the question is really testing:

You check whether the observed frequencies from a random number generator are close enough to what a fair uniform generator should produce.

Same or similar questions:

- 2025-01, Uppgift 6: related chi-square count-data test, but it is a homogeneity test using a two-way table.
- No exact earlier goodness-of-fit match found among the already processed exams.

Reusable method:

1. State the null hypothesis: the generator gives each number 1 to 6 with probability `1/6`.
2. Since there are 1000 generated numbers, each expected count is `1000/6`.
3. Compute `sum (observed - expected)^2 / expected`.
4. Use chi-square degrees of freedom `6-1=5`.
5. Compare with the 5% chi-square critical value.
6. If the test statistic is too large, reject the null hypothesis. Otherwise, do not reject it.

Exam trick:

For a fair die/random generator test, the expected counts are equal. Use counts in the chi-square formula, not percentages.

