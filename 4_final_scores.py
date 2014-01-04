# compute PMI for words in the different search corpora
# assemble the log probabilities from the outputs of log_px.py and log_pxy.py
# no, there is no smoothing in these calculations.

import sys, json, re, gzip
from math import log

# saves memory
CS_DICT = {}
def CS(s):
    return CS_DICT.setdefault(s,s)

denom = 2600000
# hard-coded from offline analysis
py = {CS('geek'):38873.0, CS('nerd'):30670.0, CS('dweeb'):13669.0, CS('dork'):25248.0}
for (y, val) in py.iteritems():
    py[y] = log(py[y]/denom, 2)

px = dict()
file1 = open(sys.argv[1], 'rb')
for line in file1:
    bits = line.split('\t')
    px[CS(bits[1].strip())] = float(bits[0])

scores = dict()

for i in range(2, len(sys.argv)):
    y = sys.argv[i].split('.')[0]
    file2 = open(sys.argv[i], 'rb')
    for line in file2:
        [pxy, x] = line.strip().split('\t')
        _pxy = float(pxy)
        try:
            scores[CS(x)][CS(y)] = (_pxy - px[CS(x)])
        except KeyError:
            scores[CS(x)] = dict()
            try:
                scores[CS(x)][CS(y)] = (_pxy - px[CS(x)])
            except KeyError:
                pass

ys = sorted(py.keys())
print 'word\t%s' % '\t'.join(ys)
for (x, vals) in scores.iteritems():
    v = []
    for y in ys:
        try:
            val = vals[y]
        except KeyError:
            val = 0
        v.append('%.6f' % val)
    print '%s\t%s' % (x, '\t'.join(v))