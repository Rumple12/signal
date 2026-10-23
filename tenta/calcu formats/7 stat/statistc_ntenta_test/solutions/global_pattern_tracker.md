# MA087G Global Pattern Tracker

Scope of this tracker:

- Fully compared here: 2024-05, 2024-08, 2025-01, 2025-06, 2025-08, 2026-01.
- The 2024-05 official PDF was image-only, but the rendered pages were readable.
- The 2024-08 official PDF was image-only, but the rendered pages were readable.

This file is for pattern recognition, not full solutions. The goal is: when you see a question, quickly know which method to use.

## Pattern: Two-event probability table, conditional probability, and independence

### Repeated in

| Exam | Question | Same/Variation/New | Notes |
|------|----------|--------------------|-------|
| 2026-01 | Uppgift 1 | Base pattern | Reconstruct event probabilities and check independence. |
| 2025-08 | Uppgift 1 | Variation | More complement notation, same probability-table thinking. |
| 2024-05 | Uppgift 1a-c | Same pattern | Uses `L`, `M`, vegetarian/not vegetarian, conditional probability, union, and independence. |
| 2024-08 | Uppgift 1 | Variation | Three events, but still uses union, conditional probability, and independence checks. |

### Original questions in this pattern

#### 2026-01 — Uppgift 1

Låt \(A\) och \(B\) vara två händelser i ett och samma utfallsrum. Sannolikheten för att ingen av händelserna \(A\) eller \(B\) inträffar är 60 %, medan sannolikheten för att både \(A\) och \(B\) inträffar är 20 %. Dessutom är sannolikheten 10 % för att händelsen \(B\) inträffar utan att händelsen \(A\) inträffar.

a) Är \(A\) och \(B\) oberoende händelser? (4 p)

b) Beräkna den betingade sannolikheten för händelsen \(B\) givet att händelsen \(A\) inte inträffar. (2 p)

#### 2025-08 — Uppgift 1

Låt \(A\) och \(B\) vara två händelser sådana att
\[
P(A^c|B^c)=0.6,\qquad P(B^c|A^c)=0.4,\qquad P(A^c\cup B^c)=0.8.
\]
Beräkna \(P(A)\) och \(P(B)\). (6 p)

#### 2024-05 — Uppgift 1a-c

I ett stort land kandiderar Lena och Mats för att bli president. För enkelhetens skull antar vi att alla röstberättigade medborgare vet vilken kandidat de föredrar (\(L\) eller \(M\)) och att ingen vill lägga ner sin röst. Vi vill undersöka huruvida den politiska läggningen hänger ihop med omständigheten att man är vegetarian (\(V\)) eller inte (ej \(V\)). Följande sannolikheter är kända:
\[
P(L\cap V)=0.15,\qquad P(M\cap V)=0.05,\qquad P(L)=0.47.
\]

a) Bestäm sannolikheterna \(P(V)\), \(P(\text{ej }V)\) och \(P(L|V)\). (1.5 p)

b) Bestäm sannolikheten \(P(L\cup V)\). (1 p)

c) Är händelserna \(L\) och \(V\) oberoende? (1 p)

#### 2024-08 — Uppgift 1

För händelserna \(A\), \(B\) och \(C\) är följande sannolikheter kända:
\[
P(A)=\frac{1}{3},\qquad P(B)=\frac{1}{4},\qquad P(C)=\frac{1}{2}.
\]
Dessutom vet man att \(P(A\cup B\cup C)=1\) och att \(P(A\cap C)=P(B\cap C)=0\).

a) Bevisa att \(P(A\cup B)=\frac{1}{2}\). (2.5 p)

b) Bestäm \(P(A\cap B)\) och \(P(A|B)\). (2 p)

c) Vilka par av händelserna \(A\), \(B\), \(C\) är oberoende? Motivera dina svar! (1.5 p)

### What this pattern means

You have two yes/no ideas at the same time. For example: votes for Lena or Mats, and vegetarian or not vegetarian. The question wants you to fill in missing probabilities and then answer things like "given that someone is vegetarian, what is the chance they vote Lena?"

### How to recognize it

- The question uses events like `A`, `B`, `L`, `V`.
- You see symbols like `cap`, `cup`, `|`, or words like "given that".
- It asks whether two events are independent.

