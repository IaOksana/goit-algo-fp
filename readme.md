# Comparative Analysis: Analytical Method vs Monte-Carlo

## Introduction

This README compares the results of calculating the probability distribution of the sum of two dice using two distinct methods: the analytical method and the Monte Carlo method. The analytical method derives probabilities directly from combinatorial principles, providing exact results. In contrast, the Monte Carlo method relies on repeated random sampling to estimate probabilities. This simulation involves a large number of virtual dice rolls, and the observed frequencies of different sums are used to approximate the true probabilities. We will analyze how closely the Monte Carlo estimates converge to the analytical probabilities, highlighting the strengths and limitations of each approach. This comparison serves to illustrate the utility of the Monte Carlo method, especially in scenarios where analytical solutions are complex or intractable.

## Probabilities received:

|    SUM OF TWO DICE      |  probability_estimates  |  analytical_probability  |
|-------------------------|-------------------------|--------------------------|
|           2             |        2.76            |        2.78           |
|           3             |        5.571            |        5.56           |
|           4             |        8.376            |        8.33           |
|           5             |        11.112            |        11.11           |
|           6             |        13.963            |        13.89           |
|           7             |        16.821            |        16.67           |
|           8             |        13.873            |        13.89           |
|           9             |        11.152            |        11.11           |
|           10             |        8.16            |        8.33           |
|           11             |        5.464            |        5.56           |
|           12             |        2.748            |        2.78           |


## Conclusion

No significant differences between 2 methods were observed (num_samples = 100000).

However, it's important to performe a large number of experimets to achieve a good result.