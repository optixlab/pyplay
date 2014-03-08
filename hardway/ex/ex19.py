# Exercise 19
# -----------

def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print "You have %d cheeses!" % cheese_count
  print "You have %d boxes of crackers" % boxes_of_crackers

print "Give function numbers directly"
cheese_and_crackers(20, 30)

print "OR, print variables"
amount_of_cheese = 10
amount_of_crackers = 30

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "Doing math inside"
cheese_and_crackers(10+30, 5+6)

print "Combining numbers & variables:"
cheese_and_crackers(10+amount_of_cheese, 5+amount_of_crackers)