### Reusable solving recipe

1. Make a small 2-by-2 table.
2. Put the known overlap probabilities into the table.
3. Use row totals and column totals to find missing pieces.
4. For conditional probability, use overlap divided by the condition.
5. For independence, compare `P(A cap B)` with `P(A)P(B)`.

### Formula cheat

`P(A|B)=P(A cap B)/P(B)`

`P(A cup B)=P(A)+P(B)-P(A cap B)`

Independent means: `P(A cap B)=P(A)P(B)`

### Common twist

The teacher changes the story, but it is still only a two-way table.

### Beginner warning

For `P(A|B)`, the bottom of the fraction is always the thing after the vertical bar.

## Pattern: Binomial count probability

### Repeated in

| Exam | Question | Same/Variation/New | Notes |
|------|----------|--------------------|-------|
| 2024-05 | Uppgift 1d | New pattern in processed set | Ten independent/repeated answers, probability of more than five non-vegetarians. |
| 2024-08 | Uppgift 3c-d | Same pattern | Repeats one event 8 or 16 times and counts how often it happens. |
| 2025-01 | Uppgift 2b-c | Related only | Uses repeated independent items and complements, but not a full binomial count table. |

### What this pattern means

You repeat the same yes/no experiment several times and count how many successes you get.

### How to recognize it

- The question says a fixed number of people/items/trials, like 10.
- Each trial has the same probability.
- It asks for "more than", "at least", "exactly", or "fewer than" a number of successes.

### Reusable solving recipe

1. Decide what counts as success.
2. Identify `n`, the number of trials.
3. Identify `p`, the chance of success in one trial.
4. Add the binomial probabilities for all allowed success counts.
5. Use the complement if that is shorter.

### Formula cheat

`P(X=k)=binom(n,k)p^k(1-p)^{n-k}`

### Common twist

"More than 5" means `6,7,8,9,10`, not `5,6,7,8,9,10`.

### Beginner warning

Binomial needs repeated trials with the same probability. If the question says without replacement, think combinations/hypergeometric instead.

## Pattern: Continuous density, CDF, probability, and moments

### Repeated in

| Exam | Question | Same/Variation/New | Notes |
|------|----------|--------------------|-------|
| 2026-01 | Uppgift 2 | Base pattern | Unknown constant, CDF, probability, expectation, standard deviation. |
| 2025-08 | Uppgift 2 | Same pattern | Unknown constant and same density checklist. |
| 2025-06 | Uppgift 2 | Same pattern | Unknown constant, CDF, probability, moments. |
| 2025-01 | Uppgift 3a-c | Same pattern | Unknown constant and CDF/probability. |
| 2024-05 | Uppgift 2a-c | Variation | Density is already normalized; still checks density, probability, expectation, variance. |
| 2024-08 | Uppgift 3a-b | Variation | Unknown support endpoint `a`; then probability from the density. |

### What this pattern means

You are given a curve called a density. The area under the curve is probability. The question usually asks you to check the curve, integrate it, and find probabilities or averages.

### How to recognize it

- The question gives `f_X(x)`.
- It asks if `f_X` is a density.
- It asks for `P(X <= c)`, `E(X)`, or `V(X)`.

### Reusable solving recipe

1. Check that the density is never negative.
2. Check that the total area/integral equals 1.
3. For probability, integrate the density over the wanted interval.
4. For expected value, integrate `x f(x)`.
5. For variance, find `E(X^2)` and use `V(X)=E(X^2)-[E(X)]^2`.

### Formula cheat

`P(a <= X <= b)=int_a^b f(x) dx`

`E(X)=int x f(x) dx`

`V(X)=E(X^2)-[E(X)]^2`

### Common twist

Sometimes the density has an unknown constant. Sometimes, like 2024-05, the density is already complete and you only verify it.

### Beginner warning

For continuous variables, probability is area. Do not plug into the density and treat that as the probability.

## Pattern: Maximum of independent variables

### Repeated in

