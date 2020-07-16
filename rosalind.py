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

r = requests.get(rosalind_url+prob)

if r.status_code != 200:
    print("Cannot get requested problem")
    print("Error "+str(r.status_code))
    sys.exit(1)

soup = BeautifulSoup(r.text, 'html.parser')
sample = soup.find(class_='codehilite').pre.text

if os.path.isdir(prob):
    print('Dir {} already exists'.format(prob))
    sys.exit(1)

os.mkdir(prob)
with open(os.path.join(prob, 'sample.txt'), 'w') as f:
    f.write(sample)

shutil.copy(os.path.join('template', 'template.'+lang), os.path.join(prob, prob.lower()+'.'+lang))
print('Done')
