#!/usr/bin/env python3

import sys
import os
import shutil
import requests
from bs4 import BeautifulSoup

if len(sys.argv) < 3:
    print("Usage: {} [problem] [hs|py]".format(sys.argv[0]))
    sys.exit(1)

rosalind_url = 'http://rosalind.info/problems/'
prob = sys.argv[1].upper()
lang = sys.argv[2]
output_file = os.path.join(prob, prob.lower()+'.'+lang)

r = requests.get(rosalind_url+prob)

if r.status_code != 200:
    print("Cannot get requested problem")
    print("Error "+str(r.status_code))
    sys.exit(1)

soup = BeautifulSoup(r.text, 'html.parser')
sample = soup.find(class_='codehilite').pre.text

if os.path.isfile(output_file):
    print('File {} already exists'.format(output_file))
    sys.exit(1)

if not os.path.isdir(prob):
    os.mkdir(prob)
with open(os.path.join(prob, 'sample.txt'), 'w') as f:
    f.write(sample)

shutil.copy(os.path.join('template', 'template.'+lang), output_file)
print('Done')
