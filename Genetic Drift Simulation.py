import random

#Starting allele frequency
p = 0.5
population = 50
generations = 20

print("Genetic Allele Frequency")

for gen in range(generations):
    A_count = 0

    for i in range(2*population):
        if random.random() < p:
            A_count += 1

    #New allele frequency
    p = A_count / (2*population)
    print(gen, "    ", p)

    if p == 0:
        print("Allele lost")
    elif p == 1:
        print("Allele fixed")
        break