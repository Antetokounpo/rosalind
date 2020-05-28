import sys

with open(sys.argv[1], 'r') as f:
    ds = f.read().strip()

def fastaToList(fasta):
    return list(filter(bool, list(map(lambda s: ''.join(list(filter(lambda c: c in 'AGCT', s))), fasta.split('>')))))

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

dna = fastaToList(ds)[0]
for p in range(len(dna)):
    for l in range(4, 13):
        if len(dna) < p+l:
            break
        if dna[p:p+l] == reverseDna(dna[p:p+l]):
            print(p+1, l)

