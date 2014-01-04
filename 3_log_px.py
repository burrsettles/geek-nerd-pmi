# parse Twitter streaming API results (background corpus)
# write log probabilities each word, tab-delimited, one per line

import sys, json, re, gzip
from math import log

counter = {}
total = 0.0

def legal(w):
    return not (len(w) == 0 or w[0] == '@')

# saves memory
CS_DICT = {}
def CS(s):
    return CS_DICT.setdefault(s,s)

p = re.compile(r'[^\@\#\w\d]+')

for i in range(1, len(sys.argv)):
    logfile = gzip.open(sys.argv[i], 'rb')
    try:
        for line in logfile:
            obj = json.loads(line)
            try:
                words = p.split(obj['text'].lower())
                for w in words:
                    if legal(w):
                        try:
                            counter[CS(w)] += 1
                        except KeyError:
                            counter[CS(w)] = 1
                        total += 1
            except KeyError:
                pass
    except ValueError:
        pass

for (w, ct) in counter.iteritems():
    print '%.6f\t%s' % (log(ct/total, 2), w)
