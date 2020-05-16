import sys

with open(sys.argv[1], 'r') as f:
    ds = f.read()

def fasta_to_list(fasta):
    dna_list = fasta.split('>')[1:]
    dna_list = [*map(lambda x: filter(lambda y: y in ['A', 'C', 'G', 'T'], x), dna_list)]
    return [''.join([*i]) for i in dna_list]

def get_substrings_by_len(s, n):
    start = 0
    end = n
    return [s[start+i:end+i] for i in range(len(s)-n+1)]

def is_in_every_string(s, strings):
    for i in strings:
        if i.find(s) == -1:
            return False
    return True

def flatten(l):
    return [item for sublist in l for item in sublist]

def find_match(dnas):
    for n in reversed(range(0, len(dnas[0]))):
        substrings = flatten([get_substrings_by_len(s, n) for s in dnas])
        for substring in substrings:
            if is_in_every_string(substring, dnas):
                return substring

dnas = fasta_to_list(ds)
print(len(dnas))

print(find_match(dnas))
