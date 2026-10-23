# Pattern Tracker for 2024-08

Official exam PDF:

- `2024-08 tenta.pdf`
- Status: image-only PDF, but the rendered pages were readable.

Compared against already processed exams:

- 2026-01
- 2025-08
- 2025-06
- 2025-01
- 2024-05

This file tracks patterns only. It is not a full solution guide.

## Uppgift 1

Pattern:

- Three-event probability with union logic.
- Conditional probability.
- Pairwise independence checks.

What the question is really testing:

You are given three events `A`, `B`, and `C`, but some overlaps with `C` are impossible. The task is to use this structure to find missing event probabilities and check which pairs behave independently.

Same or similar questions:

- 2025-01, Uppgift 1: same three-set/inclusion-exclusion family.
- 2024-05, Uppgift 1a-c: similar conditional probability and independence-check pattern, but with two main categories.
- 2026-01, Uppgift 1: similar event table and independence-check idea.
- 2025-08, Uppgift 1: similar conditional probability/complement algebra.

Reusable method:

1. Write down the given probabilities for `A`, `B`, and `C`.
2. Use the fact that `A cap C=0` and `B cap C=0`; this means `C` does not overlap with `A` or `B`.
3. Since `P(A cup B cup C)=1`, use the union formula to find `P(A cup B)`.
4. Use `P(A cup B)=P(A)+P(B)-P(A cap B)` to find the overlap.
5. Use `P(A|B)=P(A cap B)/P(B)` for the conditional probability.
6. For independence, check each pair with `P(X cap Y)=P(X)P(Y)`.

Exam trick:

If an overlap is given as zero, treat it as "these two events cannot happen together." That makes the Venn diagram much easier.

## Uppgift 2

Pattern:

- Tree diagram for a dice game.
- Discrete probability function for winnings.
- Expected value as long-run average profit/loss.

What the question is really testing:

You must turn a game description into possible money outcomes. The outcome depends on whether the first die roll is odd/even, and sometimes on a second roll.

Same or similar questions:

- 2024-05, Uppgift 3: very similar game/expected-profit pattern.
- 2026-01, Uppgift 4a: related discrete distribution and expectation pattern.

Reusable method:

1. Split the game into branches: first roll odd or even.
2. If the first roll is odd, the game ends with a win of `k`.
3. If the first roll is even, draw the second branch for the second roll.
4. Convert each final game path into a money value for `X`.
5. Add probabilities for paths that give the same value of `X`.
6. Compute `E(X)=sum xP(X=x)` and interpret it as average winnings per game.

Exam trick:

For game questions, the expected value tells you the long-run result. Positive means good for the player; negative means bad for the player.

## Uppgift 3

Pattern:

- Continuous density normalization with an unknown endpoint.
- Probability from a density.
- Binomial probability for repeated independent trials.
- Complement/all-fail probability.

What the question is really testing:

First you make the function into a valid density by choosing the endpoint `a`. Then one event probability from the density becomes the success probability in repeated trials.

Same or similar questions:

- 2026-01, Uppgift 2: same density-normalization/probability family.
- 2025-08, Uppgift 2: same density/CDF/probability family.
- 2025-06, Uppgift 2: same density/CDF/probability family.
- 2025-01, Uppgift 3a-c: same density/probability family.
- 2024-05, Uppgift 2a-c: same density/probability/moments family.
- 2024-05, Uppgift 1d: same binomial count idea.
- 2025-01, Uppgift 2b-c: related repeated-independent-trials and complement idea.

Reusable method:

1. A density must have total area 1.
2. Set `int_0^a (-x+sqrt(3)) dx = 1` to find `a`.
3. For `P(X <= 1/sqrt(3))`, integrate the density from `0` to `1/sqrt(3)`.
4. In part c, use the given rounded value `p=0.8` as the success chance.
5. With 8 independent trials, use a binomial count for "more than two successes."
6. In part d, doubling the trials means use 16 trials and the complement/no-success idea.

