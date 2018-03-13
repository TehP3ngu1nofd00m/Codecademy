def censor(text, word):
  lst_txt = text.split()
  c = 0
#  print lst_txt
  for s in lst_txt:
    if s == word:
      lst_txt[c] = '*' * len(word)
    c += 1
#  print ' '.join(lst_txt) 
return ' '.join(lst_txt)
