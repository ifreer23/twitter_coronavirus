#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
#print(items)
#for k,v in items:
#    print(k,':',v)

#x = items[0]
#y = items[1]
#plt.bar(x,y)
#plt.xlabel('Hashtag')
#plt.ylabel('Frequency')
#plt.show()

frequency = []
hashtag = []

#for i in range(10):
for k,v in items:
    hashtag.append(k)
    frequency.append(v)
#print(hashtag,frequency)
plt.plot(hashtag,frequency)
#plt.bar(hashtag[:10],frequency[:10])
plt.savefig(f"{args.key}.png")
plt.show()
