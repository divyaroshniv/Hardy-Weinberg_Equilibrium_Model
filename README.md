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
This simulates genetic drift, a random evolutionary process that changes allele frequencies in small populations. The program starts with an initial allele frequency (p = 0.5) and repeatedly simulates inheritance across multiple generations using random sampling. In each generation, alleles are randomly assigned to individuals, and the new allele frequency is calculated. Over time, due to chnace events, the allele may become fixed (frequency = 1) or lost (frequency = 0), demonstrating how genetic drift can reduce genetic variation even without natural selection. This model helps illustrate the impact of population size and randomness on evolutionary change.
