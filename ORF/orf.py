import sys
import string

with open(sys.argv[1], 'r') as f:
    ds = f.read()

def fastaToList(fasta):
    return list(filter(bool, list(map(lambda s: ''.join(list(filter(lambda c: c in 'AGCT', s))), fasta.split('>')))))

def getDnaCodonTable(filename):
    with open(filename, 'r') as f:
        table = f.read().strip()
    table = list(filter(bool, table.replace('\n', ' ').split(' ')))
    table = dict([(table[i], table[i+1])for i in range(0, len(table), 2)])
    
    return table

def reverseDna(dna):
    r_dna = ""
    table = {
        'A' : 'T',
        'T' : 'A',
        'C' : 'G',
        'G' : 'C'
    }
    for i in dna:
        r_dna += table[i]
    return r_dna[::-1]

def dnaToProt(dna, table):
    prot = ""
    for i in range(0, len(dna)-2, 3):
        codon = dna[i:i+3]
        p = table[codon]
        if p == 'M':
            prot += p
            continue
        elif p == 'Stop' and prot:
            return prot
        if prot:
            prot += p
        
dna = fastaToList(ds)[0]
table = getDnaCodonTable("dna_codon.txt")
r_dna = reverseDna(dna)
prots = []
for i in range(len(dna)):
    prots.append(dnaToProt(dna[i:], table))
for i in range(len(dna)):
    prots.append(dnaToProt(r_dna[i:], table))
prots = list(filter(bool, list(set(prots))))
for i in prots:
    print(i)