Exam trick:

This is a two-stage question: first find one probability from a continuous density, then reuse that probability as `p` in a binomial model.

## Uppgift 4

Pattern:

- Normal distribution direct probability.
- Continuous point probability equals zero.
- Maximum of independent normal variables.
- Linear combination expectation and variance.

What the question is really testing:

The variables are normal and independent. You need to remember three separate facts: exact point probability is zero for continuous variables, `max <= c` means all variables are `<= c`, and variance squares the coefficients.

Same or similar questions:

- 2024-05, Uppgift 4a: same direct normal probability idea.
- 2025-01, Uppgift 2a-c: same normal standardization idea.
- 2024-05, Uppgift 2d; 2025-08, Uppgift 3b; 2025-06, Uppgift 3d; 2025-01, Uppgift 4d: same maximum pattern.
- 2026-01, Uppgift 4b; 2025-08, Uppgift 3c; 2025-06, Uppgift 3b; 2024-05, Uppgift 2e: same linear-combination expectation/variance pattern.

Reusable method:

1. For `P(X_1=1)`, remember continuous variables have probability 0 at one exact point.
2. For `P(|X_1|<=1)`, rewrite it as `P(-1 <= X_1 <= 1)` and standardize both endpoints.
3. For `P(max(X_1,X_2,X_3)<=1)`, rewrite it as all three variables being `<=1`.
4. Because they are independent, multiply the three probabilities.
5. For `Y=X_1-2X_2+3X_3`, use linearity for `E(Y)`.
6. For `V(Y)`, square the coefficients: `1^2`, `(-2)^2`, and `3^2`.

Exam trick:

For variance, the minus sign does not stay minus because `(-2)^2=4`.

## Uppgift 5

Pattern:

- Maximum likelihood estimation for a continuous density.

What the question is really testing:

You are given two observations and a density with unknown parameter `a`. You must choose the `a` value that makes those observations most likely.

Same or similar questions:

- 2024-05, Uppgift 5: same ML checklist for a continuous density.
- 2026-01, Uppgift 5: same ML checklist, but a geometric distribution.
- 2025-08, Uppgift 4: same ML checklist.
- 2025-06, Uppgift 4: same ML checklist.
- 2025-01, Uppgift 5: related ML idea, but with a finite set of possible parameter values.

Reusable method:

1. Write the likelihood as `L(a)=f(x_1;a)f(x_2;a)`.
2. Insert the observed values `x_1=3` and `x_2=5`.
3. Take `ln L(a)` because products and exponentials become easier.
4. Differentiate with respect to `a`.
5. Set the derivative equal to zero.
6. Solve for `a` and check that `a>0`.

Exam trick:

For ML questions with exponentials, the log usually turns the ugly expression into something manageable.

## Uppgift 6

Pattern:

- Two-sample confidence interval for difference of means.
- Two-sample hypothesis test for equal means.
- Common unknown standard deviation, so use pooled variance and t-method.

What the question is really testing:

There are two independent groups, mine A and mine B. The question asks whether their true average log-gold contents differ.

Same or similar questions:

- No exact earlier match found among the already processed exams.
- Related to 2026-01, Uppgift 6 and 2025-06, Uppgift 5b because those also use t-methods for means.
- Related to 2024-05, Uppgift 4 and 2025-08, Uppgift 6 because those are also mean inference questions, but with known `sigma` or one sample.

Reusable method:

1. Compute the sample mean for group A and group B.
2. Compute the sample variance for group A and group B.
3. Because the problem says both populations have the same `sigma`, pool the variances.
4. Build a confidence interval for `mu_1-mu_2`.
5. For the test, use `H_0: mu_1=mu_2`, which is the same as `mu_1-mu_2=0`.
6. If 0 is inside the 95% interval, you usually do not reject equality at 5%.

Exam trick:

Two groups means the center of the interval is `bar{x}-bar{y}`, not just one sample mean.

