def double(p):
  if type(p) != list:
    return p
  else:
    if type(p[0]) == list and len(p) == 1:
      if len(p[0]) == 1:
        return double(p[0][0])
  return p
#Changes a ~~p => p in one item


def remove_double(arg):
  arg = double(arg)
  if type(arg)!=list:
    return arg
  for i in range(len(arg)):
    if type(arg[i]) == list:
      arg[i] = remove_double(arg[i])
  return arg
