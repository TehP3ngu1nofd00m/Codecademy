score = {
  "a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
  "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
  "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
  "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
  "x": 8, "z": 10
}

def scrabble_score(word):
  s = 0
  l = []
  for c in word:
    l.append(c.lower()) # string to list
  for k in score.keys(): # checks the letters
    for i in l: # iterates over list items
      if k == i: # if the letter in dict == list index
        s += score[k] # add to score
  return s

'''
does not account for all rules, like multipliers
'''