| Exam | Question | Same/Variation/New | Notes |
|------|----------|--------------------|-------|
| 2025-08 | Uppgift 3b | Base pattern | `max(X_1,X_2) <= c` with independent identical variables. |
| 2025-06 | Uppgift 3d | Same pattern | Maximum of independent variables. |
| 2025-01 | Uppgift 4d | Same pattern | Maximum below a boundary. |
| 2024-05 | Uppgift 2d | Same pattern | `P(max(X,Y) <= 0)` with independent `X` and `Y`. |
| 2024-08 | Uppgift 4b | Same pattern | `P(max(X_1,X_2,X_3) <= 1)` for independent normal variables. |

### What this pattern means

The biggest value is below a boundary only if every single variable is below that boundary.

### How to recognize it

- The question contains `max(...)`.
- It asks for probability that the maximum is `<=` some value.
- It says the variables are independent.

### Reusable solving recipe

1. Rewrite `max(X,Y) <= c` as `X <= c` and `Y <= c`.
2. Find each separate probability.
3. Multiply them because of independence.

### Formula cheat

`P(max(X,Y) <= c)=P(X <= c)P(Y <= c)` when `X` and `Y` are independent.

### Common twist

The variables may have different distributions. You still multiply, but each probability may be found in a different way.

### Beginner warning

`max <= c` means all variables are below `c`. `max > c` means at least one variable is above `c`.

## Pattern: Linear combination expectation and variance

### Repeated in

| Exam | Question | Same/Variation/New | Notes |
|------|----------|--------------------|-------|
| 2026-01 | Uppgift 4b | Base pattern | Linear combination of normal variables. |
| 2025-08 | Uppgift 3c | Same core method | Expectation and variance of a linear expression. |
| 2025-06 | Uppgift 3b | Same core method | Coefficients matter in variance. |
| 2025-01 | Uppgift 4a-c | Variation | Uniform variable plus linear transformation. |
| 2024-05 | Uppgift 2e | Same core method | `V(X+Y)` for independent variables. |
| 2024-08 | Uppgift 4c | Same core method | `Y=X_1-2X_2+3X_3`, so coefficients must be squared in variance. |

### What this pattern means

You combine random variables by adding, subtracting, or multiplying by constants. The average and spread of the new variable come from the old ones.

### How to recognize it

- The question asks for `E(aX+bY)` or `V(aX+bY)`.
- It says variables are independent.
- It defines a new variable using a formula.

### Reusable solving recipe

1. For expectation, multiply each mean by its coefficient and add.
2. For variance, square each coefficient first.
3. If variables are independent, add the variance parts.

### Formula cheat

`E(aX+bY)=aE(X)+bE(Y)`

`V(aX+bY)=a^2V(X)+b^2V(Y)` if independent.

### Common twist

The minus sign disappears inside variance because the coefficient is squared.

### Beginner warning

Never add standard deviations directly. Work with variances first.

## Pattern: Discrete distribution from counting outcomes and game expected value

### Repeated in

| Exam | Question | Same/Variation/New | Notes |
|------|----------|--------------------|-------|
| 2026-01 | Uppgift 4a | Variation | Discrete distribution from word proportions. |
| 2024-05 | Uppgift 3 | New stronger version | Build distribution of `|i-j|` from dice outcomes and decide if a game is profitable. |
| 2024-08 | Uppgift 2 | Same game pattern | Tree diagram, probability function for winnings, and long-run expected profit. |

### What this pattern means

There are only a few possible values. You count how often each value happens, turn counts into probabilities, then compute the expected value.

### How to recognize it

- The sample space is finite, like dice outcomes.
- A variable is defined by a rule, like `X=|i-j|`.
- The question asks for a probability function or long-run profit.

### Reusable solving recipe

1. List or count all equally likely outcomes.
2. Count how many outcomes give each value of `X`.
3. Divide by the total number of outcomes.
4. Compute `E(X)=sum x P(X=x)`.
5. For a game, compute expected winnings and check if it is positive.

### Formula cheat

`E(X)=sum x P(X=x)`

Expected profit = sum of each profit/loss times its probability.

### Common twist

The teacher may hide the distribution inside a story, so you must build the table yourself.

### Beginner warning

For dice thrown twice, `(1,5)` and `(5,1)` are different ordered outcomes.

## Pattern: Normal distribution direct probability

### Repeated in

