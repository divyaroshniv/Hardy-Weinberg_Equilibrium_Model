import matplotlib.pyplot as plt

#Observed Genotype counts
AA = 450
Aa = 400
aa = 150

N = AA + Aa + aa

p = (2*AA + Aa)/(2*N)
q = 1 - p

print("Allele Frequency p(A):", p)
print("Allele Frequency q(a):", q)

#Expected Genotype counts
exp_AA = p**2 * N
exp_Aa = 2*p*q * N
exp_aa = q**2 * N

print("Expected AA =", exp_AA)
print("Expected Aa =", exp_Aa)
print("Expected aa =", exp_aa)

labels = ["AA", "Aa", "aa"]
observed = [AA, Aa, aa]
expected = [exp_AA, exp_Aa, exp_aa]

x = [0, 1, 2]

plt.bar(x, observed)
plt.bar(x, expected)
plt.xticks(x, labels)
plt.ylabel("Number of Individuals")
plt.title("Observed vs Expected Genotypes")
plt.show()