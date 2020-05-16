import sys
import requests
import re

with open(sys.argv[1], 'r') as f:
    ds = f.read().strip()

def get_fasta(name):
    return requests.get("http://www.uniprot.org/uniprot/{}.fasta".format(name)).text.split("\n", 1)[1]

re1 = r"(?=N[^P][ST][^P])"

for protein in ds.split("\n"):
    matches = re.finditer(re1, get_fasta(protein).replace('\n', ''))
    matches = list(matches)
    if matches:
        print(protein)
        print(' '.join([str(match.start() + 1) for match in matches]))