| Exam | Question | Same/Variation/New | Notes |
|------|----------|--------------------|-------|
| 2025-01 | Uppgift 2a-c | Base pattern | Normal cutoff probability, then repeated items. |
| 2024-05 | Uppgift 4a | Same direct normal method | `X` is normal and asks for `P(X <= 10.375)`. |
| 2024-08 | Uppgift 4a | Variation | Includes continuous point probability `P(X=1)=0` and interval probability `P(|X|<=1)`. |

### What this pattern means

The variable is normally distributed, and you need a probability below, above, or between values.

### How to recognize it

- The question says `normalfördelad` or writes `N(mu,sigma)`.
- It gives a mean and a standard deviation.
- It asks for a probability involving one measurement.

### Reusable solving recipe

1. Write down the value `x`, the mean `mu`, and standard deviation `sigma`.
2. Convert to a `z`-value.
3. Use the standard normal table or calculator.
4. Use complements for "greater than".

### Formula cheat

`z=(x-mu)/sigma`

### Common twist

Sometimes the question asks for `P(X > x)` instead of `P(X <= x)`. Then use `1 - table value`.

### Beginner warning

Use `sigma` for one observation. Use `sigma/sqrt(n)` only for a sample mean.

## Pattern: Confidence interval for mean, sigma known

### Repeated in

| Exam | Question | Same/Variation/New | Notes |
|------|----------|--------------------|-------|
| 2025-06 | Uppgift 5a | Base pattern | Confidence interval for `mu` with known `sigma`. |
| 2024-05 | Uppgift 4b | Same pattern | Normal sample with known `sigma=0.5` and `n=5`. |

### What this pattern means

You estimate the true mean using a sample mean, and the population standard deviation is known.

### How to recognize it

- It asks for a confidence interval for `mu`.
- It gives `sigma`.
- It gives `n` and `bar{x}`.

### Reusable solving recipe

1. Write down `bar{x}`, `sigma`, and `n`.
2. Choose the `z` value for the confidence level.
3. Compute the margin of error.
4. Put `bar{x}` in the middle and add/subtract the margin.

### Formula cheat

`bar{x} +/- z_{alpha/2} sigma/sqrt(n)`

### Common twist

If `sigma` is not known and only sample standard deviation `s` is given, switch to the t-method.

### Beginner warning

Do not use `sigma` alone in the denominator. For a sample mean, use `sigma/sqrt(n)`.

## Pattern: Hypothesis test for mean, sigma known

### Repeated in

| Exam | Question | Same/Variation/New | Notes |
|------|----------|--------------------|-------|
| 2025-01 | Uppgift 2d | Base pattern | One-sided z-test for a mean. |
| 2025-06 | Uppgift 6 | Same pattern | One-sided known-sigma mean test. |
| 2025-08 | Uppgift 6a-b | Same pattern | One-sided known-sigma mean test. |
| 2024-05 | Uppgift 4c-d | Variation | Two-sided and one-sided tests with known `sigma=0.5`. |

### What this pattern means

You check whether a claimed mean is believable using sample data.

### How to recognize it

- It asks you to test a hypothesis about `mu`.
- The population standard deviation is given.
- It gives `bar{x}`, `n`, and a significance level like 5%.

### Reusable solving recipe

1. State `H_0` and `H_1`.
2. Compute the z-statistic.
3. Choose two-sided or one-sided critical value based on the wording.
4. Reject only if the statistic is far enough into the rejection area.
5. Explain the conclusion in normal words.

### Formula cheat

`z=(bar{x}-mu_0)/(sigma/sqrt(n))`

### Common twist

"Has changed" usually means two-sided. "Larger than" or "smaller than" means one-sided.

### Beginner warning

Do not reject just because the sample mean is different. It must be different enough compared with the standard error.

## Pattern: Maximum likelihood estimation

### Repeated in

