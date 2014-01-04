# parse Twitter search API results (search corpus)
# write to a tab-delimited format of date/user/tweet

import sys, json

for i in range(1, len(sys.argv)):
    log = open(sys.argv[i], 'r')
    try:
        for line in log:
            obj = json.loads(line)
            for tweet in obj['results']:
                print '%s\t%s\t%s' % (tweet['created_at'], tweet['from_user'], tweet['text'].encode('utf-8', 'replace').replace('\n',' '))
    except ValueError:
        pass