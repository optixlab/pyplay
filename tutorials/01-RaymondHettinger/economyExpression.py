import collections, glob, gzip, re, heapq, pprint

counter = collections.Counter()
for filename in glob.glob('Data/logs/*.gz'):
    for line in gzip.open(filename):
        mo = re.search(r'GET (.*) HTTP/1', line)
        if mo is not None:
            url = mo.group(1)
            counter[url] += 1

result = heapq.nlargest(13,
                           counter.items(),
                           key=lambda (url, cnt): cnt)
pprint.pprint(result)