| Exam | Question | Same/Variation/New | Notes |
|------|----------|--------------------|-------|
| 2026-01 | Uppgift 5 | Base pattern | ML for geometric distribution. |
| 2025-08 | Uppgift 4 | Same checklist | Likelihood, log, derivative, solve. |
| 2025-06 | Uppgift 4 | Same checklist | ML with continuous density. |
| 2025-01 | Uppgift 5 | Variation | Finite parameter set, compare likelihoods directly. |
| 2024-05 | Uppgift 5 | Same checklist | ML for `f(x)=theta x^{theta-1}` on `(0,1)`. |
| 2024-08 | Uppgift 5 | Same checklist | ML for density `x/a exp(-x^2/(2a))` with two observations. |

### What this pattern means

You choose the parameter value that makes the observed sample most likely.

### How to recognize it

- The question says `ML-skattning`.
- There is an unknown parameter like `p`, `theta`, or `lambda`.
- You are given a sample.

### Reusable solving recipe

1. Write the likelihood as the product of all individual probabilities/densities.
2. Take `ln L` if the expression has products or powers.
3. Differentiate with respect to the unknown parameter.
4. Set the derivative equal to zero.
5. Solve for the parameter.
6. Check that the answer is allowed by the parameter range.

### Formula cheat

`L(theta)=prod f(x_i;theta)`

`ell(theta)=ln L(theta)`

Solve `ell'(theta)=0`.

### Common twist

Sometimes the parameter has only a few allowed values. Then compare the likelihood values instead of differentiating.

### Beginner warning

The likelihood is a function of the parameter, not of the data. The data are already observed numbers.

## Pattern: Chi-square test for count data

### Repeated in

| Exam | Question | Same/Variation/New | Notes |
|------|----------|--------------------|-------|
| 2025-01 | Uppgift 6 | Base related pattern | Chi-square homogeneity test for a two-way table. |
| 2024-05 | Uppgift 6 | Variation | Chi-square goodness-of-fit test for a fair discrete uniform generator. |

### What this pattern means

You compare observed counts with expected counts. If the difference is too large, the model is suspicious.

### How to recognize it

- The data are frequencies/counts.
- The question asks whether a distribution fits or whether groups behave the same.
- There are categories, not raw measurements.

### Reusable solving recipe

1. State the null hypothesis.
2. Compute expected counts.
3. For each category, compute `(observed - expected)^2 / expected`.
4. Add the pieces.
5. Compare with a chi-square critical value.
6. Conclude in words.

### Formula cheat

`chi^2=sum (O_i-E_i)^2/E_i`

Goodness-of-fit degrees of freedom: number of categories minus 1, if no parameters are estimated.

### Common twist

2025-01 compares groups in a table. 2024-05 compares one observed frequency row to a claimed distribution.

### Beginner warning

Use counts, not percentages, inside the chi-square formula.

## Pattern: Exponential distribution and exponential survival

### Repeated in

| Exam | Question | Same/Variation/New | Notes |
|------|----------|--------------------|-------|
| 2026-01 | Uppgift 3 | Variation | Minimum of independent exponentials; add rates. |
| 2025-06 | Uppgift 3a | Base probability pattern | Direct exponential probabilities. |

### What this pattern means

The exponential distribution is usually about waiting times. Right-tail probabilities are especially simple.

### How to recognize it

- The question says `Exp(lambda)`.
- It asks for waiting-time probabilities or a minimum of waiting times.

### Reusable solving recipe

1. Identify the rate `lambda`.
2. Use `P(X>t)=e^{-lambda t}` for right tails.
3. For a minimum, use survival and independence.

### Formula cheat

`F(t)=1-e^{-lambda t}`

`P(X>t)=e^{-lambda t}`

### Common twist

For the minimum of independent exponentials, the rates add.

### Beginner warning

Do not confuse the rate `lambda` with the mean. For exponential, the mean is `1/lambda`.

## Pattern: Transformed variable distribution

### Repeated in

| Exam | Question | Same/Variation/New | Notes |
|------|----------|--------------------|-------|
| 2025-06 | Uppgift 3c | Base pattern | Distribution function of `4X+1`. |
| 2025-01 | Uppgift 3d | Same pattern | Transform variable and find distribution/density. |
| 2025-01 | Uppgift 4a-c | Related | Uniform plus linear transformation. |

### What this pattern means

A new random variable is made from an old one, and you need the distribution of the new one.

### How to recognize it

- The question defines something like `Y=g(X)`.
- It asks for the distribution function or density of `Y`.

