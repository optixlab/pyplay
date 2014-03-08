# Exercise 16
# -----------

from sys import argv

# Import the arguments
script, filename = argv

print "We're going to erase %r." % filename
print "to cancel, hit [CTRL-C]."
print "else, hit RETURN."

raw_input("?")

print "opening the file"
target = open(filename, 'w');

print "Erasing file..."
target.truncate()

print "provide 3 lines:"

line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")

print "Writing to the file."

# This can also be written in separate target.write commands
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "finally we close it."
target.close()
