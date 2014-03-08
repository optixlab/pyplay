# Exercise 25
# -----------

def break_words(stuff):
  """This function will break up words for us."""
  words = stuff.split(' ')
  return words

def sort_words(words):
  """Sorts the words."""
  return sorted(words)

def print_first_word(words):
  """Returns 1st word in list"""
  word = words.pop(0)
  print word

def print_last_word(words):
  """Returns last word in list."""
  word = words.pop(-1)
  print word

def sort_sentence(sentence):
  """Returns a sorted sentence."""
  words = break_words(sentence)
  return sort_words(words)

def print_first_and_last_sentence(sentence):
  """Print first and last words of each sentence"""
  words = break_words(sentence)
  print_first_word(words)
  print_last_word(words)

def print_first_and_last_sorted(sentence):
  """Sort sentence words & print 1st and last words."""
  words = sort_sentence(sentence)
  print_first_word(words)
  print_last_word(words)

