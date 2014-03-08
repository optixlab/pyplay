# Exercise 32
#------------

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'bananas', 'apricots']
change = [1, 'pennnies', 2, 'dimes', 3, 'quarters']

# for loop
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# going through a mixed list. but with %r since we don't know the type
for i in change:
    print "I got %r" % i

# Building lists
elements = []

# use range to do the count
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function of lists
    elements.append(i)

# now we can print them out as well
for i in elements:
    print "Element was %d" % i

