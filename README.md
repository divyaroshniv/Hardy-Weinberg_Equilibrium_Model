# Hardy-Weinberg Equilibrium Model

## Hardy-Weinberg Equilibrium Gene Frequency Modelling
In a simple bi-allelic system (alleles A and a), we define the frequencies as:
- p: Frequency of the dominant allele (A)
- q: Frequency of the recessive allele (a)
- The fundamental equation: p + q = 1

  To predict genotype frequencies, we use:
  p^2 + 2pq + q^2 = 1 

## Statistical Validation (Chi-Squared Test)
Used scipy.stats to perform a Chi-square test. This determines if the deviation between observed and expected genotype frequencies is statistically significant (p < 0.05), indicating that the population may be evolving.

## Wright-Fisher Genetic Drift Simulation
This simulates the effect of sampling error in small populations. It can be used to visualise how allele frequencies fluctuate over hundreds of generations, leading to either fixation (allele frequency = 1) or loss (allele frequency = 0)