### Reusable solving recipe

1. Start with `F_Y(y)=P(Y<=y)`.
2. Replace `Y` by the expression in `X`.
3. Solve the inequality for `X`.
4. Insert into `F_X`.
5. Differentiate only if a density is needed.

### Formula cheat

`F_Y(y)=P(g(X)<=y)`

### Common twist

If the transformation is decreasing, the inequality flips.

### Beginner warning

Do not plug into the old density directly unless you also handle the transformation factor correctly.

## Pattern: Uniform distribution and linear transformation

### Repeated in

| Exam | Question | Same/Variation/New | Notes |
|------|----------|--------------------|-------|
| 2025-01 | Uppgift 4a-c | Base pattern | Uniform probability by interval length, then `2X-1` expectation, variance, and CDF. |

### What this pattern means

The variable is equally spread over an interval. Probabilities are just lengths, and a linear transformation shifts or stretches the interval.

### How to recognize it

- The question says `likformigt fördelad`.
- It gives an interval like `(-1,1)`.
- It asks for interval probability, expectation/variance of `aX+b`, or the CDF of `aX+b`.

### Reusable solving recipe

1. For probability, use wanted interval length divided by total interval length.
2. For expectation, use `E(aX+b)=aE(X)+b`.
3. For variance, use `V(aX+b)=a^2V(X)`.
4. For the CDF of the transformed variable, start with `P(aX+b <= y)` and solve for `X`.

### Formula cheat

If `X` is uniform on `(a,b)`, then:

`P(c<X<d)=(d-c)/(b-a)` inside the interval.

For a linear transformation:

`E(rX+s)=rE(X)+s`

`V(rX+s)=r^2V(X)`

### Common twist

The transformed variable may have a new interval, so the CDF must be 0 before that interval and 1 after it.

### Beginner warning

Uniform does not mean every decimal value has a positive point probability. It means equal interval lengths have equal probability.

## Pattern: Hypergeometric/combinations without replacement

### Repeated in

| Exam | Question | Same/Variation/New | Notes |
|------|----------|--------------------|-------|
| 2025-06 | Uppgift 1 | New pattern in processed set | Draw balls without replacement. |

### What this pattern means

You draw items without putting them back, so the probabilities change after each draw.

### How to recognize it

- The question says without replacement.
- Order does not matter.
- It asks for a mix of item types.

### Reusable solving recipe

1. Count total ways to choose the sample.
2. Count favorable ways to choose the wanted mix.
3. Divide favorable by total.
4. Use complements for "at least one" when shorter.

### Formula cheat

`P = favorable combinations / total combinations`

### Common twist

The question may ask conditional probability after restricting the sample.

### Beginner warning

Without replacement is not binomial unless the course explicitly says to approximate.

## Pattern: Confidence interval for mean, sigma unknown

### Repeated in

| Exam | Question | Same/Variation/New | Notes |
|------|----------|--------------------|-------|
| 2026-01 | Uppgift 6a | Base pattern | t-interval for mean. |
| 2025-06 | Uppgift 5b | Same pattern | Unknown sigma, use sample standard deviation. |

### What this pattern means

You estimate a mean, but the real population standard deviation is not known.

### How to recognize it

- It asks for a confidence interval for `mu`.
- It gives sample standard deviation `s`, not known `sigma`.

### Reusable solving recipe

1. Find `bar{x}`, `s`, and `n`.
2. Use degrees of freedom `n-1`.
3. Use the t critical value.
4. Build `bar{x} +/- t s/sqrt(n)`.

### Formula cheat

`bar{x} +/- t_{alpha/2,n-1} s/sqrt(n)`

### Common twist

Small samples make the t-method more obvious.

### Beginner warning

Known `sigma` means z. Unknown `sigma` and sample `s` means t.

## Pattern: Confidence interval for normal sigma

### Repeated in

| Exam | Question | Same/Variation/New | Notes |
|------|----------|--------------------|-------|
| 2025-08 | Uppgift 5 | New pattern in processed set | Interval for variance/standard deviation using chi-square. |

### What this pattern means

You estimate how spread out a normal population is, not where its mean is.

### How to recognize it

- The question asks for `sigma` or `sigma^2`.
- The data are assumed normal.
- It asks for an interval for spread.

