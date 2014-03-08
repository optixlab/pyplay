# Exercise 37
#------------

# Symbol review

x = 33
y = x / 2

# Assert statement: assert expr1 [, expr2]
assert x == y * 2, "Multiply fails"
# equivalent to:
if __debug__:
  if not x == y * 2: raise AssertionError("Multiply fails again")

# pass
def f(arg): pass
class C: pass

