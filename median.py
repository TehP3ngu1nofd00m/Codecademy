def median(l):
  a = sorted(l)
  # if odd length list, return middle index
  if len(a) % 2 != 0:
    return a[int((len(a)/2.0)-0.5)]
  # if even length list, return average of middle 2 indexes
  else:
    return (a[int((len(a)/2.0)-1)] + (a[int((len(a)/2.0))]))  / 2.0
