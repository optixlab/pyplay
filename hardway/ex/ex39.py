# Exercise 39
#------------

class Thing(object):
  def test(hi):
    print "hello"

a = Thing()
a.test()

# Fails: test(a,"Hello") has 2 args; 1 expected
try:
  x = 1/1
finally:
  print "cannot run a.test('hello')"

ten_things = "Apples Oranges Crows Test Routine"

print "Wait there's not 10 things!"

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Toy", "More", "Stuff", "king"]

while len(stuff) != 10:
  next_one = more_stuff.pop()
  print "Popped: ", next_one
  stuff.append(next_one)
  print "There're %d items now." % len(stuff)

print "len(stuff) =", len(stuff)
for ind in range(len(stuff)):
  print ind,":",stuff[ind]

print "There we go: Stuff = ", stuff

print " [1] in list: ", stuff[1]
print "[-1] in list: ", stuff[-1]
# print stuff.pop()
print ','.join(stuff)
print '#'.join(stuff[3:6])

print ','.join(stuff[3:5])
print "%s" % stuff[3]
print "%s" % stuff[4]
print "%s" % stuff[5]

aa = stuff[3:5]
print '#'.join(aa), "len=", len(aa), "stuff[3:5] len=", len(stuff[3:5])

