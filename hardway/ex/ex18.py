# Exercise 18
# -----------

# Calling a script with arguments
def print_two(*args):
  arg1, arg2 = args
  print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
  print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
  print "arg1: %r" % arg1

def print_none():
  print "nothing"

print_two("Zed", "Shaw")
print_two_again("Zed2", "Shaw2")
print_one("first!")
print_none()
