def reverse(text):
	lst = []
	new_lst = []
	s = len(text)
	txt = ''
	for c in text:
		lst.append(c)
	while s:
		new_lst.append(lst[s-1])
		s -= 1
	for c in new_lst:
		txt += c
	return txt
	print txt

'''
# This easier way uses the slice method, [begin:end:step]

def reverse_txt(s):
	return s[::-1]
  
'''
