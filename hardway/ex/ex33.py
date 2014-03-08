# Exercise 33
#------------

numbers = []

def fill_list(high, numbers):
    i = 0
    while i < high:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

# Variable passed to function by reference
fill_list(5, numbers)
print "The numbers: %r (len: %d)" % (numbers, len(numbers))

# Continue to top off the number list
fill_list(3, numbers)
print "After another call to the function:"
for num in numbers:
    print num,

