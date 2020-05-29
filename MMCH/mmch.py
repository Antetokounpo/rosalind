import sys; sys.path.append('..')
from rosalind import *
from math import factorial
rna = list(fasta(sys.argv[1]).values())[0]

au_min, au_max = sorted([rna.count('A'), rna.count('U')])
gc_min, gc_max = sorted([rna.count('G'), rna.count('C')])
print((factorial(au_max)//factorial(au_max-au_min))*(factorial(gc_max)//factorial(gc_max-gc_min)))
