# Exercise 17
# -----------

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

input = open(from_file)
indata = input.read()
#Alt: indata = input.read(open(from_file))

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready? RETURN to continue, CTRL-C to quit"

raw_input('?')

output = open(to_file, 'w')
output.write(indata)

print "All done!"

output.close()
input.close()
