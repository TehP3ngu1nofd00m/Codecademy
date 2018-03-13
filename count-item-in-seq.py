def count(sequence, item):
  c = 0
  
  if sequence == str:
    lst = c.split()
  for i in sequence or lst:
    if type(i) == list:
      for x in i:
        if x == item:
          c += 1
    else:
      if i == item:
        c += 1
  print c
  return c