### Reusable solving recipe

1. Compute sample variance `s^2`.
2. Use chi-square values with `n-1` degrees of freedom.
3. Build the interval for `sigma^2`.
4. Square-root the endpoints if the question asks for `sigma`.

### Formula cheat

`((n-1)s^2/chi^2_upper, (n-1)s^2/chi^2_lower)`

### Common twist

The interval for `sigma` is the square root of the interval for `sigma^2`.

### Beginner warning

Mean intervals use z or t. Spread intervals use chi-square.

## Pattern: Power or sample size for a mean test

### Repeated in

| Exam | Question | Same/Variation/New | Notes |
|------|----------|--------------------|-------|
| 2025-08 | Uppgift 6c | New pattern in processed set | Find `n` so a one-sided test has enough detection probability. |

### What this pattern means

You are not testing one observed sample anymore. You are choosing a sample size so the test will probably detect a real change.

### How to recognize it

- It asks how large `n` must be.
- It gives a desired probability of rejecting.
- It mentions a specific true mean under the alternative.

### Reusable solving recipe

1. Write the rejection boundary from the test.
2. Assume the alternative mean is true.
3. Standardize the rejection probability under that mean.
4. Solve for `n`.
5. Round up.

### Formula cheat

Use the same z-standardization, but under the alternative mean.

### Common twist

The question may give a normal-table clue instead of asking for power directly.

### Beginner warning

Power is the chance of rejecting when the alternative is true, not the significance level.

## Pattern: Three-set inclusion-exclusion

### Repeated in

| Exam | Question | Same/Variation/New | Notes |
|------|----------|--------------------|-------|
| 2025-01 | Uppgift 1 | New pattern in processed set | Three sets with overlaps and triple overlap. |
| 2024-08 | Uppgift 1 | Variation | Three events with union equal to 1 and some impossible overlaps. |

### What this pattern means

You count people/items that belong to at least one of three groups, while correcting for overlaps.

### How to recognize it

- There are three sets, like `A`, `B`, and `C`.
- Pairwise overlaps and triple overlap appear.
- It asks for at least one, none, or exactly one.

### Reusable solving recipe

1. Add the three single counts.
2. Subtract the pairwise overlaps.
3. Add back the triple overlap.
4. Use complement for none.
5. For exactly one, subtract overlaps from each single group carefully.

### Formula cheat

`P(A cup B cup C)=P(A)+P(B)+P(C)-P(A cap B)-P(A cap C)-P(B cap C)+P(A cap B cap C)`

### Common twist

"Exactly one" is not the same as "at least one".

### Beginner warning

The triple overlap gets subtracted too many times, so it must be added back once.

## Pattern: Two-sample confidence interval and test for difference of means

### Repeated in

| Exam | Question | Same/Variation/New | Notes |
|------|----------|--------------------|-------|
| 2024-08 | Uppgift 6 | New pattern in processed set | Compare two independent normal samples with common unknown standard deviation. |

### What this pattern means

You compare two groups and ask whether their true averages are different. Here the groups are two mining locations, and the values have been log-transformed first.

### How to recognize it

- There are two independent samples.
- The question asks for a confidence interval for `mu_1-mu_2`.
- It also asks to test whether the means are equal.
- The model says both groups are normal and have the same `sigma`.

### Reusable solving recipe

1. Compute each sample mean.
2. Compute each sample variance.
3. Pool the variances because the problem assumes the same `sigma`.
4. Build a t-interval for `mu_1-mu_2`.
5. For the test, use `H_0: mu_1=mu_2`.
6. Check whether 0 is inside the interval, or compute the matching t-test.

### Formula cheat

`s_p^2=((n_1-1)s_1^2+(n_2-1)s_2^2)/(n_1+n_2-2)`

`(bar{x}-bar{y}) +/- t_{alpha/2,n_1+n_2-2} s_p sqrt(1/n_1+1/n_2)`

### Common twist

Sometimes the question gives raw data, so you must compute the means and standard deviations yourself. Sometimes it gives summary values directly.

### Beginner warning

This is not a one-sample mean interval. There are two samples, so the center is `bar{x}-bar{y}`.
