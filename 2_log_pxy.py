# parse the results of rfmt_queries.py (search corpus)
# write log probabilities each word, tab-delimited, one per line

import sys, json, re
from math import log

key = sys.argv[1].split('.')[0]

counter = {}
total = 0.0

# saves memory
CS_DICT = {}
def legal(w):
    if len(w) == 0 or w[0] == '@':
        return False
    return w.find(key) == -1

def CS(s):
    return CS_DICT.setdefault(s,s)

p = re.compile(r'[^\@\#\w\d]+')

logfile = open(sys.argv[1], 'r')
for line in logfile:
    bits = line.split('\t')
    words = p.split(bits[2].lower())
    for w in words:
        if legal(w):
            try:
                counter[w] += 1
            except KeyError:
                counter[w] = 1
            total += 1

for (w, ct) in counter.iteritems():
    print '%.6f\t%s' % (log(ct/total, 2), w)
    # print '%s\t%.6f' % (w, ct/total)