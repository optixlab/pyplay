# Exercise 15
# -----------

from sys import argv

# Import the arguments
script, filename = argv

# open returns 'file' object. pydoc file for details.
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "I'll also ask you to type it again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

print "this is a readline():"
txt.readline()

print "resetting:"
txt.seek(0)
print txt.readline(),
print txt.readline(),
print txt.readline(),
print txt.readline(),  # the last few calls won't work
print txt.readline(),
print txt.readline()



